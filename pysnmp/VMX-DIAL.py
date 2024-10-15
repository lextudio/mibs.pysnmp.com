# SNMP MIB module (VMX-DIAL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMX-DIAL
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:01 2024
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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Octel_ObjectIdentity = ObjectIdentity
octel = _Octel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662)
)
_OctelOIDs_ObjectIdentity = ObjectIdentity
octelOIDs = _OctelOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 1)
)
_OctelPlatforms_ObjectIdentity = ObjectIdentity
octelPlatforms = _OctelPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 1, 1)
)
_Vmx200_ObjectIdentity = ObjectIdentity
vmx200 = _Vmx200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 1, 1, 3)
)
_Vmx300_ObjectIdentity = ObjectIdentity
vmx300 = _Vmx300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 1, 1, 4)
)
_OctelProducts_ObjectIdentity = ObjectIdentity
octelProducts = _OctelProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3)
)
_VmxDial_ObjectIdentity = ObjectIdentity
vmxDial = _VmxDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("mandatory")


class _SysSerialNum_Type(DisplayString):
    """Custom type sysSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSerialNum_Type.__name__ = "DisplayString"
_SysSerialNum_Object = MibScalar
sysSerialNum = _SysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 1, 2),
    _SysSerialNum_Type()
)
sysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNum.setStatus("mandatory")


class _SystemID_Type(DisplayString):
    """Custom type systemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemID_Type.__name__ = "DisplayString"
_SystemID_Object = MibScalar
systemID = _SystemID_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 1, 3),
    _SystemID_Type()
)
systemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemID.setStatus("mandatory")
_DNetstat_ObjectIdentity = ObjectIdentity
dNetstat = _DNetstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2)
)
_Message_ObjectIdentity = ObjectIdentity
message = _Message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1)
)
_SentVoiceMsgs_Type = Counter32
_SentVoiceMsgs_Object = MibScalar
sentVoiceMsgs = _SentVoiceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 1),
    _SentVoiceMsgs_Type()
)
sentVoiceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sentVoiceMsgs.setStatus("mandatory")
_RecvVoiceMsgs_Type = Counter32
_RecvVoiceMsgs_Object = MibScalar
recvVoiceMsgs = _RecvVoiceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 2),
    _RecvVoiceMsgs_Type()
)
recvVoiceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recvVoiceMsgs.setStatus("mandatory")
_SentFaxMsgs_Type = Counter32
_SentFaxMsgs_Object = MibScalar
sentFaxMsgs = _SentFaxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 3),
    _SentFaxMsgs_Type()
)
sentFaxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sentFaxMsgs.setStatus("mandatory")
_RecvFaxMsgs_Type = Counter32
_RecvFaxMsgs_Object = MibScalar
recvFaxMsgs = _RecvFaxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 4),
    _RecvFaxMsgs_Type()
)
recvFaxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recvFaxMsgs.setStatus("mandatory")
_RecvNames_Type = Counter32
_RecvNames_Object = MibScalar
recvNames = _RecvNames_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 5),
    _RecvNames_Type()
)
recvNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recvNames.setStatus("mandatory")
_PlayedRtNames_Type = Counter32
_PlayedRtNames_Object = MibScalar
playedRtNames = _PlayedRtNames_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 6),
    _PlayedRtNames_Type()
)
playedRtNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    playedRtNames.setStatus("mandatory")
_SecSent_Type = Integer32
_SecSent_Object = MibScalar
secSent = _SecSent_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 7),
    _SecSent_Type()
)
secSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secSent.setStatus("mandatory")
_SecRecv_Type = Integer32
_SecRecv_Object = MibScalar
secRecv = _SecRecv_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 1, 8),
    _SecRecv_Type()
)
secRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secRecv.setStatus("mandatory")
_LanCh_ObjectIdentity = ObjectIdentity
lanCh = _LanCh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2)
)
_LchNumber_Type = Integer32
_LchNumber_Object = MibScalar
lchNumber = _LchNumber_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 1),
    _LchNumber_Type()
)
lchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lchNumber.setStatus("mandatory")
_Sec50pct_Type = Integer32
_Sec50pct_Object = MibScalar
sec50pct = _Sec50pct_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 2),
    _Sec50pct_Type()
)
sec50pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sec50pct.setStatus("mandatory")
_Sec75pct_Type = Integer32
_Sec75pct_Object = MibScalar
sec75pct = _Sec75pct_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 3),
    _Sec75pct_Type()
)
sec75pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sec75pct.setStatus("mandatory")
_Sec100pct_Type = Integer32
_Sec100pct_Object = MibScalar
sec100pct = _Sec100pct_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 4),
    _Sec100pct_Type()
)
sec100pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sec100pct.setStatus("mandatory")
_LchInSendSec_Type = Integer32
_LchInSendSec_Object = MibScalar
lchInSendSec = _LchInSendSec_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 5),
    _LchInSendSec_Type()
)
lchInSendSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lchInSendSec.setStatus("mandatory")
_LchInRecvSec_Type = Integer32
_LchInRecvSec_Object = MibScalar
lchInRecvSec = _LchInRecvSec_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 2, 6),
    _LchInRecvSec_Type()
)
lchInRecvSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lchInRecvSec.setStatus("mandatory")
_LanConn_ObjectIdentity = ObjectIdentity
lanConn = _LanConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3)
)
_OutAttempts_Type = Counter32
_OutAttempts_Object = MibScalar
outAttempts = _OutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 1),
    _OutAttempts_Type()
)
outAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outAttempts.setStatus("mandatory")
_OutRejects_Type = Counter32
_OutRejects_Object = MibScalar
outRejects = _OutRejects_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 2),
    _OutRejects_Type()
)
outRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outRejects.setStatus("mandatory")
_OutGotBusys_Type = Counter32
_OutGotBusys_Object = MibScalar
outGotBusys = _OutGotBusys_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 3),
    _OutGotBusys_Type()
)
outGotBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outGotBusys.setStatus("mandatory")
_InAttempts_Type = Counter32
_InAttempts_Object = MibScalar
inAttempts = _InAttempts_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 4),
    _InAttempts_Type()
)
inAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAttempts.setStatus("mandatory")
_InRejects_Type = Counter32
_InRejects_Object = MibScalar
inRejects = _InRejects_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 5),
    _InRejects_Type()
)
inRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inRejects.setStatus("mandatory")
_InGotBusys_Type = Counter32
_InGotBusys_Object = MibScalar
inGotBusys = _InGotBusys_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 3, 6),
    _InGotBusys_Type()
)
inGotBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inGotBusys.setStatus("mandatory")
_LanAvailPct_Type = Integer32
_LanAvailPct_Object = MibScalar
lanAvailPct = _LanAvailPct_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 2, 4),
    _LanAvailPct_Type()
)
lanAvailPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanAvailPct.setStatus("mandatory")
_Location_ObjectIdentity = ObjectIdentity
location = _Location_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3)
)
_LocTable_Object = MibTable
locTable = _LocTable_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    locTable.setStatus("mandatory")
_LocEntry_Object = MibTableRow
locEntry = _LocEntry_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1)
)
locEntry.setIndexNames(
    (0, "VMX-DIAL", "locIndex"),
)
if mibBuilder.loadTexts:
    locEntry.setStatus("mandatory")
_LocIndex_Type = Integer32
_LocIndex_Object = MibTableColumn
locIndex = _LocIndex_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 1),
    _LocIndex_Type()
)
locIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIndex.setStatus("mandatory")


class _LocName_Type(DisplayString):
    """Custom type locName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocName_Type.__name__ = "DisplayString"
_LocName_Object = MibTableColumn
locName = _LocName_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 2),
    _LocName_Type()
)
locName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locName.setStatus("mandatory")
_LocIpAddr_Type = IpAddress
_LocIpAddr_Object = MibTableColumn
locIpAddr = _LocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 3),
    _LocIpAddr_Type()
)
locIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIpAddr.setStatus("mandatory")


class _LocLinkType_Type(Integer32):
    """Custom type locLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highspeed", 2),
          ("lowspeed", 1))
    )


_LocLinkType_Type.__name__ = "Integer32"
_LocLinkType_Object = MibTableColumn
locLinkType = _LocLinkType_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 4),
    _LocLinkType_Type()
)
locLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkType.setStatus("mandatory")


class _LocInDomain_Type(Integer32):
    """Custom type locInDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LocInDomain_Type.__name__ = "Integer32"
_LocInDomain_Object = MibTableColumn
locInDomain = _LocInDomain_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 5),
    _LocInDomain_Type()
)
locInDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locInDomain.setStatus("mandatory")


class _LocColocated_Type(Integer32):
    """Custom type locColocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LocColocated_Type.__name__ = "Integer32"
_LocColocated_Object = MibTableColumn
locColocated = _LocColocated_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 6),
    _LocColocated_Type()
)
locColocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locColocated.setStatus("mandatory")
_Locroute_ObjectIdentity = ObjectIdentity
locroute = _Locroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 7)
)


class _Route1_Type(DisplayString):
    """Custom type route1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Route1_Type.__name__ = "DisplayString"
_Route1_Object = MibTableColumn
route1 = _Route1_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 7, 1),
    _Route1_Type()
)
route1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route1.setStatus("mandatory")


class _Route2_Type(DisplayString):
    """Custom type route2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Route2_Type.__name__ = "DisplayString"
_Route2_Object = MibTableColumn
route2 = _Route2_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 7, 2),
    _Route2_Type()
)
route2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route2.setStatus("mandatory")


class _Route3_Type(DisplayString):
    """Custom type route3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Route3_Type.__name__ = "DisplayString"
_Route3_Object = MibTableColumn
route3 = _Route3_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 7, 3),
    _Route3_Type()
)
route3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route3.setStatus("mandatory")
_LocConn_ObjectIdentity = ObjectIdentity
locConn = _LocConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8)
)
_Cattempts_Type = Counter32
_Cattempts_Object = MibTableColumn
cattempts = _Cattempts_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 1),
    _Cattempts_Type()
)
cattempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cattempts.setStatus("mandatory")
_Cfailures_Type = Counter32
_Cfailures_Object = MibTableColumn
cfailures = _Cfailures_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 2),
    _Cfailures_Type()
)
cfailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfailures.setStatus("mandatory")
_Cdroppeds_Type = Counter32
_Cdroppeds_Object = MibTableColumn
cdroppeds = _Cdroppeds_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 3),
    _Cdroppeds_Type()
)
cdroppeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdroppeds.setStatus("mandatory")
_Cbusys_Type = Counter32
_Cbusys_Object = MibTableColumn
cbusys = _Cbusys_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 4),
    _Cbusys_Type()
)
cbusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbusys.setStatus("mandatory")
_CdayMin_Type = Integer32
_CdayMin_Object = MibTableColumn
cdayMin = _CdayMin_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 5),
    _CdayMin_Type()
)
cdayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdayMin.setStatus("mandatory")
_CnightMin_Type = Integer32
_CnightMin_Object = MibTableColumn
cnightMin = _CnightMin_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 8, 6),
    _CnightMin_Type()
)
cnightMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnightMin.setStatus("mandatory")
_MsgDelivery_ObjectIdentity = ObjectIdentity
msgDelivery = _MsgDelivery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9)
)
_MdvcAttempts_Type = Counter32
_MdvcAttempts_Object = MibTableColumn
mdvcAttempts = _MdvcAttempts_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 1),
    _MdvcAttempts_Type()
)
mdvcAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdvcAttempts.setStatus("mandatory")
_MdvcFails_Type = Counter32
_MdvcFails_Object = MibTableColumn
mdvcFails = _MdvcFails_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 2),
    _MdvcFails_Type()
)
mdvcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdvcFails.setStatus("mandatory")
_MdvcRetries_Type = Counter32
_MdvcRetries_Object = MibTableColumn
mdvcRetries = _MdvcRetries_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 3),
    _MdvcRetries_Type()
)
mdvcRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdvcRetries.setStatus("mandatory")
_MdfxAttempts_Type = Counter32
_MdfxAttempts_Object = MibTableColumn
mdfxAttempts = _MdfxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 4),
    _MdfxAttempts_Type()
)
mdfxAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdfxAttempts.setStatus("mandatory")
_MdfxFails_Type = Counter32
_MdfxFails_Object = MibTableColumn
mdfxFails = _MdfxFails_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 5),
    _MdfxFails_Type()
)
mdfxFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdfxFails.setStatus("mandatory")
_MdfxRetries_Type = Counter32
_MdfxRetries_Object = MibTableColumn
mdfxRetries = _MdfxRetries_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 6),
    _MdfxRetries_Type()
)
mdfxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdfxRetries.setStatus("mandatory")
_MdDiskfulls_Type = Counter32
_MdDiskfulls_Object = MibTableColumn
mdDiskfulls = _MdDiskfulls_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 7),
    _MdDiskfulls_Type()
)
mdDiskfulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdDiskfulls.setStatus("mandatory")
_MdMbxfails_Type = Counter32
_MdMbxfails_Object = MibTableColumn
mdMbxfails = _MdMbxfails_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 8),
    _MdMbxfails_Type()
)
mdMbxfails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdMbxfails.setStatus("mandatory")
_MdMinute_Type = Integer32
_MdMinute_Object = MibTableColumn
mdMinute = _MdMinute_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 9, 9),
    _MdMinute_Type()
)
mdMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdMinute.setStatus("mandatory")
_LocPlayedNames_Type = Counter32
_LocPlayedNames_Object = MibTableColumn
locPlayedNames = _LocPlayedNames_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 10),
    _LocPlayedNames_Type()
)
locPlayedNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locPlayedNames.setStatus("mandatory")
_LocLinkdrops_Type = Counter32
_LocLinkdrops_Object = MibTableColumn
locLinkdrops = _LocLinkdrops_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 11),
    _LocLinkdrops_Type()
)
locLinkdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkdrops.setStatus("mandatory")
_LocAnalogstndbys_Type = Counter32
_LocAnalogstndbys_Object = MibTableColumn
locAnalogstndbys = _LocAnalogstndbys_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 3, 1, 1, 12),
    _LocAnalogstndbys_Type()
)
locAnalogstndbys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAnalogstndbys.setStatus("mandatory")
_Hwerr_ObjectIdentity = ObjectIdentity
hwerr = _Hwerr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4)
)
_HwerrTable_Object = MibTable
hwerrTable = _HwerrTable_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwerrTable.setStatus("mandatory")
_HwerrEntry_Object = MibTableRow
hwerrEntry = _HwerrEntry_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1)
)
hwerrEntry.setIndexNames(
    (0, "VMX-DIAL", "heIdx"),
)
if mibBuilder.loadTexts:
    hwerrEntry.setStatus("mandatory")
_HeIdx_Type = Integer32
_HeIdx_Object = MibTableColumn
heIdx = _HeIdx_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 1),
    _HeIdx_Type()
)
heIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heIdx.setStatus("mandatory")
_HeType_Type = Integer32
_HeType_Object = MibTableColumn
heType = _HeType_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 2),
    _HeType_Type()
)
heType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heType.setStatus("mandatory")
_HeSlot_Type = Integer32
_HeSlot_Object = MibTableColumn
heSlot = _HeSlot_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 3),
    _HeSlot_Type()
)
heSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heSlot.setStatus("mandatory")


class _HeMon_Type(Integer32):
    """Custom type heMon based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_HeMon_Type.__name__ = "Integer32"
_HeMon_Object = MibTableColumn
heMon = _HeMon_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 4),
    _HeMon_Type()
)
heMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heMon.setStatus("mandatory")
_HeDay_Type = Integer32
_HeDay_Object = MibTableColumn
heDay = _HeDay_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 5),
    _HeDay_Type()
)
heDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heDay.setStatus("mandatory")
_HeHour_Type = Integer32
_HeHour_Object = MibTableColumn
heHour = _HeHour_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 6),
    _HeHour_Type()
)
heHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heHour.setStatus("mandatory")
_HeMin_Type = Integer32
_HeMin_Object = MibTableColumn
heMin = _HeMin_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 7),
    _HeMin_Type()
)
heMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heMin.setStatus("mandatory")
_HeCh_Type = OctetString
_HeCh_Object = MibTableColumn
heCh = _HeCh_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 8),
    _HeCh_Type()
)
heCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCh.setStatus("mandatory")
_HePrio_Type = Integer32
_HePrio_Object = MibTableColumn
hePrio = _HePrio_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 9),
    _HePrio_Type()
)
hePrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePrio.setStatus("mandatory")
_HeCnt_Type = Integer32
_HeCnt_Object = MibTableColumn
heCnt = _HeCnt_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 10),
    _HeCnt_Type()
)
heCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCnt.setStatus("mandatory")
_HeData1_Type = OctetString
_HeData1_Object = MibTableColumn
heData1 = _HeData1_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 11),
    _HeData1_Type()
)
heData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heData1.setStatus("mandatory")
_HeData2_Type = OctetString
_HeData2_Object = MibTableColumn
heData2 = _HeData2_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 12),
    _HeData2_Type()
)
heData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heData2.setStatus("mandatory")
_HeData3_Type = OctetString
_HeData3_Object = MibTableColumn
heData3 = _HeData3_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 13),
    _HeData3_Type()
)
heData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heData3.setStatus("mandatory")
_HeData4_Type = OctetString
_HeData4_Object = MibTableColumn
heData4 = _HeData4_Object(
    (1, 3, 6, 1, 4, 1, 662, 3, 1, 4, 1, 1, 14),
    _HeData4_Type()
)
heData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heData4.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hwerrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 662, 0, 1)
)
hwerrTrap.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("VMX-DIAL", "heType"),
        ("VMX-DIAL", "heSlot"),
        ("VMX-DIAL", "heMon"),
        ("VMX-DIAL", "heDay"),
        ("VMX-DIAL", "heHour"),
        ("VMX-DIAL", "heMin"),
        ("VMX-DIAL", "heCh"),
        ("VMX-DIAL", "hePrio"),
        ("VMX-DIAL", "heCnt"),
        ("VMX-DIAL", "heData1"),
        ("VMX-DIAL", "heData2"),
        ("VMX-DIAL", "heData3"),
        ("VMX-DIAL", "heData4"))
)
if mibBuilder.loadTexts:
    hwerrTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMX-DIAL",
    **{"octel": octel,
       "hwerrTrap": hwerrTrap,
       "octelOIDs": octelOIDs,
       "octelPlatforms": octelPlatforms,
       "vmx200": vmx200,
       "vmx300": vmx300,
       "octelProducts": octelProducts,
       "vmxDial": vmxDial,
       "config": config,
       "systemName": systemName,
       "sysSerialNum": sysSerialNum,
       "systemID": systemID,
       "dNetstat": dNetstat,
       "message": message,
       "sentVoiceMsgs": sentVoiceMsgs,
       "recvVoiceMsgs": recvVoiceMsgs,
       "sentFaxMsgs": sentFaxMsgs,
       "recvFaxMsgs": recvFaxMsgs,
       "recvNames": recvNames,
       "playedRtNames": playedRtNames,
       "secSent": secSent,
       "secRecv": secRecv,
       "lanCh": lanCh,
       "lchNumber": lchNumber,
       "sec50pct": sec50pct,
       "sec75pct": sec75pct,
       "sec100pct": sec100pct,
       "lchInSendSec": lchInSendSec,
       "lchInRecvSec": lchInRecvSec,
       "lanConn": lanConn,
       "outAttempts": outAttempts,
       "outRejects": outRejects,
       "outGotBusys": outGotBusys,
       "inAttempts": inAttempts,
       "inRejects": inRejects,
       "inGotBusys": inGotBusys,
       "lanAvailPct": lanAvailPct,
       "location": location,
       "locTable": locTable,
       "locEntry": locEntry,
       "locIndex": locIndex,
       "locName": locName,
       "locIpAddr": locIpAddr,
       "locLinkType": locLinkType,
       "locInDomain": locInDomain,
       "locColocated": locColocated,
       "locroute": locroute,
       "route1": route1,
       "route2": route2,
       "route3": route3,
       "locConn": locConn,
       "cattempts": cattempts,
       "cfailures": cfailures,
       "cdroppeds": cdroppeds,
       "cbusys": cbusys,
       "cdayMin": cdayMin,
       "cnightMin": cnightMin,
       "msgDelivery": msgDelivery,
       "mdvcAttempts": mdvcAttempts,
       "mdvcFails": mdvcFails,
       "mdvcRetries": mdvcRetries,
       "mdfxAttempts": mdfxAttempts,
       "mdfxFails": mdfxFails,
       "mdfxRetries": mdfxRetries,
       "mdDiskfulls": mdDiskfulls,
       "mdMbxfails": mdMbxfails,
       "mdMinute": mdMinute,
       "locPlayedNames": locPlayedNames,
       "locLinkdrops": locLinkdrops,
       "locAnalogstndbys": locAnalogstndbys,
       "hwerr": hwerr,
       "hwerrTable": hwerrTable,
       "hwerrEntry": hwerrEntry,
       "heIdx": heIdx,
       "heType": heType,
       "heSlot": heSlot,
       "heMon": heMon,
       "heDay": heDay,
       "heHour": heHour,
       "heMin": heMin,
       "heCh": heCh,
       "hePrio": hePrio,
       "heCnt": heCnt,
       "heData1": heData1,
       "heData2": heData2,
       "heData3": heData3,
       "heData4": heData4}
)
