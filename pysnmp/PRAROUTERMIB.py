# SNMP MIB module (PRAROUTERMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRAROUTERMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:37 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Itk_ObjectIdentity = ObjectIdentity
itk = _Itk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195)
)
_Pramib_ObjectIdentity = ObjectIdentity
pramib = _Pramib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1)
)
_Prasoftware_ObjectIdentity = ObjectIdentity
prasoftware = _Prasoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3)
)


class _PraVersion_Type(OctetString):
    """Custom type praVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PraVersion_Type.__name__ = "OctetString"
_PraVersion_Object = MibScalar
praVersion = _PraVersion_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 1),
    _PraVersion_Type()
)
praVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    praVersion.setStatus("mandatory")
_AsIpTable_Object = MibTable
asIpTable = _AsIpTable_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    asIpTable.setStatus("mandatory")
_AsIpEntry_Object = MibTableRow
asIpEntry = _AsIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1)
)
asIpEntry.setIndexNames(
    (0, "PRAROUTERMIB", "asNumber"),
)
if mibBuilder.loadTexts:
    asIpEntry.setStatus("mandatory")
_AsNumber_Type = Integer32
_AsNumber_Object = MibTableColumn
asNumber = _AsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1, 1),
    _AsNumber_Type()
)
asNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asNumber.setStatus("mandatory")
_AsIpAddr_Type = OctetString
_AsIpAddr_Object = MibTableColumn
asIpAddr = _AsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1, 2),
    _AsIpAddr_Type()
)
asIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asIpAddr.setStatus("mandatory")
_LinecntPspdn_Type = Integer32
_LinecntPspdn_Object = MibScalar
linecntPspdn = _LinecntPspdn_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 3),
    _LinecntPspdn_Type()
)
linecntPspdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecntPspdn.setStatus("mandatory")
_LinecntPspdnPerBchannel_Type = Integer32
_LinecntPspdnPerBchannel_Object = MibScalar
linecntPspdnPerBchannel = _LinecntPspdnPerBchannel_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 4),
    _LinecntPspdnPerBchannel_Type()
)
linecntPspdnPerBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecntPspdnPerBchannel.setStatus("mandatory")
_LinecntPspdnPh_Type = Integer32
_LinecntPspdnPh_Object = MibScalar
linecntPspdnPh = _LinecntPspdnPh_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 5),
    _LinecntPspdnPh_Type()
)
linecntPspdnPh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecntPspdnPh.setStatus("mandatory")
_LinecntMax_Type = Integer32
_LinecntMax_Object = MibScalar
linecntMax = _LinecntMax_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 6),
    _LinecntMax_Type()
)
linecntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecntMax.setStatus("mandatory")
_AsIpAddrTableMaxIndex_Type = Integer32
_AsIpAddrTableMaxIndex_Object = MibScalar
asIpAddrTableMaxIndex = _AsIpAddrTableMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 7),
    _AsIpAddrTableMaxIndex_Type()
)
asIpAddrTableMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asIpAddrTableMaxIndex.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2)
)
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 1)
)
_NumberOfEngagedBchan_Type = Integer32
_NumberOfEngagedBchan_Object = MibScalar
numberOfEngagedBchan = _NumberOfEngagedBchan_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 1),
    _NumberOfEngagedBchan_Type()
)
numberOfEngagedBchan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfEngagedBchan.setStatus("mandatory")
_NumberOfFreeBchan_Type = Integer32
_NumberOfFreeBchan_Object = MibScalar
numberOfFreeBchan = _NumberOfFreeBchan_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 2),
    _NumberOfFreeBchan_Type()
)
numberOfFreeBchan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfFreeBchan.setStatus("mandatory")
_NumberOfTransToAs_Type = Integer32
_NumberOfTransToAs_Object = MibScalar
numberOfTransToAs = _NumberOfTransToAs_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 3),
    _NumberOfTransToAs_Type()
)
numberOfTransToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTransToAs.setStatus("mandatory")
_NumberOfRecvToAs_Type = Integer32
_NumberOfRecvToAs_Object = MibScalar
numberOfRecvToAs = _NumberOfRecvToAs_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 4),
    _NumberOfRecvToAs_Type()
)
numberOfRecvToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRecvToAs.setStatus("mandatory")
_Watchdog_ObjectIdentity = ObjectIdentity
watchdog = _Watchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 2)
)
_Temperature_Type = Integer32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 2, 1),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3)
)
_IsdnMuxOk_Type = Integer32
_IsdnMuxOk_Object = MibScalar
isdnMuxOk = _IsdnMuxOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 1),
    _IsdnMuxOk_Type()
)
isdnMuxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnMuxOk.setStatus("mandatory")
_ModemAdapterTable_Object = MibTable
modemAdapterTable = _ModemAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    modemAdapterTable.setStatus("mandatory")
_ModemEntry_Object = MibTableRow
modemEntry = _ModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1)
)
modemEntry.setIndexNames(
    (0, "PRAROUTERMIB", "modemCardNumber"),
)
if mibBuilder.loadTexts:
    modemEntry.setStatus("mandatory")
_ModemCardNumber_Type = Integer32
_ModemCardNumber_Object = MibTableColumn
modemCardNumber = _ModemCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 1),
    _ModemCardNumber_Type()
)
modemCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCardNumber.setStatus("mandatory")
_ModemAdapterOk_Type = Integer32
_ModemAdapterOk_Object = MibTableColumn
modemAdapterOk = _ModemAdapterOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 2),
    _ModemAdapterOk_Type()
)
modemAdapterOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemAdapterOk.setStatus("mandatory")
_Modem1_Type = Integer32
_Modem1_Object = MibTableColumn
modem1 = _Modem1_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 3),
    _Modem1_Type()
)
modem1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem1.setStatus("mandatory")
_Modem2_Type = Integer32
_Modem2_Object = MibTableColumn
modem2 = _Modem2_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 4),
    _Modem2_Type()
)
modem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem2.setStatus("mandatory")
_Modem3_Type = Integer32
_Modem3_Object = MibTableColumn
modem3 = _Modem3_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 5),
    _Modem3_Type()
)
modem3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem3.setStatus("mandatory")
_Modem4_Type = Integer32
_Modem4_Object = MibTableColumn
modem4 = _Modem4_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 6),
    _Modem4_Type()
)
modem4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem4.setStatus("mandatory")
_Modem5_Type = Integer32
_Modem5_Object = MibTableColumn
modem5 = _Modem5_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 7),
    _Modem5_Type()
)
modem5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem5.setStatus("mandatory")
_Modem6_Type = Integer32
_Modem6_Object = MibTableColumn
modem6 = _Modem6_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 8),
    _Modem6_Type()
)
modem6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem6.setStatus("mandatory")
_Modem7_Type = Integer32
_Modem7_Object = MibTableColumn
modem7 = _Modem7_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 9),
    _Modem7_Type()
)
modem7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem7.setStatus("mandatory")
_Modem8_Type = Integer32
_Modem8_Object = MibTableColumn
modem8 = _Modem8_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 10),
    _Modem8_Type()
)
modem8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modem8.setStatus("mandatory")
_PractrlOk_Type = Integer32
_PractrlOk_Object = MibScalar
practrlOk = _PractrlOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 3),
    _PractrlOk_Type()
)
practrlOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    practrlOk.setStatus("mandatory")
_IsdnInOk_Type = Integer32
_IsdnInOk_Object = MibScalar
isdnInOk = _IsdnInOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 4),
    _IsdnInOk_Type()
)
isdnInOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnInOk.setStatus("mandatory")
_IsdnOutOk_Type = Integer32
_IsdnOutOk_Object = MibScalar
isdnOutOk = _IsdnOutOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 5),
    _IsdnOutOk_Type()
)
isdnOutOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnOutOk.setStatus("mandatory")
_PstnInOk_Type = Integer32
_PstnInOk_Object = MibScalar
pstnInOk = _PstnInOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 6),
    _PstnInOk_Type()
)
pstnInOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pstnInOk.setStatus("mandatory")
_PspdnOk_Type = Integer32
_PspdnOk_Object = MibScalar
pspdnOk = _PspdnOk_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 7),
    _PspdnOk_Type()
)
pspdnOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspdnOk.setStatus("mandatory")
_ModemCardMax_Type = Integer32
_ModemCardMax_Object = MibScalar
modemCardMax = _ModemCardMax_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 8),
    _ModemCardMax_Type()
)
modemCardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCardMax.setStatus("mandatory")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3)
)
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 1)
)
_CpuCapacity_Type = Integer32
_CpuCapacity_Object = MibScalar
cpuCapacity = _CpuCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 1, 1),
    _CpuCapacity_Type()
)
cpuCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCapacity.setStatus("mandatory")
_Sessions_ObjectIdentity = ObjectIdentity
sessions = _Sessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2)
)
_SessionTable_Object = MibTable
sessionTable = _SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sessionTable.setStatus("mandatory")
_SessionEntry_Object = MibTableRow
sessionEntry = _SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1)
)
sessionEntry.setIndexNames(
    (0, "PRAROUTERMIB", "sessionNumber"),
)
if mibBuilder.loadTexts:
    sessionEntry.setStatus("mandatory")
_SessionNumber_Type = Integer32
_SessionNumber_Object = MibTableColumn
sessionNumber = _SessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 1),
    _SessionNumber_Type()
)
sessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionNumber.setStatus("mandatory")
_SessionType_Type = Integer32
_SessionType_Object = MibTableColumn
sessionType = _SessionType_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 2),
    _SessionType_Type()
)
sessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionType.setStatus("mandatory")


class _B2Protocol_Type(DisplayString):
    """Custom type b2Protocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_B2Protocol_Type.__name__ = "DisplayString"
_B2Protocol_Object = MibTableColumn
b2Protocol = _B2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 3),
    _B2Protocol_Type()
)
b2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    b2Protocol.setStatus("mandatory")
_CntRcvByteCapi_Type = Integer32
_CntRcvByteCapi_Object = MibTableColumn
cntRcvByteCapi = _CntRcvByteCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 4),
    _CntRcvByteCapi_Type()
)
cntRcvByteCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvByteCapi.setStatus("mandatory")
_CntSndByteCapi_Type = Integer32
_CntSndByteCapi_Object = MibTableColumn
cntSndByteCapi = _CntSndByteCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 5),
    _CntSndByteCapi_Type()
)
cntSndByteCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndByteCapi.setStatus("mandatory")
_CntRcvMsgCapi_Type = Integer32
_CntRcvMsgCapi_Object = MibTableColumn
cntRcvMsgCapi = _CntRcvMsgCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 6),
    _CntRcvMsgCapi_Type()
)
cntRcvMsgCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvMsgCapi.setStatus("mandatory")
_CntSndMsgCapi_Type = Integer32
_CntSndMsgCapi_Object = MibTableColumn
cntSndMsgCapi = _CntSndMsgCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 7),
    _CntSndMsgCapi_Type()
)
cntSndMsgCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndMsgCapi.setStatus("mandatory")
_CntRcvBytePsp_Type = Integer32
_CntRcvBytePsp_Object = MibTableColumn
cntRcvBytePsp = _CntRcvBytePsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 8),
    _CntRcvBytePsp_Type()
)
cntRcvBytePsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvBytePsp.setStatus("mandatory")
_CntSndBytePsp_Type = Integer32
_CntSndBytePsp_Object = MibTableColumn
cntSndBytePsp = _CntSndBytePsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 9),
    _CntSndBytePsp_Type()
)
cntSndBytePsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndBytePsp.setStatus("mandatory")
_CntRcvMsgPsp_Type = Integer32
_CntRcvMsgPsp_Object = MibTableColumn
cntRcvMsgPsp = _CntRcvMsgPsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 10),
    _CntRcvMsgPsp_Type()
)
cntRcvMsgPsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvMsgPsp.setStatus("mandatory")
_CntSndMsgPsp_Type = Integer32
_CntSndMsgPsp_Object = MibTableColumn
cntSndMsgPsp = _CntSndMsgPsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 11),
    _CntSndMsgPsp_Type()
)
cntSndMsgPsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndMsgPsp.setStatus("mandatory")
_CntRcvTotalByteCapi_Type = Integer32
_CntRcvTotalByteCapi_Object = MibScalar
cntRcvTotalByteCapi = _CntRcvTotalByteCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 2),
    _CntRcvTotalByteCapi_Type()
)
cntRcvTotalByteCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvTotalByteCapi.setStatus("mandatory")
_CntSndTotalByteCapi_Type = Integer32
_CntSndTotalByteCapi_Object = MibScalar
cntSndTotalByteCapi = _CntSndTotalByteCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 3),
    _CntSndTotalByteCapi_Type()
)
cntSndTotalByteCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndTotalByteCapi.setStatus("mandatory")
_CntRcvTotalMsgCapi_Type = Integer32
_CntRcvTotalMsgCapi_Object = MibScalar
cntRcvTotalMsgCapi = _CntRcvTotalMsgCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 4),
    _CntRcvTotalMsgCapi_Type()
)
cntRcvTotalMsgCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvTotalMsgCapi.setStatus("mandatory")
_CntSndTotalMsgCapi_Type = Integer32
_CntSndTotalMsgCapi_Object = MibScalar
cntSndTotalMsgCapi = _CntSndTotalMsgCapi_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 5),
    _CntSndTotalMsgCapi_Type()
)
cntSndTotalMsgCapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndTotalMsgCapi.setStatus("mandatory")
_CntRcvTotalBytePsp_Type = Integer32
_CntRcvTotalBytePsp_Object = MibScalar
cntRcvTotalBytePsp = _CntRcvTotalBytePsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 6),
    _CntRcvTotalBytePsp_Type()
)
cntRcvTotalBytePsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvTotalBytePsp.setStatus("mandatory")
_CntSndTotalBytePsp_Type = Integer32
_CntSndTotalBytePsp_Object = MibScalar
cntSndTotalBytePsp = _CntSndTotalBytePsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 7),
    _CntSndTotalBytePsp_Type()
)
cntSndTotalBytePsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndTotalBytePsp.setStatus("mandatory")
_CntRcvTotalMsgPsp_Type = Integer32
_CntRcvTotalMsgPsp_Object = MibScalar
cntRcvTotalMsgPsp = _CntRcvTotalMsgPsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 8),
    _CntRcvTotalMsgPsp_Type()
)
cntRcvTotalMsgPsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvTotalMsgPsp.setStatus("mandatory")
_CntSndTotalMsgPsp_Type = Integer32
_CntSndTotalMsgPsp_Object = MibScalar
cntSndTotalMsgPsp = _CntSndTotalMsgPsp_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 9),
    _CntSndTotalMsgPsp_Type()
)
cntSndTotalMsgPsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSndTotalMsgPsp.setStatus("mandatory")
_SessionTableMaxIndex_Type = Integer32
_SessionTableMaxIndex_Object = MibScalar
sessionTableMaxIndex = _SessionTableMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 10),
    _SessionTableMaxIndex_Type()
)
sessionTableMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTableMaxIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRAROUTERMIB",
    **{"itk": itk,
       "pramib": pramib,
       "config": config,
       "prasoftware": prasoftware,
       "praVersion": praVersion,
       "asIpTable": asIpTable,
       "asIpEntry": asIpEntry,
       "asNumber": asNumber,
       "asIpAddr": asIpAddr,
       "linecntPspdn": linecntPspdn,
       "linecntPspdnPerBchannel": linecntPspdnPerBchannel,
       "linecntPspdnPh": linecntPspdnPh,
       "linecntMax": linecntMax,
       "asIpAddrTableMaxIndex": asIpAddrTableMaxIndex,
       "status": status,
       "channels": channels,
       "numberOfEngagedBchan": numberOfEngagedBchan,
       "numberOfFreeBchan": numberOfFreeBchan,
       "numberOfTransToAs": numberOfTransToAs,
       "numberOfRecvToAs": numberOfRecvToAs,
       "watchdog": watchdog,
       "temperature": temperature,
       "fault": fault,
       "isdnMuxOk": isdnMuxOk,
       "modemAdapterTable": modemAdapterTable,
       "modemEntry": modemEntry,
       "modemCardNumber": modemCardNumber,
       "modemAdapterOk": modemAdapterOk,
       "modem1": modem1,
       "modem2": modem2,
       "modem3": modem3,
       "modem4": modem4,
       "modem5": modem5,
       "modem6": modem6,
       "modem7": modem7,
       "modem8": modem8,
       "practrlOk": practrlOk,
       "isdnInOk": isdnInOk,
       "isdnOutOk": isdnOutOk,
       "pstnInOk": pstnInOk,
       "pspdnOk": pspdnOk,
       "modemCardMax": modemCardMax,
       "performance": performance,
       "cpu": cpu,
       "cpuCapacity": cpuCapacity,
       "sessions": sessions,
       "sessionTable": sessionTable,
       "sessionEntry": sessionEntry,
       "sessionNumber": sessionNumber,
       "sessionType": sessionType,
       "b2Protocol": b2Protocol,
       "cntRcvByteCapi": cntRcvByteCapi,
       "cntSndByteCapi": cntSndByteCapi,
       "cntRcvMsgCapi": cntRcvMsgCapi,
       "cntSndMsgCapi": cntSndMsgCapi,
       "cntRcvBytePsp": cntRcvBytePsp,
       "cntSndBytePsp": cntSndBytePsp,
       "cntRcvMsgPsp": cntRcvMsgPsp,
       "cntSndMsgPsp": cntSndMsgPsp,
       "cntRcvTotalByteCapi": cntRcvTotalByteCapi,
       "cntSndTotalByteCapi": cntSndTotalByteCapi,
       "cntRcvTotalMsgCapi": cntRcvTotalMsgCapi,
       "cntSndTotalMsgCapi": cntSndTotalMsgCapi,
       "cntRcvTotalBytePsp": cntRcvTotalBytePsp,
       "cntSndTotalBytePsp": cntSndTotalBytePsp,
       "cntRcvTotalMsgPsp": cntRcvTotalMsgPsp,
       "cntSndTotalMsgPsp": cntSndTotalMsgPsp,
       "sessionTableMaxIndex": sessionTableMaxIndex}
)
