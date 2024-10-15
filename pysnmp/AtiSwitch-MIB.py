# SNMP MIB module (AtiSwitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AtiSwitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:10 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atiSwitchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15)
)


# Types definitions



class MACAddress(OctetString):
    """Custom type MACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_AtiProduct_ObjectIdentity = ObjectIdentity
atiProduct = _AtiProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_Swhub_ObjectIdentity = ObjectIdentity
swhub = _Swhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
_At_8024_ObjectIdentity = ObjectIdentity
at_8024 = _At_8024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 66)
)
_At_8024GB_ObjectIdentity = ObjectIdentity
at_8024GB = _At_8024GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 67)
)
_At_8024M_ObjectIdentity = ObjectIdentity
at_8024M = _At_8024M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 78)
)
_At_8016F_SC_ObjectIdentity = ObjectIdentity
at_8016F_SC = _At_8016F_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 79)
)
_At_8026FC_ObjectIdentity = ObjectIdentity
at_8026FC = _At_8026FC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 80)
)
_At_8016F_MT_ObjectIdentity = ObjectIdentity
at_8016F_MT = _At_8016F_MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 82)
)
_At_8012M_ObjectIdentity = ObjectIdentity
at_8012M = _At_8012M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 86)
)
_At_8088_SC_ObjectIdentity = ObjectIdentity
at_8088_SC = _At_8088_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 87)
)
_At_8088_MT_ObjectIdentity = ObjectIdentity
at_8088_MT = _At_8088_MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 88)
)
_At_8026T_ObjectIdentity = ObjectIdentity
at_8026T = _At_8026T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 89)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiswitchSysGroup_ObjectIdentity = ObjectIdentity
atiswitchSysGroup = _AtiswitchSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1)
)


class _AtiswitchProductType_Type(Integer32):
    """Custom type atiswitchProductType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("at8012M", 7),
          ("at8016F-MT", 5),
          ("at8016F-SC", 4),
          ("at8024", 1),
          ("at8024GB", 2),
          ("at8024M", 3),
          ("at8026FC", 6),
          ("at8026T", 10),
          ("at8088-MT", 9),
          ("at8088-SC", 8),
          ("other", 20))
    )


_AtiswitchProductType_Type.__name__ = "Integer32"
_AtiswitchProductType_Object = MibScalar
atiswitchProductType = _AtiswitchProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 1),
    _AtiswitchProductType_Type()
)
atiswitchProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchProductType.setStatus("current")
_AtiswitchBasePortCount_Type = Integer32
_AtiswitchBasePortCount_Object = MibScalar
atiswitchBasePortCount = _AtiswitchBasePortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 2),
    _AtiswitchBasePortCount_Type()
)
atiswitchBasePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchBasePortCount.setStatus("current")
_AtiswitchUplinkPortCount_Type = Integer32
_AtiswitchUplinkPortCount_Object = MibScalar
atiswitchUplinkPortCount = _AtiswitchUplinkPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 3),
    _AtiswitchUplinkPortCount_Type()
)
atiswitchUplinkPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchUplinkPortCount.setStatus("current")


class _AtiswitchReset_Type(Integer32):
    """Custom type atiswitchReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchnoreset", 1),
          ("switchreset", 2))
    )


_AtiswitchReset_Type.__name__ = "Integer32"
_AtiswitchReset_Object = MibScalar
atiswitchReset = _AtiswitchReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 4),
    _AtiswitchReset_Type()
)
atiswitchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchReset.setStatus("current")


class _AtiswitchUplink1Type_Type(Integer32):
    """Custom type atiswitchUplink1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("none", 3))
    )


_AtiswitchUplink1Type_Type.__name__ = "Integer32"
_AtiswitchUplink1Type_Object = MibScalar
atiswitchUplink1Type = _AtiswitchUplink1Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 5),
    _AtiswitchUplink1Type_Type()
)
atiswitchUplink1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchUplink1Type.setStatus("current")


class _AtiswitchUplink2Type_Type(Integer32):
    """Custom type atiswitchUplink2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("none", 3))
    )


_AtiswitchUplink2Type_Type.__name__ = "Integer32"
_AtiswitchUplink2Type_Object = MibScalar
atiswitchUplink2Type = _AtiswitchUplink2Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 6),
    _AtiswitchUplink2Type_Type()
)
atiswitchUplink2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchUplink2Type.setStatus("current")
_AtiswitchSwGroup_ObjectIdentity = ObjectIdentity
atiswitchSwGroup = _AtiswitchSwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 7)
)


class _AtiswitchSw_Type(DisplayString):
    """Custom type atiswitchSw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiswitchSw_Type.__name__ = "DisplayString"
_AtiswitchSw_Object = MibScalar
atiswitchSw = _AtiswitchSw_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 7, 1),
    _AtiswitchSw_Type()
)
atiswitchSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchSw.setStatus("current")


class _AtiswitchSwVersion_Type(DisplayString):
    """Custom type atiswitchSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiswitchSwVersion_Type.__name__ = "DisplayString"
_AtiswitchSwVersion_Object = MibScalar
atiswitchSwVersion = _AtiswitchSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 7, 2),
    _AtiswitchSwVersion_Type()
)
atiswitchSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchSwVersion.setStatus("current")
_AtiswitchIpGroup_ObjectIdentity = ObjectIdentity
atiswitchIpGroup = _AtiswitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8)
)
_AtiswitchConfigIpAddress_Type = IpAddress
_AtiswitchConfigIpAddress_Object = MibScalar
atiswitchConfigIpAddress = _AtiswitchConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 1),
    _AtiswitchConfigIpAddress_Type()
)
atiswitchConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchConfigIpAddress.setStatus("current")
_AtiswitchConfigSubMask_Type = IpAddress
_AtiswitchConfigSubMask_Object = MibScalar
atiswitchConfigSubMask = _AtiswitchConfigSubMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 2),
    _AtiswitchConfigSubMask_Type()
)
atiswitchConfigSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchConfigSubMask.setStatus("current")
_AtiswitchConfigRouting_Type = IpAddress
_AtiswitchConfigRouting_Object = MibScalar
atiswitchConfigRouting = _AtiswitchConfigRouting_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 3),
    _AtiswitchConfigRouting_Type()
)
atiswitchConfigRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchConfigRouting.setStatus("current")


class _AtiswitchIPAddressStatus_Type(Integer32):
    """Custom type atiswitchIPAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromBootp", 2),
          ("fromDhcp", 1),
          ("fromStatic", 3))
    )


_AtiswitchIPAddressStatus_Type.__name__ = "Integer32"
_AtiswitchIPAddressStatus_Object = MibScalar
atiswitchIPAddressStatus = _AtiswitchIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 4),
    _AtiswitchIPAddressStatus_Type()
)
atiswitchIPAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchIPAddressStatus.setStatus("current")
_AtiswitchDNServer_Type = IpAddress
_AtiswitchDNServer_Object = MibScalar
atiswitchDNServer = _AtiswitchDNServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 5),
    _AtiswitchDNServer_Type()
)
atiswitchDNServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchDNServer.setStatus("current")
_AtiswitchDefaultDomainName_Type = DisplayString
_AtiswitchDefaultDomainName_Object = MibScalar
atiswitchDefaultDomainName = _AtiswitchDefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 8, 6),
    _AtiswitchDefaultDomainName_Type()
)
atiswitchDefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchDefaultDomainName.setStatus("current")
_AtiswitchNMGroup_ObjectIdentity = ObjectIdentity
atiswitchNMGroup = _AtiswitchNMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 9)
)
_AtiswitchNwMgrTable_Object = MibTable
atiswitchNwMgrTable = _AtiswitchNwMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 9, 1)
)
if mibBuilder.loadTexts:
    atiswitchNwMgrTable.setStatus("current")
_AtiswitchNwMgrEntry_Object = MibTableRow
atiswitchNwMgrEntry = _AtiswitchNwMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 9, 1, 1)
)
atiswitchNwMgrEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchNwMgrIndex"),
)
if mibBuilder.loadTexts:
    atiswitchNwMgrEntry.setStatus("current")


class _AtiswitchNwMgrIndex_Type(Integer32):
    """Custom type atiswitchNwMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtiswitchNwMgrIndex_Type.__name__ = "Integer32"
_AtiswitchNwMgrIndex_Object = MibTableColumn
atiswitchNwMgrIndex = _AtiswitchNwMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 9, 1, 1, 1),
    _AtiswitchNwMgrIndex_Type()
)
atiswitchNwMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchNwMgrIndex.setStatus("current")
_AtiswitchNwMgrIpAddr_Type = IpAddress
_AtiswitchNwMgrIpAddr_Object = MibTableColumn
atiswitchNwMgrIpAddr = _AtiswitchNwMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 1, 9, 1, 1, 2),
    _AtiswitchNwMgrIpAddr_Type()
)
atiswitchNwMgrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchNwMgrIpAddr.setStatus("current")
_AtiswitchConfigGroup_ObjectIdentity = ObjectIdentity
atiswitchConfigGroup = _AtiswitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2)
)


class _AtiswitchMirrorState_Type(Integer32):
    """Custom type atiswitchMirrorState based on Integer32"""
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
        *(("both", 3),
          ("disabled", 4),
          ("receive", 1),
          ("transmit", 2))
    )


_AtiswitchMirrorState_Type.__name__ = "Integer32"
_AtiswitchMirrorState_Object = MibScalar
atiswitchMirrorState = _AtiswitchMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2, 1),
    _AtiswitchMirrorState_Type()
)
atiswitchMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchMirrorState.setStatus("current")
_AtiswitchMirroringSourcePorts_Type = DisplayString
_AtiswitchMirroringSourcePorts_Object = MibScalar
atiswitchMirroringSourcePorts = _AtiswitchMirroringSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2, 2),
    _AtiswitchMirroringSourcePorts_Type()
)
atiswitchMirroringSourcePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchMirroringSourcePorts.setStatus("current")
_AtiswitchMirroringDestinationPort_Type = Integer32
_AtiswitchMirroringDestinationPort_Object = MibScalar
atiswitchMirroringDestinationPort = _AtiswitchMirroringDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2, 3),
    _AtiswitchMirroringDestinationPort_Type()
)
atiswitchMirroringDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchMirroringDestinationPort.setStatus("current")


class _AtiswitchSecurityConfig_Type(Integer32):
    """Custom type atiswitchSecurityConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledLearningLocked", 2),
          ("enabledLimited", 3),
          ("enabledSecured", 4))
    )


_AtiswitchSecurityConfig_Type.__name__ = "Integer32"
_AtiswitchSecurityConfig_Object = MibScalar
atiswitchSecurityConfig = _AtiswitchSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2, 4),
    _AtiswitchSecurityConfig_Type()
)
atiswitchSecurityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchSecurityConfig.setStatus("current")


class _AtiswitchSecurityAction_Type(Integer32):
    """Custom type atiswitchSecurityAction based on Integer32"""
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
        *(("disablePortAndSendTrap", 3),
          ("disablePortOnly", 2),
          ("doNothing", 4),
          ("sendTrapOnly", 1))
    )


_AtiswitchSecurityAction_Type.__name__ = "Integer32"
_AtiswitchSecurityAction_Object = MibScalar
atiswitchSecurityAction = _AtiswitchSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 2, 5),
    _AtiswitchSecurityAction_Type()
)
atiswitchSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchSecurityAction.setStatus("current")
_AtiswitchPortGroup_ObjectIdentity = ObjectIdentity
atiswitchPortGroup = _AtiswitchPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3)
)
_AtiswitchPortTable_Object = MibTable
atiswitchPortTable = _AtiswitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1)
)
if mibBuilder.loadTexts:
    atiswitchPortTable.setStatus("current")
_AtiswitchPortEntry_Object = MibTableRow
atiswitchPortEntry = _AtiswitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1)
)
atiswitchPortEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchPortNumber"),
)
if mibBuilder.loadTexts:
    atiswitchPortEntry.setStatus("current")


class _AtiswitchPortNumber_Type(Integer32):
    """Custom type atiswitchPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchPortNumber_Type.__name__ = "Integer32"
_AtiswitchPortNumber_Object = MibTableColumn
atiswitchPortNumber = _AtiswitchPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 1),
    _AtiswitchPortNumber_Type()
)
atiswitchPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPortNumber.setStatus("current")


class _AtiswitchPortName_Type(DisplayString):
    """Custom type atiswitchPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchPortName_Type.__name__ = "DisplayString"
_AtiswitchPortName_Object = MibTableColumn
atiswitchPortName = _AtiswitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 2),
    _AtiswitchPortName_Type()
)
atiswitchPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortName.setStatus("current")


class _AtiswitchPortAutosenseOrHalfDuplex_Type(Integer32):
    """Custom type atiswitchPortAutosenseOrHalfDuplex based on Integer32"""
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
        *(("forceFullDuplex-100M", 5),
          ("forceFullDuplex-10M", 4),
          ("forceFullDuplex-1G", 7),
          ("forceHalfDuplex-100M", 3),
          ("forceHalfDuplex-10M", 2),
          ("forceHalfDuplex-1G", 6),
          ("portAutoSense", 1))
    )


_AtiswitchPortAutosenseOrHalfDuplex_Type.__name__ = "Integer32"
_AtiswitchPortAutosenseOrHalfDuplex_Object = MibTableColumn
atiswitchPortAutosenseOrHalfDuplex = _AtiswitchPortAutosenseOrHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 3),
    _AtiswitchPortAutosenseOrHalfDuplex_Type()
)
atiswitchPortAutosenseOrHalfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortAutosenseOrHalfDuplex.setStatus("current")


class _AtiswitchPortLinkState_Type(Integer32):
    """Custom type atiswitchPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_AtiswitchPortLinkState_Type.__name__ = "Integer32"
_AtiswitchPortLinkState_Object = MibTableColumn
atiswitchPortLinkState = _AtiswitchPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 4),
    _AtiswitchPortLinkState_Type()
)
atiswitchPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPortLinkState.setStatus("current")


class _AtiswitchPortDuplexStatus_Type(Integer32):
    """Custom type atiswitchPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autosense", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_AtiswitchPortDuplexStatus_Type.__name__ = "Integer32"
_AtiswitchPortDuplexStatus_Object = MibTableColumn
atiswitchPortDuplexStatus = _AtiswitchPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 5),
    _AtiswitchPortDuplexStatus_Type()
)
atiswitchPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPortDuplexStatus.setStatus("current")


class _AtiswitchPortSpeed_Type(Integer32):
    """Custom type atiswitchPortSpeed based on Integer32"""
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
        *(("gigaBits", 3),
          ("hundredMBits", 2),
          ("tenMBits", 1),
          ("unknown", 4))
    )


_AtiswitchPortSpeed_Type.__name__ = "Integer32"
_AtiswitchPortSpeed_Object = MibTableColumn
atiswitchPortSpeed = _AtiswitchPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 6),
    _AtiswitchPortSpeed_Type()
)
atiswitchPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPortSpeed.setStatus("current")


class _AtiswitchPortState_Type(Integer32):
    """Custom type atiswitchPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("learning", 5),
          ("listening", 4),
          ("unknown", 6))
    )


_AtiswitchPortState_Type.__name__ = "Integer32"
_AtiswitchPortState_Object = MibTableColumn
atiswitchPortState = _AtiswitchPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 7),
    _AtiswitchPortState_Type()
)
atiswitchPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortState.setStatus("current")


class _AtiswitchPortFlowControlConfig_Type(Integer32):
    """Custom type atiswitchPortFlowControlConfig based on Integer32"""
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
        *(("disable", 1),
          ("receive-only", 3),
          ("transmit-and-receive", 4),
          ("transmit-only", 2),
          ("unknown", 5))
    )


_AtiswitchPortFlowControlConfig_Type.__name__ = "Integer32"
_AtiswitchPortFlowControlConfig_Object = MibTableColumn
atiswitchPortFlowControlConfig = _AtiswitchPortFlowControlConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 8),
    _AtiswitchPortFlowControlConfig_Type()
)
atiswitchPortFlowControlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortFlowControlConfig.setStatus("current")


class _AtiswitchPortBackPressureConfig_Type(Integer32):
    """Custom type atiswitchPortBackPressureConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("unknown", 3))
    )


_AtiswitchPortBackPressureConfig_Type.__name__ = "Integer32"
_AtiswitchPortBackPressureConfig_Object = MibTableColumn
atiswitchPortBackPressureConfig = _AtiswitchPortBackPressureConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 9),
    _AtiswitchPortBackPressureConfig_Type()
)
atiswitchPortBackPressureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortBackPressureConfig.setStatus("current")


class _AtiswitchPortVlanTagPriorityConfig_Type(Integer32):
    """Custom type atiswitchPortVlanTagPriorityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("override-vlan-priority", 2),
          ("use-vlan-priority", 1))
    )


_AtiswitchPortVlanTagPriorityConfig_Type.__name__ = "Integer32"
_AtiswitchPortVlanTagPriorityConfig_Object = MibTableColumn
atiswitchPortVlanTagPriorityConfig = _AtiswitchPortVlanTagPriorityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 10),
    _AtiswitchPortVlanTagPriorityConfig_Type()
)
atiswitchPortVlanTagPriorityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortVlanTagPriorityConfig.setStatus("current")


class _AtiswitchPortCOSPriorityConfig_Type(Integer32):
    """Custom type atiswitchPortCOSPriorityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtiswitchPortCOSPriorityConfig_Type.__name__ = "Integer32"
_AtiswitchPortCOSPriorityConfig_Object = MibTableColumn
atiswitchPortCOSPriorityConfig = _AtiswitchPortCOSPriorityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 11),
    _AtiswitchPortCOSPriorityConfig_Type()
)
atiswitchPortCOSPriorityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortCOSPriorityConfig.setStatus("current")


class _AtiswitchPortBroadcastConfig_Type(Integer32):
    """Custom type atiswitchPortBroadcastConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard-broadcasts", 1),
          ("do-not-discard-broadcasts", 2))
    )


_AtiswitchPortBroadcastConfig_Type.__name__ = "Integer32"
_AtiswitchPortBroadcastConfig_Object = MibTableColumn
atiswitchPortBroadcastConfig = _AtiswitchPortBroadcastConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 12),
    _AtiswitchPortBroadcastConfig_Type()
)
atiswitchPortBroadcastConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortBroadcastConfig.setStatus("current")


class _AtiswitchPortReset_Type(Integer32):
    """Custom type atiswitchPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 2),
          ("reset", 1))
    )


_AtiswitchPortReset_Type.__name__ = "Integer32"
_AtiswitchPortReset_Object = MibTableColumn
atiswitchPortReset = _AtiswitchPortReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 3, 1, 1, 13),
    _AtiswitchPortReset_Type()
)
atiswitchPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchPortReset.setStatus("current")
_AtiswitchVlanConfigGroup_ObjectIdentity = ObjectIdentity
atiswitchVlanConfigGroup = _AtiswitchVlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4)
)
_AtiswitchBasicVlanTable_Object = MibTable
atiswitchBasicVlanTable = _AtiswitchBasicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1)
)
if mibBuilder.loadTexts:
    atiswitchBasicVlanTable.setStatus("current")
_AtiswitchBasicVlanEntry_Object = MibTableRow
atiswitchBasicVlanEntry = _AtiswitchBasicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1)
)
atiswitchBasicVlanEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchBeVlanIndex"),
)
if mibBuilder.loadTexts:
    atiswitchBasicVlanEntry.setStatus("current")


class _AtiswitchBeVlanIndex_Type(Integer32):
    """Custom type atiswitchBeVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtiswitchBeVlanIndex_Type.__name__ = "Integer32"
_AtiswitchBeVlanIndex_Object = MibTableColumn
atiswitchBeVlanIndex = _AtiswitchBeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 1),
    _AtiswitchBeVlanIndex_Type()
)
atiswitchBeVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchBeVlanIndex.setStatus("current")


class _AtiswitchBeVlanName_Type(DisplayString):
    """Custom type atiswitchBeVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchBeVlanName_Type.__name__ = "DisplayString"
_AtiswitchBeVlanName_Object = MibTableColumn
atiswitchBeVlanName = _AtiswitchBeVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 2),
    _AtiswitchBeVlanName_Type()
)
atiswitchBeVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanName.setStatus("current")


class _AtiswitchBeVlanTagId_Type(Integer32):
    """Custom type atiswitchBeVlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtiswitchBeVlanTagId_Type.__name__ = "Integer32"
_AtiswitchBeVlanTagId_Object = MibTableColumn
atiswitchBeVlanTagId = _AtiswitchBeVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 3),
    _AtiswitchBeVlanTagId_Type()
)
atiswitchBeVlanTagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanTagId.setStatus("current")
_AtiswitchBeVlanTaggedPortMask_Type = DisplayString
_AtiswitchBeVlanTaggedPortMask_Object = MibTableColumn
atiswitchBeVlanTaggedPortMask = _AtiswitchBeVlanTaggedPortMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 4),
    _AtiswitchBeVlanTaggedPortMask_Type()
)
atiswitchBeVlanTaggedPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanTaggedPortMask.setStatus("current")
_AtiswitchBeVlanUntaggedPortMask_Type = DisplayString
_AtiswitchBeVlanUntaggedPortMask_Object = MibTableColumn
atiswitchBeVlanUntaggedPortMask = _AtiswitchBeVlanUntaggedPortMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 5),
    _AtiswitchBeVlanUntaggedPortMask_Type()
)
atiswitchBeVlanUntaggedPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanUntaggedPortMask.setStatus("current")


class _AtiswitchBeVlanMirrorPort_Type(Integer32):
    """Custom type atiswitchBeVlanMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtiswitchBeVlanMirrorPort_Type.__name__ = "Integer32"
_AtiswitchBeVlanMirrorPort_Object = MibTableColumn
atiswitchBeVlanMirrorPort = _AtiswitchBeVlanMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 6),
    _AtiswitchBeVlanMirrorPort_Type()
)
atiswitchBeVlanMirrorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanMirrorPort.setStatus("current")
_AtiswitchBeVlanRowStatus_Type = RowStatus
_AtiswitchBeVlanRowStatus_Object = MibTableColumn
atiswitchBeVlanRowStatus = _AtiswitchBeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 1, 1, 7),
    _AtiswitchBeVlanRowStatus_Type()
)
atiswitchBeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiswitchBeVlanRowStatus.setStatus("current")
_AtiswitchPort2VlanTable_Object = MibTable
atiswitchPort2VlanTable = _AtiswitchPort2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 2)
)
if mibBuilder.loadTexts:
    atiswitchPort2VlanTable.setStatus("current")
_AtiswitchPort2VlanEntry_Object = MibTableRow
atiswitchPort2VlanEntry = _AtiswitchPort2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 2, 1)
)
atiswitchPort2VlanEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchPvPortNumber"),
)
if mibBuilder.loadTexts:
    atiswitchPort2VlanEntry.setStatus("current")


class _AtiswitchPvPortNumber_Type(Integer32):
    """Custom type atiswitchPvPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchPvPortNumber_Type.__name__ = "Integer32"
_AtiswitchPvPortNumber_Object = MibTableColumn
atiswitchPvPortNumber = _AtiswitchPvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 2, 1, 1),
    _AtiswitchPvPortNumber_Type()
)
atiswitchPvPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPvPortNumber.setStatus("current")
_AtiswitchPvVlanName_Type = DisplayString
_AtiswitchPvVlanName_Object = MibTableColumn
atiswitchPvVlanName = _AtiswitchPvVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 2, 1, 2),
    _AtiswitchPvVlanName_Type()
)
atiswitchPvVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchPvVlanName.setStatus("current")


class _AtiswitchVlanMode_Type(Integer32):
    """Custom type atiswitchVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 2),
          ("multiple-802-1Q", 3),
          ("user-configured", 1))
    )


_AtiswitchVlanMode_Type.__name__ = "Integer32"
_AtiswitchVlanMode_Object = MibScalar
atiswitchVlanMode = _AtiswitchVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 3),
    _AtiswitchVlanMode_Type()
)
atiswitchVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchVlanMode.setStatus("current")
_AtiswitchVlanUplinkVlanPort_Type = Integer32
_AtiswitchVlanUplinkVlanPort_Object = MibScalar
atiswitchVlanUplinkVlanPort = _AtiswitchVlanUplinkVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 4, 4),
    _AtiswitchVlanUplinkVlanPort_Type()
)
atiswitchVlanUplinkVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchVlanUplinkVlanPort.setStatus("current")
_AtiswitchEthernetStatsGroup_ObjectIdentity = ObjectIdentity
atiswitchEthernetStatsGroup = _AtiswitchEthernetStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5)
)
_AtiswitchEthMonStats_ObjectIdentity = ObjectIdentity
atiswitchEthMonStats = _AtiswitchEthMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1)
)
_AtiswitchEthMonRxGoodFrames_Type = Counter32
_AtiswitchEthMonRxGoodFrames_Object = MibScalar
atiswitchEthMonRxGoodFrames = _AtiswitchEthMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 1),
    _AtiswitchEthMonRxGoodFrames_Type()
)
atiswitchEthMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonRxGoodFrames.setStatus("current")
_AtiswitchEthMonTxGoodFrames_Type = Counter32
_AtiswitchEthMonTxGoodFrames_Object = MibScalar
atiswitchEthMonTxGoodFrames = _AtiswitchEthMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 2),
    _AtiswitchEthMonTxGoodFrames_Type()
)
atiswitchEthMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxGoodFrames.setStatus("current")
_AtiswitchEthMonTxTotalBytes_Type = Counter32
_AtiswitchEthMonTxTotalBytes_Object = MibScalar
atiswitchEthMonTxTotalBytes = _AtiswitchEthMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 3),
    _AtiswitchEthMonTxTotalBytes_Type()
)
atiswitchEthMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxTotalBytes.setStatus("current")
_AtiswitchEthMonTxDeferred_Type = Counter32
_AtiswitchEthMonTxDeferred_Object = MibScalar
atiswitchEthMonTxDeferred = _AtiswitchEthMonTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 4),
    _AtiswitchEthMonTxDeferred_Type()
)
atiswitchEthMonTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxDeferred.setStatus("current")
_AtiswitchEthMonTxCollisions_Type = Counter32
_AtiswitchEthMonTxCollisions_Object = MibScalar
atiswitchEthMonTxCollisions = _AtiswitchEthMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 5),
    _AtiswitchEthMonTxCollisions_Type()
)
atiswitchEthMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxCollisions.setStatus("current")
_AtiswitchEthMonTxBroadcastFrames_Type = Counter32
_AtiswitchEthMonTxBroadcastFrames_Object = MibScalar
atiswitchEthMonTxBroadcastFrames = _AtiswitchEthMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 6),
    _AtiswitchEthMonTxBroadcastFrames_Type()
)
atiswitchEthMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxBroadcastFrames.setStatus("current")
_AtiswitchEthMonTxMulticastFrames_Type = Counter32
_AtiswitchEthMonTxMulticastFrames_Object = MibScalar
atiswitchEthMonTxMulticastFrames = _AtiswitchEthMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 7),
    _AtiswitchEthMonTxMulticastFrames_Type()
)
atiswitchEthMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonTxMulticastFrames.setStatus("current")
_AtiswitchEthMonRxOverruns_Type = Counter32
_AtiswitchEthMonRxOverruns_Object = MibScalar
atiswitchEthMonRxOverruns = _AtiswitchEthMonRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 1, 8),
    _AtiswitchEthMonRxOverruns_Type()
)
atiswitchEthMonRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthMonRxOverruns.setStatus("current")
_AtiswitchEthErrorStats_ObjectIdentity = ObjectIdentity
atiswitchEthErrorStats = _AtiswitchEthErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2)
)
_AtiswitchEthErrorCRC_Type = Counter32
_AtiswitchEthErrorCRC_Object = MibScalar
atiswitchEthErrorCRC = _AtiswitchEthErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2, 1),
    _AtiswitchEthErrorCRC_Type()
)
atiswitchEthErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthErrorCRC.setStatus("current")
_AtiswitchEthErrorAlignment_Type = Counter32
_AtiswitchEthErrorAlignment_Object = MibScalar
atiswitchEthErrorAlignment = _AtiswitchEthErrorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2, 2),
    _AtiswitchEthErrorAlignment_Type()
)
atiswitchEthErrorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthErrorAlignment.setStatus("current")
_AtiswitchEthErrorRxBadFrames_Type = Counter32
_AtiswitchEthErrorRxBadFrames_Object = MibScalar
atiswitchEthErrorRxBadFrames = _AtiswitchEthErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2, 3),
    _AtiswitchEthErrorRxBadFrames_Type()
)
atiswitchEthErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthErrorRxBadFrames.setStatus("current")
_AtiswitchEthErrorLateCollision_Type = Counter32
_AtiswitchEthErrorLateCollision_Object = MibScalar
atiswitchEthErrorLateCollision = _AtiswitchEthErrorLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2, 4),
    _AtiswitchEthErrorLateCollision_Type()
)
atiswitchEthErrorLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthErrorLateCollision.setStatus("current")
_AtiswitchEthErrorTxTotal_Type = Counter32
_AtiswitchEthErrorTxTotal_Object = MibScalar
atiswitchEthErrorTxTotal = _AtiswitchEthErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 5, 2, 5),
    _AtiswitchEthErrorTxTotal_Type()
)
atiswitchEthErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthErrorTxTotal.setStatus("current")
_AtiswitchEthPortStatsGroup_ObjectIdentity = ObjectIdentity
atiswitchEthPortStatsGroup = _AtiswitchEthPortStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6)
)
_AtiswitchEthPortMonStats_ObjectIdentity = ObjectIdentity
atiswitchEthPortMonStats = _AtiswitchEthPortMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1)
)
_AtiswitchEthPortMonTable_Object = MibTable
atiswitchEthPortMonTable = _AtiswitchEthPortMonTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atiswitchEthPortMonTable.setStatus("current")
_AtiswitchEthPortMonEntry_Object = MibTableRow
atiswitchEthPortMonEntry = _AtiswitchEthPortMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1)
)
atiswitchEthPortMonEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchEthPortMonId"),
)
if mibBuilder.loadTexts:
    atiswitchEthPortMonEntry.setStatus("current")


class _AtiswitchEthPortMonId_Type(Integer32):
    """Custom type atiswitchEthPortMonId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchEthPortMonId_Type.__name__ = "Integer32"
_AtiswitchEthPortMonId_Object = MibTableColumn
atiswitchEthPortMonId = _AtiswitchEthPortMonId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 1),
    _AtiswitchEthPortMonId_Type()
)
atiswitchEthPortMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonId.setStatus("current")
_AtiswitchEthPortMonRxGoodFrames_Type = Counter32
_AtiswitchEthPortMonRxGoodFrames_Object = MibTableColumn
atiswitchEthPortMonRxGoodFrames = _AtiswitchEthPortMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 2),
    _AtiswitchEthPortMonRxGoodFrames_Type()
)
atiswitchEthPortMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonRxGoodFrames.setStatus("current")
_AtiswitchEthPortMonTxGoodFrames_Type = Counter32
_AtiswitchEthPortMonTxGoodFrames_Object = MibTableColumn
atiswitchEthPortMonTxGoodFrames = _AtiswitchEthPortMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 3),
    _AtiswitchEthPortMonTxGoodFrames_Type()
)
atiswitchEthPortMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxGoodFrames.setStatus("current")
_AtiswitchEthPortMonTxTotalBytes_Type = Counter32
_AtiswitchEthPortMonTxTotalBytes_Object = MibTableColumn
atiswitchEthPortMonTxTotalBytes = _AtiswitchEthPortMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 4),
    _AtiswitchEthPortMonTxTotalBytes_Type()
)
atiswitchEthPortMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxTotalBytes.setStatus("current")
_AtiswitchEthPortMonTxDeferred_Type = Counter32
_AtiswitchEthPortMonTxDeferred_Object = MibTableColumn
atiswitchEthPortMonTxDeferred = _AtiswitchEthPortMonTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 5),
    _AtiswitchEthPortMonTxDeferred_Type()
)
atiswitchEthPortMonTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxDeferred.setStatus("current")
_AtiswitchEthPortMonTxCollisions_Type = Counter32
_AtiswitchEthPortMonTxCollisions_Object = MibTableColumn
atiswitchEthPortMonTxCollisions = _AtiswitchEthPortMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 6),
    _AtiswitchEthPortMonTxCollisions_Type()
)
atiswitchEthPortMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxCollisions.setStatus("current")
_AtiswitchEthPortMonTxBroadcastFrames_Type = Counter32
_AtiswitchEthPortMonTxBroadcastFrames_Object = MibTableColumn
atiswitchEthPortMonTxBroadcastFrames = _AtiswitchEthPortMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 7),
    _AtiswitchEthPortMonTxBroadcastFrames_Type()
)
atiswitchEthPortMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxBroadcastFrames.setStatus("current")
_AtiswitchEthPortMonTxMulticastFrames_Type = Counter32
_AtiswitchEthPortMonTxMulticastFrames_Object = MibTableColumn
atiswitchEthPortMonTxMulticastFrames = _AtiswitchEthPortMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 8),
    _AtiswitchEthPortMonTxMulticastFrames_Type()
)
atiswitchEthPortMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonTxMulticastFrames.setStatus("current")
_AtiswitchEthPortMonRxOverruns_Type = Counter32
_AtiswitchEthPortMonRxOverruns_Object = MibTableColumn
atiswitchEthPortMonRxOverruns = _AtiswitchEthPortMonRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 1, 1, 1, 9),
    _AtiswitchEthPortMonRxOverruns_Type()
)
atiswitchEthPortMonRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortMonRxOverruns.setStatus("current")
_AtiswitchEthPortError_ObjectIdentity = ObjectIdentity
atiswitchEthPortError = _AtiswitchEthPortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2)
)
_AtiswitchEthPortErrorTable_Object = MibTable
atiswitchEthPortErrorTable = _AtiswitchEthPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atiswitchEthPortErrorTable.setStatus("current")
_AtiswitchEthPortErrorEntry_Object = MibTableRow
atiswitchEthPortErrorEntry = _AtiswitchEthPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2, 1, 1)
)
atiswitchEthPortErrorEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchEthPortErrorId"),
)
if mibBuilder.loadTexts:
    atiswitchEthPortErrorEntry.setStatus("current")


class _AtiswitchEthPortErrorId_Type(Integer32):
    """Custom type atiswitchEthPortErrorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchEthPortErrorId_Type.__name__ = "Integer32"
_AtiswitchEthPortErrorId_Object = MibTableColumn
atiswitchEthPortErrorId = _AtiswitchEthPortErrorId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2, 1, 1, 1),
    _AtiswitchEthPortErrorId_Type()
)
atiswitchEthPortErrorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortErrorId.setStatus("current")
_AtiswitchEthPortErrorRxBadFrames_Type = Counter32
_AtiswitchEthPortErrorRxBadFrames_Object = MibTableColumn
atiswitchEthPortErrorRxBadFrames = _AtiswitchEthPortErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2, 1, 1, 2),
    _AtiswitchEthPortErrorRxBadFrames_Type()
)
atiswitchEthPortErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortErrorRxBadFrames.setStatus("current")
_AtiswitchEthPortErrorTxTotal_Type = Counter32
_AtiswitchEthPortErrorTxTotal_Object = MibTableColumn
atiswitchEthPortErrorTxTotal = _AtiswitchEthPortErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 6, 2, 1, 1, 3),
    _AtiswitchEthPortErrorTxTotal_Type()
)
atiswitchEthPortErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEthPortErrorTxTotal.setStatus("current")
_AtiswitchFwdVlanGroup_ObjectIdentity = ObjectIdentity
atiswitchFwdVlanGroup = _AtiswitchFwdVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7)
)
_AtiswitchFwdVlanTable_Object = MibTable
atiswitchFwdVlanTable = _AtiswitchFwdVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1)
)
if mibBuilder.loadTexts:
    atiswitchFwdVlanTable.setStatus("current")
_AtiswitchFwdVlanEntry_Object = MibTableRow
atiswitchFwdVlanEntry = _AtiswitchFwdVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1)
)
atiswitchFwdVlanEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchFwdVlanMACAddr"),
)
if mibBuilder.loadTexts:
    atiswitchFwdVlanEntry.setStatus("current")
_AtiswitchFwdVlanMACAddr_Type = MACAddress
_AtiswitchFwdVlanMACAddr_Object = MibTableColumn
atiswitchFwdVlanMACAddr = _AtiswitchFwdVlanMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1, 1),
    _AtiswitchFwdVlanMACAddr_Type()
)
atiswitchFwdVlanMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchFwdVlanMACAddr.setStatus("current")
_AtiswitchFwdVlanVlanId_Type = Integer32
_AtiswitchFwdVlanVlanId_Object = MibTableColumn
atiswitchFwdVlanVlanId = _AtiswitchFwdVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1, 2),
    _AtiswitchFwdVlanVlanId_Type()
)
atiswitchFwdVlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchFwdVlanVlanId.setStatus("current")
_AtiswitchFwdVlanAge_Type = Integer32
_AtiswitchFwdVlanAge_Object = MibTableColumn
atiswitchFwdVlanAge = _AtiswitchFwdVlanAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1, 3),
    _AtiswitchFwdVlanAge_Type()
)
atiswitchFwdVlanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchFwdVlanAge.setStatus("current")


class _AtiswitchFwdVlanStatus_Type(Integer32):
    """Custom type atiswitchFwdVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("other", 3))
    )


_AtiswitchFwdVlanStatus_Type.__name__ = "Integer32"
_AtiswitchFwdVlanStatus_Object = MibTableColumn
atiswitchFwdVlanStatus = _AtiswitchFwdVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1, 4),
    _AtiswitchFwdVlanStatus_Type()
)
atiswitchFwdVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchFwdVlanStatus.setStatus("current")
_AtiswitchFwdVlanPort_Type = Integer32
_AtiswitchFwdVlanPort_Object = MibTableColumn
atiswitchFwdVlanPort = _AtiswitchFwdVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 7, 1, 1, 5),
    _AtiswitchFwdVlanPort_Type()
)
atiswitchFwdVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchFwdVlanPort.setStatus("current")
_AtiswitchStaticMACGroup_ObjectIdentity = ObjectIdentity
atiswitchStaticMACGroup = _AtiswitchStaticMACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8)
)
_AtiswitchStaticMACTable_Object = MibTable
atiswitchStaticMACTable = _AtiswitchStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8, 1)
)
if mibBuilder.loadTexts:
    atiswitchStaticMACTable.setStatus("current")
_AtiswitchStaticMACEntry_Object = MibTableRow
atiswitchStaticMACEntry = _AtiswitchStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8, 1, 1)
)
atiswitchStaticMACEntry.setIndexNames(
    (0, "AtiSwitch-MIB", "atiswitchStaticMACAddress"),
)
if mibBuilder.loadTexts:
    atiswitchStaticMACEntry.setStatus("current")
_AtiswitchStaticMACAddress_Type = MACAddress
_AtiswitchStaticMACAddress_Object = MibTableColumn
atiswitchStaticMACAddress = _AtiswitchStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8, 1, 1, 1),
    _AtiswitchStaticMACAddress_Type()
)
atiswitchStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchStaticMACAddress.setStatus("current")


class _AtiswitchStaticMACPortNumber_Type(Integer32):
    """Custom type atiswitchStaticMACPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchStaticMACPortNumber_Type.__name__ = "Integer32"
_AtiswitchStaticMACPortNumber_Object = MibTableColumn
atiswitchStaticMACPortNumber = _AtiswitchStaticMACPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8, 1, 1, 2),
    _AtiswitchStaticMACPortNumber_Type()
)
atiswitchStaticMACPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchStaticMACPortNumber.setStatus("current")


class _AtiswitchStaticMACEntryStatus_Type(Integer32):
    """Custom type atiswitchStaticMACEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtiswitchStaticMACEntryStatus_Type.__name__ = "Integer32"
_AtiswitchStaticMACEntryStatus_Object = MibTableColumn
atiswitchStaticMACEntryStatus = _AtiswitchStaticMACEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 8, 1, 1, 3),
    _AtiswitchStaticMACEntryStatus_Type()
)
atiswitchStaticMACEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchStaticMACEntryStatus.setStatus("current")
_AtiswitchTraps_ObjectIdentity = ObjectIdentity
atiswitchTraps = _AtiswitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 9)
)

# Managed Objects groups


# Notification objects

atiswitchFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 9, 1)
)
if mibBuilder.loadTexts:
    atiswitchFanStopTrap.setStatus(
        "current"
    )

atiswitchTemperatureAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 15, 9, 2)
)
if mibBuilder.loadTexts:
    atiswitchTemperatureAbnormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AtiSwitch-MIB",
    **{"MACAddress": MACAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "alliedTelesyn": alliedTelesyn,
       "atiProduct": atiProduct,
       "swhub": swhub,
       "at-8024": at_8024,
       "at-8024GB": at_8024GB,
       "at-8024M": at_8024M,
       "at-8016F-SC": at_8016F_SC,
       "at-8026FC": at_8026FC,
       "at-8016F-MT": at_8016F_MT,
       "at-8012M": at_8012M,
       "at-8088-SC": at_8088_SC,
       "at-8088-MT": at_8088_MT,
       "at-8026T": at_8026T,
       "mibObject": mibObject,
       "atiSwitchMib": atiSwitchMib,
       "atiswitchSysGroup": atiswitchSysGroup,
       "atiswitchProductType": atiswitchProductType,
       "atiswitchBasePortCount": atiswitchBasePortCount,
       "atiswitchUplinkPortCount": atiswitchUplinkPortCount,
       "atiswitchReset": atiswitchReset,
       "atiswitchUplink1Type": atiswitchUplink1Type,
       "atiswitchUplink2Type": atiswitchUplink2Type,
       "atiswitchSwGroup": atiswitchSwGroup,
       "atiswitchSw": atiswitchSw,
       "atiswitchSwVersion": atiswitchSwVersion,
       "atiswitchIpGroup": atiswitchIpGroup,
       "atiswitchConfigIpAddress": atiswitchConfigIpAddress,
       "atiswitchConfigSubMask": atiswitchConfigSubMask,
       "atiswitchConfigRouting": atiswitchConfigRouting,
       "atiswitchIPAddressStatus": atiswitchIPAddressStatus,
       "atiswitchDNServer": atiswitchDNServer,
       "atiswitchDefaultDomainName": atiswitchDefaultDomainName,
       "atiswitchNMGroup": atiswitchNMGroup,
       "atiswitchNwMgrTable": atiswitchNwMgrTable,
       "atiswitchNwMgrEntry": atiswitchNwMgrEntry,
       "atiswitchNwMgrIndex": atiswitchNwMgrIndex,
       "atiswitchNwMgrIpAddr": atiswitchNwMgrIpAddr,
       "atiswitchConfigGroup": atiswitchConfigGroup,
       "atiswitchMirrorState": atiswitchMirrorState,
       "atiswitchMirroringSourcePorts": atiswitchMirroringSourcePorts,
       "atiswitchMirroringDestinationPort": atiswitchMirroringDestinationPort,
       "atiswitchSecurityConfig": atiswitchSecurityConfig,
       "atiswitchSecurityAction": atiswitchSecurityAction,
       "atiswitchPortGroup": atiswitchPortGroup,
       "atiswitchPortTable": atiswitchPortTable,
       "atiswitchPortEntry": atiswitchPortEntry,
       "atiswitchPortNumber": atiswitchPortNumber,
       "atiswitchPortName": atiswitchPortName,
       "atiswitchPortAutosenseOrHalfDuplex": atiswitchPortAutosenseOrHalfDuplex,
       "atiswitchPortLinkState": atiswitchPortLinkState,
       "atiswitchPortDuplexStatus": atiswitchPortDuplexStatus,
       "atiswitchPortSpeed": atiswitchPortSpeed,
       "atiswitchPortState": atiswitchPortState,
       "atiswitchPortFlowControlConfig": atiswitchPortFlowControlConfig,
       "atiswitchPortBackPressureConfig": atiswitchPortBackPressureConfig,
       "atiswitchPortVlanTagPriorityConfig": atiswitchPortVlanTagPriorityConfig,
       "atiswitchPortCOSPriorityConfig": atiswitchPortCOSPriorityConfig,
       "atiswitchPortBroadcastConfig": atiswitchPortBroadcastConfig,
       "atiswitchPortReset": atiswitchPortReset,
       "atiswitchVlanConfigGroup": atiswitchVlanConfigGroup,
       "atiswitchBasicVlanTable": atiswitchBasicVlanTable,
       "atiswitchBasicVlanEntry": atiswitchBasicVlanEntry,
       "atiswitchBeVlanIndex": atiswitchBeVlanIndex,
       "atiswitchBeVlanName": atiswitchBeVlanName,
       "atiswitchBeVlanTagId": atiswitchBeVlanTagId,
       "atiswitchBeVlanTaggedPortMask": atiswitchBeVlanTaggedPortMask,
       "atiswitchBeVlanUntaggedPortMask": atiswitchBeVlanUntaggedPortMask,
       "atiswitchBeVlanMirrorPort": atiswitchBeVlanMirrorPort,
       "atiswitchBeVlanRowStatus": atiswitchBeVlanRowStatus,
       "atiswitchPort2VlanTable": atiswitchPort2VlanTable,
       "atiswitchPort2VlanEntry": atiswitchPort2VlanEntry,
       "atiswitchPvPortNumber": atiswitchPvPortNumber,
       "atiswitchPvVlanName": atiswitchPvVlanName,
       "atiswitchVlanMode": atiswitchVlanMode,
       "atiswitchVlanUplinkVlanPort": atiswitchVlanUplinkVlanPort,
       "atiswitchEthernetStatsGroup": atiswitchEthernetStatsGroup,
       "atiswitchEthMonStats": atiswitchEthMonStats,
       "atiswitchEthMonRxGoodFrames": atiswitchEthMonRxGoodFrames,
       "atiswitchEthMonTxGoodFrames": atiswitchEthMonTxGoodFrames,
       "atiswitchEthMonTxTotalBytes": atiswitchEthMonTxTotalBytes,
       "atiswitchEthMonTxDeferred": atiswitchEthMonTxDeferred,
       "atiswitchEthMonTxCollisions": atiswitchEthMonTxCollisions,
       "atiswitchEthMonTxBroadcastFrames": atiswitchEthMonTxBroadcastFrames,
       "atiswitchEthMonTxMulticastFrames": atiswitchEthMonTxMulticastFrames,
       "atiswitchEthMonRxOverruns": atiswitchEthMonRxOverruns,
       "atiswitchEthErrorStats": atiswitchEthErrorStats,
       "atiswitchEthErrorCRC": atiswitchEthErrorCRC,
       "atiswitchEthErrorAlignment": atiswitchEthErrorAlignment,
       "atiswitchEthErrorRxBadFrames": atiswitchEthErrorRxBadFrames,
       "atiswitchEthErrorLateCollision": atiswitchEthErrorLateCollision,
       "atiswitchEthErrorTxTotal": atiswitchEthErrorTxTotal,
       "atiswitchEthPortStatsGroup": atiswitchEthPortStatsGroup,
       "atiswitchEthPortMonStats": atiswitchEthPortMonStats,
       "atiswitchEthPortMonTable": atiswitchEthPortMonTable,
       "atiswitchEthPortMonEntry": atiswitchEthPortMonEntry,
       "atiswitchEthPortMonId": atiswitchEthPortMonId,
       "atiswitchEthPortMonRxGoodFrames": atiswitchEthPortMonRxGoodFrames,
       "atiswitchEthPortMonTxGoodFrames": atiswitchEthPortMonTxGoodFrames,
       "atiswitchEthPortMonTxTotalBytes": atiswitchEthPortMonTxTotalBytes,
       "atiswitchEthPortMonTxDeferred": atiswitchEthPortMonTxDeferred,
       "atiswitchEthPortMonTxCollisions": atiswitchEthPortMonTxCollisions,
       "atiswitchEthPortMonTxBroadcastFrames": atiswitchEthPortMonTxBroadcastFrames,
       "atiswitchEthPortMonTxMulticastFrames": atiswitchEthPortMonTxMulticastFrames,
       "atiswitchEthPortMonRxOverruns": atiswitchEthPortMonRxOverruns,
       "atiswitchEthPortError": atiswitchEthPortError,
       "atiswitchEthPortErrorTable": atiswitchEthPortErrorTable,
       "atiswitchEthPortErrorEntry": atiswitchEthPortErrorEntry,
       "atiswitchEthPortErrorId": atiswitchEthPortErrorId,
       "atiswitchEthPortErrorRxBadFrames": atiswitchEthPortErrorRxBadFrames,
       "atiswitchEthPortErrorTxTotal": atiswitchEthPortErrorTxTotal,
       "atiswitchFwdVlanGroup": atiswitchFwdVlanGroup,
       "atiswitchFwdVlanTable": atiswitchFwdVlanTable,
       "atiswitchFwdVlanEntry": atiswitchFwdVlanEntry,
       "atiswitchFwdVlanMACAddr": atiswitchFwdVlanMACAddr,
       "atiswitchFwdVlanVlanId": atiswitchFwdVlanVlanId,
       "atiswitchFwdVlanAge": atiswitchFwdVlanAge,
       "atiswitchFwdVlanStatus": atiswitchFwdVlanStatus,
       "atiswitchFwdVlanPort": atiswitchFwdVlanPort,
       "atiswitchStaticMACGroup": atiswitchStaticMACGroup,
       "atiswitchStaticMACTable": atiswitchStaticMACTable,
       "atiswitchStaticMACEntry": atiswitchStaticMACEntry,
       "atiswitchStaticMACAddress": atiswitchStaticMACAddress,
       "atiswitchStaticMACPortNumber": atiswitchStaticMACPortNumber,
       "atiswitchStaticMACEntryStatus": atiswitchStaticMACEntryStatus,
       "atiswitchTraps": atiswitchTraps,
       "atiswitchFanStopTrap": atiswitchFanStopTrap,
       "atiswitchTemperatureAbnormalTrap": atiswitchTemperatureAbnormalTrap}
)
