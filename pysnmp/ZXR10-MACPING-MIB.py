# SNMP MIB module (ZXR10-MACPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MACPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:56 2024
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
 enterprises,
 experimental,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxr10L2vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L2vpn")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class OptionType(Integer32):
    """Custom type OptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ce", 0),
          ("pe", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10MacPingMIB_ObjectIdentity = ObjectIdentity
zxr10MacPingMIB = _Zxr10MacPingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4)
)
_Zxr10MacPingTable_Object = MibTable
zxr10MacPingTable = _Zxr10MacPingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1)
)
if mibBuilder.loadTexts:
    zxr10MacPingTable.setStatus("current")
_Zxr10MacPingEntry_Object = MibTableRow
zxr10MacPingEntry = _Zxr10MacPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1)
)
zxr10MacPingEntry.setIndexNames(
    (0, "ZXR10-MACPING-MIB", "zxr10PingMacSerial"),
)
if mibBuilder.loadTexts:
    zxr10MacPingEntry.setStatus("current")
_Zxr10PingMacSerial_Type = Integer32
_Zxr10PingMacSerial_Object = MibTableColumn
zxr10PingMacSerial = _Zxr10PingMacSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 1),
    _Zxr10PingMacSerial_Type()
)
zxr10PingMacSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacSerial.setStatus("current")
_Zxr10PingMacDestMac_Type = MacAddress
_Zxr10PingMacDestMac_Object = MibTableColumn
zxr10PingMacDestMac = _Zxr10PingMacDestMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 2),
    _Zxr10PingMacDestMac_Type()
)
zxr10PingMacDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacDestMac.setStatus("current")
_Zxr10PingMacControlOutEtherIf_Type = Integer32
_Zxr10PingMacControlOutEtherIf_Object = MibTableColumn
zxr10PingMacControlOutEtherIf = _Zxr10PingMacControlOutEtherIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 3),
    _Zxr10PingMacControlOutEtherIf_Type()
)
zxr10PingMacControlOutEtherIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacControlOutEtherIf.setStatus("current")


class _Zxr10PingMacIfOption_Type(Integer32):
    """Custom type zxr10PingMacIfOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("option", 1))
    )


_Zxr10PingMacIfOption_Type.__name__ = "Integer32"
_Zxr10PingMacIfOption_Object = MibTableColumn
zxr10PingMacIfOption = _Zxr10PingMacIfOption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 4),
    _Zxr10PingMacIfOption_Type()
)
zxr10PingMacIfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacIfOption.setStatus("current")
_Zxr10PingMacPacketCount_Type = Integer32
_Zxr10PingMacPacketCount_Object = MibTableColumn
zxr10PingMacPacketCount = _Zxr10PingMacPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 5),
    _Zxr10PingMacPacketCount_Type()
)
zxr10PingMacPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacPacketCount.setStatus("current")


class _Zxr10PingMacTimeOut_Type(Integer32):
    """Custom type zxr10PingMacTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Zxr10PingMacTimeOut_Type.__name__ = "Integer32"
_Zxr10PingMacTimeOut_Object = MibTableColumn
zxr10PingMacTimeOut = _Zxr10PingMacTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 6),
    _Zxr10PingMacTimeOut_Type()
)
zxr10PingMacTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacTimeOut.setStatus("current")


class _Zxr10PingMacHops_Type(Integer32):
    """Custom type zxr10PingMacHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Zxr10PingMacHops_Type.__name__ = "Integer32"
_Zxr10PingMacHops_Object = MibTableColumn
zxr10PingMacHops = _Zxr10PingMacHops_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 7),
    _Zxr10PingMacHops_Type()
)
zxr10PingMacHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacHops.setStatus("current")


class _Zxr10PingMacControlResultType_Type(Integer32):
    """Custom type zxr10PingMacControlResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detail", 1),
          ("summary", 0))
    )


_Zxr10PingMacControlResultType_Type.__name__ = "Integer32"
_Zxr10PingMacControlResultType_Object = MibTableColumn
zxr10PingMacControlResultType = _Zxr10PingMacControlResultType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 8),
    _Zxr10PingMacControlResultType_Type()
)
zxr10PingMacControlResultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacControlResultType.setStatus("current")


class _Zxr10PingMacTrapOncompletion_Type(TruthValue):
    """Custom type zxr10PingMacTrapOncompletion based on TruthValue"""


_Zxr10PingMacTrapOncompletion_Object = MibTableColumn
zxr10PingMacTrapOncompletion = _Zxr10PingMacTrapOncompletion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 9),
    _Zxr10PingMacTrapOncompletion_Type()
)
zxr10PingMacTrapOncompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacTrapOncompletion.setStatus("current")


class _Zxr10PingMacRosStatus_Type(Integer32):
    """Custom type zxr10PingMacRosStatus based on Integer32"""
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
        *(("not-active", 1),
          ("ping-completed", 4),
          ("ping-processing", 3),
          ("start-ping", 2))
    )


_Zxr10PingMacRosStatus_Type.__name__ = "Integer32"
_Zxr10PingMacRosStatus_Object = MibTableColumn
zxr10PingMacRosStatus = _Zxr10PingMacRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 10),
    _Zxr10PingMacRosStatus_Type()
)
zxr10PingMacRosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacRosStatus.setStatus("current")
_Zxr10PingMacEntryOwner_Type = DisplayString
_Zxr10PingMacEntryOwner_Object = MibTableColumn
zxr10PingMacEntryOwner = _Zxr10PingMacEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 11),
    _Zxr10PingMacEntryOwner_Type()
)
zxr10PingMacEntryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacEntryOwner.setStatus("current")
_Zxr10PingMacIfPeOption_Type = OptionType
_Zxr10PingMacIfPeOption_Object = MibTableColumn
zxr10PingMacIfPeOption = _Zxr10PingMacIfPeOption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 12),
    _Zxr10PingMacIfPeOption_Type()
)
zxr10PingMacIfPeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacIfPeOption.setStatus("current")
_Zxr10PingMacVfiName_Type = DisplayString
_Zxr10PingMacVfiName_Object = MibTableColumn
zxr10PingMacVfiName = _Zxr10PingMacVfiName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 13),
    _Zxr10PingMacVfiName_Type()
)
zxr10PingMacVfiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacVfiName.setStatus("current")
_Zxr10PingMacPeerAddress_Type = IpAddress
_Zxr10PingMacPeerAddress_Object = MibTableColumn
zxr10PingMacPeerAddress = _Zxr10PingMacPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 1, 1, 14),
    _Zxr10PingMacPeerAddress_Type()
)
zxr10PingMacPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingMacPeerAddress.setStatus("current")
_Zxr10PingMacResultTable_Object = MibTable
zxr10PingMacResultTable = _Zxr10PingMacResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2)
)
if mibBuilder.loadTexts:
    zxr10PingMacResultTable.setStatus("current")
_Zxr10pingMacResultEntry_Object = MibTableRow
zxr10pingMacResultEntry = _Zxr10pingMacResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1)
)
zxr10pingMacResultEntry.setIndexNames(
    (0, "ZXR10-MACPING-MIB", "zxr10PingMacResultSerial"),
)
if mibBuilder.loadTexts:
    zxr10pingMacResultEntry.setStatus("current")
_Zxr10PingMacResultSerial_Type = Integer32
_Zxr10PingMacResultSerial_Object = MibTableColumn
zxr10PingMacResultSerial = _Zxr10PingMacResultSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 1),
    _Zxr10PingMacResultSerial_Type()
)
zxr10PingMacResultSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultSerial.setStatus("current")
_Zxr10PingMacResultSentPkts_Type = Integer32
_Zxr10PingMacResultSentPkts_Object = MibTableColumn
zxr10PingMacResultSentPkts = _Zxr10PingMacResultSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 2),
    _Zxr10PingMacResultSentPkts_Type()
)
zxr10PingMacResultSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultSentPkts.setStatus("current")
_Zxr10PingMacResultRcvPkts_Type = Integer32
_Zxr10PingMacResultRcvPkts_Object = MibTableColumn
zxr10PingMacResultRcvPkts = _Zxr10PingMacResultRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 3),
    _Zxr10PingMacResultRcvPkts_Type()
)
zxr10PingMacResultRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRcvPkts.setStatus("current")
_Zxr10PingMacResultRoundTripMinTime_Type = Integer32
_Zxr10PingMacResultRoundTripMinTime_Object = MibTableColumn
zxr10PingMacResultRoundTripMinTime = _Zxr10PingMacResultRoundTripMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 4),
    _Zxr10PingMacResultRoundTripMinTime_Type()
)
zxr10PingMacResultRoundTripMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundTripMinTime.setStatus("current")
_Zxr10PingMacResultRoundTripMaxTime_Type = Integer32
_Zxr10PingMacResultRoundTripMaxTime_Object = MibTableColumn
zxr10PingMacResultRoundTripMaxTime = _Zxr10PingMacResultRoundTripMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 5),
    _Zxr10PingMacResultRoundTripMaxTime_Type()
)
zxr10PingMacResultRoundTripMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundTripMaxTime.setStatus("current")
_Zxr10PingMacResultRoundTripAvgTime_Type = Integer32
_Zxr10PingMacResultRoundTripAvgTime_Object = MibTableColumn
zxr10PingMacResultRoundTripAvgTime = _Zxr10PingMacResultRoundTripAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 6),
    _Zxr10PingMacResultRoundTripAvgTime_Type()
)
zxr10PingMacResultRoundTripAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundTripAvgTime.setStatus("current")


class _Zxr10PingMacResultType_Type(Integer32):
    """Custom type zxr10PingMacResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detail", 1),
          ("summary", 0))
    )


_Zxr10PingMacResultType_Type.__name__ = "Integer32"
_Zxr10PingMacResultType_Object = MibTableColumn
zxr10PingMacResultType = _Zxr10PingMacResultType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 7),
    _Zxr10PingMacResultType_Type()
)
zxr10PingMacResultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultType.setStatus("current")


class _Zxr10PingMacExtResultDestIfName_Type(DisplayString):
    """Custom type zxr10PingMacExtResultDestIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10PingMacExtResultDestIfName_Type.__name__ = "DisplayString"
_Zxr10PingMacExtResultDestIfName_Object = MibTableColumn
zxr10PingMacExtResultDestIfName = _Zxr10PingMacExtResultDestIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 8),
    _Zxr10PingMacExtResultDestIfName_Type()
)
zxr10PingMacExtResultDestIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultDestIfName.setStatus("current")


class _Zxr10PingMacExtResultDestHostName_Type(DisplayString):
    """Custom type zxr10PingMacExtResultDestHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Zxr10PingMacExtResultDestHostName_Type.__name__ = "DisplayString"
_Zxr10PingMacExtResultDestHostName_Object = MibTableColumn
zxr10PingMacExtResultDestHostName = _Zxr10PingMacExtResultDestHostName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 9),
    _Zxr10PingMacExtResultDestHostName_Type()
)
zxr10PingMacExtResultDestHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultDestHostName.setStatus("current")


class _Zxr10PingMacExtResultSourceIfName_Type(DisplayString):
    """Custom type zxr10PingMacExtResultSourceIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10PingMacExtResultSourceIfName_Type.__name__ = "DisplayString"
_Zxr10PingMacExtResultSourceIfName_Object = MibTableColumn
zxr10PingMacExtResultSourceIfName = _Zxr10PingMacExtResultSourceIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 10),
    _Zxr10PingMacExtResultSourceIfName_Type()
)
zxr10PingMacExtResultSourceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultSourceIfName.setStatus("current")


class _Zxr10PingMacExtResultSourceHostName_Type(DisplayString):
    """Custom type zxr10PingMacExtResultSourceHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Zxr10PingMacExtResultSourceHostName_Type.__name__ = "DisplayString"
_Zxr10PingMacExtResultSourceHostName_Object = MibTableColumn
zxr10PingMacExtResultSourceHostName = _Zxr10PingMacExtResultSourceHostName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 11),
    _Zxr10PingMacExtResultSourceHostName_Type()
)
zxr10PingMacExtResultSourceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultSourceHostName.setStatus("current")


class _Zxr10PingMacExtResultOutVlanId_Type(Integer32):
    """Custom type zxr10PingMacExtResultOutVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Zxr10PingMacExtResultOutVlanId_Type.__name__ = "Integer32"
_Zxr10PingMacExtResultOutVlanId_Object = MibTableColumn
zxr10PingMacExtResultOutVlanId = _Zxr10PingMacExtResultOutVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 12),
    _Zxr10PingMacExtResultOutVlanId_Type()
)
zxr10PingMacExtResultOutVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultOutVlanId.setStatus("current")


class _Zxr10PingMacExtResultInVlanId_Type(Integer32):
    """Custom type zxr10PingMacExtResultInVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Zxr10PingMacExtResultInVlanId_Type.__name__ = "Integer32"
_Zxr10PingMacExtResultInVlanId_Object = MibTableColumn
zxr10PingMacExtResultInVlanId = _Zxr10PingMacExtResultInVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 13),
    _Zxr10PingMacExtResultInVlanId_Type()
)
zxr10PingMacExtResultInVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacExtResultInVlanId.setStatus("current")
_Zxr10PingMacResultEntryOwner_Type = DisplayString
_Zxr10PingMacResultEntryOwner_Object = MibTableColumn
zxr10PingMacResultEntryOwner = _Zxr10PingMacResultEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 14),
    _Zxr10PingMacResultEntryOwner_Type()
)
zxr10PingMacResultEntryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultEntryOwner.setStatus("current")
_Zxr10PingMacResultRoundWobbleMinTime_Type = Integer32
_Zxr10PingMacResultRoundWobbleMinTime_Object = MibTableColumn
zxr10PingMacResultRoundWobbleMinTime = _Zxr10PingMacResultRoundWobbleMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 15),
    _Zxr10PingMacResultRoundWobbleMinTime_Type()
)
zxr10PingMacResultRoundWobbleMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundWobbleMinTime.setStatus("current")
_Zxr10PingMacResultRoundWobbleMaxTime_Type = Integer32
_Zxr10PingMacResultRoundWobbleMaxTime_Object = MibTableColumn
zxr10PingMacResultRoundWobbleMaxTime = _Zxr10PingMacResultRoundWobbleMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 16),
    _Zxr10PingMacResultRoundWobbleMaxTime_Type()
)
zxr10PingMacResultRoundWobbleMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundWobbleMaxTime.setStatus("current")
_Zxr10PingMacResultRoundWobbleAvgTime_Type = Integer32
_Zxr10PingMacResultRoundWobbleAvgTime_Object = MibTableColumn
zxr10PingMacResultRoundWobbleAvgTime = _Zxr10PingMacResultRoundWobbleAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 2, 1, 17),
    _Zxr10PingMacResultRoundWobbleAvgTime_Type()
)
zxr10PingMacResultRoundWobbleAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingMacResultRoundWobbleAvgTime.setStatus("current")
_MacpingNotifications_ObjectIdentity = ObjectIdentity
macpingNotifications = _MacpingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 3)
)

# Managed Objects groups


# Notification objects

macpingTrapResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 4, 3, 1)
)
macpingTrapResult.setObjects(
      *(("ZXR10-MACPING-MIB", "zxr10PingMacResultSerial"),
        ("ZXR10-MACPING-MIB", "zxr10PingMacResultSentPkts"),
        ("ZXR10-MACPING-MIB", "zxr10PingMacResultRcvPkts"),
        ("ZXR10-MACPING-MIB", "zxr10PingMacResultRoundTripMinTime"),
        ("ZXR10-MACPING-MIB", "zxr10PingMacResultRoundTripMaxTime"),
        ("ZXR10-MACPING-MIB", "zxr10PingMacResultRoundTripAvgTime"))
)
if mibBuilder.loadTexts:
    macpingTrapResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MACPING-MIB",
    **{"DisplayString": DisplayString,
       "OptionType": OptionType,
       "zxr10MacPingMIB": zxr10MacPingMIB,
       "zxr10MacPingTable": zxr10MacPingTable,
       "zxr10MacPingEntry": zxr10MacPingEntry,
       "zxr10PingMacSerial": zxr10PingMacSerial,
       "zxr10PingMacDestMac": zxr10PingMacDestMac,
       "zxr10PingMacControlOutEtherIf": zxr10PingMacControlOutEtherIf,
       "zxr10PingMacIfOption": zxr10PingMacIfOption,
       "zxr10PingMacPacketCount": zxr10PingMacPacketCount,
       "zxr10PingMacTimeOut": zxr10PingMacTimeOut,
       "zxr10PingMacHops": zxr10PingMacHops,
       "zxr10PingMacControlResultType": zxr10PingMacControlResultType,
       "zxr10PingMacTrapOncompletion": zxr10PingMacTrapOncompletion,
       "zxr10PingMacRosStatus": zxr10PingMacRosStatus,
       "zxr10PingMacEntryOwner": zxr10PingMacEntryOwner,
       "zxr10PingMacIfPeOption": zxr10PingMacIfPeOption,
       "zxr10PingMacVfiName": zxr10PingMacVfiName,
       "zxr10PingMacPeerAddress": zxr10PingMacPeerAddress,
       "zxr10PingMacResultTable": zxr10PingMacResultTable,
       "zxr10pingMacResultEntry": zxr10pingMacResultEntry,
       "zxr10PingMacResultSerial": zxr10PingMacResultSerial,
       "zxr10PingMacResultSentPkts": zxr10PingMacResultSentPkts,
       "zxr10PingMacResultRcvPkts": zxr10PingMacResultRcvPkts,
       "zxr10PingMacResultRoundTripMinTime": zxr10PingMacResultRoundTripMinTime,
       "zxr10PingMacResultRoundTripMaxTime": zxr10PingMacResultRoundTripMaxTime,
       "zxr10PingMacResultRoundTripAvgTime": zxr10PingMacResultRoundTripAvgTime,
       "zxr10PingMacResultType": zxr10PingMacResultType,
       "zxr10PingMacExtResultDestIfName": zxr10PingMacExtResultDestIfName,
       "zxr10PingMacExtResultDestHostName": zxr10PingMacExtResultDestHostName,
       "zxr10PingMacExtResultSourceIfName": zxr10PingMacExtResultSourceIfName,
       "zxr10PingMacExtResultSourceHostName": zxr10PingMacExtResultSourceHostName,
       "zxr10PingMacExtResultOutVlanId": zxr10PingMacExtResultOutVlanId,
       "zxr10PingMacExtResultInVlanId": zxr10PingMacExtResultInVlanId,
       "zxr10PingMacResultEntryOwner": zxr10PingMacResultEntryOwner,
       "zxr10PingMacResultRoundWobbleMinTime": zxr10PingMacResultRoundWobbleMinTime,
       "zxr10PingMacResultRoundWobbleMaxTime": zxr10PingMacResultRoundWobbleMaxTime,
       "zxr10PingMacResultRoundWobbleAvgTime": zxr10PingMacResultRoundWobbleAvgTime,
       "macpingNotifications": macpingNotifications,
       "macpingTrapResult": macpingTrapResult}
)
