# SNMP MIB module (TPLINK-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:36 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkRipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40)
)
tplinkRipMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkRipMIBObjects_ObjectIdentity = ObjectIdentity
tplinkRipMIBObjects = _TplinkRipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1)
)
_TpRipBasicConfig_ObjectIdentity = ObjectIdentity
tpRipBasicConfig = _TpRipBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1)
)


class _TpRipProtocolCtrl_Type(Integer32):
    """Custom type tpRipProtocolCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipProtocolCtrl_Type.__name__ = "Integer32"
_TpRipProtocolCtrl_Object = MibScalar
tpRipProtocolCtrl = _TpRipProtocolCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 1),
    _TpRipProtocolCtrl_Type()
)
tpRipProtocolCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipProtocolCtrl.setStatus("current")


class _TpRipProtocolVersion_Type(Integer32):
    """Custom type tpRipProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("ripv1", 1),
          ("ripv2", 2))
    )


_TpRipProtocolVersion_Type.__name__ = "Integer32"
_TpRipProtocolVersion_Object = MibScalar
tpRipProtocolVersion = _TpRipProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 2),
    _TpRipProtocolVersion_Type()
)
tpRipProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipProtocolVersion.setStatus("current")


class _TpRipDistance_Type(Integer32):
    """Custom type tpRipDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpRipDistance_Type.__name__ = "Integer32"
_TpRipDistance_Object = MibScalar
tpRipDistance = _TpRipDistance_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 3),
    _TpRipDistance_Type()
)
tpRipDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipDistance.setStatus("current")


class _TpRipAutoSumm_Type(Integer32):
    """Custom type tpRipAutoSumm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipAutoSumm_Type.__name__ = "Integer32"
_TpRipAutoSumm_Object = MibScalar
tpRipAutoSumm = _TpRipAutoSumm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 4),
    _TpRipAutoSumm_Type()
)
tpRipAutoSumm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipAutoSumm.setStatus("current")


class _TpRipDefaultMetric_Type(Integer32):
    """Custom type tpRipDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TpRipDefaultMetric_Type.__name__ = "Integer32"
_TpRipDefaultMetric_Object = MibScalar
tpRipDefaultMetric = _TpRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 5),
    _TpRipDefaultMetric_Type()
)
tpRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipDefaultMetric.setStatus("current")


class _TpRipRedistriStatic_Type(Integer32):
    """Custom type tpRipRedistriStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipRedistriStatic_Type.__name__ = "Integer32"
_TpRipRedistriStatic_Object = MibScalar
tpRipRedistriStatic = _TpRipRedistriStatic_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 6),
    _TpRipRedistriStatic_Type()
)
tpRipRedistriStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipRedistriStatic.setStatus("current")


class _TpRipRedistriOspf_Type(Integer32):
    """Custom type tpRipRedistriOspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipRedistriOspf_Type.__name__ = "Integer32"
_TpRipRedistriOspf_Object = MibScalar
tpRipRedistriOspf = _TpRipRedistriOspf_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 7),
    _TpRipRedistriOspf_Type()
)
tpRipRedistriOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipRedistriOspf.setStatus("current")


class _TpRipRedistStaticMetric_Type(Integer32):
    """Custom type tpRipRedistStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TpRipRedistStaticMetric_Type.__name__ = "Integer32"
_TpRipRedistStaticMetric_Object = MibScalar
tpRipRedistStaticMetric = _TpRipRedistStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 8),
    _TpRipRedistStaticMetric_Type()
)
tpRipRedistStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipRedistStaticMetric.setStatus("current")


class _TpRipRedistOspfMetric_Type(Integer32):
    """Custom type tpRipRedistOspfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TpRipRedistOspfMetric_Type.__name__ = "Integer32"
_TpRipRedistOspfMetric_Object = MibScalar
tpRipRedistOspfMetric = _TpRipRedistOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 9),
    _TpRipRedistOspfMetric_Type()
)
tpRipRedistOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipRedistOspfMetric.setStatus("current")


class _TpRipUpdateTimer_Type(Integer32):
    """Custom type tpRipUpdateTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TpRipUpdateTimer_Type.__name__ = "Integer32"
_TpRipUpdateTimer_Object = MibScalar
tpRipUpdateTimer = _TpRipUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 10),
    _TpRipUpdateTimer_Type()
)
tpRipUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipUpdateTimer.setStatus("current")


class _TpRipTimeOutTimer_Type(Integer32):
    """Custom type tpRipTimeOutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpRipTimeOutTimer_Type.__name__ = "Integer32"
_TpRipTimeOutTimer_Object = MibScalar
tpRipTimeOutTimer = _TpRipTimeOutTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 11),
    _TpRipTimeOutTimer_Type()
)
tpRipTimeOutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipTimeOutTimer.setStatus("current")


class _TpRipGarbageTimer_Type(Integer32):
    """Custom type tpRipGarbageTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_TpRipGarbageTimer_Type.__name__ = "Integer32"
_TpRipGarbageTimer_Object = MibScalar
tpRipGarbageTimer = _TpRipGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 12),
    _TpRipGarbageTimer_Type()
)
tpRipGarbageTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipGarbageTimer.setStatus("current")
_TpRipNetworkConfig_ObjectIdentity = ObjectIdentity
tpRipNetworkConfig = _TpRipNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2)
)
_TpRipNetworkTable_Object = MibTable
tpRipNetworkTable = _TpRipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpRipNetworkTable.setStatus("current")
_TpRipNetworkEntry_Object = MibTableRow
tpRipNetworkEntry = _TpRipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1)
)
tpRipNetworkEntry.setIndexNames(
    (0, "TPLINK-RIP-MIB", "tpRipNetworkAddress"),
)
if mibBuilder.loadTexts:
    tpRipNetworkEntry.setStatus("current")
_TpRipNetworkAddress_Type = IpAddress
_TpRipNetworkAddress_Object = MibTableColumn
tpRipNetworkAddress = _TpRipNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1, 1),
    _TpRipNetworkAddress_Type()
)
tpRipNetworkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRipNetworkAddress.setStatus("current")
_TpRipNetworkStatus_Type = TPRowStatus
_TpRipNetworkStatus_Object = MibTableColumn
tpRipNetworkStatus = _TpRipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1, 2),
    _TpRipNetworkStatus_Type()
)
tpRipNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRipNetworkStatus.setStatus("current")
_TpRipInterfaceConfig_ObjectIdentity = ObjectIdentity
tpRipInterfaceConfig = _TpRipInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3)
)
_TpRipInterfaceTable_Object = MibTable
tpRipInterfaceTable = _TpRipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpRipInterfaceTable.setStatus("current")
_TpRipInterfaceEntry_Object = MibTableRow
tpRipInterfaceEntry = _TpRipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1)
)
tpRipInterfaceEntry.setIndexNames(
    (0, "TPLINK-RIP-MIB", "tpRipInterfaceID"),
)
if mibBuilder.loadTexts:
    tpRipInterfaceEntry.setStatus("current")


class _TpRipInterfaceID_Type(OctetString):
    """Custom type tpRipInterfaceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpRipInterfaceID_Type.__name__ = "OctetString"
_TpRipInterfaceID_Object = MibTableColumn
tpRipInterfaceID = _TpRipInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 1),
    _TpRipInterfaceID_Type()
)
tpRipInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipInterfaceID.setStatus("current")


class _TpRipInterfaceStatus_Type(OctetString):
    """Custom type tpRipInterfaceStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TpRipInterfaceStatus_Type.__name__ = "OctetString"
_TpRipInterfaceStatus_Object = MibTableColumn
tpRipInterfaceStatus = _TpRipInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 2),
    _TpRipInterfaceStatus_Type()
)
tpRipInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipInterfaceStatus.setStatus("current")


class _TpRipInterfaceSendVersion_Type(Integer32):
    """Custom type tpRipInterfaceSendVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rip-1c", 3),
          ("ripv1", 1),
          ("ripv2", 2))
    )


_TpRipInterfaceSendVersion_Type.__name__ = "Integer32"
_TpRipInterfaceSendVersion_Object = MibTableColumn
tpRipInterfaceSendVersion = _TpRipInterfaceSendVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 3),
    _TpRipInterfaceSendVersion_Type()
)
tpRipInterfaceSendVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceSendVersion.setStatus("current")


class _TpRipInterfaceRecvVersion_Type(Integer32):
    """Custom type tpRipInterfaceRecvVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ripv1", 1),
          ("ripv2", 2))
    )


_TpRipInterfaceRecvVersion_Type.__name__ = "Integer32"
_TpRipInterfaceRecvVersion_Object = MibTableColumn
tpRipInterfaceRecvVersion = _TpRipInterfaceRecvVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 4),
    _TpRipInterfaceRecvVersion_Type()
)
tpRipInterfaceRecvVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceRecvVersion.setStatus("current")


class _TpRipInterfaceRIPv2Broad_Type(Integer32):
    """Custom type tpRipInterfaceRIPv2Broad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipInterfaceRIPv2Broad_Type.__name__ = "Integer32"
_TpRipInterfaceRIPv2Broad_Object = MibTableColumn
tpRipInterfaceRIPv2Broad = _TpRipInterfaceRIPv2Broad_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 5),
    _TpRipInterfaceRIPv2Broad_Type()
)
tpRipInterfaceRIPv2Broad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceRIPv2Broad.setStatus("current")


class _TpRipInterfaceAuthMode_Type(Integer32):
    """Custom type tpRipInterfaceAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_TpRipInterfaceAuthMode_Type.__name__ = "Integer32"
_TpRipInterfaceAuthMode_Object = MibTableColumn
tpRipInterfaceAuthMode = _TpRipInterfaceAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 6),
    _TpRipInterfaceAuthMode_Type()
)
tpRipInterfaceAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceAuthMode.setStatus("current")


class _TpRipInterfaceKeyID_Type(Integer32):
    """Custom type tpRipInterfaceKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TpRipInterfaceKeyID_Type.__name__ = "Integer32"
_TpRipInterfaceKeyID_Object = MibTableColumn
tpRipInterfaceKeyID = _TpRipInterfaceKeyID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 7),
    _TpRipInterfaceKeyID_Type()
)
tpRipInterfaceKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceKeyID.setStatus("current")


class _TpRipInterfaceKey_Type(OctetString):
    """Custom type tpRipInterfaceKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpRipInterfaceKey_Type.__name__ = "OctetString"
_TpRipInterfaceKey_Object = MibTableColumn
tpRipInterfaceKey = _TpRipInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 8),
    _TpRipInterfaceKey_Type()
)
tpRipInterfaceKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceKey.setStatus("current")


class _TpRipInterfaceSplitHorizon_Type(Integer32):
    """Custom type tpRipInterfaceSplitHorizon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipInterfaceSplitHorizon_Type.__name__ = "Integer32"
_TpRipInterfaceSplitHorizon_Object = MibTableColumn
tpRipInterfaceSplitHorizon = _TpRipInterfaceSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 9),
    _TpRipInterfaceSplitHorizon_Type()
)
tpRipInterfaceSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfaceSplitHorizon.setStatus("current")


class _TpRipInterfacePoisonReverse_Type(Integer32):
    """Custom type tpRipInterfacePoisonReverse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRipInterfacePoisonReverse_Type.__name__ = "Integer32"
_TpRipInterfacePoisonReverse_Object = MibTableColumn
tpRipInterfacePoisonReverse = _TpRipInterfacePoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 10),
    _TpRipInterfacePoisonReverse_Type()
)
tpRipInterfacePoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRipInterfacePoisonReverse.setStatus("current")
_TpRipRouteItems_ObjectIdentity = ObjectIdentity
tpRipRouteItems = _TpRipRouteItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4)
)
_TpRipRouteTable_Object = MibTable
tpRipRouteTable = _TpRipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpRipRouteTable.setStatus("current")
_TpRipRouteEntry_Object = MibTableRow
tpRipRouteEntry = _TpRipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1)
)
tpRipRouteEntry.setIndexNames(
    (0, "TPLINK-RIP-MIB", "tpRipIpAddressMask"),
)
if mibBuilder.loadTexts:
    tpRipRouteEntry.setStatus("current")


class _TpRipIpAddressMask_Type(OctetString):
    """Custom type tpRipIpAddressMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpRipIpAddressMask_Type.__name__ = "OctetString"
_TpRipIpAddressMask_Object = MibTableColumn
tpRipIpAddressMask = _TpRipIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 1),
    _TpRipIpAddressMask_Type()
)
tpRipIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipIpAddressMask.setStatus("current")
_TpRipGateway_Type = IpAddress
_TpRipGateway_Object = MibTableColumn
tpRipGateway = _TpRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 2),
    _TpRipGateway_Type()
)
tpRipGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipGateway.setStatus("current")


class _TpRipMetric_Type(Integer32):
    """Custom type tpRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TpRipMetric_Type.__name__ = "Integer32"
_TpRipMetric_Object = MibTableColumn
tpRipMetric = _TpRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 3),
    _TpRipMetric_Type()
)
tpRipMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipMetric.setStatus("current")


class _TpRipInterfaceName_Type(OctetString):
    """Custom type tpRipInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpRipInterfaceName_Type.__name__ = "OctetString"
_TpRipInterfaceName_Object = MibTableColumn
tpRipInterfaceName = _TpRipInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 4),
    _TpRipInterfaceName_Type()
)
tpRipInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipInterfaceName.setStatus("current")


class _TpRipTimers_Type(Integer32):
    """Custom type tpRipTimers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TpRipTimers_Type.__name__ = "Integer32"
_TpRipTimers_Object = MibTableColumn
tpRipTimers = _TpRipTimers_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 5),
    _TpRipTimers_Type()
)
tpRipTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRipTimers.setStatus("current")
_TplinkRipNotifications_ObjectIdentity = ObjectIdentity
tplinkRipNotifications = _TplinkRipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 40, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-RIP-MIB",
    **{"tplinkRipMIB": tplinkRipMIB,
       "tplinkRipMIBObjects": tplinkRipMIBObjects,
       "tpRipBasicConfig": tpRipBasicConfig,
       "tpRipProtocolCtrl": tpRipProtocolCtrl,
       "tpRipProtocolVersion": tpRipProtocolVersion,
       "tpRipDistance": tpRipDistance,
       "tpRipAutoSumm": tpRipAutoSumm,
       "tpRipDefaultMetric": tpRipDefaultMetric,
       "tpRipRedistriStatic": tpRipRedistriStatic,
       "tpRipRedistriOspf": tpRipRedistriOspf,
       "tpRipRedistStaticMetric": tpRipRedistStaticMetric,
       "tpRipRedistOspfMetric": tpRipRedistOspfMetric,
       "tpRipUpdateTimer": tpRipUpdateTimer,
       "tpRipTimeOutTimer": tpRipTimeOutTimer,
       "tpRipGarbageTimer": tpRipGarbageTimer,
       "tpRipNetworkConfig": tpRipNetworkConfig,
       "tpRipNetworkTable": tpRipNetworkTable,
       "tpRipNetworkEntry": tpRipNetworkEntry,
       "tpRipNetworkAddress": tpRipNetworkAddress,
       "tpRipNetworkStatus": tpRipNetworkStatus,
       "tpRipInterfaceConfig": tpRipInterfaceConfig,
       "tpRipInterfaceTable": tpRipInterfaceTable,
       "tpRipInterfaceEntry": tpRipInterfaceEntry,
       "tpRipInterfaceID": tpRipInterfaceID,
       "tpRipInterfaceStatus": tpRipInterfaceStatus,
       "tpRipInterfaceSendVersion": tpRipInterfaceSendVersion,
       "tpRipInterfaceRecvVersion": tpRipInterfaceRecvVersion,
       "tpRipInterfaceRIPv2Broad": tpRipInterfaceRIPv2Broad,
       "tpRipInterfaceAuthMode": tpRipInterfaceAuthMode,
       "tpRipInterfaceKeyID": tpRipInterfaceKeyID,
       "tpRipInterfaceKey": tpRipInterfaceKey,
       "tpRipInterfaceSplitHorizon": tpRipInterfaceSplitHorizon,
       "tpRipInterfacePoisonReverse": tpRipInterfacePoisonReverse,
       "tpRipRouteItems": tpRipRouteItems,
       "tpRipRouteTable": tpRipRouteTable,
       "tpRipRouteEntry": tpRipRouteEntry,
       "tpRipIpAddressMask": tpRipIpAddressMask,
       "tpRipGateway": tpRipGateway,
       "tpRipMetric": tpRipMetric,
       "tpRipInterfaceName": tpRipInterfaceName,
       "tpRipTimers": tpRipTimers,
       "tplinkRipNotifications": tplinkRipNotifications}
)
