# SNMP MIB module (LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:00 2024
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

(ifGeneralInformationGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifGeneralInformationGroup")

(lldpV2Xdot1MIB,) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-V2-MIB",
    "lldpV2Xdot1MIB")

(lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpXDot1EvbExtensions = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1)
)
lldpXDot1EvbExtensions.setRevisions(
        ("2018-06-21 00:00",
         "2014-12-15 00:00",
         "2012-02-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpXdot1StandAloneExtensions_ObjectIdentity = ObjectIdentity
lldpXdot1StandAloneExtensions = _LldpXdot1StandAloneExtensions_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7)
)
_LldpXdot1EvbMIB_ObjectIdentity = ObjectIdentity
lldpXdot1EvbMIB = _LldpXdot1EvbMIB_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1)
)
_LldpXdot1EvbObjects_ObjectIdentity = ObjectIdentity
lldpXdot1EvbObjects = _LldpXdot1EvbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1)
)
_LldpXdot1EvbConfig_ObjectIdentity = ObjectIdentity
lldpXdot1EvbConfig = _LldpXdot1EvbConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1)
)
_LldpXdot1EvbConfigEvbTable_Object = MibTable
lldpXdot1EvbConfigEvbTable = _LldpXdot1EvbConfigEvbTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigEvbTable.setStatus("current")
_LldpXdot1EvbConfigEvbEntry_Object = MibTableRow
lldpXdot1EvbConfigEvbEntry = _LldpXdot1EvbConfigEvbEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigEvbEntry.setStatus("current")


class _LldpXdot1EvbConfigEvbTxEnable_Type(TruthValue):
    """Custom type lldpXdot1EvbConfigEvbTxEnable based on TruthValue"""


_LldpXdot1EvbConfigEvbTxEnable_Object = MibTableColumn
lldpXdot1EvbConfigEvbTxEnable = _LldpXdot1EvbConfigEvbTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1, 1, 1),
    _LldpXdot1EvbConfigEvbTxEnable_Type()
)
lldpXdot1EvbConfigEvbTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigEvbTxEnable.setStatus("current")
_LldpXdot1EvbConfigCdcpTable_Object = MibTable
lldpXdot1EvbConfigCdcpTable = _LldpXdot1EvbConfigCdcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigCdcpTable.setStatus("current")
_LldpXdot1EvbConfigCdcpEntry_Object = MibTableRow
lldpXdot1EvbConfigCdcpEntry = _LldpXdot1EvbConfigCdcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigCdcpEntry.setStatus("current")


class _LldpXdot1EvbConfigCdcpTxEnable_Type(TruthValue):
    """Custom type lldpXdot1EvbConfigCdcpTxEnable based on TruthValue"""


_LldpXdot1EvbConfigCdcpTxEnable_Object = MibTableColumn
lldpXdot1EvbConfigCdcpTxEnable = _LldpXdot1EvbConfigCdcpTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2, 1, 1),
    _LldpXdot1EvbConfigCdcpTxEnable_Type()
)
lldpXdot1EvbConfigCdcpTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1EvbConfigCdcpTxEnable.setStatus("current")
_LldpXdot1EvbLocalData_ObjectIdentity = ObjectIdentity
lldpXdot1EvbLocalData = _LldpXdot1EvbLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2)
)
_LldpV2Xdot1LocEvbTlvTable_Object = MibTable
lldpV2Xdot1LocEvbTlvTable = _LldpV2Xdot1LocEvbTlvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocEvbTlvTable.setStatus("current")
_LldpV2Xdot1LocEvbTlvEntry_Object = MibTableRow
lldpV2Xdot1LocEvbTlvEntry = _LldpV2Xdot1LocEvbTlvEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1, 1)
)
lldpV2Xdot1LocEvbTlvEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocEvbTlvEntry.setStatus("current")


class _LldpV2Xdot1LocEvbTlvString_Type(OctetString):
    """Custom type lldpV2Xdot1LocEvbTlvString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 514),
    )


_LldpV2Xdot1LocEvbTlvString_Type.__name__ = "OctetString"
_LldpV2Xdot1LocEvbTlvString_Object = MibTableColumn
lldpV2Xdot1LocEvbTlvString = _LldpV2Xdot1LocEvbTlvString_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1, 1, 1),
    _LldpV2Xdot1LocEvbTlvString_Type()
)
lldpV2Xdot1LocEvbTlvString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocEvbTlvString.setStatus("current")
_LldpV2Xdot1LocCdcpTlvTable_Object = MibTable
lldpV2Xdot1LocCdcpTlvTable = _LldpV2Xdot1LocCdcpTlvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCdcpTlvTable.setStatus("current")
_LldpV2Xdot1LocCdcpTlvEntry_Object = MibTableRow
lldpV2Xdot1LocCdcpTlvEntry = _LldpV2Xdot1LocCdcpTlvEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2, 1)
)
lldpV2Xdot1LocCdcpTlvEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCdcpTlvEntry.setStatus("current")


class _LldpV2Xdot1LocCdcpTlvString_Type(OctetString):
    """Custom type lldpV2Xdot1LocCdcpTlvString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 514),
    )


_LldpV2Xdot1LocCdcpTlvString_Type.__name__ = "OctetString"
_LldpV2Xdot1LocCdcpTlvString_Object = MibTableColumn
lldpV2Xdot1LocCdcpTlvString = _LldpV2Xdot1LocCdcpTlvString_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2, 1, 1),
    _LldpV2Xdot1LocCdcpTlvString_Type()
)
lldpV2Xdot1LocCdcpTlvString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCdcpTlvString.setStatus("current")
_LldpXdot1EvbRemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1EvbRemoteData = _LldpXdot1EvbRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3)
)
_LldpV2Xdot1RemEvbTlvTable_Object = MibTable
lldpV2Xdot1RemEvbTlvTable = _LldpV2Xdot1RemEvbTlvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemEvbTlvTable.setStatus("current")
_LldpV2Xdot1RemEvbTlvEntry_Object = MibTableRow
lldpV2Xdot1RemEvbTlvEntry = _LldpV2Xdot1RemEvbTlvEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1, 1)
)
lldpV2Xdot1RemEvbTlvEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemEvbTlvEntry.setStatus("current")


class _LldpV2Xdot1RemEvbTlvString_Type(OctetString):
    """Custom type lldpV2Xdot1RemEvbTlvString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 514),
    )


_LldpV2Xdot1RemEvbTlvString_Type.__name__ = "OctetString"
_LldpV2Xdot1RemEvbTlvString_Object = MibTableColumn
lldpV2Xdot1RemEvbTlvString = _LldpV2Xdot1RemEvbTlvString_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1, 1, 1),
    _LldpV2Xdot1RemEvbTlvString_Type()
)
lldpV2Xdot1RemEvbTlvString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemEvbTlvString.setStatus("current")
_LldpV2Xdot1RemCdcpTlvTable_Object = MibTable
lldpV2Xdot1RemCdcpTlvTable = _LldpV2Xdot1RemCdcpTlvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCdcpTlvTable.setStatus("current")
_LldpV2Xdot1RemCdcpTlvEntry_Object = MibTableRow
lldpV2Xdot1RemCdcpTlvEntry = _LldpV2Xdot1RemCdcpTlvEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2, 1)
)
lldpV2Xdot1RemCdcpTlvEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCdcpTlvEntry.setStatus("current")


class _LldpV2Xdot1RemCdcpTlvString_Type(OctetString):
    """Custom type lldpV2Xdot1RemCdcpTlvString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 514),
    )


_LldpV2Xdot1RemCdcpTlvString_Type.__name__ = "OctetString"
_LldpV2Xdot1RemCdcpTlvString_Object = MibTableColumn
lldpV2Xdot1RemCdcpTlvString = _LldpV2Xdot1RemCdcpTlvString_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2, 1, 1),
    _LldpV2Xdot1RemCdcpTlvString_Type()
)
lldpV2Xdot1RemCdcpTlvString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCdcpTlvString.setStatus("current")
_LldpXdot1EvbConformance_ObjectIdentity = ObjectIdentity
lldpXdot1EvbConformance = _LldpXdot1EvbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2)
)
_LldpXdot1EvbCompliances_ObjectIdentity = ObjectIdentity
lldpXdot1EvbCompliances = _LldpXdot1EvbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 1)
)
_LldpXdot1EvbGroups_ObjectIdentity = ObjectIdentity
lldpXdot1EvbGroups = _LldpXdot1EvbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB",
     "lldpXdot1EvbConfigEvbEntry")
)
lldpXdot1EvbConfigEvbEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB",
     "lldpXdot1EvbConfigCdcpEntry")
)
lldpXdot1EvbConfigCdcpEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXdot1EvbGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 2, 1)
)
lldpXdot1EvbGroup.setObjects(
      *(("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigEvbTxEnable"),
        ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigCdcpTxEnable"),
        ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1LocEvbTlvString"),
        ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1LocCdcpTlvString"),
        ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1RemEvbTlvString"),
        ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1RemCdcpTlvString"))
)
if mibBuilder.loadTexts:
    lldpXdot1EvbGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXdot1EvbCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1EvbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB",
    **{"lldpXdot1StandAloneExtensions": lldpXdot1StandAloneExtensions,
       "lldpXDot1EvbExtensions": lldpXDot1EvbExtensions,
       "lldpXdot1EvbMIB": lldpXdot1EvbMIB,
       "lldpXdot1EvbObjects": lldpXdot1EvbObjects,
       "lldpXdot1EvbConfig": lldpXdot1EvbConfig,
       "lldpXdot1EvbConfigEvbTable": lldpXdot1EvbConfigEvbTable,
       "lldpXdot1EvbConfigEvbEntry": lldpXdot1EvbConfigEvbEntry,
       "lldpXdot1EvbConfigEvbTxEnable": lldpXdot1EvbConfigEvbTxEnable,
       "lldpXdot1EvbConfigCdcpTable": lldpXdot1EvbConfigCdcpTable,
       "lldpXdot1EvbConfigCdcpEntry": lldpXdot1EvbConfigCdcpEntry,
       "lldpXdot1EvbConfigCdcpTxEnable": lldpXdot1EvbConfigCdcpTxEnable,
       "lldpXdot1EvbLocalData": lldpXdot1EvbLocalData,
       "lldpV2Xdot1LocEvbTlvTable": lldpV2Xdot1LocEvbTlvTable,
       "lldpV2Xdot1LocEvbTlvEntry": lldpV2Xdot1LocEvbTlvEntry,
       "lldpV2Xdot1LocEvbTlvString": lldpV2Xdot1LocEvbTlvString,
       "lldpV2Xdot1LocCdcpTlvTable": lldpV2Xdot1LocCdcpTlvTable,
       "lldpV2Xdot1LocCdcpTlvEntry": lldpV2Xdot1LocCdcpTlvEntry,
       "lldpV2Xdot1LocCdcpTlvString": lldpV2Xdot1LocCdcpTlvString,
       "lldpXdot1EvbRemoteData": lldpXdot1EvbRemoteData,
       "lldpV2Xdot1RemEvbTlvTable": lldpV2Xdot1RemEvbTlvTable,
       "lldpV2Xdot1RemEvbTlvEntry": lldpV2Xdot1RemEvbTlvEntry,
       "lldpV2Xdot1RemEvbTlvString": lldpV2Xdot1RemEvbTlvString,
       "lldpV2Xdot1RemCdcpTlvTable": lldpV2Xdot1RemCdcpTlvTable,
       "lldpV2Xdot1RemCdcpTlvEntry": lldpV2Xdot1RemCdcpTlvEntry,
       "lldpV2Xdot1RemCdcpTlvString": lldpV2Xdot1RemCdcpTlvString,
       "lldpXdot1EvbConformance": lldpXdot1EvbConformance,
       "lldpXdot1EvbCompliances": lldpXdot1EvbCompliances,
       "lldpXdot1EvbCompliance": lldpXdot1EvbCompliance,
       "lldpXdot1EvbGroups": lldpXdot1EvbGroups,
       "lldpXdot1EvbGroup": lldpXdot1EvbGroup}
)
