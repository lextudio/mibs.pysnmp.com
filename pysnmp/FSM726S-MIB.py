# SNMP MIB module (FSM726S-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSM726S-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:30 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_SnmpManagedSwitch_ObjectIdentity = ObjectIdentity
snmpManagedSwitch = _SnmpManagedSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1)
)
_Fsm726s_ObjectIdentity = ObjectIdentity
fsm726s = _Fsm726s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1)
)
_NetgearCommGroup_ObjectIdentity = ObjectIdentity
netgearCommGroup = _NetgearCommGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1)
)
_CommTable_Object = MibTable
commTable = _CommTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    commTable.setStatus("mandatory")
_CommEntry_Object = MibTableRow
commEntry = _CommEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1)
)
commEntry.setIndexNames(
    (0, "FSM726S-MIB", "commIndex"),
)
if mibBuilder.loadTexts:
    commEntry.setStatus("mandatory")


class _CommIndex_Type(Integer32):
    """Custom type commIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CommIndex_Type.__name__ = "Integer32"
_CommIndex_Object = MibTableColumn
commIndex = _CommIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 1),
    _CommIndex_Type()
)
commIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commIndex.setStatus("mandatory")


class _CommName_Type(DisplayString):
    """Custom type commName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CommName_Type.__name__ = "DisplayString"
_CommName_Object = MibTableColumn
commName = _CommName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 2),
    _CommName_Type()
)
commName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commName.setStatus("mandatory")


class _CommGet_Type(Integer32):
    """Custom type commGet based on Integer32"""
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


_CommGet_Type.__name__ = "Integer32"
_CommGet_Object = MibTableColumn
commGet = _CommGet_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 3),
    _CommGet_Type()
)
commGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commGet.setStatus("mandatory")


class _CommSet_Type(Integer32):
    """Custom type commSet based on Integer32"""
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


_CommSet_Type.__name__ = "Integer32"
_CommSet_Object = MibTableColumn
commSet = _CommSet_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 4),
    _CommSet_Type()
)
commSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSet.setStatus("mandatory")


class _CommTrap_Type(Integer32):
    """Custom type commTrap based on Integer32"""
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


_CommTrap_Type.__name__ = "Integer32"
_CommTrap_Object = MibTableColumn
commTrap = _CommTrap_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 5),
    _CommTrap_Type()
)
commTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrap.setStatus("mandatory")


class _CommStatus_Type(Integer32):
    """Custom type commStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CommStatus_Type.__name__ = "Integer32"
_CommStatus_Object = MibTableColumn
commStatus = _CommStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 1, 1, 1, 6),
    _CommStatus_Type()
)
commStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commStatus.setStatus("mandatory")
_NetgearHostGroup_ObjectIdentity = ObjectIdentity
netgearHostGroup = _NetgearHostGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2)
)
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("mandatory")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1)
)
hostEntry.setIndexNames(
    (0, "FSM726S-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("mandatory")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("mandatory")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_HostIP_Type = IpAddress
_HostIP_Object = MibTableColumn
hostIP = _HostIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1, 3),
    _HostIP_Type()
)
hostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIP.setStatus("mandatory")


class _HostComm_Type(DisplayString):
    """Custom type hostComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HostComm_Type.__name__ = "DisplayString"
_HostComm_Object = MibTableColumn
hostComm = _HostComm_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1, 4),
    _HostComm_Type()
)
hostComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostComm.setStatus("mandatory")


class _HostStatus_Type(Integer32):
    """Custom type hostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HostStatus_Type.__name__ = "Integer32"
_HostStatus_Object = MibTableColumn
hostStatus = _HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 2, 1, 1, 5),
    _HostStatus_Type()
)
hostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostStatus.setStatus("mandatory")
_NetgearMiscGroup_ObjectIdentity = ObjectIdentity
netgearMiscGroup = _NetgearMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 3)
)


class _MiscReset_Type(Integer32):
    """Custom type miscReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscReset_Type.__name__ = "Integer32"
_MiscReset_Object = MibScalar
miscReset = _MiscReset_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 3, 2),
    _MiscReset_Type()
)
miscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscReset.setStatus("mandatory")


class _MiscStatisticsReset_Type(Integer32):
    """Custom type miscStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscStatisticsReset_Type.__name__ = "Integer32"
_MiscStatisticsReset_Object = MibScalar
miscStatisticsReset = _MiscStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 3, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("mandatory")
_NetgearSpanGroup_ObjectIdentity = ObjectIdentity
netgearSpanGroup = _NetgearSpanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 4)
)


class _SpanOnOff_Type(Integer32):
    """Custom type spanOnOff based on Integer32"""
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


_SpanOnOff_Type.__name__ = "Integer32"
_SpanOnOff_Object = MibScalar
spanOnOff = _SpanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 4, 1),
    _SpanOnOff_Type()
)
spanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanOnOff.setStatus("mandatory")
_NetgearConfigGroup_ObjectIdentity = ObjectIdentity
netgearConfigGroup = _NetgearConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11)
)


class _ConfigVerSwPrimary_Type(DisplayString):
    """Custom type configVerSwPrimary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConfigVerSwPrimary_Type.__name__ = "DisplayString"
_ConfigVerSwPrimary_Object = MibScalar
configVerSwPrimary = _ConfigVerSwPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 1),
    _ConfigVerSwPrimary_Type()
)
configVerSwPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerSwPrimary.setStatus("mandatory")


class _ConfigVerHwChipSet_Type(DisplayString):
    """Custom type configVerHwChipSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConfigVerHwChipSet_Type.__name__ = "DisplayString"
_ConfigVerHwChipSet_Object = MibScalar
configVerHwChipSet = _ConfigVerHwChipSet_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 2),
    _ConfigVerHwChipSet_Type()
)
configVerHwChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerHwChipSet.setStatus("mandatory")


class _ConfigBootMode_Type(Integer32):
    """Custom type configBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lastSaved", 1),
          ("net", 2),
          ("netAndSave", 3))
    )


_ConfigBootMode_Type.__name__ = "Integer32"
_ConfigBootMode_Object = MibScalar
configBootMode = _ConfigBootMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 3),
    _ConfigBootMode_Type()
)
configBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootMode.setStatus("mandatory")
_ConfigBootFtpServerIp_Type = IpAddress
_ConfigBootFtpServerIp_Object = MibScalar
configBootFtpServerIp = _ConfigBootFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 4),
    _ConfigBootFtpServerIp_Type()
)
configBootFtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootFtpServerIp.setStatus("mandatory")


class _ConfigBootImageFileName_Type(DisplayString):
    """Custom type configBootImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigBootImageFileName_Type.__name__ = "DisplayString"
_ConfigBootImageFileName_Object = MibScalar
configBootImageFileName = _ConfigBootImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 5),
    _ConfigBootImageFileName_Type()
)
configBootImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootImageFileName.setStatus("mandatory")
_ConfigPortTable_Object = MibTable
configPortTable = _ConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6)
)
if mibBuilder.loadTexts:
    configPortTable.setStatus("mandatory")
_ConfigPortEntry_Object = MibTableRow
configPortEntry = _ConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1)
)
configPortEntry.setIndexNames(
    (0, "FSM726S-MIB", "configPort"),
)
if mibBuilder.loadTexts:
    configPortEntry.setStatus("mandatory")
_ConfigPort_Type = Integer32
_ConfigPort_Object = MibTableColumn
configPort = _ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 1),
    _ConfigPort_Type()
)
configPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPort.setStatus("mandatory")


class _ConfigPortDuplex_Type(Integer32):
    """Custom type configPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_ConfigPortDuplex_Type.__name__ = "Integer32"
_ConfigPortDuplex_Object = MibTableColumn
configPortDuplex = _ConfigPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 3),
    _ConfigPortDuplex_Type()
)
configPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortDuplex.setStatus("mandatory")


class _ConfigPortDataRate_Type(Integer32):
    """Custom type configPortDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rate100Meg", 2),
          ("rate10Meg", 1),
          ("rate1Gig", 4))
    )


_ConfigPortDataRate_Type.__name__ = "Integer32"
_ConfigPortDataRate_Object = MibTableColumn
configPortDataRate = _ConfigPortDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 6),
    _ConfigPortDataRate_Type()
)
configPortDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortDataRate.setStatus("mandatory")


class _ConfigPortDuplexOper_Type(Integer32):
    """Custom type configPortDuplexOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_ConfigPortDuplexOper_Type.__name__ = "Integer32"
_ConfigPortDuplexOper_Object = MibTableColumn
configPortDuplexOper = _ConfigPortDuplexOper_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 8),
    _ConfigPortDuplexOper_Type()
)
configPortDuplexOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortDuplexOper.setStatus("mandatory")


class _ConfigPortDataRateOper_Type(Integer32):
    """Custom type configPortDataRateOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rate100Meg", 2),
          ("rate10Meg", 1),
          ("rate1Gig", 4))
    )


_ConfigPortDataRateOper_Type.__name__ = "Integer32"
_ConfigPortDataRateOper_Object = MibTableColumn
configPortDataRateOper = _ConfigPortDataRateOper_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 9),
    _ConfigPortDataRateOper_Type()
)
configPortDataRateOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortDataRateOper.setStatus("mandatory")


class _ConfigPortStateOper_Type(Integer32):
    """Custom type configPortStateOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_ConfigPortStateOper_Type.__name__ = "Integer32"
_ConfigPortStateOper_Object = MibTableColumn
configPortStateOper = _ConfigPortStateOper_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 10),
    _ConfigPortStateOper_Type()
)
configPortStateOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortStateOper.setStatus("mandatory")


class _ConfigPortFlowControl_Type(Integer32):
    """Custom type configPortFlowControl based on Integer32"""
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


_ConfigPortFlowControl_Type.__name__ = "Integer32"
_ConfigPortFlowControl_Object = MibTableColumn
configPortFlowControl = _ConfigPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 11),
    _ConfigPortFlowControl_Type()
)
configPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortFlowControl.setStatus("mandatory")


class _ConfigPortDefaultVlanId_Type(Integer32):
    """Custom type configPortDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ConfigPortDefaultVlanId_Type.__name__ = "Integer32"
_ConfigPortDefaultVlanId_Object = MibTableColumn
configPortDefaultVlanId = _ConfigPortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 12),
    _ConfigPortDefaultVlanId_Type()
)
configPortDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortDefaultVlanId.setStatus("mandatory")


class _ConfigPortComments_Type(DisplayString):
    """Custom type configPortComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigPortComments_Type.__name__ = "DisplayString"
_ConfigPortComments_Object = MibTableColumn
configPortComments = _ConfigPortComments_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 13),
    _ConfigPortComments_Type()
)
configPortComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortComments.setStatus("mandatory")


class _ConfigPortAutoNegotiation_Type(Integer32):
    """Custom type configPortAutoNegotiation based on Integer32"""
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


_ConfigPortAutoNegotiation_Type.__name__ = "Integer32"
_ConfigPortAutoNegotiation_Object = MibTableColumn
configPortAutoNegotiation = _ConfigPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 14),
    _ConfigPortAutoNegotiation_Type()
)
configPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortAutoNegotiation.setStatus("mandatory")


class _ConfigPortFlowControlOper_Type(Integer32):
    """Custom type configPortFlowControlOper based on Integer32"""
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


_ConfigPortFlowControlOper_Type.__name__ = "Integer32"
_ConfigPortFlowControlOper_Object = MibTableColumn
configPortFlowControlOper = _ConfigPortFlowControlOper_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 16),
    _ConfigPortFlowControlOper_Type()
)
configPortFlowControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortFlowControlOper.setStatus("mandatory")


class _ConfigPortGBIC_Type(Integer32):
    """Custom type configPortGBIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 1),
          ("fx", 3),
          ("gigabitEthernetGBIC", 6),
          ("gigabitEthernetLX", 5),
          ("gigabitEthernetSX", 4),
          ("gigabitEthernetTP", 7),
          ("mii", 2))
    )


_ConfigPortGBIC_Type.__name__ = "Integer32"
_ConfigPortGBIC_Object = MibTableColumn
configPortGBIC = _ConfigPortGBIC_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 17),
    _ConfigPortGBIC_Type()
)
configPortGBIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortGBIC.setStatus("mandatory")


class _ConfigPortFastLink_Type(Integer32):
    """Custom type configPortFastLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfigPortFastLink_Type.__name__ = "Integer32"
_ConfigPortFastLink_Object = MibTableColumn
configPortFastLink = _ConfigPortFastLink_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 18),
    _ConfigPortFastLink_Type()
)
configPortFastLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortFastLink.setStatus("mandatory")


class _ConfigPortPriority_Type(Integer32):
    """Custom type configPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_ConfigPortPriority_Type.__name__ = "Integer32"
_ConfigPortPriority_Object = MibTableColumn
configPortPriority = _ConfigPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 19),
    _ConfigPortPriority_Type()
)
configPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortPriority.setStatus("mandatory")


class _ConfigPortBroadcastControl_Type(Integer32):
    """Custom type configPortBroadcastControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488100),
    )


_ConfigPortBroadcastControl_Type.__name__ = "Integer32"
_ConfigPortBroadcastControl_Object = MibTableColumn
configPortBroadcastControl = _ConfigPortBroadcastControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 6, 1, 20),
    _ConfigPortBroadcastControl_Type()
)
configPortBroadcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortBroadcastControl.setStatus("mandatory")


class _ConfigMirroringOnOff_Type(Integer32):
    """Custom type configMirroringOnOff based on Integer32"""
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


_ConfigMirroringOnOff_Type.__name__ = "Integer32"
_ConfigMirroringOnOff_Object = MibScalar
configMirroringOnOff = _ConfigMirroringOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 8),
    _ConfigMirroringOnOff_Type()
)
configMirroringOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirroringOnOff.setStatus("mandatory")
_ConfigMirrorSrc_Type = Integer32
_ConfigMirrorSrc_Object = MibScalar
configMirrorSrc = _ConfigMirrorSrc_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 9),
    _ConfigMirrorSrc_Type()
)
configMirrorSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorSrc.setStatus("mandatory")
_ConfigMirrorMon_Type = Integer32
_ConfigMirrorMon_Object = MibScalar
configMirrorMon = _ConfigMirrorMon_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 10),
    _ConfigMirrorMon_Type()
)
configMirrorMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorMon.setStatus("mandatory")


class _ConfigIpAssignmentMode_Type(Integer32):
    """Custom type configIpAssignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootP", 2),
          ("dhcp", 3),
          ("manual", 1))
    )


_ConfigIpAssignmentMode_Type.__name__ = "Integer32"
_ConfigIpAssignmentMode_Object = MibScalar
configIpAssignmentMode = _ConfigIpAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 12),
    _ConfigIpAssignmentMode_Type()
)
configIpAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAssignmentMode.setStatus("mandatory")
_ConfigPhysAddress_Type = MacAddress
_ConfigPhysAddress_Object = MibScalar
configPhysAddress = _ConfigPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 13),
    _ConfigPhysAddress_Type()
)
configPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhysAddress.setStatus("mandatory")


class _ConfigPasswordAdmin_Type(DisplayString):
    """Custom type configPasswordAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConfigPasswordAdmin_Type.__name__ = "DisplayString"
_ConfigPasswordAdmin_Object = MibScalar
configPasswordAdmin = _ConfigPasswordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 15),
    _ConfigPasswordAdmin_Type()
)
configPasswordAdmin.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    configPasswordAdmin.setStatus("mandatory")
_ConfigIpAddress_Type = IpAddress
_ConfigIpAddress_Object = MibScalar
configIpAddress = _ConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 16),
    _ConfigIpAddress_Type()
)
configIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAddress.setStatus("mandatory")
_ConfigNetMask_Type = IpAddress
_ConfigNetMask_Object = MibScalar
configNetMask = _ConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 17),
    _ConfigNetMask_Type()
)
configNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetMask.setStatus("mandatory")
_ConfigGateway_Type = IpAddress
_ConfigGateway_Object = MibScalar
configGateway = _ConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 18),
    _ConfigGateway_Type()
)
configGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configGateway.setStatus("mandatory")


class _ConfigSave_Type(Integer32):
    """Custom type configSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("save", 1))
    )


_ConfigSave_Type.__name__ = "Integer32"
_ConfigSave_Object = MibScalar
configSave = _ConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 19),
    _ConfigSave_Type()
)
configSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSave.setStatus("mandatory")


class _ConfigVerBootRomImage_Type(DisplayString):
    """Custom type configVerBootRomImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConfigVerBootRomImage_Type.__name__ = "DisplayString"
_ConfigVerBootRomImage_Object = MibScalar
configVerBootRomImage = _ConfigVerBootRomImage_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 21),
    _ConfigVerBootRomImage_Type()
)
configVerBootRomImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerBootRomImage.setStatus("mandatory")


class _ConfigRestoreDefaults_Type(Integer32):
    """Custom type configRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restore", 1))
    )


_ConfigRestoreDefaults_Type.__name__ = "Integer32"
_ConfigRestoreDefaults_Object = MibScalar
configRestoreDefaults = _ConfigRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 22),
    _ConfigRestoreDefaults_Type()
)
configRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRestoreDefaults.setStatus("mandatory")


class _ConfigIGMPOnOff_Type(Integer32):
    """Custom type configIGMPOnOff based on Integer32"""
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


_ConfigIGMPOnOff_Type.__name__ = "Integer32"
_ConfigIGMPOnOff_Object = MibScalar
configIGMPOnOff = _ConfigIGMPOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 23),
    _ConfigIGMPOnOff_Type()
)
configIGMPOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIGMPOnOff.setStatus("mandatory")


class _ConfigWebOnOff_Type(Integer32):
    """Custom type configWebOnOff based on Integer32"""
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


_ConfigWebOnOff_Type.__name__ = "Integer32"
_ConfigWebOnOff_Object = MibScalar
configWebOnOff = _ConfigWebOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 24),
    _ConfigWebOnOff_Type()
)
configWebOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configWebOnOff.setStatus("mandatory")


class _ConfigHighPriorityOptimization_Type(Integer32):
    """Custom type configHighPriorityOptimization based on Integer32"""
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


_ConfigHighPriorityOptimization_Type.__name__ = "Integer32"
_ConfigHighPriorityOptimization_Object = MibScalar
configHighPriorityOptimization = _ConfigHighPriorityOptimization_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 25),
    _ConfigHighPriorityOptimization_Type()
)
configHighPriorityOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHighPriorityOptimization.setStatus("mandatory")


class _ConfigUserAuthenticationMode_Type(Integer32):
    """Custom type configUserAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("basicPasswordOnly", 1),
          ("basicPasswordThenRemoteRADIUS", 2),
          ("remoteRADIUSOnly", 4))
    )


_ConfigUserAuthenticationMode_Type.__name__ = "Integer32"
_ConfigUserAuthenticationMode_Object = MibScalar
configUserAuthenticationMode = _ConfigUserAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 27),
    _ConfigUserAuthenticationMode_Type()
)
configUserAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configUserAuthenticationMode.setStatus("mandatory")
_ConfigRadiusServerIpAddress_Type = IpAddress
_ConfigRadiusServerIpAddress_Object = MibScalar
configRadiusServerIpAddress = _ConfigRadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 28),
    _ConfigRadiusServerIpAddress_Type()
)
configRadiusServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRadiusServerIpAddress.setStatus("mandatory")


class _ConfigRadiusSharedSecret_Type(DisplayString):
    """Custom type configRadiusSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigRadiusSharedSecret_Type.__name__ = "DisplayString"
_ConfigRadiusSharedSecret_Object = MibScalar
configRadiusSharedSecret = _ConfigRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 29),
    _ConfigRadiusSharedSecret_Type()
)
configRadiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRadiusSharedSecret.setStatus("mandatory")


class _ConfigTelnetConsole_Type(Integer32):
    """Custom type configTelnetConsole based on Integer32"""
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


_ConfigTelnetConsole_Type.__name__ = "Integer32"
_ConfigTelnetConsole_Object = MibScalar
configTelnetConsole = _ConfigTelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 30),
    _ConfigTelnetConsole_Type()
)
configTelnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTelnetConsole.setStatus("mandatory")
_ConfigDiffServTable_Object = MibTable
configDiffServTable = _ConfigDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 31)
)
if mibBuilder.loadTexts:
    configDiffServTable.setStatus("mandatory")
_ConfigDiffServEntry_Object = MibTableRow
configDiffServEntry = _ConfigDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 31, 1)
)
configDiffServEntry.setIndexNames(
    (0, "FSM726S-MIB", "configDiffServDSCP"),
)
if mibBuilder.loadTexts:
    configDiffServEntry.setStatus("mandatory")
_ConfigDiffServDSCP_Type = Integer32
_ConfigDiffServDSCP_Object = MibTableColumn
configDiffServDSCP = _ConfigDiffServDSCP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 31, 1, 1),
    _ConfigDiffServDSCP_Type()
)
configDiffServDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDiffServDSCP.setStatus("mandatory")


class _ConfigDiffServPriority_Type(Integer32):
    """Custom type configDiffServPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_ConfigDiffServPriority_Type.__name__ = "Integer32"
_ConfigDiffServPriority_Object = MibTableColumn
configDiffServPriority = _ConfigDiffServPriority_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 31, 1, 2),
    _ConfigDiffServPriority_Type()
)
configDiffServPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDiffServPriority.setStatus("mandatory")
_ConfigTftpServerIpAddress_Type = IpAddress
_ConfigTftpServerIpAddress_Object = MibScalar
configTftpServerIpAddress = _ConfigTftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 32),
    _ConfigTftpServerIpAddress_Type()
)
configTftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpServerIpAddress.setStatus("mandatory")


class _ConfigTftpServerFileName_Type(DisplayString):
    """Custom type configTftpServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigTftpServerFileName_Type.__name__ = "DisplayString"
_ConfigTftpServerFileName_Object = MibScalar
configTftpServerFileName = _ConfigTftpServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 33),
    _ConfigTftpServerFileName_Type()
)
configTftpServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpServerFileName.setStatus("mandatory")


class _ConfigTftpOperation_Type(Integer32):
    """Custom type configTftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ConfigTftpOperation_Type.__name__ = "Integer32"
_ConfigTftpOperation_Object = MibScalar
configTftpOperation = _ConfigTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 34),
    _ConfigTftpOperation_Type()
)
configTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpOperation.setStatus("mandatory")


class _ConfigIpFilter_Type(Integer32):
    """Custom type configIpFilter based on Integer32"""
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


_ConfigIpFilter_Type.__name__ = "Integer32"
_ConfigIpFilter_Object = MibScalar
configIpFilter = _ConfigIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 35),
    _ConfigIpFilter_Type()
)
configIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFilter.setStatus("mandatory")
_ConfigIpFilterTable_Object = MibTable
configIpFilterTable = _ConfigIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 36)
)
if mibBuilder.loadTexts:
    configIpFilterTable.setStatus("mandatory")
_ConfigIpFilterEntry_Object = MibTableRow
configIpFilterEntry = _ConfigIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 36, 1)
)
configIpFilterEntry.setIndexNames(
    (0, "FSM726S-MIB", "configIpFilterIpAddress"),
)
if mibBuilder.loadTexts:
    configIpFilterEntry.setStatus("mandatory")
_ConfigIpFilterIpAddress_Type = IpAddress
_ConfigIpFilterIpAddress_Object = MibTableColumn
configIpFilterIpAddress = _ConfigIpFilterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 36, 1, 1),
    _ConfigIpFilterIpAddress_Type()
)
configIpFilterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpFilterIpAddress.setStatus("mandatory")


class _ConfigIpFilterStatus_Type(Integer32):
    """Custom type configIpFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_ConfigIpFilterStatus_Type.__name__ = "Integer32"
_ConfigIpFilterStatus_Object = MibTableColumn
configIpFilterStatus = _ConfigIpFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 36, 1, 2),
    _ConfigIpFilterStatus_Type()
)
configIpFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpFilterStatus.setStatus("mandatory")


class _ConfigUserName_Type(DisplayString):
    """Custom type configUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConfigUserName_Type.__name__ = "DisplayString"
_ConfigUserName_Object = MibScalar
configUserName = _ConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 37),
    _ConfigUserName_Type()
)
configUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configUserName.setStatus("mandatory")


class _ConfigPasswordProtection_Type(Integer32):
    """Custom type configPasswordProtection based on Integer32"""
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


_ConfigPasswordProtection_Type.__name__ = "Integer32"
_ConfigPasswordProtection_Object = MibScalar
configPasswordProtection = _ConfigPasswordProtection_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 38),
    _ConfigPasswordProtection_Type()
)
configPasswordProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasswordProtection.setStatus("mandatory")


class _ConfigPasswordEncryption_Type(Integer32):
    """Custom type configPasswordEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearText", 1),
          ("encrypted", 2))
    )


_ConfigPasswordEncryption_Type.__name__ = "Integer32"
_ConfigPasswordEncryption_Object = MibScalar
configPasswordEncryption = _ConfigPasswordEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 39),
    _ConfigPasswordEncryption_Type()
)
configPasswordEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPasswordEncryption.setStatus("mandatory")
_ConfigAuthServerIpAddress_Type = IpAddress
_ConfigAuthServerIpAddress_Object = MibScalar
configAuthServerIpAddress = _ConfigAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 40),
    _ConfigAuthServerIpAddress_Type()
)
configAuthServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAuthServerIpAddress.setStatus("mandatory")


class _ConfigAuthServerSharedSecret_Type(DisplayString):
    """Custom type configAuthServerSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigAuthServerSharedSecret_Type.__name__ = "DisplayString"
_ConfigAuthServerSharedSecret_Object = MibScalar
configAuthServerSharedSecret = _ConfigAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 11, 41),
    _ConfigAuthServerSharedSecret_Type()
)
configAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAuthServerSharedSecret.setStatus("mandatory")
_NetgearVlanGroup_ObjectIdentity = ObjectIdentity
netgearVlanGroup = _NetgearVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("mandatory")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "FSM726S-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("mandatory")
_VlanId_Type = Integer32
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 1, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("mandatory")


class _VlanName_Type(DisplayString):
    """Custom type vlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VlanName_Type.__name__ = "DisplayString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 1, 1, 2),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanName.setStatus("mandatory")


class _VlanStatus_Type(Integer32):
    """Custom type vlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VlanStatus_Type.__name__ = "Integer32"
_VlanStatus_Object = MibTableColumn
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 1, 1, 3),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("mandatory")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("mandatory")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "FSM726S-MIB", "vlanPortPortId"),
    (0, "FSM726S-MIB", "vlanPortVlanId"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("mandatory")
_VlanPortPortId_Type = Integer32
_VlanPortPortId_Object = MibTableColumn
vlanPortPortId = _VlanPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2, 1, 1),
    _VlanPortPortId_Type()
)
vlanPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortPortId.setStatus("mandatory")
_VlanPortVlanId_Type = Integer32
_VlanPortVlanId_Object = MibTableColumn
vlanPortVlanId = _VlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2, 1, 2),
    _VlanPortVlanId_Type()
)
vlanPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortVlanId.setStatus("mandatory")


class _VlanPortStatus_Type(Integer32):
    """Custom type vlanPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VlanPortStatus_Type.__name__ = "Integer32"
_VlanPortStatus_Object = MibTableColumn
vlanPortStatus = _VlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2, 1, 3),
    _VlanPortStatus_Type()
)
vlanPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortStatus.setStatus("mandatory")


class _VlanPortTaggedMode_Type(Integer32):
    """Custom type vlanPortTaggedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 1))
    )


_VlanPortTaggedMode_Type.__name__ = "Integer32"
_VlanPortTaggedMode_Object = MibTableColumn
vlanPortTaggedMode = _VlanPortTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 13, 2, 1, 4),
    _VlanPortTaggedMode_Type()
)
vlanPortTaggedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortTaggedMode.setStatus("mandatory")
_NetgearPortTrunkGroup_ObjectIdentity = ObjectIdentity
netgearPortTrunkGroup = _NetgearPortTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14)
)
_PortTrunkTable_Object = MibTable
portTrunkTable = _PortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    portTrunkTable.setStatus("mandatory")
_PortTrunkEntry_Object = MibTableRow
portTrunkEntry = _PortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14, 1, 1)
)
portTrunkEntry.setIndexNames(
    (0, "FSM726S-MIB", "portTrunkId"),
    (0, "FSM726S-MIB", "portTrunkMember"),
)
if mibBuilder.loadTexts:
    portTrunkEntry.setStatus("mandatory")
_PortTrunkId_Type = Integer32
_PortTrunkId_Object = MibTableColumn
portTrunkId = _PortTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14, 1, 1, 1),
    _PortTrunkId_Type()
)
portTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkId.setStatus("mandatory")
_PortTrunkMember_Type = Integer32
_PortTrunkMember_Object = MibTableColumn
portTrunkMember = _PortTrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14, 1, 1, 2),
    _PortTrunkMember_Type()
)
portTrunkMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkMember.setStatus("mandatory")
_PortTrunkMemberValue_Type = Integer32
_PortTrunkMemberValue_Object = MibTableColumn
portTrunkMemberValue = _PortTrunkMemberValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1, 14, 1, 1, 3),
    _PortTrunkMemberValue_Type()
)
portTrunkMemberValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkMemberValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSM726S-MIB",
    **{"OwnerString": OwnerString,
       "MacAddress": MacAddress,
       "netgear": netgear,
       "snmpManagedSwitch": snmpManagedSwitch,
       "fsm726s": fsm726s,
       "netgearCommGroup": netgearCommGroup,
       "commTable": commTable,
       "commEntry": commEntry,
       "commIndex": commIndex,
       "commName": commName,
       "commGet": commGet,
       "commSet": commSet,
       "commTrap": commTrap,
       "commStatus": commStatus,
       "netgearHostGroup": netgearHostGroup,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostIndex": hostIndex,
       "hostName": hostName,
       "hostIP": hostIP,
       "hostComm": hostComm,
       "hostStatus": hostStatus,
       "netgearMiscGroup": netgearMiscGroup,
       "miscReset": miscReset,
       "miscStatisticsReset": miscStatisticsReset,
       "netgearSpanGroup": netgearSpanGroup,
       "spanOnOff": spanOnOff,
       "netgearConfigGroup": netgearConfigGroup,
       "configVerSwPrimary": configVerSwPrimary,
       "configVerHwChipSet": configVerHwChipSet,
       "configBootMode": configBootMode,
       "configBootFtpServerIp": configBootFtpServerIp,
       "configBootImageFileName": configBootImageFileName,
       "configPortTable": configPortTable,
       "configPortEntry": configPortEntry,
       "configPort": configPort,
       "configPortDuplex": configPortDuplex,
       "configPortDataRate": configPortDataRate,
       "configPortDuplexOper": configPortDuplexOper,
       "configPortDataRateOper": configPortDataRateOper,
       "configPortStateOper": configPortStateOper,
       "configPortFlowControl": configPortFlowControl,
       "configPortDefaultVlanId": configPortDefaultVlanId,
       "configPortComments": configPortComments,
       "configPortAutoNegotiation": configPortAutoNegotiation,
       "configPortFlowControlOper": configPortFlowControlOper,
       "configPortGBIC": configPortGBIC,
       "configPortFastLink": configPortFastLink,
       "configPortPriority": configPortPriority,
       "configPortBroadcastControl": configPortBroadcastControl,
       "configMirroringOnOff": configMirroringOnOff,
       "configMirrorSrc": configMirrorSrc,
       "configMirrorMon": configMirrorMon,
       "configIpAssignmentMode": configIpAssignmentMode,
       "configPhysAddress": configPhysAddress,
       "configPasswordAdmin": configPasswordAdmin,
       "configIpAddress": configIpAddress,
       "configNetMask": configNetMask,
       "configGateway": configGateway,
       "configSave": configSave,
       "configVerBootRomImage": configVerBootRomImage,
       "configRestoreDefaults": configRestoreDefaults,
       "configIGMPOnOff": configIGMPOnOff,
       "configWebOnOff": configWebOnOff,
       "configHighPriorityOptimization": configHighPriorityOptimization,
       "configUserAuthenticationMode": configUserAuthenticationMode,
       "configRadiusServerIpAddress": configRadiusServerIpAddress,
       "configRadiusSharedSecret": configRadiusSharedSecret,
       "configTelnetConsole": configTelnetConsole,
       "configDiffServTable": configDiffServTable,
       "configDiffServEntry": configDiffServEntry,
       "configDiffServDSCP": configDiffServDSCP,
       "configDiffServPriority": configDiffServPriority,
       "configTftpServerIpAddress": configTftpServerIpAddress,
       "configTftpServerFileName": configTftpServerFileName,
       "configTftpOperation": configTftpOperation,
       "configIpFilter": configIpFilter,
       "configIpFilterTable": configIpFilterTable,
       "configIpFilterEntry": configIpFilterEntry,
       "configIpFilterIpAddress": configIpFilterIpAddress,
       "configIpFilterStatus": configIpFilterStatus,
       "configUserName": configUserName,
       "configPasswordProtection": configPasswordProtection,
       "configPasswordEncryption": configPasswordEncryption,
       "configAuthServerIpAddress": configAuthServerIpAddress,
       "configAuthServerSharedSecret": configAuthServerSharedSecret,
       "netgearVlanGroup": netgearVlanGroup,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "vlanName": vlanName,
       "vlanStatus": vlanStatus,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortPortId": vlanPortPortId,
       "vlanPortVlanId": vlanPortVlanId,
       "vlanPortStatus": vlanPortStatus,
       "vlanPortTaggedMode": vlanPortTaggedMode,
       "netgearPortTrunkGroup": netgearPortTrunkGroup,
       "portTrunkTable": portTrunkTable,
       "portTrunkEntry": portTrunkEntry,
       "portTrunkId": portTrunkId,
       "portTrunkMember": portTrunkMember,
       "portTrunkMemberValue": portTrunkMemberValue}
)
