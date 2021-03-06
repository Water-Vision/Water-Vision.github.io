/******************************************************************************
 * $Id: MajorObject.i b1fd4d61e877e5d9de96ed4a590b06adf80a905f 2021-02-25 02:44:52 -0500 Elliott Sales de Andrade $
 *
 * Project:  GDAL SWIG Interfaces.
 * Purpose:  SWIG Definitions for GDALMajorObject.
 * Author:   Kevin Ruland, kruland@ku.edu
 *
 ******************************************************************************
 * Copyright (c) 2005, Kevin Ruland
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 *****************************************************************************/

/* For Python we don't import, but include MajorObject.i to avoid */
/* cyclic dependency between gdal.py and ogr.py. */
/* We should probably define a new module for MajorObject, or merge gdal and ogr */
/* modules */
#ifndef FROM_PYTHON_OGR_I
#ifdef PERL_CPAN_NAMESPACE
%module "Geo::GDAL"
#elif defined(SWIGCSHARP)
%module Gdal
#elif defined(SWIGPYTHON)
%module (package="osgeo") gdal
#else
%module gdal
#endif
#endif /* FROM_PYTHON_OGR_I */

%rename (MajorObject) GDALMajorObjectShadow;

class GDALMajorObjectShadow {
private:
  GDALMajorObjectShadow();
  ~GDALMajorObjectShadow();

public:
%extend {
/*
 * GetDescription
 */
  const char *GetDescription() {
    return GDALGetDescription( self );
  }

/*
 * SetDescription
 */
%apply Pointer NONNULL {const char * pszNewDesc};
  void SetDescription( const char *pszNewDesc ) {
    GDALSetDescription( self, pszNewDesc );
  }
%clear const char * pszNewDesc;


%apply (char **CSL) {(char **)};
  char ** GetMetadataDomainList( ) {
    return GDALGetMetadataDomainList( self );
  }
%clear char **;

/*
 * GetMetadata methods
 */
%apply (char **dict) { char ** };
  char ** GetMetadata_Dict( const char * pszDomain = "" ) {
    return GDALGetMetadata( self, pszDomain );
  }
%clear char **;

%apply (char **options) {char **};
  char **GetMetadata_List( const char *pszDomain = "" ) {
    return GDALGetMetadata( self, pszDomain );
  }
%clear char **;

/*
 * SetMetadata methods
 */

#ifdef SWIGJAVA
%apply (char **options) { char ** papszMetadata };
  CPLErr SetMetadata( char ** papszMetadata, const char * pszDomain = "" ) {
    return GDALSetMetadata( self, papszMetadata, pszDomain );
  }
%clear char **papszMetadata;
#else
%apply (char **dict) { char ** papszMetadata };
  CPLErr SetMetadata( char ** papszMetadata, const char * pszDomain = "" ) {
    return GDALSetMetadata( self, papszMetadata, pszDomain );
  }
%clear char **papszMetadata;
#endif

  CPLErr SetMetadata( char * pszMetadataString , const char *pszDomain = "" ) {
    char *tmpList[2];
    tmpList[0] = pszMetadataString;
    tmpList[1] = 0;
    return GDALSetMetadata( self, tmpList, pszDomain );
  }

/*
 * GetMetadataItem
 */
  %apply Pointer NONNULL {const char * pszName};
  const char *GetMetadataItem( const char *pszName, const char *pszDomain = "" ) {
    return GDALGetMetadataItem( self, pszName, pszDomain);
  }

/*
 * SetMetadataItem
 */
  CPLErr SetMetadataItem( const char * pszName, const char * pszValue,
                                            const char * pszDomain = "" ) {
    return GDALSetMetadataItem( self, pszName, pszValue, pszDomain);
  }
  %clear const char * pszName;

} /* %extend */
};
