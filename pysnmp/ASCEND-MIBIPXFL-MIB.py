# SNMP MIB module (ASCEND-MIBIPXFL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPXFL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:48 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibipxsapFilterProfile_ObjectIdentity = ObjectIdentity
mibipxsapFilterProfile = _MibipxsapFilterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 88)
)
_MibipxsapFilterProfileTable_Object = MibTable
mibipxsapFilterProfileTable = _MibipxsapFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 1)
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfileTable.setStatus("mandatory")
_MibipxsapFilterProfileEntry_Object = MibTableRow
mibipxsapFilterProfileEntry = _MibipxsapFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1)
)
mibipxsapFilterProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-IpxSapFilterName"),
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfileEntry.setStatus("mandatory")
_IpxsapFilterProfile_IpxSapFilterName_Type = DisplayString
_IpxsapFilterProfile_IpxSapFilterName_Object = MibScalar
ipxsapFilterProfile_IpxSapFilterName = _IpxsapFilterProfile_IpxSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1, 1),
    _IpxsapFilterProfile_IpxSapFilterName_Type()
)
ipxsapFilterProfile_IpxSapFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_IpxSapFilterName.setStatus("mandatory")


class _IpxsapFilterProfile_Action_o_Type(Integer32):
    """Custom type ipxsapFilterProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_IpxsapFilterProfile_Action_o_Type.__name__ = "Integer32"
_IpxsapFilterProfile_Action_o_Object = MibScalar
ipxsapFilterProfile_Action_o = _IpxsapFilterProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1, 2),
    _IpxsapFilterProfile_Action_o_Type()
)
ipxsapFilterProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_Action_o.setStatus("mandatory")
_MibipxsapFilterProfile_OutputIpxSapFiltersTable_Object = MibTable
mibipxsapFilterProfile_OutputIpxSapFiltersTable = _MibipxsapFilterProfile_OutputIpxSapFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2)
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfile_OutputIpxSapFiltersTable.setStatus("mandatory")
_MibipxsapFilterProfile_OutputIpxSapFiltersEntry_Object = MibTableRow
mibipxsapFilterProfile_OutputIpxSapFiltersEntry = _MibipxsapFilterProfile_OutputIpxSapFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1)
)
mibipxsapFilterProfile_OutputIpxSapFiltersEntry.setIndexNames(
    (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-OutputIpxSapFilters-IpxSapFilterName"),
    (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-OutputIpxSapFilters-Index-o"),
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfile_OutputIpxSapFiltersEntry.setStatus("mandatory")
_IpxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName_Type = DisplayString
_IpxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName = _IpxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 1),
    _IpxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName.setStatus("mandatory")
_IpxsapFilterProfile_OutputIpxSapFilters_Index_o_Type = Integer32
_IpxsapFilterProfile_OutputIpxSapFilters_Index_o_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_Index_o = _IpxsapFilterProfile_OutputIpxSapFilters_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 2),
    _IpxsapFilterProfile_OutputIpxSapFilters_Index_o_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_Index_o.setStatus("mandatory")


class _IpxsapFilterProfile_OutputIpxSapFilters_ValidFilter_Type(Integer32):
    """Custom type ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxsapFilterProfile_OutputIpxSapFilters_ValidFilter_Type.__name__ = "Integer32"
_IpxsapFilterProfile_OutputIpxSapFilters_ValidFilter_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter = _IpxsapFilterProfile_OutputIpxSapFilters_ValidFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 3),
    _IpxsapFilterProfile_OutputIpxSapFilters_ValidFilter_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter.setStatus("mandatory")


class _IpxsapFilterProfile_OutputIpxSapFilters_TypeFilter_Type(Integer32):
    """Custom type ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 1),
          ("include", 2))
    )


_IpxsapFilterProfile_OutputIpxSapFilters_TypeFilter_Type.__name__ = "Integer32"
_IpxsapFilterProfile_OutputIpxSapFilters_TypeFilter_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter = _IpxsapFilterProfile_OutputIpxSapFilters_TypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 4),
    _IpxsapFilterProfile_OutputIpxSapFilters_TypeFilter_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter.setStatus("mandatory")
_IpxsapFilterProfile_OutputIpxSapFilters_ServerType_Type = DisplayString
_IpxsapFilterProfile_OutputIpxSapFilters_ServerType_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_ServerType = _IpxsapFilterProfile_OutputIpxSapFilters_ServerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 5),
    _IpxsapFilterProfile_OutputIpxSapFilters_ServerType_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_ServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_ServerType.setStatus("mandatory")
_IpxsapFilterProfile_OutputIpxSapFilters_ServerName_Type = DisplayString
_IpxsapFilterProfile_OutputIpxSapFilters_ServerName_Object = MibScalar
ipxsapFilterProfile_OutputIpxSapFilters_ServerName = _IpxsapFilterProfile_OutputIpxSapFilters_ServerName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 6),
    _IpxsapFilterProfile_OutputIpxSapFilters_ServerName_Type()
)
ipxsapFilterProfile_OutputIpxSapFilters_ServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_OutputIpxSapFilters_ServerName.setStatus("mandatory")
_MibipxsapFilterProfile_InputIpxSapFiltersTable_Object = MibTable
mibipxsapFilterProfile_InputIpxSapFiltersTable = _MibipxsapFilterProfile_InputIpxSapFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3)
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfile_InputIpxSapFiltersTable.setStatus("mandatory")
_MibipxsapFilterProfile_InputIpxSapFiltersEntry_Object = MibTableRow
mibipxsapFilterProfile_InputIpxSapFiltersEntry = _MibipxsapFilterProfile_InputIpxSapFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1)
)
mibipxsapFilterProfile_InputIpxSapFiltersEntry.setIndexNames(
    (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-InputIpxSapFilters-IpxSapFilterName"),
    (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-InputIpxSapFilters-Index-o"),
)
if mibBuilder.loadTexts:
    mibipxsapFilterProfile_InputIpxSapFiltersEntry.setStatus("mandatory")
_IpxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName_Type = DisplayString
_IpxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName = _IpxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 1),
    _IpxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName.setStatus("mandatory")
_IpxsapFilterProfile_InputIpxSapFilters_Index_o_Type = Integer32
_IpxsapFilterProfile_InputIpxSapFilters_Index_o_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_Index_o = _IpxsapFilterProfile_InputIpxSapFilters_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 2),
    _IpxsapFilterProfile_InputIpxSapFilters_Index_o_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_Index_o.setStatus("mandatory")


class _IpxsapFilterProfile_InputIpxSapFilters_ValidFilter_Type(Integer32):
    """Custom type ipxsapFilterProfile_InputIpxSapFilters_ValidFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxsapFilterProfile_InputIpxSapFilters_ValidFilter_Type.__name__ = "Integer32"
_IpxsapFilterProfile_InputIpxSapFilters_ValidFilter_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_ValidFilter = _IpxsapFilterProfile_InputIpxSapFilters_ValidFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 3),
    _IpxsapFilterProfile_InputIpxSapFilters_ValidFilter_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_ValidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_ValidFilter.setStatus("mandatory")


class _IpxsapFilterProfile_InputIpxSapFilters_TypeFilter_Type(Integer32):
    """Custom type ipxsapFilterProfile_InputIpxSapFilters_TypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 1),
          ("include", 2))
    )


_IpxsapFilterProfile_InputIpxSapFilters_TypeFilter_Type.__name__ = "Integer32"
_IpxsapFilterProfile_InputIpxSapFilters_TypeFilter_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_TypeFilter = _IpxsapFilterProfile_InputIpxSapFilters_TypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 4),
    _IpxsapFilterProfile_InputIpxSapFilters_TypeFilter_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_TypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_TypeFilter.setStatus("mandatory")
_IpxsapFilterProfile_InputIpxSapFilters_ServerType_Type = DisplayString
_IpxsapFilterProfile_InputIpxSapFilters_ServerType_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_ServerType = _IpxsapFilterProfile_InputIpxSapFilters_ServerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 5),
    _IpxsapFilterProfile_InputIpxSapFilters_ServerType_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_ServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_ServerType.setStatus("mandatory")
_IpxsapFilterProfile_InputIpxSapFilters_ServerName_Type = DisplayString
_IpxsapFilterProfile_InputIpxSapFilters_ServerName_Object = MibScalar
ipxsapFilterProfile_InputIpxSapFilters_ServerName = _IpxsapFilterProfile_InputIpxSapFilters_ServerName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 6),
    _IpxsapFilterProfile_InputIpxSapFilters_ServerName_Type()
)
ipxsapFilterProfile_InputIpxSapFilters_ServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxsapFilterProfile_InputIpxSapFilters_ServerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPXFL-MIB",
    **{"DisplayString": DisplayString,
       "mibipxsapFilterProfile": mibipxsapFilterProfile,
       "mibipxsapFilterProfileTable": mibipxsapFilterProfileTable,
       "mibipxsapFilterProfileEntry": mibipxsapFilterProfileEntry,
       "ipxsapFilterProfile-IpxSapFilterName": ipxsapFilterProfile_IpxSapFilterName,
       "ipxsapFilterProfile-Action-o": ipxsapFilterProfile_Action_o,
       "mibipxsapFilterProfile-OutputIpxSapFiltersTable": mibipxsapFilterProfile_OutputIpxSapFiltersTable,
       "mibipxsapFilterProfile-OutputIpxSapFiltersEntry": mibipxsapFilterProfile_OutputIpxSapFiltersEntry,
       "ipxsapFilterProfile-OutputIpxSapFilters-IpxSapFilterName": ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName,
       "ipxsapFilterProfile-OutputIpxSapFilters-Index-o": ipxsapFilterProfile_OutputIpxSapFilters_Index_o,
       "ipxsapFilterProfile-OutputIpxSapFilters-ValidFilter": ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter,
       "ipxsapFilterProfile-OutputIpxSapFilters-TypeFilter": ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter,
       "ipxsapFilterProfile-OutputIpxSapFilters-ServerType": ipxsapFilterProfile_OutputIpxSapFilters_ServerType,
       "ipxsapFilterProfile-OutputIpxSapFilters-ServerName": ipxsapFilterProfile_OutputIpxSapFilters_ServerName,
       "mibipxsapFilterProfile-InputIpxSapFiltersTable": mibipxsapFilterProfile_InputIpxSapFiltersTable,
       "mibipxsapFilterProfile-InputIpxSapFiltersEntry": mibipxsapFilterProfile_InputIpxSapFiltersEntry,
       "ipxsapFilterProfile-InputIpxSapFilters-IpxSapFilterName": ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName,
       "ipxsapFilterProfile-InputIpxSapFilters-Index-o": ipxsapFilterProfile_InputIpxSapFilters_Index_o,
       "ipxsapFilterProfile-InputIpxSapFilters-ValidFilter": ipxsapFilterProfile_InputIpxSapFilters_ValidFilter,
       "ipxsapFilterProfile-InputIpxSapFilters-TypeFilter": ipxsapFilterProfile_InputIpxSapFilters_TypeFilter,
       "ipxsapFilterProfile-InputIpxSapFilters-ServerType": ipxsapFilterProfile_InputIpxSapFilters_ServerType,
       "ipxsapFilterProfile-InputIpxSapFilters-ServerName": ipxsapFilterProfile_InputIpxSapFilters_ServerName}
)
