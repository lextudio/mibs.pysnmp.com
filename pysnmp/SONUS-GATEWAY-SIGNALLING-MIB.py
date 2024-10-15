# SNMP MIB module (SONUS-GATEWAY-SIGNALLING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-GATEWAY-SIGNALLING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:57 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(SonusAdminState,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusServiceState")


# MODULE-IDENTITY

sonusGatewaySignallingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusGatewaySignallingMIBObjects_ObjectIdentity = ObjectIdentity
sonusGatewaySignallingMIBObjects = _SonusGatewaySignallingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1)
)
_SonusGwSigTimerObjects_ObjectIdentity = ObjectIdentity
sonusGwSigTimerObjects = _SonusGwSigTimerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1)
)


class _SonusGwSigSrvTimerT301_Type(Integer32):
    """Custom type sonusGwSigSrvTimerT301 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigSrvTimerT301_Type.__name__ = "Integer32"
_SonusGwSigSrvTimerT301_Object = MibScalar
sonusGwSigSrvTimerT301 = _SonusGwSigSrvTimerT301_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 1),
    _SonusGwSigSrvTimerT301_Type()
)
sonusGwSigSrvTimerT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigSrvTimerT301.setStatus("obsolete")


class _SonusGwSigSrvTimerT303_Type(Integer32):
    """Custom type sonusGwSigSrvTimerT303 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigSrvTimerT303_Type.__name__ = "Integer32"
_SonusGwSigSrvTimerT303_Object = MibScalar
sonusGwSigSrvTimerT303 = _SonusGwSigSrvTimerT303_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 2),
    _SonusGwSigSrvTimerT303_Type()
)
sonusGwSigSrvTimerT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigSrvTimerT303.setStatus("obsolete")


class _SonusGwSigTimerEstabish_Type(Integer32):
    """Custom type sonusGwSigTimerEstabish based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigTimerEstabish_Type.__name__ = "Integer32"
_SonusGwSigTimerEstabish_Object = MibScalar
sonusGwSigTimerEstabish = _SonusGwSigTimerEstabish_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 3),
    _SonusGwSigTimerEstabish_Type()
)
sonusGwSigTimerEstabish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigTimerEstabish.setStatus("current")


class _SonusGwSigTimerKeepalive_Type(Integer32):
    """Custom type sonusGwSigTimerKeepalive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigTimerKeepalive_Type.__name__ = "Integer32"
_SonusGwSigTimerKeepalive_Object = MibScalar
sonusGwSigTimerKeepalive = _SonusGwSigTimerKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 4),
    _SonusGwSigTimerKeepalive_Type()
)
sonusGwSigTimerKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigTimerKeepalive.setStatus("current")
_SonusGwSigActionObjects_ObjectIdentity = ObjectIdentity
sonusGwSigActionObjects = _SonusGwSigActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2)
)


class _SonusGwSigAction_Type(Integer32):
    """Custom type sonusGwSigAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("none", 3),
          ("open", 1))
    )


_SonusGwSigAction_Type.__name__ = "Integer32"
_SonusGwSigAction_Object = MibScalar
sonusGwSigAction = _SonusGwSigAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 1),
    _SonusGwSigAction_Type()
)
sonusGwSigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigAction.setStatus("current")


class _SonusGwSigActionDestIpAddr_Type(IpAddress):
    """Custom type sonusGwSigActionDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SonusGwSigActionDestIpAddr_Object = MibScalar
sonusGwSigActionDestIpAddr = _SonusGwSigActionDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 2),
    _SonusGwSigActionDestIpAddr_Type()
)
sonusGwSigActionDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigActionDestIpAddr.setStatus("current")


class _SonusGwSigActionDestPort_Type(Integer32):
    """Custom type sonusGwSigActionDestPort based on Integer32"""
    defaultValue = 2569

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigActionDestPort_Type.__name__ = "Integer32"
_SonusGwSigActionDestPort_Object = MibScalar
sonusGwSigActionDestPort = _SonusGwSigActionDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 3),
    _SonusGwSigActionDestPort_Type()
)
sonusGwSigActionDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigActionDestPort.setStatus("current")


class _SonusGwSigActionDir_Type(Integer32):
    """Custom type sonusGwSigActionDir based on Integer32"""
    defaultValue = 1

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
          ("from", 2),
          ("to", 1))
    )


_SonusGwSigActionDir_Type.__name__ = "Integer32"
_SonusGwSigActionDir_Object = MibScalar
sonusGwSigActionDir = _SonusGwSigActionDir_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 4),
    _SonusGwSigActionDir_Type()
)
sonusGwSigActionDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigActionDir.setStatus("current")
_SonusGwSigPortTable_Object = MibTable
sonusGwSigPortTable = _SonusGwSigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sonusGwSigPortTable.setStatus("current")
_SonusGwSigPortEntry_Object = MibTableRow
sonusGwSigPortEntry = _SonusGwSigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1)
)
sonusGwSigPortEntry.setIndexNames(
    (0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigPortIndex"),
)
if mibBuilder.loadTexts:
    sonusGwSigPortEntry.setStatus("current")
_SonusGwSigPortIndex_Type = Integer32
_SonusGwSigPortIndex_Object = MibTableColumn
sonusGwSigPortIndex = _SonusGwSigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 1),
    _SonusGwSigPortIndex_Type()
)
sonusGwSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortIndex.setStatus("current")


class _SonusGwSigPortIpAddress_Type(IpAddress):
    """Custom type sonusGwSigPortIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SonusGwSigPortIpAddress_Object = MibTableColumn
sonusGwSigPortIpAddress = _SonusGwSigPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 2),
    _SonusGwSigPortIpAddress_Type()
)
sonusGwSigPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortIpAddress.setStatus("current")


class _SonusGwSigPortNum_Type(Integer32):
    """Custom type sonusGwSigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGwSigPortNum_Type.__name__ = "Integer32"
_SonusGwSigPortNum_Object = MibTableColumn
sonusGwSigPortNum = _SonusGwSigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 3),
    _SonusGwSigPortNum_Type()
)
sonusGwSigPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortNum.setStatus("current")


class _SonusGwSigPortInterface_Type(Integer32):
    """Custom type sonusGwSigPortInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgtNif", 1),
          ("nif", 2))
    )


_SonusGwSigPortInterface_Type.__name__ = "Integer32"
_SonusGwSigPortInterface_Object = MibTableColumn
sonusGwSigPortInterface = _SonusGwSigPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 4),
    _SonusGwSigPortInterface_Type()
)
sonusGwSigPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortInterface.setStatus("current")


class _SonusGwSigPortRole_Type(Integer32):
    """Custom type sonusGwSigPortRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SonusGwSigPortRole_Type.__name__ = "Integer32"
_SonusGwSigPortRole_Object = MibTableColumn
sonusGwSigPortRole = _SonusGwSigPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 5),
    _SonusGwSigPortRole_Type()
)
sonusGwSigPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortRole.setStatus("current")


class _SonusGwSigPortMode_Type(SonusServiceState):
    """Custom type sonusGwSigPortMode based on SonusServiceState"""


_SonusGwSigPortMode_Object = MibTableColumn
sonusGwSigPortMode = _SonusGwSigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 6),
    _SonusGwSigPortMode_Type()
)
sonusGwSigPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortMode.setStatus("current")


class _SonusGwSigPortState_Type(SonusAdminState):
    """Custom type sonusGwSigPortState based on SonusAdminState"""


_SonusGwSigPortState_Object = MibTableColumn
sonusGwSigPortState = _SonusGwSigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 7),
    _SonusGwSigPortState_Type()
)
sonusGwSigPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortState.setStatus("current")
_SonusGwSigPortRowStatus_Type = RowStatus
_SonusGwSigPortRowStatus_Object = MibTableColumn
sonusGwSigPortRowStatus = _SonusGwSigPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 8),
    _SonusGwSigPortRowStatus_Type()
)
sonusGwSigPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGwSigPortRowStatus.setStatus("current")
_SonusGwSigPortStatTable_Object = MibTable
sonusGwSigPortStatTable = _SonusGwSigPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sonusGwSigPortStatTable.setStatus("current")
_SonusGwSigPortStatEntry_Object = MibTableRow
sonusGwSigPortStatEntry = _SonusGwSigPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1)
)
sonusGwSigPortStatEntry.setIndexNames(
    (0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigPortStatIndex"),
)
if mibBuilder.loadTexts:
    sonusGwSigPortStatEntry.setStatus("current")
_SonusGwSigPortStatIndex_Type = Integer32
_SonusGwSigPortStatIndex_Object = MibTableColumn
sonusGwSigPortStatIndex = _SonusGwSigPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 1),
    _SonusGwSigPortStatIndex_Type()
)
sonusGwSigPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatIndex.setStatus("current")
_SonusGwSigPortStatIpAddress_Type = IpAddress
_SonusGwSigPortStatIpAddress_Object = MibTableColumn
sonusGwSigPortStatIpAddress = _SonusGwSigPortStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 2),
    _SonusGwSigPortStatIpAddress_Type()
)
sonusGwSigPortStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatIpAddress.setStatus("current")
_SonusGwSigPortStatNum_Type = Integer32
_SonusGwSigPortStatNum_Object = MibTableColumn
sonusGwSigPortStatNum = _SonusGwSigPortStatNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 3),
    _SonusGwSigPortStatNum_Type()
)
sonusGwSigPortStatNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatNum.setStatus("current")


class _SonusGwSigPortStatInterface_Type(Integer32):
    """Custom type sonusGwSigPortStatInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgtNif", 1),
          ("nif", 2))
    )


_SonusGwSigPortStatInterface_Type.__name__ = "Integer32"
_SonusGwSigPortStatInterface_Object = MibTableColumn
sonusGwSigPortStatInterface = _SonusGwSigPortStatInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 4),
    _SonusGwSigPortStatInterface_Type()
)
sonusGwSigPortStatInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatInterface.setStatus("current")


class _SonusGwSigPortStatRole_Type(Integer32):
    """Custom type sonusGwSigPortStatRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SonusGwSigPortStatRole_Type.__name__ = "Integer32"
_SonusGwSigPortStatRole_Object = MibTableColumn
sonusGwSigPortStatRole = _SonusGwSigPortStatRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 5),
    _SonusGwSigPortStatRole_Type()
)
sonusGwSigPortStatRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatRole.setStatus("current")
_SonusGwSigPortStatNif_Type = Integer32
_SonusGwSigPortStatNif_Object = MibTableColumn
sonusGwSigPortStatNif = _SonusGwSigPortStatNif_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 6),
    _SonusGwSigPortStatNif_Type()
)
sonusGwSigPortStatNif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatNif.setStatus("current")
_SonusGwSigPortStatState_Type = SonusServiceState
_SonusGwSigPortStatState_Object = MibTableColumn
sonusGwSigPortStatState = _SonusGwSigPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 7),
    _SonusGwSigPortStatState_Type()
)
sonusGwSigPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigPortStatState.setStatus("current")
_SonusGwSigActGwStatusTable_Object = MibTable
sonusGwSigActGwStatusTable = _SonusGwSigActGwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    sonusGwSigActGwStatusTable.setStatus("current")
_SonusGwSigActGwStatusEntry_Object = MibTableRow
sonusGwSigActGwStatusEntry = _SonusGwSigActGwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1)
)
sonusGwSigActGwStatusEntry.setIndexNames(
    (0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigActGwIpAddress"),
)
if mibBuilder.loadTexts:
    sonusGwSigActGwStatusEntry.setStatus("current")


class _SonusGwSigActGwName_Type(DisplayString):
    """Custom type sonusGwSigActGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusGwSigActGwName_Type.__name__ = "DisplayString"
_SonusGwSigActGwName_Object = MibTableColumn
sonusGwSigActGwName = _SonusGwSigActGwName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 1),
    _SonusGwSigActGwName_Type()
)
sonusGwSigActGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwName.setStatus("deprecated")
_SonusGwSigActGwIpAddress_Type = IpAddress
_SonusGwSigActGwIpAddress_Object = MibTableColumn
sonusGwSigActGwIpAddress = _SonusGwSigActGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 2),
    _SonusGwSigActGwIpAddress_Type()
)
sonusGwSigActGwIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwIpAddress.setStatus("current")


class _SonusGwSigActGwLnkProto_Type(Integer32):
    """Custom type sonusGwSigActGwLnkProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("ioi", 1))
    )


_SonusGwSigActGwLnkProto_Type.__name__ = "Integer32"
_SonusGwSigActGwLnkProto_Object = MibTableColumn
sonusGwSigActGwLnkProto = _SonusGwSigActGwLnkProto_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 3),
    _SonusGwSigActGwLnkProto_Type()
)
sonusGwSigActGwLnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwLnkProto.setStatus("current")
_SonusGwSigActGwNumActiveCalls_Type = Integer32
_SonusGwSigActGwNumActiveCalls_Object = MibTableColumn
sonusGwSigActGwNumActiveCalls = _SonusGwSigActGwNumActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 4),
    _SonusGwSigActGwNumActiveCalls_Type()
)
sonusGwSigActGwNumActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwNumActiveCalls.setStatus("current")
_SonusGwSigActGwNumActiveCallsTo_Type = Integer32
_SonusGwSigActGwNumActiveCallsTo_Object = MibTableColumn
sonusGwSigActGwNumActiveCallsTo = _SonusGwSigActGwNumActiveCallsTo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 5),
    _SonusGwSigActGwNumActiveCallsTo_Type()
)
sonusGwSigActGwNumActiveCallsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwNumActiveCallsTo.setStatus("current")
_SonusGwSigActGwNumActiveCallsFrom_Type = Integer32
_SonusGwSigActGwNumActiveCallsFrom_Object = MibTableColumn
sonusGwSigActGwNumActiveCallsFrom = _SonusGwSigActGwNumActiveCallsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 6),
    _SonusGwSigActGwNumActiveCallsFrom_Type()
)
sonusGwSigActGwNumActiveCallsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwNumActiveCallsFrom.setStatus("current")
_SonusGwSigActGwToState_Type = SonusServiceState
_SonusGwSigActGwToState_Object = MibTableColumn
sonusGwSigActGwToState = _SonusGwSigActGwToState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 7),
    _SonusGwSigActGwToState_Type()
)
sonusGwSigActGwToState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToState.setStatus("current")
_SonusGwSigActGwFromState_Type = SonusServiceState
_SonusGwSigActGwFromState_Object = MibTableColumn
sonusGwSigActGwFromState = _SonusGwSigActGwFromState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 8),
    _SonusGwSigActGwFromState_Type()
)
sonusGwSigActGwFromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromState.setStatus("current")


class _SonusGwSigActGwInterface_Type(Integer32):
    """Custom type sonusGwSigActGwInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgtNif", 1),
          ("nif", 2))
    )


_SonusGwSigActGwInterface_Type.__name__ = "Integer32"
_SonusGwSigActGwInterface_Object = MibTableColumn
sonusGwSigActGwInterface = _SonusGwSigActGwInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 9),
    _SonusGwSigActGwInterface_Type()
)
sonusGwSigActGwInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwInterface.setStatus("current")
_SonusGwSigActGwFromBytesSent_Type = Counter64
_SonusGwSigActGwFromBytesSent_Object = MibTableColumn
sonusGwSigActGwFromBytesSent = _SonusGwSigActGwFromBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 10),
    _SonusGwSigActGwFromBytesSent_Type()
)
sonusGwSigActGwFromBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromBytesSent.setStatus("current")
_SonusGwSigActGwFromPdusSent_Type = Counter64
_SonusGwSigActGwFromPdusSent_Object = MibTableColumn
sonusGwSigActGwFromPdusSent = _SonusGwSigActGwFromPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 11),
    _SonusGwSigActGwFromPdusSent_Type()
)
sonusGwSigActGwFromPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromPdusSent.setStatus("current")
_SonusGwSigActGwFromBytesReceived_Type = Counter64
_SonusGwSigActGwFromBytesReceived_Object = MibTableColumn
sonusGwSigActGwFromBytesReceived = _SonusGwSigActGwFromBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 12),
    _SonusGwSigActGwFromBytesReceived_Type()
)
sonusGwSigActGwFromBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromBytesReceived.setStatus("current")
_SonusGwSigActGwFromPdusReceived_Type = Counter64
_SonusGwSigActGwFromPdusReceived_Object = MibTableColumn
sonusGwSigActGwFromPdusReceived = _SonusGwSigActGwFromPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 13),
    _SonusGwSigActGwFromPdusReceived_Type()
)
sonusGwSigActGwFromPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromPdusReceived.setStatus("current")
_SonusGwSigActGwFromTotalCalls_Type = Counter64
_SonusGwSigActGwFromTotalCalls_Object = MibTableColumn
sonusGwSigActGwFromTotalCalls = _SonusGwSigActGwFromTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 14),
    _SonusGwSigActGwFromTotalCalls_Type()
)
sonusGwSigActGwFromTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromTotalCalls.setStatus("current")
_SonusGwSigActGwFromCallRate_Type = Integer32
_SonusGwSigActGwFromCallRate_Object = MibTableColumn
sonusGwSigActGwFromCallRate = _SonusGwSigActGwFromCallRate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 15),
    _SonusGwSigActGwFromCallRate_Type()
)
sonusGwSigActGwFromCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromCallRate.setStatus("current")
_SonusGwSigActGwToBytesSent_Type = Counter64
_SonusGwSigActGwToBytesSent_Object = MibTableColumn
sonusGwSigActGwToBytesSent = _SonusGwSigActGwToBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 16),
    _SonusGwSigActGwToBytesSent_Type()
)
sonusGwSigActGwToBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToBytesSent.setStatus("current")
_SonusGwSigActGwToPdusSent_Type = Counter64
_SonusGwSigActGwToPdusSent_Object = MibTableColumn
sonusGwSigActGwToPdusSent = _SonusGwSigActGwToPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 17),
    _SonusGwSigActGwToPdusSent_Type()
)
sonusGwSigActGwToPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToPdusSent.setStatus("current")
_SonusGwSigActGwToBytesReceived_Type = Counter64
_SonusGwSigActGwToBytesReceived_Object = MibTableColumn
sonusGwSigActGwToBytesReceived = _SonusGwSigActGwToBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 18),
    _SonusGwSigActGwToBytesReceived_Type()
)
sonusGwSigActGwToBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToBytesReceived.setStatus("current")
_SonusGwSigActGwToPdusReceived_Type = Counter64
_SonusGwSigActGwToPdusReceived_Object = MibTableColumn
sonusGwSigActGwToPdusReceived = _SonusGwSigActGwToPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 19),
    _SonusGwSigActGwToPdusReceived_Type()
)
sonusGwSigActGwToPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToPdusReceived.setStatus("current")
_SonusGwSigActGwToTotalCalls_Type = Counter64
_SonusGwSigActGwToTotalCalls_Object = MibTableColumn
sonusGwSigActGwToTotalCalls = _SonusGwSigActGwToTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 20),
    _SonusGwSigActGwToTotalCalls_Type()
)
sonusGwSigActGwToTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToTotalCalls.setStatus("current")
_SonusGwSigActGwToCallRate_Type = Integer32
_SonusGwSigActGwToCallRate_Object = MibTableColumn
sonusGwSigActGwToCallRate = _SonusGwSigActGwToCallRate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 21),
    _SonusGwSigActGwToCallRate_Type()
)
sonusGwSigActGwToCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToCallRate.setStatus("current")
_SonusGwSigActGwFromLnkMajorVer_Type = Integer32
_SonusGwSigActGwFromLnkMajorVer_Object = MibTableColumn
sonusGwSigActGwFromLnkMajorVer = _SonusGwSigActGwFromLnkMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 22),
    _SonusGwSigActGwFromLnkMajorVer_Type()
)
sonusGwSigActGwFromLnkMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromLnkMajorVer.setStatus("current")
_SonusGwSigActGwFromLnkMinorVer_Type = Integer32
_SonusGwSigActGwFromLnkMinorVer_Object = MibTableColumn
sonusGwSigActGwFromLnkMinorVer = _SonusGwSigActGwFromLnkMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 23),
    _SonusGwSigActGwFromLnkMinorVer_Type()
)
sonusGwSigActGwFromLnkMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwFromLnkMinorVer.setStatus("current")
_SonusGwSigActGwToLnkMajorVer_Type = Integer32
_SonusGwSigActGwToLnkMajorVer_Object = MibTableColumn
sonusGwSigActGwToLnkMajorVer = _SonusGwSigActGwToLnkMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 24),
    _SonusGwSigActGwToLnkMajorVer_Type()
)
sonusGwSigActGwToLnkMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToLnkMajorVer.setStatus("current")
_SonusGwSigActGwToLnkMinorVer_Type = Integer32
_SonusGwSigActGwToLnkMinorVer_Object = MibTableColumn
sonusGwSigActGwToLnkMinorVer = _SonusGwSigActGwToLnkMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 25),
    _SonusGwSigActGwToLnkMinorVer_Type()
)
sonusGwSigActGwToLnkMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwSigActGwToLnkMinorVer.setStatus("current")
_SonusGatewaySignallingMIBNotifications_ObjectIdentity = ObjectIdentity
sonusGatewaySignallingMIBNotifications = _SonusGatewaySignallingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2)
)
_SonusGatewaySignallingMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusGatewaySignallingMIBNotificationsPrefix = _SonusGatewaySignallingMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0)
)
_SonusGatewaySignallingMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusGatewaySignallingMIBNotificationsObjects = _SonusGatewaySignallingMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1)
)


class _SonusGwRemoteGwName_Type(DisplayString):
    """Custom type sonusGwRemoteGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusGwRemoteGwName_Type.__name__ = "DisplayString"
_SonusGwRemoteGwName_Object = MibScalar
sonusGwRemoteGwName = _SonusGwRemoteGwName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 1),
    _SonusGwRemoteGwName_Type()
)
sonusGwRemoteGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwRemoteGwName.setStatus("deprecated")


class _SonusGwCloseReasonCode_Type(Integer32):
    """Custom type sonusGwCloseReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("administratorInitiatedClose", 1),
          ("closeRequestReceivedFromRemote", 2),
          ("configError", 5),
          ("internalError", 4),
          ("linkXmtCongestion", 21),
          ("openNackReceivedFromRemote", 22),
          ("recvCallSigReqFromUnknownGw", 6),
          ("recvDuplicateLinkOpenReq", 19),
          ("remoteNotResponding", 3),
          ("socketErrAlreadyConnected", 13),
          ("socketErrCantSendAfterShutdown", 15),
          ("socketErrConnectionResetByPeer", 11),
          ("socketErrConnectionTimedOut", 17),
          ("socketErrExceptionEvent", 20),
          ("socketErrNetworkDown", 7),
          ("socketErrNetworkReset", 9),
          ("socketErrNetworkUnreachable", 8),
          ("socketErrNoBufferSpaceAvail", 12),
          ("socketErrNotConnected", 14),
          ("socketErrSoftwareConnectionAbort", 10),
          ("socketErrTooManyReferences", 16),
          ("socketErrUnknown", 18))
    )


_SonusGwCloseReasonCode_Type.__name__ = "Integer32"
_SonusGwCloseReasonCode_Object = MibScalar
sonusGwCloseReasonCode = _SonusGwCloseReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 2),
    _SonusGwCloseReasonCode_Type()
)
sonusGwCloseReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwCloseReasonCode.setStatus("current")
_SonusGwRemoteGwAddr_Type = IpAddress
_SonusGwRemoteGwAddr_Object = MibScalar
sonusGwRemoteGwAddr = _SonusGwRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 3),
    _SonusGwRemoteGwAddr_Type()
)
sonusGwRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwRemoteGwAddr.setStatus("current")

# Managed Objects groups


# Notification objects

sonusGwCallSigChanOpenNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 1)
)
sonusGwCallSigChanOpenNotification.setObjects(
      *(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusGwCallSigChanOpenNotification.setStatus(
        "deprecated"
    )

sonusGwCallSigChanCloseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 2)
)
sonusGwCallSigChanCloseNotification.setObjects(
      *(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwName"),
        ("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwCloseReasonCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusGwCallSigChanCloseNotification.setStatus(
        "deprecated"
    )

sonusGwSigChanOpenNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 3)
)
sonusGwSigChanOpenNotification.setObjects(
      *(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwAddr"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusGwSigChanOpenNotification.setStatus(
        "current"
    )

sonusGwSigChanCloseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 4)
)
sonusGwSigChanCloseNotification.setObjects(
      *(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwAddr"),
        ("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwCloseReasonCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusGwSigChanCloseNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-GATEWAY-SIGNALLING-MIB",
    **{"sonusGatewaySignallingMIB": sonusGatewaySignallingMIB,
       "sonusGatewaySignallingMIBObjects": sonusGatewaySignallingMIBObjects,
       "sonusGwSigTimerObjects": sonusGwSigTimerObjects,
       "sonusGwSigSrvTimerT301": sonusGwSigSrvTimerT301,
       "sonusGwSigSrvTimerT303": sonusGwSigSrvTimerT303,
       "sonusGwSigTimerEstabish": sonusGwSigTimerEstabish,
       "sonusGwSigTimerKeepalive": sonusGwSigTimerKeepalive,
       "sonusGwSigActionObjects": sonusGwSigActionObjects,
       "sonusGwSigAction": sonusGwSigAction,
       "sonusGwSigActionDestIpAddr": sonusGwSigActionDestIpAddr,
       "sonusGwSigActionDestPort": sonusGwSigActionDestPort,
       "sonusGwSigActionDir": sonusGwSigActionDir,
       "sonusGwSigPortTable": sonusGwSigPortTable,
       "sonusGwSigPortEntry": sonusGwSigPortEntry,
       "sonusGwSigPortIndex": sonusGwSigPortIndex,
       "sonusGwSigPortIpAddress": sonusGwSigPortIpAddress,
       "sonusGwSigPortNum": sonusGwSigPortNum,
       "sonusGwSigPortInterface": sonusGwSigPortInterface,
       "sonusGwSigPortRole": sonusGwSigPortRole,
       "sonusGwSigPortMode": sonusGwSigPortMode,
       "sonusGwSigPortState": sonusGwSigPortState,
       "sonusGwSigPortRowStatus": sonusGwSigPortRowStatus,
       "sonusGwSigPortStatTable": sonusGwSigPortStatTable,
       "sonusGwSigPortStatEntry": sonusGwSigPortStatEntry,
       "sonusGwSigPortStatIndex": sonusGwSigPortStatIndex,
       "sonusGwSigPortStatIpAddress": sonusGwSigPortStatIpAddress,
       "sonusGwSigPortStatNum": sonusGwSigPortStatNum,
       "sonusGwSigPortStatInterface": sonusGwSigPortStatInterface,
       "sonusGwSigPortStatRole": sonusGwSigPortStatRole,
       "sonusGwSigPortStatNif": sonusGwSigPortStatNif,
       "sonusGwSigPortStatState": sonusGwSigPortStatState,
       "sonusGwSigActGwStatusTable": sonusGwSigActGwStatusTable,
       "sonusGwSigActGwStatusEntry": sonusGwSigActGwStatusEntry,
       "sonusGwSigActGwName": sonusGwSigActGwName,
       "sonusGwSigActGwIpAddress": sonusGwSigActGwIpAddress,
       "sonusGwSigActGwLnkProto": sonusGwSigActGwLnkProto,
       "sonusGwSigActGwNumActiveCalls": sonusGwSigActGwNumActiveCalls,
       "sonusGwSigActGwNumActiveCallsTo": sonusGwSigActGwNumActiveCallsTo,
       "sonusGwSigActGwNumActiveCallsFrom": sonusGwSigActGwNumActiveCallsFrom,
       "sonusGwSigActGwToState": sonusGwSigActGwToState,
       "sonusGwSigActGwFromState": sonusGwSigActGwFromState,
       "sonusGwSigActGwInterface": sonusGwSigActGwInterface,
       "sonusGwSigActGwFromBytesSent": sonusGwSigActGwFromBytesSent,
       "sonusGwSigActGwFromPdusSent": sonusGwSigActGwFromPdusSent,
       "sonusGwSigActGwFromBytesReceived": sonusGwSigActGwFromBytesReceived,
       "sonusGwSigActGwFromPdusReceived": sonusGwSigActGwFromPdusReceived,
       "sonusGwSigActGwFromTotalCalls": sonusGwSigActGwFromTotalCalls,
       "sonusGwSigActGwFromCallRate": sonusGwSigActGwFromCallRate,
       "sonusGwSigActGwToBytesSent": sonusGwSigActGwToBytesSent,
       "sonusGwSigActGwToPdusSent": sonusGwSigActGwToPdusSent,
       "sonusGwSigActGwToBytesReceived": sonusGwSigActGwToBytesReceived,
       "sonusGwSigActGwToPdusReceived": sonusGwSigActGwToPdusReceived,
       "sonusGwSigActGwToTotalCalls": sonusGwSigActGwToTotalCalls,
       "sonusGwSigActGwToCallRate": sonusGwSigActGwToCallRate,
       "sonusGwSigActGwFromLnkMajorVer": sonusGwSigActGwFromLnkMajorVer,
       "sonusGwSigActGwFromLnkMinorVer": sonusGwSigActGwFromLnkMinorVer,
       "sonusGwSigActGwToLnkMajorVer": sonusGwSigActGwToLnkMajorVer,
       "sonusGwSigActGwToLnkMinorVer": sonusGwSigActGwToLnkMinorVer,
       "sonusGatewaySignallingMIBNotifications": sonusGatewaySignallingMIBNotifications,
       "sonusGatewaySignallingMIBNotificationsPrefix": sonusGatewaySignallingMIBNotificationsPrefix,
       "sonusGwCallSigChanOpenNotification": sonusGwCallSigChanOpenNotification,
       "sonusGwCallSigChanCloseNotification": sonusGwCallSigChanCloseNotification,
       "sonusGwSigChanOpenNotification": sonusGwSigChanOpenNotification,
       "sonusGwSigChanCloseNotification": sonusGwSigChanCloseNotification,
       "sonusGatewaySignallingMIBNotificationsObjects": sonusGatewaySignallingMIBNotificationsObjects,
       "sonusGwRemoteGwName": sonusGwRemoteGwName,
       "sonusGwCloseReasonCode": sonusGwCloseReasonCode,
       "sonusGwRemoteGwAddr": sonusGwRemoteGwAddr}
)
