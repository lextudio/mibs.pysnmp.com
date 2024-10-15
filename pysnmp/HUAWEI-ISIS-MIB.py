# SNMP MIB module (HUAWEI-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:14 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huaweiMgmt")

(isisCircAdjChanges,
 isisCircEntry,
 isisCircInitFails,
 isisCircLANL1DesISChanges,
 isisCircLANL2DesISChanges,
 isisCircRejAdjs,
 isisIPRAEntry,
 isisISAdjNeighSysID,
 isisISAdjState,
 isisSysAttmptToExMaxSeqNums,
 isisSysAuthFails,
 isisSysCorrLSPs,
 isisSysEntry,
 isisSysID,
 isisSysIDFieldLenMismatches,
 isisSysL1State,
 isisSysL2State,
 isisSysLSPL1DbaseOloads,
 isisSysLSPL2DbaseOloads,
 isisSysManAddrDropFromAreas,
 isisSysMaxAreaAddrMismatches,
 isisSysMaxAreaAddresses,
 isisSysOwnLSPPurges,
 isisSysSeqNumSkips,
 isisSysType,
 isisSysVersion) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "isisCircAdjChanges",
    "isisCircEntry",
    "isisCircInitFails",
    "isisCircLANL1DesISChanges",
    "isisCircLANL2DesISChanges",
    "isisCircRejAdjs",
    "isisIPRAEntry",
    "isisISAdjNeighSysID",
    "isisISAdjState",
    "isisSysAttmptToExMaxSeqNums",
    "isisSysAuthFails",
    "isisSysCorrLSPs",
    "isisSysEntry",
    "isisSysID",
    "isisSysIDFieldLenMismatches",
    "isisSysL1State",
    "isisSysL2State",
    "isisSysLSPL1DbaseOloads",
    "isisSysLSPL2DbaseOloads",
    "isisSysManAddrDropFromAreas",
    "isisSysMaxAreaAddrMismatches",
    "isisSysMaxAreaAddresses",
    "isisSysOwnLSPPurges",
    "isisSysSeqNumSkips",
    "isisSysType",
    "isisSysVersion")

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

hwISIS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24)
)


# Types definitions



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )





class OSINSAddress(OctetString):
    """Custom type OSINSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )




# TEXTUAL-CONVENTIONS



class LSPID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



# MIB Managed Objects in the order of their OIDs

_HuaweiDatacomm_ObjectIdentity = ObjectIdentity
huaweiDatacomm = _HuaweiDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_HwIsisSystem_ObjectIdentity = ObjectIdentity
hwIsisSystem = _HwIsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1)
)
if mibBuilder.loadTexts:
    hwIsisSystem.setStatus("current")
_HwIsisSysTable_Object = MibTable
hwIsisSysTable = _HwIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisSysTable.setStatus("current")
_HwIsisSysEntry_Object = MibTableRow
hwIsisSysEntry = _HwIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisSysEntry.setStatus("current")
_HwIsisSysWrongSysTypes_Type = Counter32
_HwIsisSysWrongSysTypes_Object = MibTableColumn
hwIsisSysWrongSysTypes = _HwIsisSysWrongSysTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 1),
    _HwIsisSysWrongSysTypes_Type()
)
hwIsisSysWrongSysTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisSysWrongSysTypes.setStatus("current")
_HwIsisSysAuthAreaRecvPwd1_Type = OctetString
_HwIsisSysAuthAreaRecvPwd1_Object = MibTableColumn
hwIsisSysAuthAreaRecvPwd1 = _HwIsisSysAuthAreaRecvPwd1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 2),
    _HwIsisSysAuthAreaRecvPwd1_Type()
)
hwIsisSysAuthAreaRecvPwd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthAreaRecvPwd1.setStatus("current")
_HwIsisSysAuthAreaRecvPwd2_Type = OctetString
_HwIsisSysAuthAreaRecvPwd2_Object = MibTableColumn
hwIsisSysAuthAreaRecvPwd2 = _HwIsisSysAuthAreaRecvPwd2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 3),
    _HwIsisSysAuthAreaRecvPwd2_Type()
)
hwIsisSysAuthAreaRecvPwd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthAreaRecvPwd2.setStatus("current")
_HwIsisSysAuthAreaRecvPwd3_Type = OctetString
_HwIsisSysAuthAreaRecvPwd3_Object = MibTableColumn
hwIsisSysAuthAreaRecvPwd3 = _HwIsisSysAuthAreaRecvPwd3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 4),
    _HwIsisSysAuthAreaRecvPwd3_Type()
)
hwIsisSysAuthAreaRecvPwd3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthAreaRecvPwd3.setStatus("current")
_HwIsisSysAuthDomainRecvPwd1_Type = OctetString
_HwIsisSysAuthDomainRecvPwd1_Object = MibTableColumn
hwIsisSysAuthDomainRecvPwd1 = _HwIsisSysAuthDomainRecvPwd1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 5),
    _HwIsisSysAuthDomainRecvPwd1_Type()
)
hwIsisSysAuthDomainRecvPwd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthDomainRecvPwd1.setStatus("current")
_HwIsisSysAuthDomainRecvPwd2_Type = OctetString
_HwIsisSysAuthDomainRecvPwd2_Object = MibTableColumn
hwIsisSysAuthDomainRecvPwd2 = _HwIsisSysAuthDomainRecvPwd2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 6),
    _HwIsisSysAuthDomainRecvPwd2_Type()
)
hwIsisSysAuthDomainRecvPwd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthDomainRecvPwd2.setStatus("current")
_HwIsisSysAuthDomainRecvPwd3_Type = OctetString
_HwIsisSysAuthDomainRecvPwd3_Object = MibTableColumn
hwIsisSysAuthDomainRecvPwd3 = _HwIsisSysAuthDomainRecvPwd3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 7),
    _HwIsisSysAuthDomainRecvPwd3_Type()
)
hwIsisSysAuthDomainRecvPwd3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysAuthDomainRecvPwd3.setStatus("current")


class _HwIsisSysSetLSDBOload_Type(TruthValue):
    """Custom type hwIsisSysSetLSDBOload based on TruthValue"""


_HwIsisSysSetLSDBOload_Object = MibTableColumn
hwIsisSysSetLSDBOload = _HwIsisSysSetLSDBOload_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 1, 1, 1, 8),
    _HwIsisSysSetLSDBOload_Type()
)
hwIsisSysSetLSDBOload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisSysSetLSDBOload.setStatus("current")
_HwIsisCirc_ObjectIdentity = ObjectIdentity
hwIsisCirc = _HwIsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2)
)
if mibBuilder.loadTexts:
    hwIsisCirc.setStatus("current")
_HwIsisCircTable_Object = MibTable
hwIsisCircTable = _HwIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1)
)
if mibBuilder.loadTexts:
    hwIsisCircTable.setStatus("current")
_HwIsisCircEntry_Object = MibTableRow
hwIsisCircEntry = _HwIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisCircEntry.setStatus("current")


class _HwIsisCircFuncState_Type(OperState):
    """Custom type hwIsisCircFuncState based on OperState"""


_HwIsisCircFuncState_Object = MibTableColumn
hwIsisCircFuncState = _HwIsisCircFuncState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1),
    _HwIsisCircFuncState_Type()
)
hwIsisCircFuncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisCircFuncState.setStatus("current")


class _HwIsisCircLevel_Type(Integer32):
    """Custom type hwIsisCircLevel based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2))
    )


_HwIsisCircLevel_Type.__name__ = "Integer32"
_HwIsisCircLevel_Object = MibTableColumn
hwIsisCircLevel = _HwIsisCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 2),
    _HwIsisCircLevel_Type()
)
hwIsisCircLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircLevel.setStatus("current")


class _HwIsisCircL1TransPassword_Type(OctetString):
    """Custom type hwIsisCircL1TransPassword based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL1TransPassword_Object = MibTableColumn
hwIsisCircL1TransPassword = _HwIsisCircL1TransPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 3),
    _HwIsisCircL1TransPassword_Type()
)
hwIsisCircL1TransPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL1TransPassword.setStatus("current")


class _HwIsisCircL1RecvPassword1_Type(OctetString):
    """Custom type hwIsisCircL1RecvPassword1 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL1RecvPassword1_Object = MibTableColumn
hwIsisCircL1RecvPassword1 = _HwIsisCircL1RecvPassword1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 4),
    _HwIsisCircL1RecvPassword1_Type()
)
hwIsisCircL1RecvPassword1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL1RecvPassword1.setStatus("current")


class _HwIsisCircL1RecvPassword2_Type(OctetString):
    """Custom type hwIsisCircL1RecvPassword2 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL1RecvPassword2_Object = MibTableColumn
hwIsisCircL1RecvPassword2 = _HwIsisCircL1RecvPassword2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 5),
    _HwIsisCircL1RecvPassword2_Type()
)
hwIsisCircL1RecvPassword2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL1RecvPassword2.setStatus("current")


class _HwIsisCircL1RecvPassword3_Type(OctetString):
    """Custom type hwIsisCircL1RecvPassword3 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL1RecvPassword3_Object = MibTableColumn
hwIsisCircL1RecvPassword3 = _HwIsisCircL1RecvPassword3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 6),
    _HwIsisCircL1RecvPassword3_Type()
)
hwIsisCircL1RecvPassword3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL1RecvPassword3.setStatus("current")


class _HwIsisCircL2TransPassword_Type(OctetString):
    """Custom type hwIsisCircL2TransPassword based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL2TransPassword_Object = MibTableColumn
hwIsisCircL2TransPassword = _HwIsisCircL2TransPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 7),
    _HwIsisCircL2TransPassword_Type()
)
hwIsisCircL2TransPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL2TransPassword.setStatus("current")


class _HwIsisCircL2RecvPassword1_Type(OctetString):
    """Custom type hwIsisCircL2RecvPassword1 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL2RecvPassword1_Object = MibTableColumn
hwIsisCircL2RecvPassword1 = _HwIsisCircL2RecvPassword1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 8),
    _HwIsisCircL2RecvPassword1_Type()
)
hwIsisCircL2RecvPassword1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL2RecvPassword1.setStatus("current")


class _HwIsisCircL2RecvPassword2_Type(OctetString):
    """Custom type hwIsisCircL2RecvPassword2 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL2RecvPassword2_Object = MibTableColumn
hwIsisCircL2RecvPassword2 = _HwIsisCircL2RecvPassword2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 9),
    _HwIsisCircL2RecvPassword2_Type()
)
hwIsisCircL2RecvPassword2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL2RecvPassword2.setStatus("current")


class _HwIsisCircL2RecvPassword3_Type(OctetString):
    """Custom type hwIsisCircL2RecvPassword3 based on OctetString"""
    defaultHexValue = ""


_HwIsisCircL2RecvPassword3_Object = MibTableColumn
hwIsisCircL2RecvPassword3 = _HwIsisCircL2RecvPassword3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 10),
    _HwIsisCircL2RecvPassword3_Type()
)
hwIsisCircL2RecvPassword3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisCircL2RecvPassword3.setStatus("current")
_HwIsisCircVersionSkews_Type = Counter32
_HwIsisCircVersionSkews_Object = MibTableColumn
hwIsisCircVersionSkews = _HwIsisCircVersionSkews_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 11),
    _HwIsisCircVersionSkews_Type()
)
hwIsisCircVersionSkews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisCircVersionSkews.setStatus("current")
_HwIsisCircStateChanges_Type = Counter32
_HwIsisCircStateChanges_Object = MibTableColumn
hwIsisCircStateChanges = _HwIsisCircStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 12),
    _HwIsisCircStateChanges_Type()
)
hwIsisCircStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisCircStateChanges.setStatus("current")
_HwIsisCircAreaMismatches_Type = Counter32
_HwIsisCircAreaMismatches_Object = MibTableColumn
hwIsisCircAreaMismatches = _HwIsisCircAreaMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 13),
    _HwIsisCircAreaMismatches_Type()
)
hwIsisCircAreaMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisCircAreaMismatches.setStatus("current")
_HwIsisIPReachAddr_ObjectIdentity = ObjectIdentity
hwIsisIPReachAddr = _HwIsisIPReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 3)
)
if mibBuilder.loadTexts:
    hwIsisIPReachAddr.setStatus("current")
_HwIsisIPRATable_Object = MibTable
hwIsisIPRATable = _HwIsisIPRATable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 3, 1)
)
if mibBuilder.loadTexts:
    hwIsisIPRATable.setStatus("current")
_HwIsisIPRAEntry_Object = MibTableRow
hwIsisIPRAEntry = _HwIsisIPRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisIPRAEntry.setStatus("current")


class _HwIsisIPRAFuncState_Type(OperState):
    """Custom type hwIsisIPRAFuncState based on OperState"""


_HwIsisIPRAFuncState_Object = MibTableColumn
hwIsisIPRAFuncState = _HwIsisIPRAFuncState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 3, 1, 1, 1),
    _HwIsisIPRAFuncState_Type()
)
hwIsisIPRAFuncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisIPRAFuncState.setStatus("current")
_HwIsisIPRANextHopAddress_Type = IpAddress
_HwIsisIPRANextHopAddress_Object = MibTableColumn
hwIsisIPRANextHopAddress = _HwIsisIPRANextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 3, 1, 1, 3),
    _HwIsisIPRANextHopAddress_Type()
)
hwIsisIPRANextHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsisIPRANextHopAddress.setStatus("current")
_HwIsisNotifications_ObjectIdentity = ObjectIdentity
hwIsisNotifications = _HwIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4)
)
if mibBuilder.loadTexts:
    hwIsisNotifications.setStatus("current")
_HwIsisTrapTable_Object = MibTable
hwIsisTrapTable = _HwIsisTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5)
)
if mibBuilder.loadTexts:
    hwIsisTrapTable.setStatus("current")
_HwIsisTrapEntry_Object = MibTableRow
hwIsisTrapEntry = _HwIsisTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1)
)
hwIsisTrapEntry.setIndexNames(
    (0, "HUAWEI-ISIS-MIB", "hwIsisTrapSysInstance"),
)
if mibBuilder.loadTexts:
    hwIsisTrapEntry.setStatus("current")


class _HwIsisTrapSysInstance_Type(Integer32):
    """Custom type hwIsisTrapSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIsisTrapSysInstance_Type.__name__ = "Integer32"
_HwIsisTrapSysInstance_Object = MibTableColumn
hwIsisTrapSysInstance = _HwIsisTrapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 1),
    _HwIsisTrapSysInstance_Type()
)
hwIsisTrapSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisTrapSysInstance.setStatus("current")
_HwIsisTrapDroppedAreaAddr_Type = OSINSAddress
_HwIsisTrapDroppedAreaAddr_Object = MibTableColumn
hwIsisTrapDroppedAreaAddr = _HwIsisTrapDroppedAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 2),
    _HwIsisTrapDroppedAreaAddr_Type()
)
hwIsisTrapDroppedAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapDroppedAreaAddr.setStatus("current")
_HwIsisTrapCorruptedLSPID_Type = LSPID
_HwIsisTrapCorruptedLSPID_Object = MibTableColumn
hwIsisTrapCorruptedLSPID = _HwIsisTrapCorruptedLSPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 3),
    _HwIsisTrapCorruptedLSPID_Type()
)
hwIsisTrapCorruptedLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapCorruptedLSPID.setStatus("current")
_HwIsisTrapSysIDLength_Type = Integer32
_HwIsisTrapSysIDLength_Object = MibTableColumn
hwIsisTrapSysIDLength = _HwIsisTrapSysIDLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 4),
    _HwIsisTrapSysIDLength_Type()
)
hwIsisTrapSysIDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapSysIDLength.setStatus("current")
_HwIsisTrapRecdSysIDLength_Type = Integer32
_HwIsisTrapRecdSysIDLength_Object = MibTableColumn
hwIsisTrapRecdSysIDLength = _HwIsisTrapRecdSysIDLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 5),
    _HwIsisTrapRecdSysIDLength_Type()
)
hwIsisTrapRecdSysIDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapRecdSysIDLength.setStatus("current")
_HwIsisTrapRecdAreaAddr_Type = OSINSAddress
_HwIsisTrapRecdAreaAddr_Object = MibTableColumn
hwIsisTrapRecdAreaAddr = _HwIsisTrapRecdAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 6),
    _HwIsisTrapRecdAreaAddr_Type()
)
hwIsisTrapRecdAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapRecdAreaAddr.setStatus("current")
_HwIsisTrapAuthErrorType_Type = Integer32
_HwIsisTrapAuthErrorType_Object = MibTableColumn
hwIsisTrapAuthErrorType = _HwIsisTrapAuthErrorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 7),
    _HwIsisTrapAuthErrorType_Type()
)
hwIsisTrapAuthErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapAuthErrorType.setStatus("current")


class _HwIsisTrapAuthErrorInfo_Type(OctetString):
    """Custom type hwIsisTrapAuthErrorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIsisTrapAuthErrorInfo_Type.__name__ = "OctetString"
_HwIsisTrapAuthErrorInfo_Object = MibTableColumn
hwIsisTrapAuthErrorInfo = _HwIsisTrapAuthErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 8),
    _HwIsisTrapAuthErrorInfo_Type()
)
hwIsisTrapAuthErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapAuthErrorInfo.setStatus("current")
_HwIsisTrapRecdSysType_Type = Integer32
_HwIsisTrapRecdSysType_Object = MibTableColumn
hwIsisTrapRecdSysType = _HwIsisTrapRecdSysType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 9),
    _HwIsisTrapRecdSysType_Type()
)
hwIsisTrapRecdSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapRecdSysType.setStatus("current")
_HwIsisTrapRecdVersion_Type = DisplayString
_HwIsisTrapRecdVersion_Object = MibTableColumn
hwIsisTrapRecdVersion = _HwIsisTrapRecdVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 10),
    _HwIsisTrapRecdVersion_Type()
)
hwIsisTrapRecdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapRecdVersion.setStatus("current")
_HwIsisTrapRecdMaxAreaAddr_Type = Integer32
_HwIsisTrapRecdMaxAreaAddr_Object = MibTableColumn
hwIsisTrapRecdMaxAreaAddr = _HwIsisTrapRecdMaxAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 5, 1, 11),
    _HwIsisTrapRecdMaxAreaAddr_Type()
)
hwIsisTrapRecdMaxAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisTrapRecdMaxAreaAddr.setStatus("current")
_HwIsisConformance_ObjectIdentity = ObjectIdentity
hwIsisConformance = _HwIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6)
)
_HwIsisCompliances_ObjectIdentity = ObjectIdentity
hwIsisCompliances = _HwIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 1)
)
_HwIsisGroups_ObjectIdentity = ObjectIdentity
hwIsisGroups = _HwIsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 2)
)
isisSysEntry.registerAugmentions(
    ("HUAWEI-ISIS-MIB",
     "hwIsisSysEntry")
)
hwIsisSysEntry.setIndexNames(*isisSysEntry.getIndexNames())
isisCircEntry.registerAugmentions(
    ("HUAWEI-ISIS-MIB",
     "hwIsisCircEntry")
)
hwIsisCircEntry.setIndexNames(*isisCircEntry.getIndexNames())
isisIPRAEntry.registerAugmentions(
    ("HUAWEI-ISIS-MIB",
     "hwIsisIPRAEntry")
)
hwIsisIPRAEntry.setIndexNames(*isisIPRAEntry.getIndexNames())

# Managed Objects groups

hwIsisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 2, 1)
)
hwIsisGroup.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisSysWrongSysTypes"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthAreaRecvPwd1"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthAreaRecvPwd2"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthAreaRecvPwd3"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthDomainRecvPwd1"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthDomainRecvPwd2"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysAuthDomainRecvPwd3"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysSetLSDBOload"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircFuncState"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircLevel"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL1TransPassword"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL1RecvPassword1"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL1RecvPassword2"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL1RecvPassword3"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL2TransPassword"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL2RecvPassword1"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL2RecvPassword2"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircL2RecvPassword3"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircVersionSkews"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircStateChanges"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircAreaMismatches"),
        ("HUAWEI-ISIS-MIB", "hwIsisIPRAFuncState"),
        ("HUAWEI-ISIS-MIB", "hwIsisIPRANextHopAddress"))
)
if mibBuilder.loadTexts:
    hwIsisGroup.setStatus("current")

hwIsisTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 2, 3)
)
hwIsisTrapInfoGroup.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisTrapDroppedAreaAddr"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapCorruptedLSPID"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapSysIDLength"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdSysIDLength"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdAreaAddr"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapAuthErrorType"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapAuthErrorInfo"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdSysType"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdVersion"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdMaxAreaAddr"))
)
if mibBuilder.loadTexts:
    hwIsisTrapInfoGroup.setStatus("current")


# Notification objects

hwIsisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 1)
)
if mibBuilder.loadTexts:
    hwIsisCorruptedLSPDetected.setStatus(
        "current"
    )

hwIsisCorruptedLSPReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 2)
)
hwIsisCorruptedLSPReceived.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisTrapCorruptedLSPID"),
        ("ISIS-MIB", "isisSysCorrLSPs"))
)
if mibBuilder.loadTexts:
    hwIsisCorruptedLSPReceived.setStatus(
        "current"
    )

hwIsisLSPL1DatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 3)
)
hwIsisLSPL1DatabaseOverload.setObjects(
      *(("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysLSPL1DbaseOloads"))
)
if mibBuilder.loadTexts:
    hwIsisLSPL1DatabaseOverload.setStatus(
        "current"
    )

hwIsisLSPL2DatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 4)
)
hwIsisLSPL2DatabaseOverload.setObjects(
      *(("ISIS-MIB", "isisSysL2State"),
        ("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysLSPL2DbaseOloads"))
)
if mibBuilder.loadTexts:
    hwIsisLSPL2DatabaseOverload.setStatus(
        "current"
    )

hwIsisAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 5)
)
hwIsisAuthenticationFailure.setObjects(
      *(("ISIS-MIB", "isisISAdjNeighSysID"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapAuthErrorType"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapAuthErrorInfo"),
        ("ISIS-MIB", "isisSysAuthFails"))
)
if mibBuilder.loadTexts:
    hwIsisAuthenticationFailure.setStatus(
        "current"
    )

hwIsisWrongSysType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 6)
)
hwIsisWrongSysType.setObjects(
      *(("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysType"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdSysType"),
        ("HUAWEI-ISIS-MIB", "hwIsisSysWrongSysTypes"))
)
if mibBuilder.loadTexts:
    hwIsisWrongSysType.setStatus(
        "current"
    )

hwIsisVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 7)
)
hwIsisVersionSkew.setObjects(
      *(("ISIS-MIB", "isisSysVersion"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdVersion"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircVersionSkews"))
)
if mibBuilder.loadTexts:
    hwIsisVersionSkew.setStatus(
        "current"
    )

hwIsisIDFieldLengthMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 8)
)
hwIsisIDFieldLengthMismatch.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisTrapSysIDLength"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdSysIDLength"),
        ("ISIS-MIB", "isisSysIDFieldLenMismatches"))
)
if mibBuilder.loadTexts:
    hwIsisIDFieldLengthMismatch.setStatus(
        "current"
    )

hwIsisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 9)
)
hwIsisAreaMismatch.setObjects(
      *(("ISIS-MIB", "isisSysID"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdAreaAddr"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircAreaMismatches"))
)
if mibBuilder.loadTexts:
    hwIsisAreaMismatch.setStatus(
        "current"
    )

hwIsisMaxAreaAddrMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 10)
)
hwIsisMaxAreaAddrMismatch.setObjects(
      *(("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysMaxAreaAddresses"),
        ("HUAWEI-ISIS-MIB", "hwIsisTrapRecdMaxAreaAddr"),
        ("ISIS-MIB", "isisSysMaxAreaAddrMismatches"))
)
if mibBuilder.loadTexts:
    hwIsisMaxAreaAddrMismatch.setStatus(
        "current"
    )

hwIsisManualAddressDroppedFromArea = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 11)
)
hwIsisManualAddressDroppedFromArea.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisTrapDroppedAreaAddr"),
        ("ISIS-MIB", "isisSysManAddrDropFromAreas"))
)
if mibBuilder.loadTexts:
    hwIsisManualAddressDroppedFromArea.setStatus(
        "current"
    )

hwIsisAttemptToExceedMaximumSequenceNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 12)
)
hwIsisAttemptToExceedMaximumSequenceNumber.setObjects(
    ("ISIS-MIB", "isisSysAttmptToExMaxSeqNums")
)
if mibBuilder.loadTexts:
    hwIsisAttemptToExceedMaximumSequenceNumber.setStatus(
        "current"
    )

hwIsisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 13)
)
hwIsisSequenceNumberSkip.setObjects(
    ("ISIS-MIB", "isisSysSeqNumSkips")
)
if mibBuilder.loadTexts:
    hwIsisSequenceNumberSkip.setStatus(
        "current"
    )

hwIsisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 14)
)
hwIsisOwnLSPPurge.setObjects(
    ("ISIS-MIB", "isisSysOwnLSPPurges")
)
if mibBuilder.loadTexts:
    hwIsisOwnLSPPurge.setStatus(
        "current"
    )

hwIsisCircuitChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 15)
)
hwIsisCircuitChange.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisCircFuncState"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircStateChanges"))
)
if mibBuilder.loadTexts:
    hwIsisCircuitChange.setStatus(
        "current"
    )

hwIsisAdjacencyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 16)
)
hwIsisAdjacencyStateChange.setObjects(
      *(("ISIS-MIB", "isisISAdjState"),
        ("ISIS-MIB", "isisCircAdjChanges"),
        ("ISIS-MIB", "isisISAdjNeighSysID"))
)
if mibBuilder.loadTexts:
    hwIsisAdjacencyStateChange.setStatus(
        "current"
    )

hwIsisInitializationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 17)
)
hwIsisInitializationFailure.setObjects(
      *(("ISIS-MIB", "isisISAdjNeighSysID"),
        ("ISIS-MIB", "isisCircInitFails"))
)
if mibBuilder.loadTexts:
    hwIsisInitializationFailure.setStatus(
        "current"
    )

hwIsisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 18)
)
hwIsisRejectedAdjacency.setObjects(
      *(("ISIS-MIB", "isisISAdjNeighSysID"),
        ("ISIS-MIB", "isisCircRejAdjs"))
)
if mibBuilder.loadTexts:
    hwIsisRejectedAdjacency.setStatus(
        "current"
    )

hwIsisLanL1DesignatedIntermediateSystemChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 19)
)
hwIsisLanL1DesignatedIntermediateSystemChange.setObjects(
    ("ISIS-MIB", "isisCircLANL1DesISChanges")
)
if mibBuilder.loadTexts:
    hwIsisLanL1DesignatedIntermediateSystemChange.setStatus(
        "current"
    )

hwIsisLanL2DesignatedIntermediateSystemChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 4, 20)
)
hwIsisLanL2DesignatedIntermediateSystemChange.setObjects(
    ("ISIS-MIB", "isisCircLANL2DesISChanges")
)
if mibBuilder.loadTexts:
    hwIsisLanL2DesignatedIntermediateSystemChange.setStatus(
        "current"
    )


# Notifications groups

hwIsisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 2, 2)
)
hwIsisNotificationGroup.setObjects(
      *(("HUAWEI-ISIS-MIB", "hwIsisCorruptedLSPDetected"),
        ("HUAWEI-ISIS-MIB", "hwIsisCorruptedLSPReceived"),
        ("HUAWEI-ISIS-MIB", "hwIsisLSPL1DatabaseOverload"),
        ("HUAWEI-ISIS-MIB", "hwIsisLSPL2DatabaseOverload"),
        ("HUAWEI-ISIS-MIB", "hwIsisAuthenticationFailure"),
        ("HUAWEI-ISIS-MIB", "hwIsisWrongSysType"),
        ("HUAWEI-ISIS-MIB", "hwIsisVersionSkew"),
        ("HUAWEI-ISIS-MIB", "hwIsisIDFieldLengthMismatch"),
        ("HUAWEI-ISIS-MIB", "hwIsisAreaMismatch"),
        ("HUAWEI-ISIS-MIB", "hwIsisMaxAreaAddrMismatch"),
        ("HUAWEI-ISIS-MIB", "hwIsisManualAddressDroppedFromArea"),
        ("HUAWEI-ISIS-MIB", "hwIsisAttemptToExceedMaximumSequenceNumber"),
        ("HUAWEI-ISIS-MIB", "hwIsisSequenceNumberSkip"),
        ("HUAWEI-ISIS-MIB", "hwIsisOwnLSPPurge"),
        ("HUAWEI-ISIS-MIB", "hwIsisCircuitChange"),
        ("HUAWEI-ISIS-MIB", "hwIsisAdjacencyStateChange"),
        ("HUAWEI-ISIS-MIB", "hwIsisInitializationFailure"),
        ("HUAWEI-ISIS-MIB", "hwIsisRejectedAdjacency"),
        ("HUAWEI-ISIS-MIB", "hwIsisLanL1DesignatedIntermediateSystemChange"),
        ("HUAWEI-ISIS-MIB", "hwIsisLanL2DesignatedIntermediateSystemChange"))
)
if mibBuilder.loadTexts:
    hwIsisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ISIS-MIB",
    **{"LSPID": LSPID,
       "OperState": OperState,
       "OSINSAddress": OSINSAddress,
       "huaweiDatacomm": huaweiDatacomm,
       "hwISIS": hwISIS,
       "hwIsisSystem": hwIsisSystem,
       "hwIsisSysTable": hwIsisSysTable,
       "hwIsisSysEntry": hwIsisSysEntry,
       "hwIsisSysWrongSysTypes": hwIsisSysWrongSysTypes,
       "hwIsisSysAuthAreaRecvPwd1": hwIsisSysAuthAreaRecvPwd1,
       "hwIsisSysAuthAreaRecvPwd2": hwIsisSysAuthAreaRecvPwd2,
       "hwIsisSysAuthAreaRecvPwd3": hwIsisSysAuthAreaRecvPwd3,
       "hwIsisSysAuthDomainRecvPwd1": hwIsisSysAuthDomainRecvPwd1,
       "hwIsisSysAuthDomainRecvPwd2": hwIsisSysAuthDomainRecvPwd2,
       "hwIsisSysAuthDomainRecvPwd3": hwIsisSysAuthDomainRecvPwd3,
       "hwIsisSysSetLSDBOload": hwIsisSysSetLSDBOload,
       "hwIsisCirc": hwIsisCirc,
       "hwIsisCircTable": hwIsisCircTable,
       "hwIsisCircEntry": hwIsisCircEntry,
       "hwIsisCircFuncState": hwIsisCircFuncState,
       "hwIsisCircLevel": hwIsisCircLevel,
       "hwIsisCircL1TransPassword": hwIsisCircL1TransPassword,
       "hwIsisCircL1RecvPassword1": hwIsisCircL1RecvPassword1,
       "hwIsisCircL1RecvPassword2": hwIsisCircL1RecvPassword2,
       "hwIsisCircL1RecvPassword3": hwIsisCircL1RecvPassword3,
       "hwIsisCircL2TransPassword": hwIsisCircL2TransPassword,
       "hwIsisCircL2RecvPassword1": hwIsisCircL2RecvPassword1,
       "hwIsisCircL2RecvPassword2": hwIsisCircL2RecvPassword2,
       "hwIsisCircL2RecvPassword3": hwIsisCircL2RecvPassword3,
       "hwIsisCircVersionSkews": hwIsisCircVersionSkews,
       "hwIsisCircStateChanges": hwIsisCircStateChanges,
       "hwIsisCircAreaMismatches": hwIsisCircAreaMismatches,
       "hwIsisIPReachAddr": hwIsisIPReachAddr,
       "hwIsisIPRATable": hwIsisIPRATable,
       "hwIsisIPRAEntry": hwIsisIPRAEntry,
       "hwIsisIPRAFuncState": hwIsisIPRAFuncState,
       "hwIsisIPRANextHopAddress": hwIsisIPRANextHopAddress,
       "hwIsisNotifications": hwIsisNotifications,
       "hwIsisCorruptedLSPDetected": hwIsisCorruptedLSPDetected,
       "hwIsisCorruptedLSPReceived": hwIsisCorruptedLSPReceived,
       "hwIsisLSPL1DatabaseOverload": hwIsisLSPL1DatabaseOverload,
       "hwIsisLSPL2DatabaseOverload": hwIsisLSPL2DatabaseOverload,
       "hwIsisAuthenticationFailure": hwIsisAuthenticationFailure,
       "hwIsisWrongSysType": hwIsisWrongSysType,
       "hwIsisVersionSkew": hwIsisVersionSkew,
       "hwIsisIDFieldLengthMismatch": hwIsisIDFieldLengthMismatch,
       "hwIsisAreaMismatch": hwIsisAreaMismatch,
       "hwIsisMaxAreaAddrMismatch": hwIsisMaxAreaAddrMismatch,
       "hwIsisManualAddressDroppedFromArea": hwIsisManualAddressDroppedFromArea,
       "hwIsisAttemptToExceedMaximumSequenceNumber": hwIsisAttemptToExceedMaximumSequenceNumber,
       "hwIsisSequenceNumberSkip": hwIsisSequenceNumberSkip,
       "hwIsisOwnLSPPurge": hwIsisOwnLSPPurge,
       "hwIsisCircuitChange": hwIsisCircuitChange,
       "hwIsisAdjacencyStateChange": hwIsisAdjacencyStateChange,
       "hwIsisInitializationFailure": hwIsisInitializationFailure,
       "hwIsisRejectedAdjacency": hwIsisRejectedAdjacency,
       "hwIsisLanL1DesignatedIntermediateSystemChange": hwIsisLanL1DesignatedIntermediateSystemChange,
       "hwIsisLanL2DesignatedIntermediateSystemChange": hwIsisLanL2DesignatedIntermediateSystemChange,
       "hwIsisTrapTable": hwIsisTrapTable,
       "hwIsisTrapEntry": hwIsisTrapEntry,
       "hwIsisTrapSysInstance": hwIsisTrapSysInstance,
       "hwIsisTrapDroppedAreaAddr": hwIsisTrapDroppedAreaAddr,
       "hwIsisTrapCorruptedLSPID": hwIsisTrapCorruptedLSPID,
       "hwIsisTrapSysIDLength": hwIsisTrapSysIDLength,
       "hwIsisTrapRecdSysIDLength": hwIsisTrapRecdSysIDLength,
       "hwIsisTrapRecdAreaAddr": hwIsisTrapRecdAreaAddr,
       "hwIsisTrapAuthErrorType": hwIsisTrapAuthErrorType,
       "hwIsisTrapAuthErrorInfo": hwIsisTrapAuthErrorInfo,
       "hwIsisTrapRecdSysType": hwIsisTrapRecdSysType,
       "hwIsisTrapRecdVersion": hwIsisTrapRecdVersion,
       "hwIsisTrapRecdMaxAreaAddr": hwIsisTrapRecdMaxAreaAddr,
       "hwIsisConformance": hwIsisConformance,
       "hwIsisCompliances": hwIsisCompliances,
       "hwIsisCompliance": hwIsisCompliance,
       "hwIsisGroups": hwIsisGroups,
       "hwIsisGroup": hwIsisGroup,
       "hwIsisNotificationGroup": hwIsisNotificationGroup,
       "hwIsisTrapInfoGroup": hwIsisTrapInfoGroup}
)
