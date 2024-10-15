# SNMP MIB module (HM2-TRAFFICMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-TRAFFICMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:34 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hm2TrafficMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 31)
)
hm2TrafficMgmtMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2TrafficMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2TrafficMgmtMibNotifications = _Hm2TrafficMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 0)
)
_Hm2TrafficMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2TrafficMgmtMibObjects = _Hm2TrafficMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1)
)
_Hm2TrafficMgmtIfTable_Object = MibTable
hm2TrafficMgmtIfTable = _Hm2TrafficMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1)
)
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfTable.setStatus("current")
_Hm2TrafficMgmtIfEntry_Object = MibTableRow
hm2TrafficMgmtIfEntry = _Hm2TrafficMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1)
)
hm2TrafficMgmtIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfEntry.setStatus("current")


class _Hm2TrafficMgmtIfFlowControl_Type(HmEnabledStatus):
    """Custom type hm2TrafficMgmtIfFlowControl based on HmEnabledStatus"""


_Hm2TrafficMgmtIfFlowControl_Object = MibTableColumn
hm2TrafficMgmtIfFlowControl = _Hm2TrafficMgmtIfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 1),
    _Hm2TrafficMgmtIfFlowControl_Type()
)
hm2TrafficMgmtIfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfFlowControl.setStatus("current")


class _Hm2TrafficMgmtIfEgressShapingRate_Type(Unsigned32):
    """Custom type hm2TrafficMgmtIfEgressShapingRate based on Unsigned32"""
    defaultValue = 0


_Hm2TrafficMgmtIfEgressShapingRate_Object = MibTableColumn
hm2TrafficMgmtIfEgressShapingRate = _Hm2TrafficMgmtIfEgressShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 2),
    _Hm2TrafficMgmtIfEgressShapingRate_Type()
)
hm2TrafficMgmtIfEgressShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfEgressShapingRate.setStatus("current")


class _Hm2TrafficMgmtIfEgressShapingRateUnit_Type(Integer32):
    """Custom type hm2TrafficMgmtIfEgressShapingRateUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("percent", 1))
    )


_Hm2TrafficMgmtIfEgressShapingRateUnit_Type.__name__ = "Integer32"
_Hm2TrafficMgmtIfEgressShapingRateUnit_Object = MibTableColumn
hm2TrafficMgmtIfEgressShapingRateUnit = _Hm2TrafficMgmtIfEgressShapingRateUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 3),
    _Hm2TrafficMgmtIfEgressShapingRateUnit_Type()
)
hm2TrafficMgmtIfEgressShapingRateUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfEgressShapingRateUnit.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type(Integer32):
    """Custom type hm2TrafficMgmtIfIngressStormCtlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type.__name__ = "Integer32"
_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlThresholdUnit = _Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 4),
    _Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type()
)
hm2TrafficMgmtIfIngressStormCtlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlThresholdUnit.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlBcastMode_Type(HmEnabledStatus):
    """Custom type hm2TrafficMgmtIfIngressStormCtlBcastMode based on HmEnabledStatus"""


_Hm2TrafficMgmtIfIngressStormCtlBcastMode_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlBcastMode = _Hm2TrafficMgmtIfIngressStormCtlBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 5),
    _Hm2TrafficMgmtIfIngressStormCtlBcastMode_Type()
)
hm2TrafficMgmtIfIngressStormCtlBcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlBcastMode.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type(Unsigned32):
    """Custom type hm2TrafficMgmtIfIngressStormCtlBcastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type.__name__ = "Unsigned32"
_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlBcastThreshold = _Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 6),
    _Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type()
)
hm2TrafficMgmtIfIngressStormCtlBcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlBcastThreshold.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlMcastMode_Type(HmEnabledStatus):
    """Custom type hm2TrafficMgmtIfIngressStormCtlMcastMode based on HmEnabledStatus"""


_Hm2TrafficMgmtIfIngressStormCtlMcastMode_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlMcastMode = _Hm2TrafficMgmtIfIngressStormCtlMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 7),
    _Hm2TrafficMgmtIfIngressStormCtlMcastMode_Type()
)
hm2TrafficMgmtIfIngressStormCtlMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlMcastMode.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type(Unsigned32):
    """Custom type hm2TrafficMgmtIfIngressStormCtlMcastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type.__name__ = "Unsigned32"
_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlMcastThreshold = _Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 8),
    _Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type()
)
hm2TrafficMgmtIfIngressStormCtlMcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlMcastThreshold.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlUcastMode_Type(HmEnabledStatus):
    """Custom type hm2TrafficMgmtIfIngressStormCtlUcastMode based on HmEnabledStatus"""


_Hm2TrafficMgmtIfIngressStormCtlUcastMode_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlUcastMode = _Hm2TrafficMgmtIfIngressStormCtlUcastMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 9),
    _Hm2TrafficMgmtIfIngressStormCtlUcastMode_Type()
)
hm2TrafficMgmtIfIngressStormCtlUcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlUcastMode.setStatus("current")


class _Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type(Unsigned32):
    """Custom type hm2TrafficMgmtIfIngressStormCtlUcastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type.__name__ = "Unsigned32"
_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Object = MibTableColumn
hm2TrafficMgmtIfIngressStormCtlUcastThreshold = _Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 1, 1, 10),
    _Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type()
)
hm2TrafficMgmtIfIngressStormCtlUcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIfIngressStormCtlUcastThreshold.setStatus("current")


class _Hm2TrafficMgmtFlowControl_Type(HmEnabledStatus):
    """Custom type hm2TrafficMgmtFlowControl based on HmEnabledStatus"""


_Hm2TrafficMgmtFlowControl_Object = MibScalar
hm2TrafficMgmtFlowControl = _Hm2TrafficMgmtFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 2),
    _Hm2TrafficMgmtFlowControl_Type()
)
hm2TrafficMgmtFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficMgmtFlowControl.setStatus("current")


class _Hm2TrafficMgmtIngressStormBucketType_Type(Integer32):
    """Custom type hm2TrafficMgmtIngressStormBucketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multi-bucket", 2),
          ("single-bucket", 1))
    )


_Hm2TrafficMgmtIngressStormBucketType_Type.__name__ = "Integer32"
_Hm2TrafficMgmtIngressStormBucketType_Object = MibScalar
hm2TrafficMgmtIngressStormBucketType = _Hm2TrafficMgmtIngressStormBucketType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 31, 1, 3),
    _Hm2TrafficMgmtIngressStormBucketType_Type()
)
hm2TrafficMgmtIngressStormBucketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrafficMgmtIngressStormBucketType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-TRAFFICMGMT-MIB",
    **{"hm2TrafficMgmtMib": hm2TrafficMgmtMib,
       "hm2TrafficMgmtMibNotifications": hm2TrafficMgmtMibNotifications,
       "hm2TrafficMgmtMibObjects": hm2TrafficMgmtMibObjects,
       "hm2TrafficMgmtIfTable": hm2TrafficMgmtIfTable,
       "hm2TrafficMgmtIfEntry": hm2TrafficMgmtIfEntry,
       "hm2TrafficMgmtIfFlowControl": hm2TrafficMgmtIfFlowControl,
       "hm2TrafficMgmtIfEgressShapingRate": hm2TrafficMgmtIfEgressShapingRate,
       "hm2TrafficMgmtIfEgressShapingRateUnit": hm2TrafficMgmtIfEgressShapingRateUnit,
       "hm2TrafficMgmtIfIngressStormCtlThresholdUnit": hm2TrafficMgmtIfIngressStormCtlThresholdUnit,
       "hm2TrafficMgmtIfIngressStormCtlBcastMode": hm2TrafficMgmtIfIngressStormCtlBcastMode,
       "hm2TrafficMgmtIfIngressStormCtlBcastThreshold": hm2TrafficMgmtIfIngressStormCtlBcastThreshold,
       "hm2TrafficMgmtIfIngressStormCtlMcastMode": hm2TrafficMgmtIfIngressStormCtlMcastMode,
       "hm2TrafficMgmtIfIngressStormCtlMcastThreshold": hm2TrafficMgmtIfIngressStormCtlMcastThreshold,
       "hm2TrafficMgmtIfIngressStormCtlUcastMode": hm2TrafficMgmtIfIngressStormCtlUcastMode,
       "hm2TrafficMgmtIfIngressStormCtlUcastThreshold": hm2TrafficMgmtIfIngressStormCtlUcastThreshold,
       "hm2TrafficMgmtFlowControl": hm2TrafficMgmtFlowControl,
       "hm2TrafficMgmtIngressStormBucketType": hm2TrafficMgmtIngressStormBucketType}
)
