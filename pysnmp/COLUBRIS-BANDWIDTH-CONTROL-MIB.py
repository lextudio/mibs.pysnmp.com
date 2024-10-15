# SNMP MIB module (COLUBRIS-BANDWIDTH-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-BANDWIDTH-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:11 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisPriorityQueue,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisPriorityQueue")

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

colubrisBandwidthControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisBandwidthControlMIBObjects_ObjectIdentity = ObjectIdentity
colubrisBandwidthControlMIBObjects = _ColubrisBandwidthControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1)
)
_CoBandwidthControlConfig_ObjectIdentity = ObjectIdentity
coBandwidthControlConfig = _CoBandwidthControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1)
)
_CoBandwidthControlEnable_Type = TruthValue
_CoBandwidthControlEnable_Object = MibScalar
coBandwidthControlEnable = _CoBandwidthControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 1),
    _CoBandwidthControlEnable_Type()
)
coBandwidthControlEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlEnable.setStatus("current")
_CoBandwidthControlMaxTransmitRate_Type = Integer32
_CoBandwidthControlMaxTransmitRate_Object = MibScalar
coBandwidthControlMaxTransmitRate = _CoBandwidthControlMaxTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 2),
    _CoBandwidthControlMaxTransmitRate_Type()
)
coBandwidthControlMaxTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlMaxTransmitRate.setStatus("current")
_CoBandwidthControlMaxReceiveRate_Type = Integer32
_CoBandwidthControlMaxReceiveRate_Object = MibScalar
coBandwidthControlMaxReceiveRate = _CoBandwidthControlMaxReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 3),
    _CoBandwidthControlMaxReceiveRate_Type()
)
coBandwidthControlMaxReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlMaxReceiveRate.setStatus("current")
_CoBandwidthControlLevelTable_Object = MibTable
coBandwidthControlLevelTable = _CoBandwidthControlLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    coBandwidthControlLevelTable.setStatus("current")
_CoBandwidthControlLevelEntry_Object = MibTableRow
coBandwidthControlLevelEntry = _CoBandwidthControlLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1)
)
coBandwidthControlLevelEntry.setIndexNames(
    (0, "COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelIndex"),
)
if mibBuilder.loadTexts:
    coBandwidthControlLevelEntry.setStatus("current")
_CoBandwidthControlLevelIndex_Type = ColubrisPriorityQueue
_CoBandwidthControlLevelIndex_Object = MibTableColumn
coBandwidthControlLevelIndex = _CoBandwidthControlLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 1),
    _CoBandwidthControlLevelIndex_Type()
)
coBandwidthControlLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coBandwidthControlLevelIndex.setStatus("current")


class _CoBandwidthControlLevelMinTransmitRate_Type(Integer32):
    """Custom type coBandwidthControlLevelMinTransmitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoBandwidthControlLevelMinTransmitRate_Type.__name__ = "Integer32"
_CoBandwidthControlLevelMinTransmitRate_Object = MibTableColumn
coBandwidthControlLevelMinTransmitRate = _CoBandwidthControlLevelMinTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 2),
    _CoBandwidthControlLevelMinTransmitRate_Type()
)
coBandwidthControlLevelMinTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlLevelMinTransmitRate.setStatus("current")


class _CoBandwidthControlLevelMaxTransmitRate_Type(Integer32):
    """Custom type coBandwidthControlLevelMaxTransmitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoBandwidthControlLevelMaxTransmitRate_Type.__name__ = "Integer32"
_CoBandwidthControlLevelMaxTransmitRate_Object = MibTableColumn
coBandwidthControlLevelMaxTransmitRate = _CoBandwidthControlLevelMaxTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 3),
    _CoBandwidthControlLevelMaxTransmitRate_Type()
)
coBandwidthControlLevelMaxTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlLevelMaxTransmitRate.setStatus("current")


class _CoBandwidthControlLevelMinReceiveRate_Type(Integer32):
    """Custom type coBandwidthControlLevelMinReceiveRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoBandwidthControlLevelMinReceiveRate_Type.__name__ = "Integer32"
_CoBandwidthControlLevelMinReceiveRate_Object = MibTableColumn
coBandwidthControlLevelMinReceiveRate = _CoBandwidthControlLevelMinReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 4),
    _CoBandwidthControlLevelMinReceiveRate_Type()
)
coBandwidthControlLevelMinReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlLevelMinReceiveRate.setStatus("current")


class _CoBandwidthControlLevelMaxReceiveRate_Type(Integer32):
    """Custom type coBandwidthControlLevelMaxReceiveRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoBandwidthControlLevelMaxReceiveRate_Type.__name__ = "Integer32"
_CoBandwidthControlLevelMaxReceiveRate_Object = MibTableColumn
coBandwidthControlLevelMaxReceiveRate = _CoBandwidthControlLevelMaxReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 5),
    _CoBandwidthControlLevelMaxReceiveRate_Type()
)
coBandwidthControlLevelMaxReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coBandwidthControlLevelMaxReceiveRate.setStatus("current")
_ColubrisBandwidthControlMIBConformance_ObjectIdentity = ObjectIdentity
colubrisBandwidthControlMIBConformance = _ColubrisBandwidthControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2)
)
_ColubrisBandwidthControlMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisBandwidthControlMIBCompliances = _ColubrisBandwidthControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1)
)
_ColubrisBandwidthControlMIBGroups_ObjectIdentity = ObjectIdentity
colubrisBandwidthControlMIBGroups = _ColubrisBandwidthControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2)
)

# Managed Objects groups

colubrisBandwidthControlMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 1)
)
colubrisBandwidthControlMIBGroup.setObjects(
      *(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlEnable"),
        ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxTransmitRate"),
        ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxReceiveRate"))
)
if mibBuilder.loadTexts:
    colubrisBandwidthControlMIBGroup.setStatus("current")

colubrisBandwidthControlLevelMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 2)
)
colubrisBandwidthControlLevelMIBGroup.setObjects(
      *(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinTransmitRate"),
        ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxTransmitRate"),
        ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinReceiveRate"),
        ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxReceiveRate"))
)
if mibBuilder.loadTexts:
    colubrisBandwidthControlLevelMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisBandwidthControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisBandwidthControlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-BANDWIDTH-CONTROL-MIB",
    **{"colubrisBandwidthControlMIB": colubrisBandwidthControlMIB,
       "colubrisBandwidthControlMIBObjects": colubrisBandwidthControlMIBObjects,
       "coBandwidthControlConfig": coBandwidthControlConfig,
       "coBandwidthControlEnable": coBandwidthControlEnable,
       "coBandwidthControlMaxTransmitRate": coBandwidthControlMaxTransmitRate,
       "coBandwidthControlMaxReceiveRate": coBandwidthControlMaxReceiveRate,
       "coBandwidthControlLevelTable": coBandwidthControlLevelTable,
       "coBandwidthControlLevelEntry": coBandwidthControlLevelEntry,
       "coBandwidthControlLevelIndex": coBandwidthControlLevelIndex,
       "coBandwidthControlLevelMinTransmitRate": coBandwidthControlLevelMinTransmitRate,
       "coBandwidthControlLevelMaxTransmitRate": coBandwidthControlLevelMaxTransmitRate,
       "coBandwidthControlLevelMinReceiveRate": coBandwidthControlLevelMinReceiveRate,
       "coBandwidthControlLevelMaxReceiveRate": coBandwidthControlLevelMaxReceiveRate,
       "colubrisBandwidthControlMIBConformance": colubrisBandwidthControlMIBConformance,
       "colubrisBandwidthControlMIBCompliances": colubrisBandwidthControlMIBCompliances,
       "colubrisBandwidthControlMIBCompliance": colubrisBandwidthControlMIBCompliance,
       "colubrisBandwidthControlMIBGroups": colubrisBandwidthControlMIBGroups,
       "colubrisBandwidthControlMIBGroup": colubrisBandwidthControlMIBGroup,
       "colubrisBandwidthControlLevelMIBGroup": colubrisBandwidthControlLevelMIBGroup}
)
