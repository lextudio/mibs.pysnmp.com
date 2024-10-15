# SNMP MIB module (CXCFG-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXCFG-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:12 2024
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

(Alias,
 cxIpx) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxIpx")

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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxCfgIpx_ObjectIdentity = ObjectIdentity
cxCfgIpx = _CxCfgIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1)
)
_CxCfgIpxNumClockTicksPerSecond_Type = Integer32
_CxCfgIpxNumClockTicksPerSecond_Object = MibScalar
cxCfgIpxNumClockTicksPerSecond = _CxCfgIpxNumClockTicksPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 1),
    _CxCfgIpxNumClockTicksPerSecond_Type()
)
cxCfgIpxNumClockTicksPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxNumClockTicksPerSecond.setStatus("mandatory")
_CxCfgIpxPortTable_Object = MibTable
cxCfgIpxPortTable = _CxCfgIpxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2)
)
if mibBuilder.loadTexts:
    cxCfgIpxPortTable.setStatus("mandatory")
_CxCfgIpxPortEntry_Object = MibTableRow
cxCfgIpxPortEntry = _CxCfgIpxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1)
)
cxCfgIpxPortEntry.setIndexNames(
    (0, "CXCFG-IPX-MIB", "cxCfgIpxPort"),
)
if mibBuilder.loadTexts:
    cxCfgIpxPortEntry.setStatus("mandatory")


class _CxCfgIpxPort_Type(Integer32):
    """Custom type cxCfgIpxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxCfgIpxPort_Type.__name__ = "Integer32"
_CxCfgIpxPort_Object = MibTableColumn
cxCfgIpxPort = _CxCfgIpxPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 1),
    _CxCfgIpxPort_Type()
)
cxCfgIpxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpxPort.setStatus("mandatory")
_CxCfgIpxPortIfIndex_Type = Integer32
_CxCfgIpxPortIfIndex_Object = MibTableColumn
cxCfgIpxPortIfIndex = _CxCfgIpxPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 2),
    _CxCfgIpxPortIfIndex_Type()
)
cxCfgIpxPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpxPortIfIndex.setStatus("mandatory")
_CxCfgIpxPortSubnetworkSAPAlias_Type = Alias
_CxCfgIpxPortSubnetworkSAPAlias_Object = MibTableColumn
cxCfgIpxPortSubnetworkSAPAlias = _CxCfgIpxPortSubnetworkSAPAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 3),
    _CxCfgIpxPortSubnetworkSAPAlias_Type()
)
cxCfgIpxPortSubnetworkSAPAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSubnetworkSAPAlias.setStatus("mandatory")


class _CxCfgIpxPortState_Type(Integer32):
    """Custom type cxCfgIpxPortState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortState_Type.__name__ = "Integer32"
_CxCfgIpxPortState_Object = MibTableColumn
cxCfgIpxPortState = _CxCfgIpxPortState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 4),
    _CxCfgIpxPortState_Type()
)
cxCfgIpxPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortState.setStatus("mandatory")


class _CxCfgIpxPortRowStatus_Type(Integer32):
    """Custom type cxCfgIpxPortRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgIpxPortRowStatus_Type.__name__ = "Integer32"
_CxCfgIpxPortRowStatus_Object = MibTableColumn
cxCfgIpxPortRowStatus = _CxCfgIpxPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 5),
    _CxCfgIpxPortRowStatus_Type()
)
cxCfgIpxPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortRowStatus.setStatus("mandatory")


class _CxCfgIpxPortTransportTime_Type(Integer32):
    """Custom type cxCfgIpxPortTransportTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CxCfgIpxPortTransportTime_Type.__name__ = "Integer32"
_CxCfgIpxPortTransportTime_Object = MibTableColumn
cxCfgIpxPortTransportTime = _CxCfgIpxPortTransportTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 6),
    _CxCfgIpxPortTransportTime_Type()
)
cxCfgIpxPortTransportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortTransportTime.setStatus("mandatory")


class _CxCfgIpxPortMaxHops_Type(Integer32):
    """Custom type cxCfgIpxPortMaxHops based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxCfgIpxPortMaxHops_Type.__name__ = "Integer32"
_CxCfgIpxPortMaxHops_Object = MibTableColumn
cxCfgIpxPortMaxHops = _CxCfgIpxPortMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 7),
    _CxCfgIpxPortMaxHops_Type()
)
cxCfgIpxPortMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortMaxHops.setStatus("mandatory")
_CxCfgIpxPortIntNetNum_Type = NetNumber
_CxCfgIpxPortIntNetNum_Object = MibTableColumn
cxCfgIpxPortIntNetNum = _CxCfgIpxPortIntNetNum_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 8),
    _CxCfgIpxPortIntNetNum_Type()
)
cxCfgIpxPortIntNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortIntNetNum.setStatus("mandatory")


class _CxCfgIpxPortPerSapBcast_Type(Integer32):
    """Custom type cxCfgIpxPortPerSapBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortPerSapBcast_Type.__name__ = "Integer32"
_CxCfgIpxPortPerSapBcast_Object = MibTableColumn
cxCfgIpxPortPerSapBcast = _CxCfgIpxPortPerSapBcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 9),
    _CxCfgIpxPortPerSapBcast_Type()
)
cxCfgIpxPortPerSapBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortPerSapBcast.setStatus("mandatory")


class _CxCfgIpxPortPerRipBcast_Type(Integer32):
    """Custom type cxCfgIpxPortPerRipBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortPerRipBcast_Type.__name__ = "Integer32"
_CxCfgIpxPortPerRipBcast_Object = MibTableColumn
cxCfgIpxPortPerRipBcast = _CxCfgIpxPortPerRipBcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 10),
    _CxCfgIpxPortPerRipBcast_Type()
)
cxCfgIpxPortPerRipBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortPerRipBcast.setStatus("mandatory")


class _CxCfgIpxPortSapBcast_Type(Integer32):
    """Custom type cxCfgIpxPortSapBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortSapBcast_Type.__name__ = "Integer32"
_CxCfgIpxPortSapBcast_Object = MibTableColumn
cxCfgIpxPortSapBcast = _CxCfgIpxPortSapBcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 11),
    _CxCfgIpxPortSapBcast_Type()
)
cxCfgIpxPortSapBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSapBcast.setStatus("mandatory")


class _CxCfgIpxPortRipBcast_Type(Integer32):
    """Custom type cxCfgIpxPortRipBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortRipBcast_Type.__name__ = "Integer32"
_CxCfgIpxPortRipBcast_Object = MibTableColumn
cxCfgIpxPortRipBcast = _CxCfgIpxPortRipBcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 12),
    _CxCfgIpxPortRipBcast_Type()
)
cxCfgIpxPortRipBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortRipBcast.setStatus("mandatory")


class _CxCfgIpxPortDiagPackets_Type(Integer32):
    """Custom type cxCfgIpxPortDiagPackets based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortDiagPackets_Type.__name__ = "Integer32"
_CxCfgIpxPortDiagPackets_Object = MibTableColumn
cxCfgIpxPortDiagPackets = _CxCfgIpxPortDiagPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 13),
    _CxCfgIpxPortDiagPackets_Type()
)
cxCfgIpxPortDiagPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortDiagPackets.setStatus("mandatory")


class _CxCfgIpxPortPerRipTxTimer_Type(Integer32):
    """Custom type cxCfgIpxPortPerRipTxTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CxCfgIpxPortPerRipTxTimer_Type.__name__ = "Integer32"
_CxCfgIpxPortPerRipTxTimer_Object = MibTableColumn
cxCfgIpxPortPerRipTxTimer = _CxCfgIpxPortPerRipTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 14),
    _CxCfgIpxPortPerRipTxTimer_Type()
)
cxCfgIpxPortPerRipTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortPerRipTxTimer.setStatus("mandatory")


class _CxCfgIpxPortPerSapTxTimer_Type(Integer32):
    """Custom type cxCfgIpxPortPerSapTxTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CxCfgIpxPortPerSapTxTimer_Type.__name__ = "Integer32"
_CxCfgIpxPortPerSapTxTimer_Object = MibTableColumn
cxCfgIpxPortPerSapTxTimer = _CxCfgIpxPortPerSapTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 15),
    _CxCfgIpxPortPerSapTxTimer_Type()
)
cxCfgIpxPortPerSapTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortPerSapTxTimer.setStatus("mandatory")


class _CxCfgIpxPortRipAgeTimer_Type(Integer32):
    """Custom type cxCfgIpxPortRipAgeTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CxCfgIpxPortRipAgeTimer_Type.__name__ = "Integer32"
_CxCfgIpxPortRipAgeTimer_Object = MibTableColumn
cxCfgIpxPortRipAgeTimer = _CxCfgIpxPortRipAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 16),
    _CxCfgIpxPortRipAgeTimer_Type()
)
cxCfgIpxPortRipAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortRipAgeTimer.setStatus("mandatory")


class _CxCfgIpxPortSapAgeTimer_Type(Integer32):
    """Custom type cxCfgIpxPortSapAgeTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CxCfgIpxPortSapAgeTimer_Type.__name__ = "Integer32"
_CxCfgIpxPortSapAgeTimer_Object = MibTableColumn
cxCfgIpxPortSapAgeTimer = _CxCfgIpxPortSapAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 17),
    _CxCfgIpxPortSapAgeTimer_Type()
)
cxCfgIpxPortSapAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSapAgeTimer.setStatus("mandatory")


class _CxCfgIpxPortFrameType_Type(Integer32):
    """Custom type cxCfgIpxPortFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-II", 2),
          ("llc-802-2", 3),
          ("raw-802-3", 1),
          ("snap", 4))
    )


_CxCfgIpxPortFrameType_Type.__name__ = "Integer32"
_CxCfgIpxPortFrameType_Object = MibTableColumn
cxCfgIpxPortFrameType = _CxCfgIpxPortFrameType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 18),
    _CxCfgIpxPortFrameType_Type()
)
cxCfgIpxPortFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortFrameType.setStatus("mandatory")


class _CxCfgIpxPortWatchSpoof_Type(Integer32):
    """Custom type cxCfgIpxPortWatchSpoof based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortWatchSpoof_Type.__name__ = "Integer32"
_CxCfgIpxPortWatchSpoof_Object = MibTableColumn
cxCfgIpxPortWatchSpoof = _CxCfgIpxPortWatchSpoof_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 19),
    _CxCfgIpxPortWatchSpoof_Type()
)
cxCfgIpxPortWatchSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortWatchSpoof.setStatus("mandatory")


class _CxCfgIpxPortSpxWatchSpoof_Type(Integer32):
    """Custom type cxCfgIpxPortSpxWatchSpoof based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortSpxWatchSpoof_Type.__name__ = "Integer32"
_CxCfgIpxPortSpxWatchSpoof_Object = MibTableColumn
cxCfgIpxPortSpxWatchSpoof = _CxCfgIpxPortSpxWatchSpoof_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 20),
    _CxCfgIpxPortSpxWatchSpoof_Type()
)
cxCfgIpxPortSpxWatchSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSpxWatchSpoof.setStatus("mandatory")


class _CxCfgIpxPortSerialSpoof_Type(Integer32):
    """Custom type cxCfgIpxPortSerialSpoof based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxCfgIpxPortSerialSpoof_Type.__name__ = "Integer32"
_CxCfgIpxPortSerialSpoof_Object = MibTableColumn
cxCfgIpxPortSerialSpoof = _CxCfgIpxPortSerialSpoof_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 21),
    _CxCfgIpxPortSerialSpoof_Type()
)
cxCfgIpxPortSerialSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSerialSpoof.setStatus("mandatory")


class _CxCfgIpxPortSRSupport_Type(Integer32):
    """Custom type cxCfgIpxPortSRSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CxCfgIpxPortSRSupport_Type.__name__ = "Integer32"
_CxCfgIpxPortSRSupport_Object = MibTableColumn
cxCfgIpxPortSRSupport = _CxCfgIpxPortSRSupport_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 2, 1, 22),
    _CxCfgIpxPortSRSupport_Type()
)
cxCfgIpxPortSRSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpxPortSRSupport.setStatus("mandatory")


class _CxCfgIpxMibLevel_Type(Integer32):
    """Custom type cxCfgIpxMibLevel based on Integer32"""
    defaultValue = 0


_CxCfgIpxMibLevel_Object = MibScalar
cxCfgIpxMibLevel = _CxCfgIpxMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 1, 20),
    _CxCfgIpxMibLevel_Type()
)
cxCfgIpxMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpxMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXCFG-IPX-MIB",
    **{"NetNumber": NetNumber,
       "cxCfgIpx": cxCfgIpx,
       "cxCfgIpxNumClockTicksPerSecond": cxCfgIpxNumClockTicksPerSecond,
       "cxCfgIpxPortTable": cxCfgIpxPortTable,
       "cxCfgIpxPortEntry": cxCfgIpxPortEntry,
       "cxCfgIpxPort": cxCfgIpxPort,
       "cxCfgIpxPortIfIndex": cxCfgIpxPortIfIndex,
       "cxCfgIpxPortSubnetworkSAPAlias": cxCfgIpxPortSubnetworkSAPAlias,
       "cxCfgIpxPortState": cxCfgIpxPortState,
       "cxCfgIpxPortRowStatus": cxCfgIpxPortRowStatus,
       "cxCfgIpxPortTransportTime": cxCfgIpxPortTransportTime,
       "cxCfgIpxPortMaxHops": cxCfgIpxPortMaxHops,
       "cxCfgIpxPortIntNetNum": cxCfgIpxPortIntNetNum,
       "cxCfgIpxPortPerSapBcast": cxCfgIpxPortPerSapBcast,
       "cxCfgIpxPortPerRipBcast": cxCfgIpxPortPerRipBcast,
       "cxCfgIpxPortSapBcast": cxCfgIpxPortSapBcast,
       "cxCfgIpxPortRipBcast": cxCfgIpxPortRipBcast,
       "cxCfgIpxPortDiagPackets": cxCfgIpxPortDiagPackets,
       "cxCfgIpxPortPerRipTxTimer": cxCfgIpxPortPerRipTxTimer,
       "cxCfgIpxPortPerSapTxTimer": cxCfgIpxPortPerSapTxTimer,
       "cxCfgIpxPortRipAgeTimer": cxCfgIpxPortRipAgeTimer,
       "cxCfgIpxPortSapAgeTimer": cxCfgIpxPortSapAgeTimer,
       "cxCfgIpxPortFrameType": cxCfgIpxPortFrameType,
       "cxCfgIpxPortWatchSpoof": cxCfgIpxPortWatchSpoof,
       "cxCfgIpxPortSpxWatchSpoof": cxCfgIpxPortSpxWatchSpoof,
       "cxCfgIpxPortSerialSpoof": cxCfgIpxPortSerialSpoof,
       "cxCfgIpxPortSRSupport": cxCfgIpxPortSRSupport,
       "cxCfgIpxMibLevel": cxCfgIpxMibLevel}
)
