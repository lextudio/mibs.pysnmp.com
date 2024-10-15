# SNMP MIB module (CISCO-AAA-SERVER-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAA-SERVER-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:24 2024
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

(CiscoAAAProtocol,
 casConfigEntry) = mibBuilder.importSymbols(
    "CISCO-AAA-SERVER-MIB",
    "CiscoAAAProtocol",
    "casConfigEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalMin,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalMin",
    "TimeIntervalSec")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAAAServerExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367)
)
ciscoAAAServerExtMIB.setRevisions(
        ("2005-05-23 00:00",
         "2005-05-09 00:00",
         "2003-11-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAAAServerKeyEncrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 2),
          ("notConfigured", 3),
          ("plain", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAAASvrExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAAASvrExtMIBObjects = _CiscoAAASvrExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1)
)
_CAAASvrExtGenericConfig_ObjectIdentity = ObjectIdentity
cAAASvrExtGenericConfig = _CAAASvrExtGenericConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1)
)


class _CAAASvrExtLocalAccLogMaxSize_Type(Unsigned32):
    """Custom type cAAASvrExtLocalAccLogMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CAAASvrExtLocalAccLogMaxSize_Type.__name__ = "Unsigned32"
_CAAASvrExtLocalAccLogMaxSize_Object = MibScalar
cAAASvrExtLocalAccLogMaxSize = _CAAASvrExtLocalAccLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1, 1),
    _CAAASvrExtLocalAccLogMaxSize_Type()
)
cAAASvrExtLocalAccLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAASvrExtLocalAccLogMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cAAASvrExtLocalAccLogMaxSize.setUnits("bytes")


class _CAAASvrExtSvrGrpSvrListMaxEnt_Type(Unsigned32):
    """Custom type cAAASvrExtSvrGrpSvrListMaxEnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CAAASvrExtSvrGrpSvrListMaxEnt_Type.__name__ = "Unsigned32"
_CAAASvrExtSvrGrpSvrListMaxEnt_Object = MibScalar
cAAASvrExtSvrGrpSvrListMaxEnt = _CAAASvrExtSvrGrpSvrListMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1, 2),
    _CAAASvrExtSvrGrpSvrListMaxEnt_Type()
)
cAAASvrExtSvrGrpSvrListMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAAASvrExtSvrGrpSvrListMaxEnt.setStatus("current")


class _CAAASvrExtAppToSvrGrpMaxEnt_Type(Unsigned32):
    """Custom type cAAASvrExtAppToSvrGrpMaxEnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CAAASvrExtAppToSvrGrpMaxEnt_Type.__name__ = "Unsigned32"
_CAAASvrExtAppToSvrGrpMaxEnt_Object = MibScalar
cAAASvrExtAppToSvrGrpMaxEnt = _CAAASvrExtAppToSvrGrpMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1, 3),
    _CAAASvrExtAppToSvrGrpMaxEnt_Type()
)
cAAASvrExtAppToSvrGrpMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAAASvrExtAppToSvrGrpMaxEnt.setStatus("current")


class _CAAASvrExtClearAccLog_Type(Integer32):
    """Custom type cAAASvrExtClearAccLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_CAAASvrExtClearAccLog_Type.__name__ = "Integer32"
_CAAASvrExtClearAccLog_Object = MibScalar
cAAASvrExtClearAccLog = _CAAASvrExtClearAccLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1, 4),
    _CAAASvrExtClearAccLog_Type()
)
cAAASvrExtClearAccLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAASvrExtClearAccLog.setStatus("current")


class _CAAALoginAuthTypeMSCHAP_Type(TruthValue):
    """Custom type cAAALoginAuthTypeMSCHAP based on TruthValue"""


_CAAALoginAuthTypeMSCHAP_Object = MibScalar
cAAALoginAuthTypeMSCHAP = _CAAALoginAuthTypeMSCHAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 1, 5),
    _CAAALoginAuthTypeMSCHAP_Type()
)
cAAALoginAuthTypeMSCHAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAALoginAuthTypeMSCHAP.setStatus("current")
_CAAASvrExtSvrTableConfig_ObjectIdentity = ObjectIdentity
cAAASvrExtSvrTableConfig = _CAAASvrExtSvrTableConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2)
)
_CAAASvrExtConfigTable_Object = MibTable
cAAASvrExtConfigTable = _CAAASvrExtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cAAASvrExtConfigTable.setStatus("current")
_CAAASvrExtConfigEntry_Object = MibTableRow
cAAASvrExtConfigEntry = _CAAASvrExtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cAAASvrExtConfigEntry.setStatus("current")


class _CAAAServerAddrType_Type(InetAddressType):
    """Custom type cAAAServerAddrType based on InetAddressType"""


_CAAAServerAddrType_Object = MibTableColumn
cAAAServerAddrType = _CAAAServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 1),
    _CAAAServerAddrType_Type()
)
cAAAServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerAddrType.setStatus("current")
_CAAAServerAddr_Type = InetAddress
_CAAAServerAddr_Object = MibTableColumn
cAAAServerAddr = _CAAAServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 2),
    _CAAAServerAddr_Type()
)
cAAAServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerAddr.setStatus("current")


class _CAAAServerKeyEncrType_Type(CiscoAAAServerKeyEncrType):
    """Custom type cAAAServerKeyEncrType based on CiscoAAAServerKeyEncrType"""


_CAAAServerKeyEncrType_Object = MibTableColumn
cAAAServerKeyEncrType = _CAAAServerKeyEncrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 3),
    _CAAAServerKeyEncrType_Type()
)
cAAAServerKeyEncrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerKeyEncrType.setStatus("current")


class _CAAAServerDeadTime_Type(TimeIntervalMin):
    """Custom type cAAAServerDeadTime based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CAAAServerDeadTime_Type.__name__ = "TimeIntervalMin"
_CAAAServerDeadTime_Object = MibTableColumn
cAAAServerDeadTime = _CAAAServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 4),
    _CAAAServerDeadTime_Type()
)
cAAAServerDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerDeadTime.setUnits("minutes")


class _CAAAServerTimeOut_Type(TimeIntervalSec):
    """Custom type cAAAServerTimeOut based on TimeIntervalSec"""
    defaultValue = 0

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CAAAServerTimeOut_Type.__name__ = "TimeIntervalSec"
_CAAAServerTimeOut_Object = MibTableColumn
cAAAServerTimeOut = _CAAAServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 5),
    _CAAAServerTimeOut_Type()
)
cAAAServerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerTimeOut.setUnits("seconds")


class _CAAAServerRetransmits_Type(Unsigned32):
    """Custom type cAAAServerRetransmits based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CAAAServerRetransmits_Type.__name__ = "Unsigned32"
_CAAAServerRetransmits_Object = MibTableColumn
cAAAServerRetransmits = _CAAAServerRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 6),
    _CAAAServerRetransmits_Type()
)
cAAAServerRetransmits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerRetransmits.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerRetransmits.setUnits("retransmits")


class _CAAAServerRootDN_Type(SnmpAdminString):
    """Custom type cAAAServerRootDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CAAAServerRootDN_Type.__name__ = "SnmpAdminString"
_CAAAServerRootDN_Object = MibTableColumn
cAAAServerRootDN = _CAAAServerRootDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 7),
    _CAAAServerRootDN_Type()
)
cAAAServerRootDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerRootDN.setStatus("current")


class _CAAAServerIdleTime_Type(TimeIntervalMin):
    """Custom type cAAAServerIdleTime based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CAAAServerIdleTime_Type.__name__ = "TimeIntervalMin"
_CAAAServerIdleTime_Object = MibTableColumn
cAAAServerIdleTime = _CAAAServerIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 8),
    _CAAAServerIdleTime_Type()
)
cAAAServerIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerIdleTime.setUnits("minutes")


class _CAAAServerTestUser_Type(SnmpAdminString):
    """Custom type cAAAServerTestUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CAAAServerTestUser_Type.__name__ = "SnmpAdminString"
_CAAAServerTestUser_Object = MibTableColumn
cAAAServerTestUser = _CAAAServerTestUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 9),
    _CAAAServerTestUser_Type()
)
cAAAServerTestUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerTestUser.setStatus("current")


class _CAAAServerTestPassword_Type(SnmpAdminString):
    """Custom type cAAAServerTestPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CAAAServerTestPassword_Type.__name__ = "SnmpAdminString"
_CAAAServerTestPassword_Object = MibTableColumn
cAAAServerTestPassword = _CAAAServerTestPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 2, 1, 1, 10),
    _CAAAServerTestPassword_Type()
)
cAAAServerTestPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerTestPassword.setStatus("current")
_CAAASvrExtProtoParamConfig_ObjectIdentity = ObjectIdentity
cAAASvrExtProtoParamConfig = _CAAASvrExtProtoParamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3)
)
_CAAASvrExtProtocolParamTable_Object = MibTable
cAAASvrExtProtocolParamTable = _CAAASvrExtProtocolParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cAAASvrExtProtocolParamTable.setStatus("current")
_CAAASvrExtProtocolParamEntry_Object = MibTableRow
cAAASvrExtProtocolParamEntry = _CAAASvrExtProtocolParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1)
)
cAAASvrExtProtocolParamEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtocol"),
)
if mibBuilder.loadTexts:
    cAAASvrExtProtocolParamEntry.setStatus("current")
_CAAAServerProtocol_Type = CiscoAAAProtocol
_CAAAServerProtocol_Object = MibTableColumn
cAAAServerProtocol = _CAAAServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 1),
    _CAAAServerProtocol_Type()
)
cAAAServerProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAAAServerProtocol.setStatus("current")
_CAAAServerProtoAuthKey_Type = DisplayString
_CAAAServerProtoAuthKey_Object = MibTableColumn
cAAAServerProtoAuthKey = _CAAAServerProtoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 2),
    _CAAAServerProtoAuthKey_Type()
)
cAAAServerProtoAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoAuthKey.setStatus("current")


class _CAAAServerProtoKeyEncrType_Type(CiscoAAAServerKeyEncrType):
    """Custom type cAAAServerProtoKeyEncrType based on CiscoAAAServerKeyEncrType"""


_CAAAServerProtoKeyEncrType_Object = MibTableColumn
cAAAServerProtoKeyEncrType = _CAAAServerProtoKeyEncrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 3),
    _CAAAServerProtoKeyEncrType_Type()
)
cAAAServerProtoKeyEncrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoKeyEncrType.setStatus("current")


class _CAAAServerProtoDeadTime_Type(TimeIntervalMin):
    """Custom type cAAAServerProtoDeadTime based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CAAAServerProtoDeadTime_Type.__name__ = "TimeIntervalMin"
_CAAAServerProtoDeadTime_Object = MibTableColumn
cAAAServerProtoDeadTime = _CAAAServerProtoDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 4),
    _CAAAServerProtoDeadTime_Type()
)
cAAAServerProtoDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerProtoDeadTime.setUnits("minutes")


class _CAAAServerProtoTimeOut_Type(TimeIntervalSec):
    """Custom type cAAAServerProtoTimeOut based on TimeIntervalSec"""
    defaultValue = 1

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CAAAServerProtoTimeOut_Type.__name__ = "TimeIntervalSec"
_CAAAServerProtoTimeOut_Object = MibTableColumn
cAAAServerProtoTimeOut = _CAAAServerProtoTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 5),
    _CAAAServerProtoTimeOut_Type()
)
cAAAServerProtoTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerProtoTimeOut.setUnits("seconds")


class _CAAAServerProtoRetransmits_Type(Unsigned32):
    """Custom type cAAAServerProtoRetransmits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CAAAServerProtoRetransmits_Type.__name__ = "Unsigned32"
_CAAAServerProtoRetransmits_Object = MibTableColumn
cAAAServerProtoRetransmits = _CAAAServerProtoRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 6),
    _CAAAServerProtoRetransmits_Type()
)
cAAAServerProtoRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoRetransmits.setStatus("current")
if mibBuilder.loadTexts:
    cAAAServerProtoRetransmits.setUnits("retransmits")


class _CAAAServerProtoSvrTableMaxEnt_Type(Unsigned32):
    """Custom type cAAAServerProtoSvrTableMaxEnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CAAAServerProtoSvrTableMaxEnt_Type.__name__ = "Unsigned32"
_CAAAServerProtoSvrTableMaxEnt_Object = MibTableColumn
cAAAServerProtoSvrTableMaxEnt = _CAAAServerProtoSvrTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 7),
    _CAAAServerProtoSvrTableMaxEnt_Type()
)
cAAAServerProtoSvrTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAAAServerProtoSvrTableMaxEnt.setStatus("current")


class _CAAAServerProtoDirectedReq_Type(TruthValue):
    """Custom type cAAAServerProtoDirectedReq based on TruthValue"""


_CAAAServerProtoDirectedReq_Object = MibTableColumn
cAAAServerProtoDirectedReq = _CAAAServerProtoDirectedReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 3, 1, 1, 8),
    _CAAAServerProtoDirectedReq_Type()
)
cAAAServerProtoDirectedReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAAServerProtoDirectedReq.setStatus("current")
_CAAASvrExtSvrGrpConfig_ObjectIdentity = ObjectIdentity
cAAASvrExtSvrGrpConfig = _CAAASvrExtSvrGrpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4)
)
_CAAASvrExtSvrGrpConfigTable_Object = MibTable
cAAASvrExtSvrGrpConfigTable = _CAAASvrExtSvrGrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGrpConfigTable.setStatus("current")
_CAAASvrExtSvrGrpConfigEntry_Object = MibTableRow
cAAASvrExtSvrGrpConfigEntry = _CAAASvrExtSvrGrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1)
)
cAAASvrExtSvrGrpConfigEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpIndex"),
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGrpConfigEntry.setStatus("current")


class _CAAASvrGrpIndex_Type(Unsigned32):
    """Custom type cAAASvrGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CAAASvrGrpIndex_Type.__name__ = "Unsigned32"
_CAAASvrGrpIndex_Object = MibTableColumn
cAAASvrGrpIndex = _CAAASvrGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 1),
    _CAAASvrGrpIndex_Type()
)
cAAASvrGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAAASvrGrpIndex.setStatus("current")


class _CAAASvrGrpName_Type(SnmpAdminString):
    """Custom type cAAASvrGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CAAASvrGrpName_Type.__name__ = "SnmpAdminString"
_CAAASvrGrpName_Object = MibTableColumn
cAAASvrGrpName = _CAAASvrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 2),
    _CAAASvrGrpName_Type()
)
cAAASvrGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpName.setStatus("current")


class _CAAASvrGrpProtocol_Type(CiscoAAAProtocol):
    """Custom type cAAASvrGrpProtocol based on CiscoAAAProtocol"""


_CAAASvrGrpProtocol_Object = MibTableColumn
cAAASvrGrpProtocol = _CAAASvrGrpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 3),
    _CAAASvrGrpProtocol_Type()
)
cAAASvrGrpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpProtocol.setStatus("current")


class _CAAAServerList_Type(OctetString):
    """Custom type cAAAServerList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 256),
    )


_CAAAServerList_Type.__name__ = "OctetString"
_CAAAServerList_Object = MibTableColumn
cAAAServerList = _CAAAServerList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 4),
    _CAAAServerList_Type()
)
cAAAServerList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAAServerList.setStatus("current")
_CAAASvrGrpConfigRowStatus_Type = RowStatus
_CAAASvrGrpConfigRowStatus_Object = MibTableColumn
cAAASvrGrpConfigRowStatus = _CAAASvrGrpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 5),
    _CAAASvrGrpConfigRowStatus_Type()
)
cAAASvrGrpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpConfigRowStatus.setStatus("current")


class _CAAASvrGrpConfigDeadTime_Type(TimeIntervalMin):
    """Custom type cAAASvrGrpConfigDeadTime based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CAAASvrGrpConfigDeadTime_Type.__name__ = "TimeIntervalMin"
_CAAASvrGrpConfigDeadTime_Object = MibTableColumn
cAAASvrGrpConfigDeadTime = _CAAASvrGrpConfigDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 1, 1, 6),
    _CAAASvrGrpConfigDeadTime_Type()
)
cAAASvrGrpConfigDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpConfigDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    cAAASvrGrpConfigDeadTime.setUnits("minutes")
_CAAASvrExtSvrGrpLDAPConfigTable_Object = MibTable
cAAASvrExtSvrGrpLDAPConfigTable = _CAAASvrExtSvrGrpLDAPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGrpLDAPConfigTable.setStatus("current")
_CAAASvrExtSvrGrpLDAPConfigEntry_Object = MibTableRow
cAAASvrExtSvrGrpLDAPConfigEntry = _CAAASvrExtSvrGrpLDAPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 2, 1)
)
cAAASvrExtSvrGrpLDAPConfigEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpIndex"),
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGrpLDAPConfigEntry.setStatus("current")


class _CAAASvrGrpLDAPBaseDN_Type(SnmpAdminString):
    """Custom type cAAASvrGrpLDAPBaseDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CAAASvrGrpLDAPBaseDN_Type.__name__ = "SnmpAdminString"
_CAAASvrGrpLDAPBaseDN_Object = MibTableColumn
cAAASvrGrpLDAPBaseDN = _CAAASvrGrpLDAPBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 2, 1, 1),
    _CAAASvrGrpLDAPBaseDN_Type()
)
cAAASvrGrpLDAPBaseDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpLDAPBaseDN.setStatus("current")


class _CAAASvrGrpLDAPFilterUser_Type(SnmpAdminString):
    """Custom type cAAASvrGrpLDAPFilterUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAAASvrGrpLDAPFilterUser_Type.__name__ = "SnmpAdminString"
_CAAASvrGrpLDAPFilterUser_Object = MibTableColumn
cAAASvrGrpLDAPFilterUser = _CAAASvrGrpLDAPFilterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 2, 1, 2),
    _CAAASvrGrpLDAPFilterUser_Type()
)
cAAASvrGrpLDAPFilterUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpLDAPFilterUser.setStatus("current")


class _CAAASvrGrpLDAPUserProfile_Type(SnmpAdminString):
    """Custom type cAAASvrGrpLDAPUserProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CAAASvrGrpLDAPUserProfile_Type.__name__ = "SnmpAdminString"
_CAAASvrGrpLDAPUserProfile_Object = MibTableColumn
cAAASvrGrpLDAPUserProfile = _CAAASvrGrpLDAPUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 4, 2, 1, 3),
    _CAAASvrGrpLDAPUserProfile_Type()
)
cAAASvrGrpLDAPUserProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAAASvrGrpLDAPUserProfile.setStatus("current")
_CAAASvrExtAppSvrGrpMapConfig_ObjectIdentity = ObjectIdentity
cAAASvrExtAppSvrGrpMapConfig = _CAAASvrExtAppSvrGrpMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5)
)
_CAAASvrExtAppSvrGrpConfigTable_Object = MibTable
cAAASvrExtAppSvrGrpConfigTable = _CAAASvrExtAppSvrGrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cAAASvrExtAppSvrGrpConfigTable.setStatus("current")
_CAAASvrExtAppSvrGrpConfigEntry_Object = MibTableRow
cAAASvrExtAppSvrGrpConfigEntry = _CAAASvrExtAppSvrGrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1)
)
cAAASvrExtAppSvrGrpConfigEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAAApplicationType"),
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAAApplicationSubType"),
    (0, "CISCO-AAA-SERVER-EXT-MIB", "cAAAFunction"),
)
if mibBuilder.loadTexts:
    cAAASvrExtAppSvrGrpConfigEntry.setStatus("current")


class _CAAAApplicationType_Type(Integer32):
    """Custom type cAAAApplicationType based on Integer32"""
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
        *(("default", 1),
          ("dhchap", 3),
          ("iSCSI", 4),
          ("login", 2))
    )


_CAAAApplicationType_Type.__name__ = "Integer32"
_CAAAApplicationType_Object = MibTableColumn
cAAAApplicationType = _CAAAApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 1),
    _CAAAApplicationType_Type()
)
cAAAApplicationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAAAApplicationType.setStatus("current")


class _CAAAApplicationSubType_Type(Integer32):
    """Custom type cAAAApplicationSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("console", 2))
    )


_CAAAApplicationSubType_Type.__name__ = "Integer32"
_CAAAApplicationSubType_Object = MibTableColumn
cAAAApplicationSubType = _CAAAApplicationSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 2),
    _CAAAApplicationSubType_Type()
)
cAAAApplicationSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAAAApplicationSubType.setStatus("current")


class _CAAAFunction_Type(Integer32):
    """Custom type cAAAFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 3),
          ("authentication", 1),
          ("authorization", 2))
    )


_CAAAFunction_Type.__name__ = "Integer32"
_CAAAFunction_Object = MibTableColumn
cAAAFunction = _CAAAFunction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 3),
    _CAAAFunction_Type()
)
cAAAFunction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAAAFunction.setStatus("current")
_CAAASvrGrpLocal_Type = TruthValue
_CAAASvrGrpLocal_Object = MibTableColumn
cAAASvrGrpLocal = _CAAASvrGrpLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 4),
    _CAAASvrGrpLocal_Type()
)
cAAASvrGrpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAASvrGrpLocal.setStatus("current")
_CAAASvrGrpTrivial_Type = TruthValue
_CAAASvrGrpTrivial_Object = MibTableColumn
cAAASvrGrpTrivial = _CAAASvrGrpTrivial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 5),
    _CAAASvrGrpTrivial_Type()
)
cAAASvrGrpTrivial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAASvrGrpTrivial.setStatus("current")


class _CAAASvrGrpList_Type(OctetString):
    """Custom type cAAASvrGrpList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CAAASvrGrpList_Type.__name__ = "OctetString"
_CAAASvrGrpList_Object = MibTableColumn
cAAASvrGrpList = _CAAASvrGrpList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 1, 5, 1, 1, 6),
    _CAAASvrGrpList_Type()
)
cAAASvrGrpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAAASvrGrpList.setStatus("current")
_CiscoAAASvrExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAAASvrExtMIBConformance = _CiscoAAASvrExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2)
)
_CiscoAAASvrExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAAASvrExtMIBCompliances = _CiscoAAASvrExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 1)
)
_CiscoAAASvrExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAAASvrExtMIBGroups = _CiscoAAASvrExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2)
)
casConfigEntry.registerAugmentions(
    ("CISCO-AAA-SERVER-EXT-MIB",
     "cAAASvrExtConfigEntry")
)
cAAASvrExtConfigEntry.setIndexNames(*casConfigEntry.getIndexNames())

# Managed Objects groups

cAAASvrExtGenericConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 1)
)
cAAASvrExtGenericConfGroup.setObjects(
    ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtLocalAccLogMaxSize")
)
if mibBuilder.loadTexts:
    cAAASvrExtGenericConfGroup.setStatus("deprecated")

cAAASvrExtSvrTableConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 2)
)
cAAASvrExtSvrTableConfGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerAddrType"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerAddr"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerKeyEncrType"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerDeadTime"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerTimeOut"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerRetransmits"))
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrTableConfGroup.setStatus("current")

cAAASvrExtProtoParamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 3)
)
cAAASvrExtProtoParamConfigGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoAuthKey"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoKeyEncrType"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoDeadTime"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoTimeOut"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoRetransmits"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoSvrTableMaxEnt"))
)
if mibBuilder.loadTexts:
    cAAASvrExtProtoParamConfigGroup.setStatus("deprecated")

cAAASvrExtSvrGroupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 4)
)
cAAASvrExtSvrGroupConfGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpName"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpProtocol"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerList"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpConfigRowStatus"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtSvrGrpSvrListMaxEnt"))
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGroupConfGroup.setStatus("deprecated")

cAAASvrExtAppSvrGroupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 5)
)
cAAASvrExtAppSvrGroupConfGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpLocal"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpTrivial"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpList"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtAppToSvrGrpMaxEnt"))
)
if mibBuilder.loadTexts:
    cAAASvrExtAppSvrGroupConfGroup.setStatus("current")

cAAASvrExtGenericConfGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 6)
)
cAAASvrExtGenericConfGroup1.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtLocalAccLogMaxSize"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtClearAccLog"))
)
if mibBuilder.loadTexts:
    cAAASvrExtGenericConfGroup1.setStatus("current")

cAAASvrExtGenericConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 7)
)
cAAASvrExtGenericConfGroup2.setObjects(
    ("CISCO-AAA-SERVER-EXT-MIB", "cAAALoginAuthTypeMSCHAP")
)
if mibBuilder.loadTexts:
    cAAASvrExtGenericConfGroup2.setStatus("current")

cAAASvrExtSvrGroupConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 8)
)
cAAASvrExtSvrGroupConfGroup2.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpName"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpProtocol"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerList"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpConfigRowStatus"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrExtSvrGrpSvrListMaxEnt"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpConfigDeadTime"))
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGroupConfGroup2.setStatus("current")

cAAASvrExtProtoParamConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 9)
)
cAAASvrExtProtoParamConfigGroup1.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoAuthKey"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoKeyEncrType"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoDeadTime"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoTimeOut"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoRetransmits"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoSvrTableMaxEnt"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerProtoDirectedReq"))
)
if mibBuilder.loadTexts:
    cAAASvrExtProtoParamConfigGroup1.setStatus("current")

cAAASvrExtSvrTableLDAPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 10)
)
cAAASvrExtSvrTableLDAPConfGroup.setObjects(
    ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerRootDN")
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrTableLDAPConfGroup.setStatus("current")

cAAASvrExtSvrGroupLDAPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 11)
)
cAAASvrExtSvrGroupLDAPConfGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpLDAPBaseDN"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpLDAPFilterUser"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAASvrGrpLDAPUserProfile"))
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrGroupLDAPConfGroup.setStatus("current")

cAAASvrExtSvrMonitorConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 2, 12)
)
cAAASvrExtSvrMonitorConfGroup.setObjects(
      *(("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerIdleTime"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerTestUser"),
        ("CISCO-AAA-SERVER-EXT-MIB", "cAAAServerTestPassword"))
)
if mibBuilder.loadTexts:
    cAAASvrExtSvrMonitorConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAAAServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAAAServerMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAAAServerMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAAAServerMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoAAAServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 367, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAAAServerMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-SERVER-EXT-MIB",
    **{"CiscoAAAServerKeyEncrType": CiscoAAAServerKeyEncrType,
       "ciscoAAAServerExtMIB": ciscoAAAServerExtMIB,
       "ciscoAAASvrExtMIBObjects": ciscoAAASvrExtMIBObjects,
       "cAAASvrExtGenericConfig": cAAASvrExtGenericConfig,
       "cAAASvrExtLocalAccLogMaxSize": cAAASvrExtLocalAccLogMaxSize,
       "cAAASvrExtSvrGrpSvrListMaxEnt": cAAASvrExtSvrGrpSvrListMaxEnt,
       "cAAASvrExtAppToSvrGrpMaxEnt": cAAASvrExtAppToSvrGrpMaxEnt,
       "cAAASvrExtClearAccLog": cAAASvrExtClearAccLog,
       "cAAALoginAuthTypeMSCHAP": cAAALoginAuthTypeMSCHAP,
       "cAAASvrExtSvrTableConfig": cAAASvrExtSvrTableConfig,
       "cAAASvrExtConfigTable": cAAASvrExtConfigTable,
       "cAAASvrExtConfigEntry": cAAASvrExtConfigEntry,
       "cAAAServerAddrType": cAAAServerAddrType,
       "cAAAServerAddr": cAAAServerAddr,
       "cAAAServerKeyEncrType": cAAAServerKeyEncrType,
       "cAAAServerDeadTime": cAAAServerDeadTime,
       "cAAAServerTimeOut": cAAAServerTimeOut,
       "cAAAServerRetransmits": cAAAServerRetransmits,
       "cAAAServerRootDN": cAAAServerRootDN,
       "cAAAServerIdleTime": cAAAServerIdleTime,
       "cAAAServerTestUser": cAAAServerTestUser,
       "cAAAServerTestPassword": cAAAServerTestPassword,
       "cAAASvrExtProtoParamConfig": cAAASvrExtProtoParamConfig,
       "cAAASvrExtProtocolParamTable": cAAASvrExtProtocolParamTable,
       "cAAASvrExtProtocolParamEntry": cAAASvrExtProtocolParamEntry,
       "cAAAServerProtocol": cAAAServerProtocol,
       "cAAAServerProtoAuthKey": cAAAServerProtoAuthKey,
       "cAAAServerProtoKeyEncrType": cAAAServerProtoKeyEncrType,
       "cAAAServerProtoDeadTime": cAAAServerProtoDeadTime,
       "cAAAServerProtoTimeOut": cAAAServerProtoTimeOut,
       "cAAAServerProtoRetransmits": cAAAServerProtoRetransmits,
       "cAAAServerProtoSvrTableMaxEnt": cAAAServerProtoSvrTableMaxEnt,
       "cAAAServerProtoDirectedReq": cAAAServerProtoDirectedReq,
       "cAAASvrExtSvrGrpConfig": cAAASvrExtSvrGrpConfig,
       "cAAASvrExtSvrGrpConfigTable": cAAASvrExtSvrGrpConfigTable,
       "cAAASvrExtSvrGrpConfigEntry": cAAASvrExtSvrGrpConfigEntry,
       "cAAASvrGrpIndex": cAAASvrGrpIndex,
       "cAAASvrGrpName": cAAASvrGrpName,
       "cAAASvrGrpProtocol": cAAASvrGrpProtocol,
       "cAAAServerList": cAAAServerList,
       "cAAASvrGrpConfigRowStatus": cAAASvrGrpConfigRowStatus,
       "cAAASvrGrpConfigDeadTime": cAAASvrGrpConfigDeadTime,
       "cAAASvrExtSvrGrpLDAPConfigTable": cAAASvrExtSvrGrpLDAPConfigTable,
       "cAAASvrExtSvrGrpLDAPConfigEntry": cAAASvrExtSvrGrpLDAPConfigEntry,
       "cAAASvrGrpLDAPBaseDN": cAAASvrGrpLDAPBaseDN,
       "cAAASvrGrpLDAPFilterUser": cAAASvrGrpLDAPFilterUser,
       "cAAASvrGrpLDAPUserProfile": cAAASvrGrpLDAPUserProfile,
       "cAAASvrExtAppSvrGrpMapConfig": cAAASvrExtAppSvrGrpMapConfig,
       "cAAASvrExtAppSvrGrpConfigTable": cAAASvrExtAppSvrGrpConfigTable,
       "cAAASvrExtAppSvrGrpConfigEntry": cAAASvrExtAppSvrGrpConfigEntry,
       "cAAAApplicationType": cAAAApplicationType,
       "cAAAApplicationSubType": cAAAApplicationSubType,
       "cAAAFunction": cAAAFunction,
       "cAAASvrGrpLocal": cAAASvrGrpLocal,
       "cAAASvrGrpTrivial": cAAASvrGrpTrivial,
       "cAAASvrGrpList": cAAASvrGrpList,
       "ciscoAAASvrExtMIBConformance": ciscoAAASvrExtMIBConformance,
       "ciscoAAASvrExtMIBCompliances": ciscoAAASvrExtMIBCompliances,
       "ciscoAAAServerMIBCompliance": ciscoAAAServerMIBCompliance,
       "ciscoAAAServerMIBCompliance1": ciscoAAAServerMIBCompliance1,
       "ciscoAAAServerMIBCompliance2": ciscoAAAServerMIBCompliance2,
       "ciscoAAASvrExtMIBGroups": ciscoAAASvrExtMIBGroups,
       "cAAASvrExtGenericConfGroup": cAAASvrExtGenericConfGroup,
       "cAAASvrExtSvrTableConfGroup": cAAASvrExtSvrTableConfGroup,
       "cAAASvrExtProtoParamConfigGroup": cAAASvrExtProtoParamConfigGroup,
       "cAAASvrExtSvrGroupConfGroup": cAAASvrExtSvrGroupConfGroup,
       "cAAASvrExtAppSvrGroupConfGroup": cAAASvrExtAppSvrGroupConfGroup,
       "cAAASvrExtGenericConfGroup1": cAAASvrExtGenericConfGroup1,
       "cAAASvrExtGenericConfGroup2": cAAASvrExtGenericConfGroup2,
       "cAAASvrExtSvrGroupConfGroup2": cAAASvrExtSvrGroupConfGroup2,
       "cAAASvrExtProtoParamConfigGroup1": cAAASvrExtProtoParamConfigGroup1,
       "cAAASvrExtSvrTableLDAPConfGroup": cAAASvrExtSvrTableLDAPConfGroup,
       "cAAASvrExtSvrGroupLDAPConfGroup": cAAASvrExtSvrGroupLDAPConfGroup,
       "cAAASvrExtSvrMonitorConfGroup": cAAASvrExtSvrMonitorConfGroup}
)
