# SNMP MIB module (BCST-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCST-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:30 2024
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
 enterprises,
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
    "enterprises",
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

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTSVCBroadcastTable_Object = MibTable
cdx6500GCTSVCBroadcastTable = _Cdx6500GCTSVCBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    cdx6500GCTSVCBroadcastTable.setStatus("mandatory")
_Cdx6500bcstSBCOcfgEntry_Object = MibTableRow
cdx6500bcstSBCOcfgEntry = _Cdx6500bcstSBCOcfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1)
)
cdx6500bcstSBCOcfgEntry.setIndexNames(
    (0, "BCST-OPT-MIB", "cdx6500bcstSBCOnum"),
)
if mibBuilder.loadTexts:
    cdx6500bcstSBCOcfgEntry.setStatus("mandatory")


class _Cdx6500bcstSBCOnum_Type(Integer32):
    """Custom type cdx6500bcstSBCOnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500bcstSBCOnum_Type.__name__ = "Integer32"
_Cdx6500bcstSBCOnum_Object = MibTableColumn
cdx6500bcstSBCOnum = _Cdx6500bcstSBCOnum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 1),
    _Cdx6500bcstSBCOnum_Type()
)
cdx6500bcstSBCOnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOnum.setStatus("mandatory")


class _Cdx6500bcstSBCOnet_Type(Integer32):
    """Custom type cdx6500bcstSBCOnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500bcstSBCOnet_Type.__name__ = "Integer32"
_Cdx6500bcstSBCOnet_Object = MibTableColumn
cdx6500bcstSBCOnet = _Cdx6500bcstSBCOnet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 2),
    _Cdx6500bcstSBCOnet_Type()
)
cdx6500bcstSBCOnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOnet.setStatus("mandatory")
_Cdx6500bcstSBCOcalledAddr_Type = DisplayString
_Cdx6500bcstSBCOcalledAddr_Object = MibTableColumn
cdx6500bcstSBCOcalledAddr = _Cdx6500bcstSBCOcalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 3),
    _Cdx6500bcstSBCOcalledAddr_Type()
)
cdx6500bcstSBCOcalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOcalledAddr.setStatus("mandatory")
_Cdx6500bcstSBCOcallingAddr_Type = DisplayString
_Cdx6500bcstSBCOcallingAddr_Object = MibTableColumn
cdx6500bcstSBCOcallingAddr = _Cdx6500bcstSBCOcallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 4),
    _Cdx6500bcstSBCOcallingAddr_Type()
)
cdx6500bcstSBCOcallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOcallingAddr.setStatus("mandatory")
_Cdx6500bcstSBCOfacilities_Type = DisplayString
_Cdx6500bcstSBCOfacilities_Object = MibTableColumn
cdx6500bcstSBCOfacilities = _Cdx6500bcstSBCOfacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 5),
    _Cdx6500bcstSBCOfacilities_Type()
)
cdx6500bcstSBCOfacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOfacilities.setStatus("mandatory")
_Cdx6500bcstSBCOuserData_Type = DisplayString
_Cdx6500bcstSBCOuserData_Object = MibTableColumn
cdx6500bcstSBCOuserData = _Cdx6500bcstSBCOuserData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 6),
    _Cdx6500bcstSBCOuserData_Type()
)
cdx6500bcstSBCOuserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOuserData.setStatus("mandatory")


class _Cdx6500bcstSBCOdirection_Type(Integer32):
    """Custom type cdx6500bcstSBCOdirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("calling", 3),
          ("none", 1))
    )


_Cdx6500bcstSBCOdirection_Type.__name__ = "Integer32"
_Cdx6500bcstSBCOdirection_Object = MibTableColumn
cdx6500bcstSBCOdirection = _Cdx6500bcstSBCOdirection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 7),
    _Cdx6500bcstSBCOdirection_Type()
)
cdx6500bcstSBCOdirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOdirection.setStatus("mandatory")


class _Cdx6500bcstSBCOdestination_Type(Integer32):
    """Custom type cdx6500bcstSBCOdestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bctp", 2),
          ("user", 1))
    )


_Cdx6500bcstSBCOdestination_Type.__name__ = "Integer32"
_Cdx6500bcstSBCOdestination_Object = MibTableColumn
cdx6500bcstSBCOdestination = _Cdx6500bcstSBCOdestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 8),
    _Cdx6500bcstSBCOdestination_Type()
)
cdx6500bcstSBCOdestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstSBCOdestination.setStatus("mandatory")
_Cdx6500GCTPVCBroadcastOutTable_Object = MibTable
cdx6500GCTPVCBroadcastOutTable = _Cdx6500GCTPVCBroadcastOutTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    cdx6500GCTPVCBroadcastOutTable.setStatus("mandatory")
_Cdx6500bcstPBCOcfgEntry_Object = MibTableRow
cdx6500bcstPBCOcfgEntry = _Cdx6500bcstPBCOcfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1)
)
cdx6500bcstPBCOcfgEntry.setIndexNames(
    (0, "BCST-OPT-MIB", "cdx6500bcstPBCOnum"),
)
if mibBuilder.loadTexts:
    cdx6500bcstPBCOcfgEntry.setStatus("mandatory")


class _Cdx6500bcstPBCOnum_Type(Integer32):
    """Custom type cdx6500bcstPBCOnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500bcstPBCOnum_Type.__name__ = "Integer32"
_Cdx6500bcstPBCOnum_Object = MibTableColumn
cdx6500bcstPBCOnum = _Cdx6500bcstPBCOnum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 1),
    _Cdx6500bcstPBCOnum_Type()
)
cdx6500bcstPBCOnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstPBCOnum.setStatus("mandatory")


class _Cdx6500bcstPBCOnet_Type(Integer32):
    """Custom type cdx6500bcstPBCOnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500bcstPBCOnet_Type.__name__ = "Integer32"
_Cdx6500bcstPBCOnet_Object = MibTableColumn
cdx6500bcstPBCOnet = _Cdx6500bcstPBCOnet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 2),
    _Cdx6500bcstPBCOnet_Type()
)
cdx6500bcstPBCOnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstPBCOnet.setStatus("mandatory")
_Cdx6500bcstPBCOconnection_Type = DisplayString
_Cdx6500bcstPBCOconnection_Object = MibTableColumn
cdx6500bcstPBCOconnection = _Cdx6500bcstPBCOconnection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 3),
    _Cdx6500bcstPBCOconnection_Type()
)
cdx6500bcstPBCOconnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstPBCOconnection.setStatus("mandatory")
_Cdx6500bcstPBCOdestination_Type = Integer32
_Cdx6500bcstPBCOdestination_Object = MibTableColumn
cdx6500bcstPBCOdestination = _Cdx6500bcstPBCOdestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 4),
    _Cdx6500bcstPBCOdestination_Type()
)
cdx6500bcstPBCOdestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bcstPBCOdestination.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCST-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTSVCBroadcastTable": cdx6500GCTSVCBroadcastTable,
       "cdx6500bcstSBCOcfgEntry": cdx6500bcstSBCOcfgEntry,
       "cdx6500bcstSBCOnum": cdx6500bcstSBCOnum,
       "cdx6500bcstSBCOnet": cdx6500bcstSBCOnet,
       "cdx6500bcstSBCOcalledAddr": cdx6500bcstSBCOcalledAddr,
       "cdx6500bcstSBCOcallingAddr": cdx6500bcstSBCOcallingAddr,
       "cdx6500bcstSBCOfacilities": cdx6500bcstSBCOfacilities,
       "cdx6500bcstSBCOuserData": cdx6500bcstSBCOuserData,
       "cdx6500bcstSBCOdirection": cdx6500bcstSBCOdirection,
       "cdx6500bcstSBCOdestination": cdx6500bcstSBCOdestination,
       "cdx6500GCTPVCBroadcastOutTable": cdx6500GCTPVCBroadcastOutTable,
       "cdx6500bcstPBCOcfgEntry": cdx6500bcstPBCOcfgEntry,
       "cdx6500bcstPBCOnum": cdx6500bcstPBCOnum,
       "cdx6500bcstPBCOnet": cdx6500bcstPBCOnet,
       "cdx6500bcstPBCOconnection": cdx6500bcstPBCOconnection,
       "cdx6500bcstPBCOdestination": cdx6500bcstPBCOdestination}
)
