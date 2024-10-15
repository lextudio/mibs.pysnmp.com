# SNMP MIB module (MP-FRPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MP-FRPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:46 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mgmt")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetPrefix(OctetString):
    """Custom type NetPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_NecProduct_ObjectIdentity = ObjectIdentity
necProduct = _NecProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1)
)
_Datax_ObjectIdentity = ObjectIdentity
datax = _Datax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3)
)
_Mmpf_ObjectIdentity = ObjectIdentity
mmpf = _Mmpf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13)
)
_Mmn9110_ObjectIdentity = ObjectIdentity
mmn9110 = _Mmn9110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13, 1)
)
_Mmn9120_ObjectIdentity = ObjectIdentity
mmn9120 = _Mmn9120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13, 2)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_Datax_mib_ObjectIdentity = ObjectIdentity
datax_mib = _Datax_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3)
)
_Mmpf_mib_ObjectIdentity = ObjectIdentity
mmpf_mib = _Mmpf_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13)
)
_MpSystem_ObjectIdentity = ObjectIdentity
mpSystem = _MpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 1)
)
_MpIfCard_ObjectIdentity = ObjectIdentity
mpIfCard = _MpIfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 2)
)
_MpEtherPort_ObjectIdentity = ObjectIdentity
mpEtherPort = _MpEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 3)
)
_MpVlan_ObjectIdentity = ObjectIdentity
mpVlan = _MpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 4)
)
_MpBridge_ObjectIdentity = ObjectIdentity
mpBridge = _MpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 5)
)
_MpDbAccess_ObjectIdentity = ObjectIdentity
mpDbAccess = _MpDbAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 6)
)
_MpEventLog_ObjectIdentity = ObjectIdentity
mpEventLog = _MpEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 7)
)
_MpUiSession_ObjectIdentity = ObjectIdentity
mpUiSession = _MpUiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 8)
)
_MpFtp_ObjectIdentity = ObjectIdentity
mpFtp = _MpFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 9)
)
_MpDhcp_ObjectIdentity = ObjectIdentity
mpDhcp = _MpDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 10)
)
_MpIp_ObjectIdentity = ObjectIdentity
mpIp = _MpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 11)
)
_MpRip_ObjectIdentity = ObjectIdentity
mpRip = _MpRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 12)
)
_MpSnmp_ObjectIdentity = ObjectIdentity
mpSnmp = _MpSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 13)
)
_MpStats_ObjectIdentity = ObjectIdentity
mpStats = _MpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 14)
)
_MpCli_ObjectIdentity = ObjectIdentity
mpCli = _MpCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 15)
)
_MpAtm_ObjectIdentity = ObjectIdentity
mpAtm = _MpAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 16)
)
_MpLis_ObjectIdentity = ObjectIdentity
mpLis = _MpLis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 17)
)
_MpDns_ObjectIdentity = ObjectIdentity
mpDns = _MpDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 18)
)
_MpLec_ObjectIdentity = ObjectIdentity
mpLec = _MpLec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 19)
)
_MpMpc_ObjectIdentity = ObjectIdentity
mpMpc = _MpMpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 20)
)
_MpStp_ObjectIdentity = ObjectIdentity
mpStp = _MpStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 21)
)
_MpLlc_ObjectIdentity = ObjectIdentity
mpLlc = _MpLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 22)
)
_MpOspf_ObjectIdentity = ObjectIdentity
mpOspf = _MpOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 23)
)
_MpObsCtl_ObjectIdentity = ObjectIdentity
mpObsCtl = _MpObsCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 101)
)
_MpCardInfo_ObjectIdentity = ObjectIdentity
mpCardInfo = _MpCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 102)
)
_MpInterface_ObjectIdentity = ObjectIdentity
mpInterface = _MpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 103)
)
_MpPvoice_ObjectIdentity = ObjectIdentity
mpPvoice = _MpPvoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 104)
)
_MpAtmCallCtl_ObjectIdentity = ObjectIdentity
mpAtmCallCtl = _MpAtmCallCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110)
)
_MpCes_ObjectIdentity = ObjectIdentity
mpCes = _MpCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 111)
)
_MpIpsw_ObjectIdentity = ObjectIdentity
mpIpsw = _MpIpsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 112)
)
_MpInsCtl_ObjectIdentity = ObjectIdentity
mpInsCtl = _MpInsCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 113)
)
_MpFfr_ObjectIdentity = ObjectIdentity
mpFfr = _MpFfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 114)
)
_MpIpswAtm_ObjectIdentity = ObjectIdentity
mpIpswAtm = _MpIpswAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 115)
)
_MpPpp_ObjectIdentity = ObjectIdentity
mpPpp = _MpPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 120)
)
_MpPos_ObjectIdentity = ObjectIdentity
mpPos = _MpPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 121)
)
_MpFrpp_ObjectIdentity = ObjectIdentity
mpFrpp = _MpFrpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123)
)
_MpFrppTrapInfo_ObjectIdentity = ObjectIdentity
mpFrppTrapInfo = _MpFrppTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 1)
)
_MpFrppTrapInfoMccid_Type = Integer32
_MpFrppTrapInfoMccid_Object = MibScalar
mpFrppTrapInfoMccid = _MpFrppTrapInfoMccid_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 1, 1),
    _MpFrppTrapInfoMccid_Type()
)
mpFrppTrapInfoMccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppTrapInfoMccid.setStatus("mandatory")
_MpFrppTrapInfoDlci_Type = Integer32
_MpFrppTrapInfoDlci_Object = MibScalar
mpFrppTrapInfoDlci = _MpFrppTrapInfoDlci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 1, 2),
    _MpFrppTrapInfoDlci_Type()
)
mpFrppTrapInfoDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppTrapInfoDlci.setStatus("mandatory")
_MpFrppMccCfgTable_Object = MibTable
mpFrppMccCfgTable = _MpFrppMccCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2)
)
if mibBuilder.loadTexts:
    mpFrppMccCfgTable.setStatus("mandatory")
_MpFrppMccCfgEntry_Object = MibTableRow
mpFrppMccCfgEntry = _MpFrppMccCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1)
)
mpFrppMccCfgEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppMccCfgIfIndex"),
)
if mibBuilder.loadTexts:
    mpFrppMccCfgEntry.setStatus("mandatory")
_MpFrppMccCfgIfIndex_Type = Integer32
_MpFrppMccCfgIfIndex_Object = MibTableColumn
mpFrppMccCfgIfIndex = _MpFrppMccCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 1),
    _MpFrppMccCfgIfIndex_Type()
)
mpFrppMccCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccCfgIfIndex.setStatus("mandatory")


class _MpFrppMccCfgL2Status_Type(Integer32):
    """Custom type mpFrppMccCfgL2Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MpFrppMccCfgL2Status_Type.__name__ = "Integer32"
_MpFrppMccCfgL2Status_Object = MibTableColumn
mpFrppMccCfgL2Status = _MpFrppMccCfgL2Status_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 2),
    _MpFrppMccCfgL2Status_Type()
)
mpFrppMccCfgL2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccCfgL2Status.setStatus("mandatory")


class _MpFrppMccCfgLmiProtocol_Type(Integer32):
    """Custom type mpFrppMccCfgLmiProtocol based on Integer32"""
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
        *(("ansi", 1),
          ("itu", 2),
          ("noLmi", 3))
    )


_MpFrppMccCfgLmiProtocol_Type.__name__ = "Integer32"
_MpFrppMccCfgLmiProtocol_Object = MibTableColumn
mpFrppMccCfgLmiProtocol = _MpFrppMccCfgLmiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 3),
    _MpFrppMccCfgLmiProtocol_Type()
)
mpFrppMccCfgLmiProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgLmiProtocol.setStatus("mandatory")


class _MpFrppMccCfgUniType_Type(Integer32):
    """Custom type mpFrppMccCfgUniType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_MpFrppMccCfgUniType_Type.__name__ = "Integer32"
_MpFrppMccCfgUniType_Object = MibTableColumn
mpFrppMccCfgUniType = _MpFrppMccCfgUniType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 4),
    _MpFrppMccCfgUniType_Type()
)
mpFrppMccCfgUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgUniType.setStatus("mandatory")


class _MpFrppMccCfgMonitoredEvents_Type(Integer32):
    """Custom type mpFrppMccCfgMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MpFrppMccCfgMonitoredEvents_Type.__name__ = "Integer32"
_MpFrppMccCfgMonitoredEvents_Object = MibTableColumn
mpFrppMccCfgMonitoredEvents = _MpFrppMccCfgMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 5),
    _MpFrppMccCfgMonitoredEvents_Type()
)
mpFrppMccCfgMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgMonitoredEvents.setStatus("mandatory")


class _MpFrppMccCfgErrorThreshold_Type(Integer32):
    """Custom type mpFrppMccCfgErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MpFrppMccCfgErrorThreshold_Type.__name__ = "Integer32"
_MpFrppMccCfgErrorThreshold_Object = MibTableColumn
mpFrppMccCfgErrorThreshold = _MpFrppMccCfgErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 6),
    _MpFrppMccCfgErrorThreshold_Type()
)
mpFrppMccCfgErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgErrorThreshold.setStatus("mandatory")


class _MpFrppMccCfgFullEnqInterval_Type(Integer32):
    """Custom type mpFrppMccCfgFullEnqInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpFrppMccCfgFullEnqInterval_Type.__name__ = "Integer32"
_MpFrppMccCfgFullEnqInterval_Object = MibTableColumn
mpFrppMccCfgFullEnqInterval = _MpFrppMccCfgFullEnqInterval_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 7),
    _MpFrppMccCfgFullEnqInterval_Type()
)
mpFrppMccCfgFullEnqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgFullEnqInterval.setStatus("mandatory")


class _MpFrppMccCfgLmiProcedure_Type(Integer32):
    """Custom type mpFrppMccCfgLmiProcedure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_MpFrppMccCfgLmiProcedure_Type.__name__ = "Integer32"
_MpFrppMccCfgLmiProcedure_Object = MibTableColumn
mpFrppMccCfgLmiProcedure = _MpFrppMccCfgLmiProcedure_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 8),
    _MpFrppMccCfgLmiProcedure_Type()
)
mpFrppMccCfgLmiProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgLmiProcedure.setStatus("mandatory")


class _MpFrppMccCfgNetPollInterval_Type(Integer32):
    """Custom type mpFrppMccCfgNetPollInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_MpFrppMccCfgNetPollInterval_Type.__name__ = "Integer32"
_MpFrppMccCfgNetPollInterval_Object = MibTableColumn
mpFrppMccCfgNetPollInterval = _MpFrppMccCfgNetPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 9),
    _MpFrppMccCfgNetPollInterval_Type()
)
mpFrppMccCfgNetPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgNetPollInterval.setStatus("mandatory")


class _MpFrppMccCfgUsrPollInterval_Type(Integer32):
    """Custom type mpFrppMccCfgUsrPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_MpFrppMccCfgUsrPollInterval_Type.__name__ = "Integer32"
_MpFrppMccCfgUsrPollInterval_Object = MibTableColumn
mpFrppMccCfgUsrPollInterval = _MpFrppMccCfgUsrPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 10),
    _MpFrppMccCfgUsrPollInterval_Type()
)
mpFrppMccCfgUsrPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgUsrPollInterval.setStatus("mandatory")


class _MpFrppMccCfgAsync_Type(Integer32):
    """Custom type mpFrppMccCfgAsync based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MpFrppMccCfgAsync_Type.__name__ = "Integer32"
_MpFrppMccCfgAsync_Object = MibTableColumn
mpFrppMccCfgAsync = _MpFrppMccCfgAsync_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 11),
    _MpFrppMccCfgAsync_Type()
)
mpFrppMccCfgAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgAsync.setStatus("mandatory")
_MpFrppMccCfgRowStatus_Type = RowStatus
_MpFrppMccCfgRowStatus_Object = MibTableColumn
mpFrppMccCfgRowStatus = _MpFrppMccCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 12),
    _MpFrppMccCfgRowStatus_Type()
)
mpFrppMccCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppMccCfgRowStatus.setStatus("mandatory")


class _MpFrppMccCfgErrInfo_Type(Integer32):
    """Custom type mpFrppMccCfgErrInfo based on Integer32"""
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
        *(("badIndexValue", 4),
          ("badValue", 3),
          ("correlationError", 5),
          ("ipAddressNotDeleted", 11),
          ("lowLayerConfigNotRegistered", 9),
          ("mappingDataAlreadyExist", 10),
          ("mbufHuntFailure", 7),
          ("mccIdHuntFailure", 12),
          ("memoryAllocateFailure", 6),
          ("normal", 1),
          ("parameterNotEnough", 2),
          ("relationalConfigExist", 8))
    )


_MpFrppMccCfgErrInfo_Type.__name__ = "Integer32"
_MpFrppMccCfgErrInfo_Object = MibTableColumn
mpFrppMccCfgErrInfo = _MpFrppMccCfgErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 2, 1, 13),
    _MpFrppMccCfgErrInfo_Type()
)
mpFrppMccCfgErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccCfgErrInfo.setStatus("mandatory")
_MpFrppFrppCfgTable_Object = MibTable
mpFrppFrppCfgTable = _MpFrppFrppCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3)
)
if mibBuilder.loadTexts:
    mpFrppFrppCfgTable.setStatus("mandatory")
_MpFrppFrppCfgEntry_Object = MibTableRow
mpFrppFrppCfgEntry = _MpFrppFrppCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1)
)
mpFrppFrppCfgEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppFrppCfgIfIndex"),
    (0, "MP-FRPP-MIB", "mpFrppFrppCfgMccidIndex"),
    (0, "MP-FRPP-MIB", "mpFrppFrppCfgDlciIndex"),
)
if mibBuilder.loadTexts:
    mpFrppFrppCfgEntry.setStatus("mandatory")
_MpFrppFrppCfgIfIndex_Type = Integer32
_MpFrppFrppCfgIfIndex_Object = MibTableColumn
mpFrppFrppCfgIfIndex = _MpFrppFrppCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 1),
    _MpFrppFrppCfgIfIndex_Type()
)
mpFrppFrppCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgIfIndex.setStatus("mandatory")


class _MpFrppFrppCfgMccidIndex_Type(Integer32):
    """Custom type mpFrppFrppCfgMccidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpFrppFrppCfgMccidIndex_Type.__name__ = "Integer32"
_MpFrppFrppCfgMccidIndex_Object = MibTableColumn
mpFrppFrppCfgMccidIndex = _MpFrppFrppCfgMccidIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 2),
    _MpFrppFrppCfgMccidIndex_Type()
)
mpFrppFrppCfgMccidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgMccidIndex.setStatus("mandatory")


class _MpFrppFrppCfgDlciIndex_Type(Integer32):
    """Custom type mpFrppFrppCfgDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_MpFrppFrppCfgDlciIndex_Type.__name__ = "Integer32"
_MpFrppFrppCfgDlciIndex_Object = MibTableColumn
mpFrppFrppCfgDlciIndex = _MpFrppFrppCfgDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 3),
    _MpFrppFrppCfgDlciIndex_Type()
)
mpFrppFrppCfgDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgDlciIndex.setStatus("mandatory")
_MpFrppFrppCfgFrppName_Type = DisplayString
_MpFrppFrppCfgFrppName_Object = MibTableColumn
mpFrppFrppCfgFrppName = _MpFrppFrppCfgFrppName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 4),
    _MpFrppFrppCfgFrppName_Type()
)
mpFrppFrppCfgFrppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgFrppName.setStatus("mandatory")
_MpFrppFrppCfgIpadd_Type = IpAddress
_MpFrppFrppCfgIpadd_Object = MibTableColumn
mpFrppFrppCfgIpadd = _MpFrppFrppCfgIpadd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 5),
    _MpFrppFrppCfgIpadd_Type()
)
mpFrppFrppCfgIpadd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgIpadd.setStatus("mandatory")
_MpFrppFrppCfgSubnet_Type = IpAddress
_MpFrppFrppCfgSubnet_Object = MibTableColumn
mpFrppFrppCfgSubnet = _MpFrppFrppCfgSubnet_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 6),
    _MpFrppFrppCfgSubnet_Type()
)
mpFrppFrppCfgSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgSubnet.setStatus("mandatory")


class _MpFrppFrppCfgMtuSize_Type(Integer32):
    """Custom type mpFrppFrppCfgMtuSize based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 9180),
    )


_MpFrppFrppCfgMtuSize_Type.__name__ = "Integer32"
_MpFrppFrppCfgMtuSize_Object = MibTableColumn
mpFrppFrppCfgMtuSize = _MpFrppFrppCfgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 7),
    _MpFrppFrppCfgMtuSize_Type()
)
mpFrppFrppCfgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgMtuSize.setStatus("mandatory")


class _MpFrppFrppCfgInterWorkType_Type(Integer32):
    """Custom type mpFrppFrppCfgInterWorkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipoverfr", 1),
          ("macoverfr", 2))
    )


_MpFrppFrppCfgInterWorkType_Type.__name__ = "Integer32"
_MpFrppFrppCfgInterWorkType_Object = MibTableColumn
mpFrppFrppCfgInterWorkType = _MpFrppFrppCfgInterWorkType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 8),
    _MpFrppFrppCfgInterWorkType_Type()
)
mpFrppFrppCfgInterWorkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgInterWorkType.setStatus("mandatory")


class _MpFrppFrppCfgCrtpSupport_Type(Integer32):
    """Custom type mpFrppFrppCfgCrtpSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("support", 2))
    )


_MpFrppFrppCfgCrtpSupport_Type.__name__ = "Integer32"
_MpFrppFrppCfgCrtpSupport_Object = MibTableColumn
mpFrppFrppCfgCrtpSupport = _MpFrppFrppCfgCrtpSupport_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 9),
    _MpFrppFrppCfgCrtpSupport_Type()
)
mpFrppFrppCfgCrtpSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCrtpSupport.setStatus("mandatory")


class _MpFrppFrppCfgCrtpLimit_Type(Integer32):
    """Custom type mpFrppFrppCfgCrtpLimit based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpFrppFrppCfgCrtpLimit_Type.__name__ = "Integer32"
_MpFrppFrppCfgCrtpLimit_Object = MibTableColumn
mpFrppFrppCfgCrtpLimit = _MpFrppFrppCfgCrtpLimit_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 10),
    _MpFrppFrppCfgCrtpLimit_Type()
)
mpFrppFrppCfgCrtpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCrtpLimit.setStatus("mandatory")


class _MpFrppFrppCfgCrtpMode_Type(Integer32):
    """Custom type mpFrppFrppCfgCrtpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("through", 1))
    )


_MpFrppFrppCfgCrtpMode_Type.__name__ = "Integer32"
_MpFrppFrppCfgCrtpMode_Object = MibTableColumn
mpFrppFrppCfgCrtpMode = _MpFrppFrppCfgCrtpMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 11),
    _MpFrppFrppCfgCrtpMode_Type()
)
mpFrppFrppCfgCrtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCrtpMode.setStatus("mandatory")


class _MpFrppFrppCfgCrtpAging_Type(Integer32):
    """Custom type mpFrppFrppCfgCrtpAging based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_MpFrppFrppCfgCrtpAging_Type.__name__ = "Integer32"
_MpFrppFrppCfgCrtpAging_Object = MibTableColumn
mpFrppFrppCfgCrtpAging = _MpFrppFrppCfgCrtpAging_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 12),
    _MpFrppFrppCfgCrtpAging_Type()
)
mpFrppFrppCfgCrtpAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCrtpAging.setStatus("mandatory")


class _MpFrppFrppCfgCtcpSupport_Type(Integer32):
    """Custom type mpFrppFrppCfgCtcpSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("support", 2))
    )


_MpFrppFrppCfgCtcpSupport_Type.__name__ = "Integer32"
_MpFrppFrppCfgCtcpSupport_Object = MibTableColumn
mpFrppFrppCfgCtcpSupport = _MpFrppFrppCfgCtcpSupport_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 13),
    _MpFrppFrppCfgCtcpSupport_Type()
)
mpFrppFrppCfgCtcpSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCtcpSupport.setStatus("mandatory")


class _MpFrppFrppCfgCtcpLimit_Type(Integer32):
    """Custom type mpFrppFrppCfgCtcpLimit based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpFrppFrppCfgCtcpLimit_Type.__name__ = "Integer32"
_MpFrppFrppCfgCtcpLimit_Object = MibTableColumn
mpFrppFrppCfgCtcpLimit = _MpFrppFrppCfgCtcpLimit_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 14),
    _MpFrppFrppCfgCtcpLimit_Type()
)
mpFrppFrppCfgCtcpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCtcpLimit.setStatus("mandatory")


class _MpFrppFrppCfgCtcpMode_Type(Integer32):
    """Custom type mpFrppFrppCfgCtcpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("through", 1))
    )


_MpFrppFrppCfgCtcpMode_Type.__name__ = "Integer32"
_MpFrppFrppCfgCtcpMode_Object = MibTableColumn
mpFrppFrppCfgCtcpMode = _MpFrppFrppCfgCtcpMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 15),
    _MpFrppFrppCfgCtcpMode_Type()
)
mpFrppFrppCfgCtcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCtcpMode.setStatus("mandatory")


class _MpFrppFrppCfgCtcpAging_Type(Integer32):
    """Custom type mpFrppFrppCfgCtcpAging based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_MpFrppFrppCfgCtcpAging_Type.__name__ = "Integer32"
_MpFrppFrppCfgCtcpAging_Object = MibTableColumn
mpFrppFrppCfgCtcpAging = _MpFrppFrppCfgCtcpAging_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 16),
    _MpFrppFrppCfgCtcpAging_Type()
)
mpFrppFrppCfgCtcpAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgCtcpAging.setStatus("mandatory")


class _MpFrppFrppCfgHwSticFlag_Type(Integer32):
    """Custom type mpFrppFrppCfgHwSticFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MpFrppFrppCfgHwSticFlag_Type.__name__ = "Integer32"
_MpFrppFrppCfgHwSticFlag_Object = MibTableColumn
mpFrppFrppCfgHwSticFlag = _MpFrppFrppCfgHwSticFlag_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 17),
    _MpFrppFrppCfgHwSticFlag_Type()
)
mpFrppFrppCfgHwSticFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgHwSticFlag.setStatus("mandatory")
_MpFrppDlciCfgMtuSize_Type = Integer32
_MpFrppDlciCfgMtuSize_Object = MibTableColumn
mpFrppDlciCfgMtuSize = _MpFrppDlciCfgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 18),
    _MpFrppDlciCfgMtuSize_Type()
)
mpFrppDlciCfgMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciCfgMtuSize.setStatus("mandatory")


class _MpFrppDlciCfgBecn_Type(Integer32):
    """Custom type mpFrppDlciCfgBecn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MpFrppDlciCfgBecn_Type.__name__ = "Integer32"
_MpFrppDlciCfgBecn_Object = MibTableColumn
mpFrppDlciCfgBecn = _MpFrppDlciCfgBecn_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 19),
    _MpFrppDlciCfgBecn_Type()
)
mpFrppDlciCfgBecn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgBecn.setStatus("mandatory")


class _MpFrppDlciCfgEncap_Type(Integer32):
    """Custom type mpFrppDlciCfgEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 2),
          ("nec", 1))
    )


_MpFrppDlciCfgEncap_Type.__name__ = "Integer32"
_MpFrppDlciCfgEncap_Object = MibTableColumn
mpFrppDlciCfgEncap = _MpFrppDlciCfgEncap_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 20),
    _MpFrppDlciCfgEncap_Type()
)
mpFrppDlciCfgEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgEncap.setStatus("mandatory")


class _MpFrppDlciCfgDe_Type(Integer32):
    """Custom type mpFrppDlciCfgDe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MpFrppDlciCfgDe_Type.__name__ = "Integer32"
_MpFrppDlciCfgDe_Object = MibTableColumn
mpFrppDlciCfgDe = _MpFrppDlciCfgDe_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 21),
    _MpFrppDlciCfgDe_Type()
)
mpFrppDlciCfgDe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgDe.setStatus("mandatory")


class _MpFrppDlciCfgPln_Type(Integer32):
    """Custom type mpFrppDlciCfgPln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MpFrppDlciCfgPln_Type.__name__ = "Integer32"
_MpFrppDlciCfgPln_Object = MibTableColumn
mpFrppDlciCfgPln = _MpFrppDlciCfgPln_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 22),
    _MpFrppDlciCfgPln_Type()
)
mpFrppDlciCfgPln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciCfgPln.setStatus("mandatory")


class _MpFrppDlciCfgFragSize_Type(Integer32):
    """Custom type mpFrppDlciCfgFragSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1600),
    )


_MpFrppDlciCfgFragSize_Type.__name__ = "Integer32"
_MpFrppDlciCfgFragSize_Object = MibTableColumn
mpFrppDlciCfgFragSize = _MpFrppDlciCfgFragSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 23),
    _MpFrppDlciCfgFragSize_Type()
)
mpFrppDlciCfgFragSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgFragSize.setStatus("mandatory")


class _MpFrppDlciCfgMir_Type(Integer32):
    """Custom type mpFrppDlciCfgMir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MpFrppDlciCfgMir_Type.__name__ = "Integer32"
_MpFrppDlciCfgMir_Object = MibTableColumn
mpFrppDlciCfgMir = _MpFrppDlciCfgMir_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 24),
    _MpFrppDlciCfgMir_Type()
)
mpFrppDlciCfgMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgMir.setStatus("mandatory")


class _MpFrppDlciCfgPerInc_Type(Integer32):
    """Custom type mpFrppDlciCfgPerInc based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MpFrppDlciCfgPerInc_Type.__name__ = "Integer32"
_MpFrppDlciCfgPerInc_Object = MibTableColumn
mpFrppDlciCfgPerInc = _MpFrppDlciCfgPerInc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 25),
    _MpFrppDlciCfgPerInc_Type()
)
mpFrppDlciCfgPerInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgPerInc.setStatus("mandatory")


class _MpFrppDlciCfgPerDec_Type(Integer32):
    """Custom type mpFrppDlciCfgPerDec based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MpFrppDlciCfgPerDec_Type.__name__ = "Integer32"
_MpFrppDlciCfgPerDec_Object = MibTableColumn
mpFrppDlciCfgPerDec = _MpFrppDlciCfgPerDec_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 26),
    _MpFrppDlciCfgPerDec_Type()
)
mpFrppDlciCfgPerDec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgPerDec.setStatus("mandatory")


class _MpFrppDlciCfgMincir_Type(Integer32):
    """Custom type mpFrppDlciCfgMincir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MpFrppDlciCfgMincir_Type.__name__ = "Integer32"
_MpFrppDlciCfgMincir_Object = MibTableColumn
mpFrppDlciCfgMincir = _MpFrppDlciCfgMincir_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 27),
    _MpFrppDlciCfgMincir_Type()
)
mpFrppDlciCfgMincir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgMincir.setStatus("mandatory")


class _MpFrppDlciCfgCir_Type(Integer32):
    """Custom type mpFrppDlciCfgCir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MpFrppDlciCfgCir_Type.__name__ = "Integer32"
_MpFrppDlciCfgCir_Object = MibTableColumn
mpFrppDlciCfgCir = _MpFrppDlciCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 28),
    _MpFrppDlciCfgCir_Type()
)
mpFrppDlciCfgCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgCir.setStatus("mandatory")


class _MpFrppDlciCfgSnapFlg_Type(Integer32):
    """Custom type mpFrppDlciCfgSnapFlg based on Integer32"""
    defaultValue = 1

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


_MpFrppDlciCfgSnapFlg_Type.__name__ = "Integer32"
_MpFrppDlciCfgSnapFlg_Object = MibTableColumn
mpFrppDlciCfgSnapFlg = _MpFrppDlciCfgSnapFlg_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 29),
    _MpFrppDlciCfgSnapFlg_Type()
)
mpFrppDlciCfgSnapFlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgSnapFlg.setStatus("mandatory")


class _MpFrppDlciQueueLenH_Type(Integer32):
    """Custom type mpFrppDlciQueueLenH based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpFrppDlciQueueLenH_Type.__name__ = "Integer32"
_MpFrppDlciQueueLenH_Object = MibTableColumn
mpFrppDlciQueueLenH = _MpFrppDlciQueueLenH_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 30),
    _MpFrppDlciQueueLenH_Type()
)
mpFrppDlciQueueLenH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueLenH.setStatus("mandatory")


class _MpFrppDlciQueueLenU_Type(Integer32):
    """Custom type mpFrppDlciQueueLenU based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpFrppDlciQueueLenU_Type.__name__ = "Integer32"
_MpFrppDlciQueueLenU_Object = MibTableColumn
mpFrppDlciQueueLenU = _MpFrppDlciQueueLenU_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 31),
    _MpFrppDlciQueueLenU_Type()
)
mpFrppDlciQueueLenU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueLenU.setStatus("mandatory")


class _MpFrppDlciQueueLenL_Type(Integer32):
    """Custom type mpFrppDlciQueueLenL based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpFrppDlciQueueLenL_Type.__name__ = "Integer32"
_MpFrppDlciQueueLenL_Object = MibTableColumn
mpFrppDlciQueueLenL = _MpFrppDlciQueueLenL_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 32),
    _MpFrppDlciQueueLenL_Type()
)
mpFrppDlciQueueLenL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueLenL.setStatus("mandatory")


class _MpFrppDlciQueueLenN_Type(Integer32):
    """Custom type mpFrppDlciQueueLenN based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpFrppDlciQueueLenN_Type.__name__ = "Integer32"
_MpFrppDlciQueueLenN_Object = MibTableColumn
mpFrppDlciQueueLenN = _MpFrppDlciQueueLenN_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 33),
    _MpFrppDlciQueueLenN_Type()
)
mpFrppDlciQueueLenN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueLenN.setStatus("mandatory")


class _MpFrppDlciQueueByteH_Type(Integer32):
    """Custom type mpFrppDlciQueueByteH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpFrppDlciQueueByteH_Type.__name__ = "Integer32"
_MpFrppDlciQueueByteH_Object = MibTableColumn
mpFrppDlciQueueByteH = _MpFrppDlciQueueByteH_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 34),
    _MpFrppDlciQueueByteH_Type()
)
mpFrppDlciQueueByteH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueByteH.setStatus("mandatory")


class _MpFrppDlciQueueByteU_Type(Integer32):
    """Custom type mpFrppDlciQueueByteU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpFrppDlciQueueByteU_Type.__name__ = "Integer32"
_MpFrppDlciQueueByteU_Object = MibTableColumn
mpFrppDlciQueueByteU = _MpFrppDlciQueueByteU_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 35),
    _MpFrppDlciQueueByteU_Type()
)
mpFrppDlciQueueByteU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueByteU.setStatus("mandatory")


class _MpFrppDlciQueueByteL_Type(Integer32):
    """Custom type mpFrppDlciQueueByteL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpFrppDlciQueueByteL_Type.__name__ = "Integer32"
_MpFrppDlciQueueByteL_Object = MibTableColumn
mpFrppDlciQueueByteL = _MpFrppDlciQueueByteL_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 36),
    _MpFrppDlciQueueByteL_Type()
)
mpFrppDlciQueueByteL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueByteL.setStatus("mandatory")


class _MpFrppDlciQueueByteN_Type(Integer32):
    """Custom type mpFrppDlciQueueByteN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpFrppDlciQueueByteN_Type.__name__ = "Integer32"
_MpFrppDlciQueueByteN_Object = MibTableColumn
mpFrppDlciQueueByteN = _MpFrppDlciQueueByteN_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 37),
    _MpFrppDlciQueueByteN_Type()
)
mpFrppDlciQueueByteN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciQueueByteN.setStatus("mandatory")


class _MpFrppDlciIpQosClassAf3_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassAf3 based on Integer32"""
    defaultValue = 2

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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassAf3_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassAf3_Object = MibTableColumn
mpFrppDlciIpQosClassAf3 = _MpFrppDlciIpQosClassAf3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 38),
    _MpFrppDlciIpQosClassAf3_Type()
)
mpFrppDlciIpQosClassAf3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassAf3.setStatus("mandatory")


class _MpFrppDlciIpQosClassAf2_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassAf2 based on Integer32"""
    defaultValue = 3

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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassAf2_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassAf2_Object = MibTableColumn
mpFrppDlciIpQosClassAf2 = _MpFrppDlciIpQosClassAf2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 39),
    _MpFrppDlciIpQosClassAf2_Type()
)
mpFrppDlciIpQosClassAf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassAf2.setStatus("mandatory")


class _MpFrppDlciIpQosClassAf1_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassAf1 based on Integer32"""
    defaultValue = 3

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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassAf1_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassAf1_Object = MibTableColumn
mpFrppDlciIpQosClassAf1 = _MpFrppDlciIpQosClassAf1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 40),
    _MpFrppDlciIpQosClassAf1_Type()
)
mpFrppDlciIpQosClassAf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassAf1.setStatus("mandatory")


class _MpFrppDlciIpQosClassBe_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassBe based on Integer32"""
    defaultValue = 4

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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassBe_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassBe_Object = MibTableColumn
mpFrppDlciIpQosClassBe = _MpFrppDlciIpQosClassBe_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 41),
    _MpFrppDlciIpQosClassBe_Type()
)
mpFrppDlciIpQosClassBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassBe.setStatus("mandatory")


class _MpFrppDlciIpQosClassEf3_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassEf3 based on Integer32"""
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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassEf3_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassEf3_Object = MibTableColumn
mpFrppDlciIpQosClassEf3 = _MpFrppDlciIpQosClassEf3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 42),
    _MpFrppDlciIpQosClassEf3_Type()
)
mpFrppDlciIpQosClassEf3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassEf3.setStatus("mandatory")


class _MpFrppDlciIpQosClassEf2_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassEf2 based on Integer32"""
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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassEf2_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassEf2_Object = MibTableColumn
mpFrppDlciIpQosClassEf2 = _MpFrppDlciIpQosClassEf2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 43),
    _MpFrppDlciIpQosClassEf2_Type()
)
mpFrppDlciIpQosClassEf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassEf2.setStatus("mandatory")


class _MpFrppDlciIpQosClassEf1_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassEf1 based on Integer32"""
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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassEf1_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassEf1_Object = MibTableColumn
mpFrppDlciIpQosClassEf1 = _MpFrppDlciIpQosClassEf1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 44),
    _MpFrppDlciIpQosClassEf1_Type()
)
mpFrppDlciIpQosClassEf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassEf1.setStatus("mandatory")


class _MpFrppDlciIpQosClassAf4_Type(Integer32):
    """Custom type mpFrppDlciIpQosClassAf4 based on Integer32"""
    defaultValue = 2

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
        *(("high", 2),
          ("low", 4),
          ("normal", 3),
          ("urgent", 1))
    )


_MpFrppDlciIpQosClassAf4_Type.__name__ = "Integer32"
_MpFrppDlciIpQosClassAf4_Object = MibTableColumn
mpFrppDlciIpQosClassAf4 = _MpFrppDlciIpQosClassAf4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 45),
    _MpFrppDlciIpQosClassAf4_Type()
)
mpFrppDlciIpQosClassAf4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciIpQosClassAf4.setStatus("mandatory")


class _MpFrppDlciCfgInarpMode_Type(Integer32):
    """Custom type mpFrppDlciCfgInarpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("passive", 2))
    )


_MpFrppDlciCfgInarpMode_Type.__name__ = "Integer32"
_MpFrppDlciCfgInarpMode_Object = MibTableColumn
mpFrppDlciCfgInarpMode = _MpFrppDlciCfgInarpMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 46),
    _MpFrppDlciCfgInarpMode_Type()
)
mpFrppDlciCfgInarpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgInarpMode.setStatus("mandatory")


class _MpFrppDlciCfgTrapFilter_Type(Integer32):
    """Custom type mpFrppDlciCfgTrapFilter based on Integer32"""
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
        *(("down", 3),
          ("no", 1),
          ("up", 2),
          ("up-down", 4))
    )


_MpFrppDlciCfgTrapFilter_Type.__name__ = "Integer32"
_MpFrppDlciCfgTrapFilter_Object = MibTableColumn
mpFrppDlciCfgTrapFilter = _MpFrppDlciCfgTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 47),
    _MpFrppDlciCfgTrapFilter_Type()
)
mpFrppDlciCfgTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppDlciCfgTrapFilter.setStatus("mandatory")
_MpFrppFrppCfgRowStatus_Type = RowStatus
_MpFrppFrppCfgRowStatus_Object = MibTableColumn
mpFrppFrppCfgRowStatus = _MpFrppFrppCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 48),
    _MpFrppFrppCfgRowStatus_Type()
)
mpFrppFrppCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppFrppCfgRowStatus.setStatus("mandatory")


class _MpFrppFrppCfgErrInfo_Type(Integer32):
    """Custom type mpFrppFrppCfgErrInfo based on Integer32"""
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
        *(("badIndexValue", 4),
          ("badValue", 3),
          ("correlationError", 5),
          ("ipAddressNotDeleted", 11),
          ("lowLayerConfigNotRegistered", 9),
          ("mappingDataAlreadyExist", 10),
          ("mbufHuntFailure", 7),
          ("mccIdHuntFailure", 12),
          ("memoryAllocateFailure", 6),
          ("normal", 1),
          ("parameterNotEnough", 2),
          ("relationalConfigExist", 8))
    )


_MpFrppFrppCfgErrInfo_Type.__name__ = "Integer32"
_MpFrppFrppCfgErrInfo_Object = MibTableColumn
mpFrppFrppCfgErrInfo = _MpFrppFrppCfgErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 3, 1, 49),
    _MpFrppFrppCfgErrInfo_Type()
)
mpFrppFrppCfgErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppCfgErrInfo.setStatus("mandatory")
_MpFrppInfoTable_Object = MibTable
mpFrppInfoTable = _MpFrppInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4)
)
if mibBuilder.loadTexts:
    mpFrppInfoTable.setStatus("mandatory")
_MpFrppInfoEntry_Object = MibTableRow
mpFrppInfoEntry = _MpFrppInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1)
)
mpFrppInfoEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppInfoIndex"),
)
if mibBuilder.loadTexts:
    mpFrppInfoEntry.setStatus("mandatory")
_MpFrppInfoIndex_Type = Integer32
_MpFrppInfoIndex_Object = MibTableColumn
mpFrppInfoIndex = _MpFrppInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 1),
    _MpFrppInfoIndex_Type()
)
mpFrppInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoIndex.setStatus("mandatory")


class _MpFrppInfoFrppAdminStatus_Type(Integer32):
    """Custom type mpFrppInfoFrppAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpFrppInfoFrppAdminStatus_Type.__name__ = "Integer32"
_MpFrppInfoFrppAdminStatus_Object = MibTableColumn
mpFrppInfoFrppAdminStatus = _MpFrppInfoFrppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 2),
    _MpFrppInfoFrppAdminStatus_Type()
)
mpFrppInfoFrppAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFrppInfoFrppAdminStatus.setStatus("mandatory")


class _MpFrppInfoFrppOperStatus_Type(Integer32):
    """Custom type mpFrppInfoFrppOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpFrppInfoFrppOperStatus_Type.__name__ = "Integer32"
_MpFrppInfoFrppOperStatus_Object = MibTableColumn
mpFrppInfoFrppOperStatus = _MpFrppInfoFrppOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 3),
    _MpFrppInfoFrppOperStatus_Type()
)
mpFrppInfoFrppOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoFrppOperStatus.setStatus("mandatory")
_MpFrppInfoFrppLastChange_Type = TimeTicks
_MpFrppInfoFrppLastChange_Object = MibTableColumn
mpFrppInfoFrppLastChange = _MpFrppInfoFrppLastChange_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 4),
    _MpFrppInfoFrppLastChange_Type()
)
mpFrppInfoFrppLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoFrppLastChange.setStatus("mandatory")


class _MpFrppInfoDlci_Type(Integer32):
    """Custom type mpFrppInfoDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_MpFrppInfoDlci_Type.__name__ = "Integer32"
_MpFrppInfoDlci_Object = MibTableColumn
mpFrppInfoDlci = _MpFrppInfoDlci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 5),
    _MpFrppInfoDlci_Type()
)
mpFrppInfoDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoDlci.setStatus("mandatory")


class _MpFrppInfoDlciAdminStatus_Type(Integer32):
    """Custom type mpFrppInfoDlciAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpFrppInfoDlciAdminStatus_Type.__name__ = "Integer32"
_MpFrppInfoDlciAdminStatus_Object = MibTableColumn
mpFrppInfoDlciAdminStatus = _MpFrppInfoDlciAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 6),
    _MpFrppInfoDlciAdminStatus_Type()
)
mpFrppInfoDlciAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoDlciAdminStatus.setStatus("mandatory")


class _MpFrppInfoDlciOperStatus_Type(Integer32):
    """Custom type mpFrppInfoDlciOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpFrppInfoDlciOperStatus_Type.__name__ = "Integer32"
_MpFrppInfoDlciOperStatus_Object = MibTableColumn
mpFrppInfoDlciOperStatus = _MpFrppInfoDlciOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 7),
    _MpFrppInfoDlciOperStatus_Type()
)
mpFrppInfoDlciOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoDlciOperStatus.setStatus("mandatory")
_MpFrppInfoDlciLastChange_Type = TimeTicks
_MpFrppInfoDlciLastChange_Object = MibTableColumn
mpFrppInfoDlciLastChange = _MpFrppInfoDlciLastChange_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 8),
    _MpFrppInfoDlciLastChange_Type()
)
mpFrppInfoDlciLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoDlciLastChange.setStatus("mandatory")


class _MpFrppInfoDlciOperDownEvent_Type(Integer32):
    """Custom type mpFrppInfoDlciOperDownEvent based on Integer32"""
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
        *(("dlcidown", 2),
          ("lmiStatusInactiveReceived", 4),
          ("lmierror", 3),
          ("normal", 1),
          ("unknown", 5))
    )


_MpFrppInfoDlciOperDownEvent_Type.__name__ = "Integer32"
_MpFrppInfoDlciOperDownEvent_Object = MibTableColumn
mpFrppInfoDlciOperDownEvent = _MpFrppInfoDlciOperDownEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 4, 1, 9),
    _MpFrppInfoDlciOperDownEvent_Type()
)
mpFrppInfoDlciOperDownEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppInfoDlciOperDownEvent.setStatus("mandatory")
_MpFrppMccIdStatTable_Object = MibTable
mpFrppMccIdStatTable = _MpFrppMccIdStatTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5)
)
if mibBuilder.loadTexts:
    mpFrppMccIdStatTable.setStatus("mandatory")
_MpFrppMccIdStatEntry_Object = MibTableRow
mpFrppMccIdStatEntry = _MpFrppMccIdStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1)
)
mpFrppMccIdStatEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppMccIdStatIfIndex"),
)
if mibBuilder.loadTexts:
    mpFrppMccIdStatEntry.setStatus("mandatory")
_MpFrppMccIdStatIfIndex_Type = Integer32
_MpFrppMccIdStatIfIndex_Object = MibTableColumn
mpFrppMccIdStatIfIndex = _MpFrppMccIdStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 1),
    _MpFrppMccIdStatIfIndex_Type()
)
mpFrppMccIdStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdStatIfIndex.setStatus("mandatory")
_MpFrppMccIdRcvOctets_Type = Counter32
_MpFrppMccIdRcvOctets_Object = MibTableColumn
mpFrppMccIdRcvOctets = _MpFrppMccIdRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 2),
    _MpFrppMccIdRcvOctets_Type()
)
mpFrppMccIdRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvOctets.setStatus("mandatory")
_MpFrppMccIdRcvFrames_Type = Counter32
_MpFrppMccIdRcvFrames_Object = MibTableColumn
mpFrppMccIdRcvFrames = _MpFrppMccIdRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 3),
    _MpFrppMccIdRcvFrames_Type()
)
mpFrppMccIdRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvFrames.setStatus("mandatory")
_MpFrppMccIdRcvFrameMinSize_Type = Integer32
_MpFrppMccIdRcvFrameMinSize_Object = MibTableColumn
mpFrppMccIdRcvFrameMinSize = _MpFrppMccIdRcvFrameMinSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 4),
    _MpFrppMccIdRcvFrameMinSize_Type()
)
mpFrppMccIdRcvFrameMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvFrameMinSize.setStatus("mandatory")
_MpFrppMccIdRcvFrameMaxSize_Type = Integer32
_MpFrppMccIdRcvFrameMaxSize_Object = MibTableColumn
mpFrppMccIdRcvFrameMaxSize = _MpFrppMccIdRcvFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 5),
    _MpFrppMccIdRcvFrameMaxSize_Type()
)
mpFrppMccIdRcvFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvFrameMaxSize.setStatus("mandatory")
_MpFrppMccIdRcvDiscardFrames_Type = Counter32
_MpFrppMccIdRcvDiscardFrames_Object = MibTableColumn
mpFrppMccIdRcvDiscardFrames = _MpFrppMccIdRcvDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 6),
    _MpFrppMccIdRcvDiscardFrames_Type()
)
mpFrppMccIdRcvDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvDiscardFrames.setStatus("mandatory")
_MpFrppMccIdRcvFecnFrames_Type = Counter32
_MpFrppMccIdRcvFecnFrames_Object = MibTableColumn
mpFrppMccIdRcvFecnFrames = _MpFrppMccIdRcvFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 7),
    _MpFrppMccIdRcvFecnFrames_Type()
)
mpFrppMccIdRcvFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvFecnFrames.setStatus("mandatory")
_MpFrppMccIdRcvBecnFrames_Type = Counter32
_MpFrppMccIdRcvBecnFrames_Object = MibTableColumn
mpFrppMccIdRcvBecnFrames = _MpFrppMccIdRcvBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 8),
    _MpFrppMccIdRcvBecnFrames_Type()
)
mpFrppMccIdRcvBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvBecnFrames.setStatus("mandatory")
_MpFrppMccIdRcvDeFrames_Type = Counter32
_MpFrppMccIdRcvDeFrames_Object = MibTableColumn
mpFrppMccIdRcvDeFrames = _MpFrppMccIdRcvDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 9),
    _MpFrppMccIdRcvDeFrames_Type()
)
mpFrppMccIdRcvDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvDeFrames.setStatus("mandatory")
_MpFrppMccIdRcvInvalidFrames_Type = Counter32
_MpFrppMccIdRcvInvalidFrames_Object = MibTableColumn
mpFrppMccIdRcvInvalidFrames = _MpFrppMccIdRcvInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 10),
    _MpFrppMccIdRcvInvalidFrames_Type()
)
mpFrppMccIdRcvInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvInvalidFrames.setStatus("mandatory")
_MpFrppMccIdRcvLongFrames_Type = Counter32
_MpFrppMccIdRcvLongFrames_Object = MibTableColumn
mpFrppMccIdRcvLongFrames = _MpFrppMccIdRcvLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 11),
    _MpFrppMccIdRcvLongFrames_Type()
)
mpFrppMccIdRcvLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvLongFrames.setStatus("mandatory")
_MpFrppMccIdRcvShortFrames_Type = Counter32
_MpFrppMccIdRcvShortFrames_Object = MibTableColumn
mpFrppMccIdRcvShortFrames = _MpFrppMccIdRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 12),
    _MpFrppMccIdRcvShortFrames_Type()
)
mpFrppMccIdRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvShortFrames.setStatus("mandatory")
_MpFrppMccIdXmtOctets_Type = Counter32
_MpFrppMccIdXmtOctets_Object = MibTableColumn
mpFrppMccIdXmtOctets = _MpFrppMccIdXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 13),
    _MpFrppMccIdXmtOctets_Type()
)
mpFrppMccIdXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtOctets.setStatus("mandatory")
_MpFrppMccIdXmtFrames_Type = Counter32
_MpFrppMccIdXmtFrames_Object = MibTableColumn
mpFrppMccIdXmtFrames = _MpFrppMccIdXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 14),
    _MpFrppMccIdXmtFrames_Type()
)
mpFrppMccIdXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtFrames.setStatus("mandatory")
_MpFrppMccIdXmtFrameMinSize_Type = Integer32
_MpFrppMccIdXmtFrameMinSize_Object = MibTableColumn
mpFrppMccIdXmtFrameMinSize = _MpFrppMccIdXmtFrameMinSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 15),
    _MpFrppMccIdXmtFrameMinSize_Type()
)
mpFrppMccIdXmtFrameMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtFrameMinSize.setStatus("mandatory")
_MpFrppMccIdXmtFrameMaxSize_Type = Integer32
_MpFrppMccIdXmtFrameMaxSize_Object = MibTableColumn
mpFrppMccIdXmtFrameMaxSize = _MpFrppMccIdXmtFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 16),
    _MpFrppMccIdXmtFrameMaxSize_Type()
)
mpFrppMccIdXmtFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtFrameMaxSize.setStatus("mandatory")
_MpFrppMccIdXmtDiscardFrames_Type = Counter32
_MpFrppMccIdXmtDiscardFrames_Object = MibTableColumn
mpFrppMccIdXmtDiscardFrames = _MpFrppMccIdXmtDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 17),
    _MpFrppMccIdXmtDiscardFrames_Type()
)
mpFrppMccIdXmtDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtDiscardFrames.setStatus("mandatory")
_MpFrppMccIdXmtFecnFrames_Type = Counter32
_MpFrppMccIdXmtFecnFrames_Object = MibTableColumn
mpFrppMccIdXmtFecnFrames = _MpFrppMccIdXmtFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 18),
    _MpFrppMccIdXmtFecnFrames_Type()
)
mpFrppMccIdXmtFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtFecnFrames.setStatus("mandatory")
_MpFrppMccIdXmtBecnFrames_Type = Counter32
_MpFrppMccIdXmtBecnFrames_Object = MibTableColumn
mpFrppMccIdXmtBecnFrames = _MpFrppMccIdXmtBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 19),
    _MpFrppMccIdXmtBecnFrames_Type()
)
mpFrppMccIdXmtBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtBecnFrames.setStatus("mandatory")
_MpFrppMccIdXmtDeFrames_Type = Counter32
_MpFrppMccIdXmtDeFrames_Object = MibTableColumn
mpFrppMccIdXmtDeFrames = _MpFrppMccIdXmtDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 20),
    _MpFrppMccIdXmtDeFrames_Type()
)
mpFrppMccIdXmtDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtDeFrames.setStatus("mandatory")
_MpFrppMccIdRcvCllmFrames_Type = Counter32
_MpFrppMccIdRcvCllmFrames_Object = MibTableColumn
mpFrppMccIdRcvCllmFrames = _MpFrppMccIdRcvCllmFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 5, 1, 21),
    _MpFrppMccIdRcvCllmFrames_Type()
)
mpFrppMccIdRcvCllmFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvCllmFrames.setStatus("mandatory")
_MpFrppMccIdLmiStatTable_Object = MibTable
mpFrppMccIdLmiStatTable = _MpFrppMccIdLmiStatTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6)
)
if mibBuilder.loadTexts:
    mpFrppMccIdLmiStatTable.setStatus("mandatory")
_MpFrppMccIdLmiStatEntry_Object = MibTableRow
mpFrppMccIdLmiStatEntry = _MpFrppMccIdLmiStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1)
)
mpFrppMccIdLmiStatEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppMccIdLmiStatIfIndex"),
)
if mibBuilder.loadTexts:
    mpFrppMccIdLmiStatEntry.setStatus("mandatory")
_MpFrppMccIdLmiStatIfIndex_Type = Integer32
_MpFrppMccIdLmiStatIfIndex_Object = MibTableColumn
mpFrppMccIdLmiStatIfIndex = _MpFrppMccIdLmiStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 1),
    _MpFrppMccIdLmiStatIfIndex_Type()
)
mpFrppMccIdLmiStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdLmiStatIfIndex.setStatus("mandatory")
_MpFrppMccIdRcvLmiStatEnqs_Type = Counter32
_MpFrppMccIdRcvLmiStatEnqs_Object = MibTableColumn
mpFrppMccIdRcvLmiStatEnqs = _MpFrppMccIdRcvLmiStatEnqs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 2),
    _MpFrppMccIdRcvLmiStatEnqs_Type()
)
mpFrppMccIdRcvLmiStatEnqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvLmiStatEnqs.setStatus("mandatory")
_MpFrppMccIdXmtLmiStatEnqs_Type = Counter32
_MpFrppMccIdXmtLmiStatEnqs_Object = MibTableColumn
mpFrppMccIdXmtLmiStatEnqs = _MpFrppMccIdXmtLmiStatEnqs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 3),
    _MpFrppMccIdXmtLmiStatEnqs_Type()
)
mpFrppMccIdXmtLmiStatEnqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtLmiStatEnqs.setStatus("mandatory")
_MpFrppMccIdRcvLmiStats_Type = Counter32
_MpFrppMccIdRcvLmiStats_Object = MibTableColumn
mpFrppMccIdRcvLmiStats = _MpFrppMccIdRcvLmiStats_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 4),
    _MpFrppMccIdRcvLmiStats_Type()
)
mpFrppMccIdRcvLmiStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvLmiStats.setStatus("mandatory")
_MpFrppMccIdXmtLmiStats_Type = Counter32
_MpFrppMccIdXmtLmiStats_Object = MibTableColumn
mpFrppMccIdXmtLmiStats = _MpFrppMccIdXmtLmiStats_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 5),
    _MpFrppMccIdXmtLmiStats_Type()
)
mpFrppMccIdXmtLmiStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdXmtLmiStats.setStatus("mandatory")
_MpFrppMccIdUsrLmiLinkRelErrs_Type = Counter32
_MpFrppMccIdUsrLmiLinkRelErrs_Object = MibTableColumn
mpFrppMccIdUsrLmiLinkRelErrs = _MpFrppMccIdUsrLmiLinkRelErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 6),
    _MpFrppMccIdUsrLmiLinkRelErrs_Type()
)
mpFrppMccIdUsrLmiLinkRelErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdUsrLmiLinkRelErrs.setStatus("mandatory")
_MpFrppMccIdUsrLmiT391Tos_Type = Counter32
_MpFrppMccIdUsrLmiT391Tos_Object = MibTableColumn
mpFrppMccIdUsrLmiT391Tos = _MpFrppMccIdUsrLmiT391Tos_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 7),
    _MpFrppMccIdUsrLmiT391Tos_Type()
)
mpFrppMccIdUsrLmiT391Tos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdUsrLmiT391Tos.setStatus("mandatory")
_MpFrppMccIdUsrLmiSeqErrs_Type = Counter32
_MpFrppMccIdUsrLmiSeqErrs_Object = MibTableColumn
mpFrppMccIdUsrLmiSeqErrs = _MpFrppMccIdUsrLmiSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 8),
    _MpFrppMccIdUsrLmiSeqErrs_Type()
)
mpFrppMccIdUsrLmiSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdUsrLmiSeqErrs.setStatus("mandatory")
_MpFrppMccIdUsrLmiProtErrs_Type = Counter32
_MpFrppMccIdUsrLmiProtErrs_Object = MibTableColumn
mpFrppMccIdUsrLmiProtErrs = _MpFrppMccIdUsrLmiProtErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 9),
    _MpFrppMccIdUsrLmiProtErrs_Type()
)
mpFrppMccIdUsrLmiProtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdUsrLmiProtErrs.setStatus("mandatory")
_MpFrppMccIdUsrLmiChInacts_Type = Counter32
_MpFrppMccIdUsrLmiChInacts_Object = MibTableColumn
mpFrppMccIdUsrLmiChInacts = _MpFrppMccIdUsrLmiChInacts_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 10),
    _MpFrppMccIdUsrLmiChInacts_Type()
)
mpFrppMccIdUsrLmiChInacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdUsrLmiChInacts.setStatus("mandatory")
_MpFrppMccIdNetLmiLinkRelErrs_Type = Counter32
_MpFrppMccIdNetLmiLinkRelErrs_Object = MibTableColumn
mpFrppMccIdNetLmiLinkRelErrs = _MpFrppMccIdNetLmiLinkRelErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 11),
    _MpFrppMccIdNetLmiLinkRelErrs_Type()
)
mpFrppMccIdNetLmiLinkRelErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdNetLmiLinkRelErrs.setStatus("mandatory")
_MpFrppMccIdNetLmiT392Tos_Type = Counter32
_MpFrppMccIdNetLmiT392Tos_Object = MibTableColumn
mpFrppMccIdNetLmiT392Tos = _MpFrppMccIdNetLmiT392Tos_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 12),
    _MpFrppMccIdNetLmiT392Tos_Type()
)
mpFrppMccIdNetLmiT392Tos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdNetLmiT392Tos.setStatus("mandatory")
_MpFrppMccIdNetLmiSeqErrs_Type = Counter32
_MpFrppMccIdNetLmiSeqErrs_Object = MibTableColumn
mpFrppMccIdNetLmiSeqErrs = _MpFrppMccIdNetLmiSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 13),
    _MpFrppMccIdNetLmiSeqErrs_Type()
)
mpFrppMccIdNetLmiSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdNetLmiSeqErrs.setStatus("mandatory")
_MpFrppMccIdNetLmiErrs_Type = Counter32
_MpFrppMccIdNetLmiErrs_Object = MibTableColumn
mpFrppMccIdNetLmiErrs = _MpFrppMccIdNetLmiErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 14),
    _MpFrppMccIdNetLmiErrs_Type()
)
mpFrppMccIdNetLmiErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdNetLmiErrs.setStatus("mandatory")
_MpFrppMccIdNetChInacts_Type = Counter32
_MpFrppMccIdNetChInacts_Object = MibTableColumn
mpFrppMccIdNetChInacts = _MpFrppMccIdNetChInacts_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 15),
    _MpFrppMccIdNetChInacts_Type()
)
mpFrppMccIdNetChInacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdNetChInacts.setStatus("mandatory")
_MpFrppMccIdRcvAsyncFrms_Type = Counter32
_MpFrppMccIdRcvAsyncFrms_Object = MibTableColumn
mpFrppMccIdRcvAsyncFrms = _MpFrppMccIdRcvAsyncFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 6, 1, 16),
    _MpFrppMccIdRcvAsyncFrms_Type()
)
mpFrppMccIdRcvAsyncFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppMccIdRcvAsyncFrms.setStatus("mandatory")
_MpFrppFrppStatTable_Object = MibTable
mpFrppFrppStatTable = _MpFrppFrppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7)
)
if mibBuilder.loadTexts:
    mpFrppFrppStatTable.setStatus("mandatory")
_MpFrppFrppStatEntry_Object = MibTableRow
mpFrppFrppStatEntry = _MpFrppFrppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1)
)
mpFrppFrppStatEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppFrppStatIndex"),
)
if mibBuilder.loadTexts:
    mpFrppFrppStatEntry.setStatus("mandatory")
_MpFrppFrppStatIndex_Type = Integer32
_MpFrppFrppStatIndex_Object = MibTableColumn
mpFrppFrppStatIndex = _MpFrppFrppStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 1),
    _MpFrppFrppStatIndex_Type()
)
mpFrppFrppStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatIndex.setStatus("mandatory")
_MpFrppFrppStatRcvFrames_Type = Counter32
_MpFrppFrppStatRcvFrames_Object = MibTableColumn
mpFrppFrppStatRcvFrames = _MpFrppFrppStatRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 2),
    _MpFrppFrppStatRcvFrames_Type()
)
mpFrppFrppStatRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatRcvFrames.setStatus("mandatory")
_MpFrppFrppStatXmtFrames_Type = Counter32
_MpFrppFrppStatXmtFrames_Object = MibTableColumn
mpFrppFrppStatXmtFrames = _MpFrppFrppStatXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 3),
    _MpFrppFrppStatXmtFrames_Type()
)
mpFrppFrppStatXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatXmtFrames.setStatus("mandatory")
_MpFrppFrppStatRcvDiscardFrames_Type = Counter32
_MpFrppFrppStatRcvDiscardFrames_Object = MibTableColumn
mpFrppFrppStatRcvDiscardFrames = _MpFrppFrppStatRcvDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 4),
    _MpFrppFrppStatRcvDiscardFrames_Type()
)
mpFrppFrppStatRcvDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatRcvDiscardFrames.setStatus("mandatory")
_MpFrppFrppStatXmtDiscardFrames_Type = Counter32
_MpFrppFrppStatXmtDiscardFrames_Object = MibTableColumn
mpFrppFrppStatXmtDiscardFrames = _MpFrppFrppStatXmtDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 5),
    _MpFrppFrppStatXmtDiscardFrames_Type()
)
mpFrppFrppStatXmtDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatXmtDiscardFrames.setStatus("mandatory")
_MpFrppFrppStatRcvEncapErrors_Type = Counter32
_MpFrppFrppStatRcvEncapErrors_Object = MibTableColumn
mpFrppFrppStatRcvEncapErrors = _MpFrppFrppStatRcvEncapErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 6),
    _MpFrppFrppStatRcvEncapErrors_Type()
)
mpFrppFrppStatRcvEncapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatRcvEncapErrors.setStatus("mandatory")
_MpFrppFrppStatXmtEncapErrors_Type = Counter32
_MpFrppFrppStatXmtEncapErrors_Object = MibTableColumn
mpFrppFrppStatXmtEncapErrors = _MpFrppFrppStatXmtEncapErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 7),
    _MpFrppFrppStatXmtEncapErrors_Type()
)
mpFrppFrppStatXmtEncapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatXmtEncapErrors.setStatus("mandatory")
_MpFrppFrppStatRcvArpTransErrors_Type = Counter32
_MpFrppFrppStatRcvArpTransErrors_Object = MibTableColumn
mpFrppFrppStatRcvArpTransErrors = _MpFrppFrppStatRcvArpTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 8),
    _MpFrppFrppStatRcvArpTransErrors_Type()
)
mpFrppFrppStatRcvArpTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatRcvArpTransErrors.setStatus("mandatory")
_MpFrppFrppStatXmtArpTransErrors_Type = Counter32
_MpFrppFrppStatXmtArpTransErrors_Object = MibTableColumn
mpFrppFrppStatXmtArpTransErrors = _MpFrppFrppStatXmtArpTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 9),
    _MpFrppFrppStatXmtArpTransErrors_Type()
)
mpFrppFrppStatXmtArpTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatXmtArpTransErrors.setStatus("mandatory")
_MpFrppFrppStatReassembleErrors_Type = Counter32
_MpFrppFrppStatReassembleErrors_Object = MibTableColumn
mpFrppFrppStatReassembleErrors = _MpFrppFrppStatReassembleErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 10),
    _MpFrppFrppStatReassembleErrors_Type()
)
mpFrppFrppStatReassembleErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatReassembleErrors.setStatus("mandatory")
_MpFrppFrppStatPriorityQueues_Type = Counter32
_MpFrppFrppStatPriorityQueues_Object = MibTableColumn
mpFrppFrppStatPriorityQueues = _MpFrppFrppStatPriorityQueues_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 11),
    _MpFrppFrppStatPriorityQueues_Type()
)
mpFrppFrppStatPriorityQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatPriorityQueues.setStatus("mandatory")
_MpFrppFrppStatPriorityBytes_Type = Counter32
_MpFrppFrppStatPriorityBytes_Object = MibTableColumn
mpFrppFrppStatPriorityBytes = _MpFrppFrppStatPriorityBytes_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 7, 1, 12),
    _MpFrppFrppStatPriorityBytes_Type()
)
mpFrppFrppStatPriorityBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppFrppStatPriorityBytes.setStatus("mandatory")
_MpFrppDlcStatTable_Object = MibTable
mpFrppDlcStatTable = _MpFrppDlcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8)
)
if mibBuilder.loadTexts:
    mpFrppDlcStatTable.setStatus("mandatory")
_MpFrppDlcStatEntry_Object = MibTableRow
mpFrppDlcStatEntry = _MpFrppDlcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1)
)
mpFrppDlcStatEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppDlciStatIfIndex"),
)
if mibBuilder.loadTexts:
    mpFrppDlcStatEntry.setStatus("mandatory")
_MpFrppDlciStatIfIndex_Type = Integer32
_MpFrppDlciStatIfIndex_Object = MibTableColumn
mpFrppDlciStatIfIndex = _MpFrppDlciStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 1),
    _MpFrppDlciStatIfIndex_Type()
)
mpFrppDlciStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatIfIndex.setStatus("mandatory")
_MpFrppDlciStatRcvOctets_Type = Counter32
_MpFrppDlciStatRcvOctets_Object = MibTableColumn
mpFrppDlciStatRcvOctets = _MpFrppDlciStatRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 2),
    _MpFrppDlciStatRcvOctets_Type()
)
mpFrppDlciStatRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvOctets.setStatus("mandatory")
_MpFrppDlciStatRcvFrames_Type = Counter32
_MpFrppDlciStatRcvFrames_Object = MibTableColumn
mpFrppDlciStatRcvFrames = _MpFrppDlciStatRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 3),
    _MpFrppDlciStatRcvFrames_Type()
)
mpFrppDlciStatRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvFrames.setStatus("mandatory")
_MpFrppDlciStatRcvFrameMinSize_Type = Integer32
_MpFrppDlciStatRcvFrameMinSize_Object = MibTableColumn
mpFrppDlciStatRcvFrameMinSize = _MpFrppDlciStatRcvFrameMinSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 4),
    _MpFrppDlciStatRcvFrameMinSize_Type()
)
mpFrppDlciStatRcvFrameMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvFrameMinSize.setStatus("mandatory")
_MpFrppDlciStatRcvFrameMaxSize_Type = Integer32
_MpFrppDlciStatRcvFrameMaxSize_Object = MibTableColumn
mpFrppDlciStatRcvFrameMaxSize = _MpFrppDlciStatRcvFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 5),
    _MpFrppDlciStatRcvFrameMaxSize_Type()
)
mpFrppDlciStatRcvFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvFrameMaxSize.setStatus("mandatory")
_MpFrppDlciStatRcvFECNFrames_Type = Counter32
_MpFrppDlciStatRcvFECNFrames_Object = MibTableColumn
mpFrppDlciStatRcvFECNFrames = _MpFrppDlciStatRcvFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 6),
    _MpFrppDlciStatRcvFECNFrames_Type()
)
mpFrppDlciStatRcvFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvFECNFrames.setStatus("mandatory")
_MpFrppDlciStatRcvBECNFrames_Type = Counter32
_MpFrppDlciStatRcvBECNFrames_Object = MibTableColumn
mpFrppDlciStatRcvBECNFrames = _MpFrppDlciStatRcvBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 7),
    _MpFrppDlciStatRcvBECNFrames_Type()
)
mpFrppDlciStatRcvBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvBECNFrames.setStatus("mandatory")
_MpFrppDlciStatRcvDEFrames_Type = Counter32
_MpFrppDlciStatRcvDEFrames_Object = MibTableColumn
mpFrppDlciStatRcvDEFrames = _MpFrppDlciStatRcvDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 8),
    _MpFrppDlciStatRcvDEFrames_Type()
)
mpFrppDlciStatRcvDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvDEFrames.setStatus("mandatory")
_MpFrppDlciStatRcvTaggedDEFrames_Type = Counter32
_MpFrppDlciStatRcvTaggedDEFrames_Object = MibTableColumn
mpFrppDlciStatRcvTaggedDEFrames = _MpFrppDlciStatRcvTaggedDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 9),
    _MpFrppDlciStatRcvTaggedDEFrames_Type()
)
mpFrppDlciStatRcvTaggedDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvTaggedDEFrames.setStatus("mandatory")
_MpFrppDlciStatXmtOctets_Type = Counter32
_MpFrppDlciStatXmtOctets_Object = MibTableColumn
mpFrppDlciStatXmtOctets = _MpFrppDlciStatXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 10),
    _MpFrppDlciStatXmtOctets_Type()
)
mpFrppDlciStatXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtOctets.setStatus("mandatory")
_MpFrppDlciStatXmtFrames_Type = Counter32
_MpFrppDlciStatXmtFrames_Object = MibTableColumn
mpFrppDlciStatXmtFrames = _MpFrppDlciStatXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 11),
    _MpFrppDlciStatXmtFrames_Type()
)
mpFrppDlciStatXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtFrames.setStatus("mandatory")
_MpFrppDlciStatXmtFrameMinSize_Type = Integer32
_MpFrppDlciStatXmtFrameMinSize_Object = MibTableColumn
mpFrppDlciStatXmtFrameMinSize = _MpFrppDlciStatXmtFrameMinSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 12),
    _MpFrppDlciStatXmtFrameMinSize_Type()
)
mpFrppDlciStatXmtFrameMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtFrameMinSize.setStatus("mandatory")
_MpFrppDlciStatXmtFrameMaxSize_Type = Integer32
_MpFrppDlciStatXmtFrameMaxSize_Object = MibTableColumn
mpFrppDlciStatXmtFrameMaxSize = _MpFrppDlciStatXmtFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 13),
    _MpFrppDlciStatXmtFrameMaxSize_Type()
)
mpFrppDlciStatXmtFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtFrameMaxSize.setStatus("mandatory")
_MpFrppDlciStatXmtDEDiscardFrames_Type = Counter32
_MpFrppDlciStatXmtDEDiscardFrames_Object = MibTableColumn
mpFrppDlciStatXmtDEDiscardFrames = _MpFrppDlciStatXmtDEDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 14),
    _MpFrppDlciStatXmtDEDiscardFrames_Type()
)
mpFrppDlciStatXmtDEDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtDEDiscardFrames.setStatus("mandatory")
_MpFrppDlciStatXmtFECNFrames_Type = Counter32
_MpFrppDlciStatXmtFECNFrames_Object = MibTableColumn
mpFrppDlciStatXmtFECNFrames = _MpFrppDlciStatXmtFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 15),
    _MpFrppDlciStatXmtFECNFrames_Type()
)
mpFrppDlciStatXmtFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtFECNFrames.setStatus("mandatory")
_MpFrppDlciStatXmtBECNFrames_Type = Counter32
_MpFrppDlciStatXmtBECNFrames_Object = MibTableColumn
mpFrppDlciStatXmtBECNFrames = _MpFrppDlciStatXmtBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 16),
    _MpFrppDlciStatXmtBECNFrames_Type()
)
mpFrppDlciStatXmtBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtBECNFrames.setStatus("mandatory")
_MpFrppDlciStatXmtDEFrames_Type = Counter32
_MpFrppDlciStatXmtDEFrames_Object = MibTableColumn
mpFrppDlciStatXmtDEFrames = _MpFrppDlciStatXmtDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 17),
    _MpFrppDlciStatXmtDEFrames_Type()
)
mpFrppDlciStatXmtDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtDEFrames.setStatus("mandatory")
_MpFrppDlciStatXmtTaggedDEFrames_Type = Counter32
_MpFrppDlciStatXmtTaggedDEFrames_Object = MibTableColumn
mpFrppDlciStatXmtTaggedDEFrames = _MpFrppDlciStatXmtTaggedDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 18),
    _MpFrppDlciStatXmtTaggedDEFrames_Type()
)
mpFrppDlciStatXmtTaggedDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtTaggedDEFrames.setStatus("mandatory")
_MpFrppDlciStatRcvInArpReqFrms_Type = Counter32
_MpFrppDlciStatRcvInArpReqFrms_Object = MibTableColumn
mpFrppDlciStatRcvInArpReqFrms = _MpFrppDlciStatRcvInArpReqFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 19),
    _MpFrppDlciStatRcvInArpReqFrms_Type()
)
mpFrppDlciStatRcvInArpReqFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvInArpReqFrms.setStatus("mandatory")
_MpFrppDlciStatXmtInArpReqFrms_Type = Counter32
_MpFrppDlciStatXmtInArpReqFrms_Object = MibTableColumn
mpFrppDlciStatXmtInArpReqFrms = _MpFrppDlciStatXmtInArpReqFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 20),
    _MpFrppDlciStatXmtInArpReqFrms_Type()
)
mpFrppDlciStatXmtInArpReqFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtInArpReqFrms.setStatus("mandatory")
_MpFrppDlciStatRcvInArpRlyFrms_Type = Counter32
_MpFrppDlciStatRcvInArpRlyFrms_Object = MibTableColumn
mpFrppDlciStatRcvInArpRlyFrms = _MpFrppDlciStatRcvInArpRlyFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 21),
    _MpFrppDlciStatRcvInArpRlyFrms_Type()
)
mpFrppDlciStatRcvInArpRlyFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvInArpRlyFrms.setStatus("mandatory")
_MpFrppDlciStatXmtInArpRlyFrms_Type = Counter32
_MpFrppDlciStatXmtInArpRlyFrms_Object = MibTableColumn
mpFrppDlciStatXmtInArpRlyFrms = _MpFrppDlciStatXmtInArpRlyFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 22),
    _MpFrppDlciStatXmtInArpRlyFrms_Type()
)
mpFrppDlciStatXmtInArpRlyFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtInArpRlyFrms.setStatus("mandatory")
_MpFrppDlciStatFNUnrecognizHeaders_Type = Counter32
_MpFrppDlciStatFNUnrecognizHeaders_Object = MibTableColumn
mpFrppDlciStatFNUnrecognizHeaders = _MpFrppDlciStatFNUnrecognizHeaders_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 23),
    _MpFrppDlciStatFNUnrecognizHeaders_Type()
)
mpFrppDlciStatFNUnrecognizHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatFNUnrecognizHeaders.setStatus("mandatory")
_MpFrppDlciStatNFUnrecognizHeaders_Type = Counter32
_MpFrppDlciStatNFUnrecognizHeaders_Object = MibTableColumn
mpFrppDlciStatNFUnrecognizHeaders = _MpFrppDlciStatNFUnrecognizHeaders_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 24),
    _MpFrppDlciStatNFUnrecognizHeaders_Type()
)
mpFrppDlciStatNFUnrecognizHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatNFUnrecognizHeaders.setStatus("mandatory")
_MpFrppDlciStatFNArpTranslationErrs_Type = Counter32
_MpFrppDlciStatFNArpTranslationErrs_Object = MibTableColumn
mpFrppDlciStatFNArpTranslationErrs = _MpFrppDlciStatFNArpTranslationErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 25),
    _MpFrppDlciStatFNArpTranslationErrs_Type()
)
mpFrppDlciStatFNArpTranslationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatFNArpTranslationErrs.setStatus("mandatory")
_MpFrppDlciStatNFArpTranslationErrs_Type = Counter32
_MpFrppDlciStatNFArpTranslationErrs_Object = MibTableColumn
mpFrppDlciStatNFArpTranslationErrs = _MpFrppDlciStatNFArpTranslationErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 26),
    _MpFrppDlciStatNFArpTranslationErrs_Type()
)
mpFrppDlciStatNFArpTranslationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatNFArpTranslationErrs.setStatus("mandatory")
_MpFrppDlciStatXmtVQFrms_Type = Counter32
_MpFrppDlciStatXmtVQFrms_Object = MibTableColumn
mpFrppDlciStatXmtVQFrms = _MpFrppDlciStatXmtVQFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 27),
    _MpFrppDlciStatXmtVQFrms_Type()
)
mpFrppDlciStatXmtVQFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtVQFrms.setStatus("mandatory")
_MpFrppDlciStatXmtUQFrms_Type = Counter32
_MpFrppDlciStatXmtUQFrms_Object = MibTableColumn
mpFrppDlciStatXmtUQFrms = _MpFrppDlciStatXmtUQFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 28),
    _MpFrppDlciStatXmtUQFrms_Type()
)
mpFrppDlciStatXmtUQFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtUQFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedUQLenFrms_Type = Counter32
_MpFrppDlciStatXmtXceedUQLenFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedUQLenFrms = _MpFrppDlciStatXmtXceedUQLenFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 29),
    _MpFrppDlciStatXmtXceedUQLenFrms_Type()
)
mpFrppDlciStatXmtXceedUQLenFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedUQLenFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedUQByteFrms_Type = Counter32
_MpFrppDlciStatXmtXceedUQByteFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedUQByteFrms = _MpFrppDlciStatXmtXceedUQByteFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 30),
    _MpFrppDlciStatXmtXceedUQByteFrms_Type()
)
mpFrppDlciStatXmtXceedUQByteFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedUQByteFrms.setStatus("mandatory")
_MpFrppDlciStatXmtHQFrms_Type = Counter32
_MpFrppDlciStatXmtHQFrms_Object = MibTableColumn
mpFrppDlciStatXmtHQFrms = _MpFrppDlciStatXmtHQFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 31),
    _MpFrppDlciStatXmtHQFrms_Type()
)
mpFrppDlciStatXmtHQFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtHQFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedHQLenFrms_Type = Counter32
_MpFrppDlciStatXmtXceedHQLenFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedHQLenFrms = _MpFrppDlciStatXmtXceedHQLenFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 32),
    _MpFrppDlciStatXmtXceedHQLenFrms_Type()
)
mpFrppDlciStatXmtXceedHQLenFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedHQLenFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedHQByteFrms_Type = Counter32
_MpFrppDlciStatXmtXceedHQByteFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedHQByteFrms = _MpFrppDlciStatXmtXceedHQByteFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 33),
    _MpFrppDlciStatXmtXceedHQByteFrms_Type()
)
mpFrppDlciStatXmtXceedHQByteFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedHQByteFrms.setStatus("mandatory")
_MpFrppDlciStatXmtNQFrms_Type = Counter32
_MpFrppDlciStatXmtNQFrms_Object = MibTableColumn
mpFrppDlciStatXmtNQFrms = _MpFrppDlciStatXmtNQFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 34),
    _MpFrppDlciStatXmtNQFrms_Type()
)
mpFrppDlciStatXmtNQFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtNQFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedNQLenFrms_Type = Counter32
_MpFrppDlciStatXmtXceedNQLenFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedNQLenFrms = _MpFrppDlciStatXmtXceedNQLenFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 35),
    _MpFrppDlciStatXmtXceedNQLenFrms_Type()
)
mpFrppDlciStatXmtXceedNQLenFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedNQLenFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedNQByteFrms_Type = Counter32
_MpFrppDlciStatXmtXceedNQByteFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedNQByteFrms = _MpFrppDlciStatXmtXceedNQByteFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 36),
    _MpFrppDlciStatXmtXceedNQByteFrms_Type()
)
mpFrppDlciStatXmtXceedNQByteFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedNQByteFrms.setStatus("mandatory")
_MpFrppDlciStatXmtLQFrms_Type = Counter32
_MpFrppDlciStatXmtLQFrms_Object = MibTableColumn
mpFrppDlciStatXmtLQFrms = _MpFrppDlciStatXmtLQFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 37),
    _MpFrppDlciStatXmtLQFrms_Type()
)
mpFrppDlciStatXmtLQFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtLQFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedLQLenFrms_Type = Counter32
_MpFrppDlciStatXmtXceedLQLenFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedLQLenFrms = _MpFrppDlciStatXmtXceedLQLenFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 38),
    _MpFrppDlciStatXmtXceedLQLenFrms_Type()
)
mpFrppDlciStatXmtXceedLQLenFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedLQLenFrms.setStatus("mandatory")
_MpFrppDlciStatXmtXceedLQByteFrms_Type = Counter32
_MpFrppDlciStatXmtXceedLQByteFrms_Object = MibTableColumn
mpFrppDlciStatXmtXceedLQByteFrms = _MpFrppDlciStatXmtXceedLQByteFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 39),
    _MpFrppDlciStatXmtXceedLQByteFrms_Type()
)
mpFrppDlciStatXmtXceedLQByteFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtXceedLQByteFrms.setStatus("mandatory")
_MpFrppDlciStatRcvNPBDe0Frms_Type = Counter32
_MpFrppDlciStatRcvNPBDe0Frms_Object = MibTableColumn
mpFrppDlciStatRcvNPBDe0Frms = _MpFrppDlciStatRcvNPBDe0Frms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 40),
    _MpFrppDlciStatRcvNPBDe0Frms_Type()
)
mpFrppDlciStatRcvNPBDe0Frms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvNPBDe0Frms.setStatus("mandatory")
_MpFrppDlciStatRcvNPBDe1Frms_Type = Counter32
_MpFrppDlciStatRcvNPBDe1Frms_Object = MibTableColumn
mpFrppDlciStatRcvNPBDe1Frms = _MpFrppDlciStatRcvNPBDe1Frms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 41),
    _MpFrppDlciStatRcvNPBDe1Frms_Type()
)
mpFrppDlciStatRcvNPBDe1Frms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvNPBDe1Frms.setStatus("mandatory")
_MpFrppDlciStatRcvNPBDiscardFrms_Type = Counter32
_MpFrppDlciStatRcvNPBDiscardFrms_Object = MibTableColumn
mpFrppDlciStatRcvNPBDiscardFrms = _MpFrppDlciStatRcvNPBDiscardFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 42),
    _MpFrppDlciStatRcvNPBDiscardFrms_Type()
)
mpFrppDlciStatRcvNPBDiscardFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatRcvNPBDiscardFrms.setStatus("mandatory")
_MpFrppDlciStatXmtNPBFrms_Type = Counter32
_MpFrppDlciStatXmtNPBFrms_Object = MibTableColumn
mpFrppDlciStatXmtNPBFrms = _MpFrppDlciStatXmtNPBFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 43),
    _MpFrppDlciStatXmtNPBFrms_Type()
)
mpFrppDlciStatXmtNPBFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtNPBFrms.setStatus("mandatory")
_MpFrppDlciStatXmtNPBDiscardFrms_Type = Counter32
_MpFrppDlciStatXmtNPBDiscardFrms_Object = MibTableColumn
mpFrppDlciStatXmtNPBDiscardFrms = _MpFrppDlciStatXmtNPBDiscardFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 8, 1, 44),
    _MpFrppDlciStatXmtNPBDiscardFrms_Type()
)
mpFrppDlciStatXmtNPBDiscardFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciStatXmtNPBDiscardFrms.setStatus("mandatory")
_MpFrppDlciWkStatTable_Object = MibTable
mpFrppDlciWkStatTable = _MpFrppDlciWkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9)
)
if mibBuilder.loadTexts:
    mpFrppDlciWkStatTable.setStatus("mandatory")
_MpFrppDlciWkStatEntry_Object = MibTableRow
mpFrppDlciWkStatEntry = _MpFrppDlciWkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1)
)
mpFrppDlciWkStatEntry.setIndexNames(
    (0, "MP-FRPP-MIB", "mpFrppDlciWkStatIfIndex"),
)
if mibBuilder.loadTexts:
    mpFrppDlciWkStatEntry.setStatus("mandatory")
_MpFrppDlciWkStatIfIndex_Type = Integer32
_MpFrppDlciWkStatIfIndex_Object = MibTableColumn
mpFrppDlciWkStatIfIndex = _MpFrppDlciWkStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 1),
    _MpFrppDlciWkStatIfIndex_Type()
)
mpFrppDlciWkStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatIfIndex.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapNones_Type = Counter32
_MpFrppDlciWkStatFNEncapNones_Object = MibTableColumn
mpFrppDlciWkStatFNEncapNones = _MpFrppDlciWkStatFNEncapNones_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 2),
    _MpFrppDlciWkStatFNEncapNones_Type()
)
mpFrppDlciWkStatFNEncapNones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapNones.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapBridgeds_Type = Counter32
_MpFrppDlciWkStatFNEncapBridgeds_Object = MibTableColumn
mpFrppDlciWkStatFNEncapBridgeds = _MpFrppDlciWkStatFNEncapBridgeds_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 3),
    _MpFrppDlciWkStatFNEncapBridgeds_Type()
)
mpFrppDlciWkStatFNEncapBridgeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapBridgeds.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapBridgedFCSs_Type = Counter32
_MpFrppDlciWkStatFNEncapBridgedFCSs_Object = MibTableColumn
mpFrppDlciWkStatFNEncapBridgedFCSs = _MpFrppDlciWkStatFNEncapBridgedFCSs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 4),
    _MpFrppDlciWkStatFNEncapBridgedFCSs_Type()
)
mpFrppDlciWkStatFNEncapBridgedFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapBridgedFCSs.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapBPDUs_Type = Counter32
_MpFrppDlciWkStatFNEncapBPDUs_Object = MibTableColumn
mpFrppDlciWkStatFNEncapBPDUs = _MpFrppDlciWkStatFNEncapBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 5),
    _MpFrppDlciWkStatFNEncapBPDUs_Type()
)
mpFrppDlciWkStatFNEncapBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapBPDUs.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapRoutedIPs_Type = Counter32
_MpFrppDlciWkStatFNEncapRoutedIPs_Object = MibTableColumn
mpFrppDlciWkStatFNEncapRoutedIPs = _MpFrppDlciWkStatFNEncapRoutedIPs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 6),
    _MpFrppDlciWkStatFNEncapRoutedIPs_Type()
)
mpFrppDlciWkStatFNEncapRoutedIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapRoutedIPs.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapRoutedIPSNAPs_Type = Counter32
_MpFrppDlciWkStatFNEncapRoutedIPSNAPs_Object = MibTableColumn
mpFrppDlciWkStatFNEncapRoutedIPSNAPs = _MpFrppDlciWkStatFNEncapRoutedIPSNAPs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 7),
    _MpFrppDlciWkStatFNEncapRoutedIPSNAPs_Type()
)
mpFrppDlciWkStatFNEncapRoutedIPSNAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapRoutedIPSNAPs.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP0s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP0s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP0s = _MpFrppDlciWkStatFNEncapVOIP0s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 8),
    _MpFrppDlciWkStatFNEncapVOIP0s_Type()
)
mpFrppDlciWkStatFNEncapVOIP0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP0s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP1s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP1s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP1s = _MpFrppDlciWkStatFNEncapVOIP1s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 9),
    _MpFrppDlciWkStatFNEncapVOIP1s_Type()
)
mpFrppDlciWkStatFNEncapVOIP1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP1s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP2s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP2s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP2s = _MpFrppDlciWkStatFNEncapVOIP2s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 10),
    _MpFrppDlciWkStatFNEncapVOIP2s_Type()
)
mpFrppDlciWkStatFNEncapVOIP2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP2s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP3s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP3s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP3s = _MpFrppDlciWkStatFNEncapVOIP3s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 11),
    _MpFrppDlciWkStatFNEncapVOIP3s_Type()
)
mpFrppDlciWkStatFNEncapVOIP3s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP3s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP4s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP4s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP4s = _MpFrppDlciWkStatFNEncapVOIP4s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 12),
    _MpFrppDlciWkStatFNEncapVOIP4s_Type()
)
mpFrppDlciWkStatFNEncapVOIP4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP4s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP5s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP5s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP5s = _MpFrppDlciWkStatFNEncapVOIP5s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 13),
    _MpFrppDlciWkStatFNEncapVOIP5s_Type()
)
mpFrppDlciWkStatFNEncapVOIP5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP5s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP6s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP6s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP6s = _MpFrppDlciWkStatFNEncapVOIP6s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 14),
    _MpFrppDlciWkStatFNEncapVOIP6s_Type()
)
mpFrppDlciWkStatFNEncapVOIP6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP6s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP7s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP7s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP7s = _MpFrppDlciWkStatFNEncapVOIP7s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 15),
    _MpFrppDlciWkStatFNEncapVOIP7s_Type()
)
mpFrppDlciWkStatFNEncapVOIP7s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP7s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP8s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP8s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP8s = _MpFrppDlciWkStatFNEncapVOIP8s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 16),
    _MpFrppDlciWkStatFNEncapVOIP8s_Type()
)
mpFrppDlciWkStatFNEncapVOIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP8s.setStatus("mandatory")
_MpFrppDlciWkStatFNEncapVOIP9s_Type = Counter32
_MpFrppDlciWkStatFNEncapVOIP9s_Object = MibTableColumn
mpFrppDlciWkStatFNEncapVOIP9s = _MpFrppDlciWkStatFNEncapVOIP9s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 17),
    _MpFrppDlciWkStatFNEncapVOIP9s_Type()
)
mpFrppDlciWkStatFNEncapVOIP9s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFNEncapVOIP9s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapNones_Type = Counter32
_MpFrppDlciWkStatNFEncapNones_Object = MibTableColumn
mpFrppDlciWkStatNFEncapNones = _MpFrppDlciWkStatNFEncapNones_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 18),
    _MpFrppDlciWkStatNFEncapNones_Type()
)
mpFrppDlciWkStatNFEncapNones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapNones.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapBridgeds_Type = Counter32
_MpFrppDlciWkStatNFEncapBridgeds_Object = MibTableColumn
mpFrppDlciWkStatNFEncapBridgeds = _MpFrppDlciWkStatNFEncapBridgeds_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 19),
    _MpFrppDlciWkStatNFEncapBridgeds_Type()
)
mpFrppDlciWkStatNFEncapBridgeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapBridgeds.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapBridgedFCSs_Type = Counter32
_MpFrppDlciWkStatNFEncapBridgedFCSs_Object = MibTableColumn
mpFrppDlciWkStatNFEncapBridgedFCSs = _MpFrppDlciWkStatNFEncapBridgedFCSs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 20),
    _MpFrppDlciWkStatNFEncapBridgedFCSs_Type()
)
mpFrppDlciWkStatNFEncapBridgedFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapBridgedFCSs.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapBPDUs_Type = Counter32
_MpFrppDlciWkStatNFEncapBPDUs_Object = MibTableColumn
mpFrppDlciWkStatNFEncapBPDUs = _MpFrppDlciWkStatNFEncapBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 21),
    _MpFrppDlciWkStatNFEncapBPDUs_Type()
)
mpFrppDlciWkStatNFEncapBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapBPDUs.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapRoutedIPs_Type = Counter32
_MpFrppDlciWkStatNFEncapRoutedIPs_Object = MibTableColumn
mpFrppDlciWkStatNFEncapRoutedIPs = _MpFrppDlciWkStatNFEncapRoutedIPs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 22),
    _MpFrppDlciWkStatNFEncapRoutedIPs_Type()
)
mpFrppDlciWkStatNFEncapRoutedIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapRoutedIPs.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapRoutedIPSNAPs_Type = Counter32
_MpFrppDlciWkStatNFEncapRoutedIPSNAPs_Object = MibTableColumn
mpFrppDlciWkStatNFEncapRoutedIPSNAPs = _MpFrppDlciWkStatNFEncapRoutedIPSNAPs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 23),
    _MpFrppDlciWkStatNFEncapRoutedIPSNAPs_Type()
)
mpFrppDlciWkStatNFEncapRoutedIPSNAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapRoutedIPSNAPs.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP0s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP0s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP0s = _MpFrppDlciWkStatNFEncapVOIP0s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 24),
    _MpFrppDlciWkStatNFEncapVOIP0s_Type()
)
mpFrppDlciWkStatNFEncapVOIP0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP0s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP1s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP1s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP1s = _MpFrppDlciWkStatNFEncapVOIP1s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 25),
    _MpFrppDlciWkStatNFEncapVOIP1s_Type()
)
mpFrppDlciWkStatNFEncapVOIP1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP1s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP2s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP2s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP2s = _MpFrppDlciWkStatNFEncapVOIP2s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 26),
    _MpFrppDlciWkStatNFEncapVOIP2s_Type()
)
mpFrppDlciWkStatNFEncapVOIP2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP2s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP3s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP3s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP3s = _MpFrppDlciWkStatNFEncapVOIP3s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 27),
    _MpFrppDlciWkStatNFEncapVOIP3s_Type()
)
mpFrppDlciWkStatNFEncapVOIP3s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP3s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP4s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP4s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP4s = _MpFrppDlciWkStatNFEncapVOIP4s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 28),
    _MpFrppDlciWkStatNFEncapVOIP4s_Type()
)
mpFrppDlciWkStatNFEncapVOIP4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP4s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP5s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP5s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP5s = _MpFrppDlciWkStatNFEncapVOIP5s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 29),
    _MpFrppDlciWkStatNFEncapVOIP5s_Type()
)
mpFrppDlciWkStatNFEncapVOIP5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP5s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP6s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP6s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP6s = _MpFrppDlciWkStatNFEncapVOIP6s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 30),
    _MpFrppDlciWkStatNFEncapVOIP6s_Type()
)
mpFrppDlciWkStatNFEncapVOIP6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP6s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP7s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP7s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP7s = _MpFrppDlciWkStatNFEncapVOIP7s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 31),
    _MpFrppDlciWkStatNFEncapVOIP7s_Type()
)
mpFrppDlciWkStatNFEncapVOIP7s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP7s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP8s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP8s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP8s = _MpFrppDlciWkStatNFEncapVOIP8s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 32),
    _MpFrppDlciWkStatNFEncapVOIP8s_Type()
)
mpFrppDlciWkStatNFEncapVOIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP8s.setStatus("mandatory")
_MpFrppDlciWkStatNFEncapVOIP9s_Type = Counter32
_MpFrppDlciWkStatNFEncapVOIP9s_Object = MibTableColumn
mpFrppDlciWkStatNFEncapVOIP9s = _MpFrppDlciWkStatNFEncapVOIP9s_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 33),
    _MpFrppDlciWkStatNFEncapVOIP9s_Type()
)
mpFrppDlciWkStatNFEncapVOIP9s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatNFEncapVOIP9s.setStatus("mandatory")
_MpFrppDlciWkStatRcvFragFrms_Type = Counter32
_MpFrppDlciWkStatRcvFragFrms_Object = MibTableColumn
mpFrppDlciWkStatRcvFragFrms = _MpFrppDlciWkStatRcvFragFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 34),
    _MpFrppDlciWkStatRcvFragFrms_Type()
)
mpFrppDlciWkStatRcvFragFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatRcvFragFrms.setStatus("mandatory")
_MpFrppDlciWkStatRasmCompleteds_Type = Counter32
_MpFrppDlciWkStatRasmCompleteds_Object = MibTableColumn
mpFrppDlciWkStatRasmCompleteds = _MpFrppDlciWkStatRasmCompleteds_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 35),
    _MpFrppDlciWkStatRasmCompleteds_Type()
)
mpFrppDlciWkStatRasmCompleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatRasmCompleteds.setStatus("mandatory")
_MpFrppDlciWkStatFragSequenceErrs_Type = Counter32
_MpFrppDlciWkStatFragSequenceErrs_Object = MibTableColumn
mpFrppDlciWkStatFragSequenceErrs = _MpFrppDlciWkStatFragSequenceErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 36),
    _MpFrppDlciWkStatFragSequenceErrs_Type()
)
mpFrppDlciWkStatFragSequenceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFragSequenceErrs.setStatus("mandatory")
_MpFrppDlciWkStatFragBitErrs_Type = Counter32
_MpFrppDlciWkStatFragBitErrs_Object = MibTableColumn
mpFrppDlciWkStatFragBitErrs = _MpFrppDlciWkStatFragBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 37),
    _MpFrppDlciWkStatFragBitErrs_Type()
)
mpFrppDlciWkStatFragBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFragBitErrs.setStatus("mandatory")
_MpFrppDlciWkStatRasmFrmSizeErrs_Type = Counter32
_MpFrppDlciWkStatRasmFrmSizeErrs_Object = MibTableColumn
mpFrppDlciWkStatRasmFrmSizeErrs = _MpFrppDlciWkStatRasmFrmSizeErrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 38),
    _MpFrppDlciWkStatRasmFrmSizeErrs_Type()
)
mpFrppDlciWkStatRasmFrmSizeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatRasmFrmSizeErrs.setStatus("mandatory")
_MpFrppDlciWkStatInvalidFragFrms_Type = Counter32
_MpFrppDlciWkStatInvalidFragFrms_Object = MibTableColumn
mpFrppDlciWkStatInvalidFragFrms = _MpFrppDlciWkStatInvalidFragFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 39),
    _MpFrppDlciWkStatInvalidFragFrms_Type()
)
mpFrppDlciWkStatInvalidFragFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatInvalidFragFrms.setStatus("mandatory")
_MpFrppDlciWkStatFragBufhuntNgs_Type = Counter32
_MpFrppDlciWkStatFragBufhuntNgs_Object = MibTableColumn
mpFrppDlciWkStatFragBufhuntNgs = _MpFrppDlciWkStatFragBufhuntNgs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 40),
    _MpFrppDlciWkStatFragBufhuntNgs_Type()
)
mpFrppDlciWkStatFragBufhuntNgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFragBufhuntNgs.setStatus("mandatory")
_MpFrppDlciWkStatFragSndNgs_Type = Counter32
_MpFrppDlciWkStatFragSndNgs_Object = MibTableColumn
mpFrppDlciWkStatFragSndNgs = _MpFrppDlciWkStatFragSndNgs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 41),
    _MpFrppDlciWkStatFragSndNgs_Type()
)
mpFrppDlciWkStatFragSndNgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatFragSndNgs.setStatus("mandatory")
_MpFrppDlciWkStatXmtFrames_Type = Counter32
_MpFrppDlciWkStatXmtFrames_Object = MibTableColumn
mpFrppDlciWkStatXmtFrames = _MpFrppDlciWkStatXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 42),
    _MpFrppDlciWkStatXmtFrames_Type()
)
mpFrppDlciWkStatXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatXmtFrames.setStatus("mandatory")
_MpFrppDlciWkStatXmtDiscardFrms_Type = Counter32
_MpFrppDlciWkStatXmtDiscardFrms_Object = MibTableColumn
mpFrppDlciWkStatXmtDiscardFrms = _MpFrppDlciWkStatXmtDiscardFrms_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 123, 9, 1, 43),
    _MpFrppDlciWkStatXmtDiscardFrms_Type()
)
mpFrppDlciWkStatXmtDiscardFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFrppDlciWkStatXmtDiscardFrms.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MP-FRPP-MIB",
    **{"NetPrefix": NetPrefix,
       "DisplayString": DisplayString,
       "DateAndTime": DateAndTime,
       "MacAddress": MacAddress,
       "PhysAddress": PhysAddress,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "nec": nec,
       "necProduct": necProduct,
       "datax": datax,
       "mmpf": mmpf,
       "mmn9110": mmn9110,
       "mmn9120": mmn9120,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "datax-mib": datax_mib,
       "mmpf-mib": mmpf_mib,
       "mpSystem": mpSystem,
       "mpIfCard": mpIfCard,
       "mpEtherPort": mpEtherPort,
       "mpVlan": mpVlan,
       "mpBridge": mpBridge,
       "mpDbAccess": mpDbAccess,
       "mpEventLog": mpEventLog,
       "mpUiSession": mpUiSession,
       "mpFtp": mpFtp,
       "mpDhcp": mpDhcp,
       "mpIp": mpIp,
       "mpRip": mpRip,
       "mpSnmp": mpSnmp,
       "mpStats": mpStats,
       "mpCli": mpCli,
       "mpAtm": mpAtm,
       "mpLis": mpLis,
       "mpDns": mpDns,
       "mpLec": mpLec,
       "mpMpc": mpMpc,
       "mpStp": mpStp,
       "mpLlc": mpLlc,
       "mpOspf": mpOspf,
       "mpObsCtl": mpObsCtl,
       "mpCardInfo": mpCardInfo,
       "mpInterface": mpInterface,
       "mpPvoice": mpPvoice,
       "mpAtmCallCtl": mpAtmCallCtl,
       "mpCes": mpCes,
       "mpIpsw": mpIpsw,
       "mpInsCtl": mpInsCtl,
       "mpFfr": mpFfr,
       "mpIpswAtm": mpIpswAtm,
       "mpPpp": mpPpp,
       "mpPos": mpPos,
       "mpFrpp": mpFrpp,
       "mpFrppTrapInfo": mpFrppTrapInfo,
       "mpFrppTrapInfoMccid": mpFrppTrapInfoMccid,
       "mpFrppTrapInfoDlci": mpFrppTrapInfoDlci,
       "mpFrppMccCfgTable": mpFrppMccCfgTable,
       "mpFrppMccCfgEntry": mpFrppMccCfgEntry,
       "mpFrppMccCfgIfIndex": mpFrppMccCfgIfIndex,
       "mpFrppMccCfgL2Status": mpFrppMccCfgL2Status,
       "mpFrppMccCfgLmiProtocol": mpFrppMccCfgLmiProtocol,
       "mpFrppMccCfgUniType": mpFrppMccCfgUniType,
       "mpFrppMccCfgMonitoredEvents": mpFrppMccCfgMonitoredEvents,
       "mpFrppMccCfgErrorThreshold": mpFrppMccCfgErrorThreshold,
       "mpFrppMccCfgFullEnqInterval": mpFrppMccCfgFullEnqInterval,
       "mpFrppMccCfgLmiProcedure": mpFrppMccCfgLmiProcedure,
       "mpFrppMccCfgNetPollInterval": mpFrppMccCfgNetPollInterval,
       "mpFrppMccCfgUsrPollInterval": mpFrppMccCfgUsrPollInterval,
       "mpFrppMccCfgAsync": mpFrppMccCfgAsync,
       "mpFrppMccCfgRowStatus": mpFrppMccCfgRowStatus,
       "mpFrppMccCfgErrInfo": mpFrppMccCfgErrInfo,
       "mpFrppFrppCfgTable": mpFrppFrppCfgTable,
       "mpFrppFrppCfgEntry": mpFrppFrppCfgEntry,
       "mpFrppFrppCfgIfIndex": mpFrppFrppCfgIfIndex,
       "mpFrppFrppCfgMccidIndex": mpFrppFrppCfgMccidIndex,
       "mpFrppFrppCfgDlciIndex": mpFrppFrppCfgDlciIndex,
       "mpFrppFrppCfgFrppName": mpFrppFrppCfgFrppName,
       "mpFrppFrppCfgIpadd": mpFrppFrppCfgIpadd,
       "mpFrppFrppCfgSubnet": mpFrppFrppCfgSubnet,
       "mpFrppFrppCfgMtuSize": mpFrppFrppCfgMtuSize,
       "mpFrppFrppCfgInterWorkType": mpFrppFrppCfgInterWorkType,
       "mpFrppFrppCfgCrtpSupport": mpFrppFrppCfgCrtpSupport,
       "mpFrppFrppCfgCrtpLimit": mpFrppFrppCfgCrtpLimit,
       "mpFrppFrppCfgCrtpMode": mpFrppFrppCfgCrtpMode,
       "mpFrppFrppCfgCrtpAging": mpFrppFrppCfgCrtpAging,
       "mpFrppFrppCfgCtcpSupport": mpFrppFrppCfgCtcpSupport,
       "mpFrppFrppCfgCtcpLimit": mpFrppFrppCfgCtcpLimit,
       "mpFrppFrppCfgCtcpMode": mpFrppFrppCfgCtcpMode,
       "mpFrppFrppCfgCtcpAging": mpFrppFrppCfgCtcpAging,
       "mpFrppFrppCfgHwSticFlag": mpFrppFrppCfgHwSticFlag,
       "mpFrppDlciCfgMtuSize": mpFrppDlciCfgMtuSize,
       "mpFrppDlciCfgBecn": mpFrppDlciCfgBecn,
       "mpFrppDlciCfgEncap": mpFrppDlciCfgEncap,
       "mpFrppDlciCfgDe": mpFrppDlciCfgDe,
       "mpFrppDlciCfgPln": mpFrppDlciCfgPln,
       "mpFrppDlciCfgFragSize": mpFrppDlciCfgFragSize,
       "mpFrppDlciCfgMir": mpFrppDlciCfgMir,
       "mpFrppDlciCfgPerInc": mpFrppDlciCfgPerInc,
       "mpFrppDlciCfgPerDec": mpFrppDlciCfgPerDec,
       "mpFrppDlciCfgMincir": mpFrppDlciCfgMincir,
       "mpFrppDlciCfgCir": mpFrppDlciCfgCir,
       "mpFrppDlciCfgSnapFlg": mpFrppDlciCfgSnapFlg,
       "mpFrppDlciQueueLenH": mpFrppDlciQueueLenH,
       "mpFrppDlciQueueLenU": mpFrppDlciQueueLenU,
       "mpFrppDlciQueueLenL": mpFrppDlciQueueLenL,
       "mpFrppDlciQueueLenN": mpFrppDlciQueueLenN,
       "mpFrppDlciQueueByteH": mpFrppDlciQueueByteH,
       "mpFrppDlciQueueByteU": mpFrppDlciQueueByteU,
       "mpFrppDlciQueueByteL": mpFrppDlciQueueByteL,
       "mpFrppDlciQueueByteN": mpFrppDlciQueueByteN,
       "mpFrppDlciIpQosClassAf3": mpFrppDlciIpQosClassAf3,
       "mpFrppDlciIpQosClassAf2": mpFrppDlciIpQosClassAf2,
       "mpFrppDlciIpQosClassAf1": mpFrppDlciIpQosClassAf1,
       "mpFrppDlciIpQosClassBe": mpFrppDlciIpQosClassBe,
       "mpFrppDlciIpQosClassEf3": mpFrppDlciIpQosClassEf3,
       "mpFrppDlciIpQosClassEf2": mpFrppDlciIpQosClassEf2,
       "mpFrppDlciIpQosClassEf1": mpFrppDlciIpQosClassEf1,
       "mpFrppDlciIpQosClassAf4": mpFrppDlciIpQosClassAf4,
       "mpFrppDlciCfgInarpMode": mpFrppDlciCfgInarpMode,
       "mpFrppDlciCfgTrapFilter": mpFrppDlciCfgTrapFilter,
       "mpFrppFrppCfgRowStatus": mpFrppFrppCfgRowStatus,
       "mpFrppFrppCfgErrInfo": mpFrppFrppCfgErrInfo,
       "mpFrppInfoTable": mpFrppInfoTable,
       "mpFrppInfoEntry": mpFrppInfoEntry,
       "mpFrppInfoIndex": mpFrppInfoIndex,
       "mpFrppInfoFrppAdminStatus": mpFrppInfoFrppAdminStatus,
       "mpFrppInfoFrppOperStatus": mpFrppInfoFrppOperStatus,
       "mpFrppInfoFrppLastChange": mpFrppInfoFrppLastChange,
       "mpFrppInfoDlci": mpFrppInfoDlci,
       "mpFrppInfoDlciAdminStatus": mpFrppInfoDlciAdminStatus,
       "mpFrppInfoDlciOperStatus": mpFrppInfoDlciOperStatus,
       "mpFrppInfoDlciLastChange": mpFrppInfoDlciLastChange,
       "mpFrppInfoDlciOperDownEvent": mpFrppInfoDlciOperDownEvent,
       "mpFrppMccIdStatTable": mpFrppMccIdStatTable,
       "mpFrppMccIdStatEntry": mpFrppMccIdStatEntry,
       "mpFrppMccIdStatIfIndex": mpFrppMccIdStatIfIndex,
       "mpFrppMccIdRcvOctets": mpFrppMccIdRcvOctets,
       "mpFrppMccIdRcvFrames": mpFrppMccIdRcvFrames,
       "mpFrppMccIdRcvFrameMinSize": mpFrppMccIdRcvFrameMinSize,
       "mpFrppMccIdRcvFrameMaxSize": mpFrppMccIdRcvFrameMaxSize,
       "mpFrppMccIdRcvDiscardFrames": mpFrppMccIdRcvDiscardFrames,
       "mpFrppMccIdRcvFecnFrames": mpFrppMccIdRcvFecnFrames,
       "mpFrppMccIdRcvBecnFrames": mpFrppMccIdRcvBecnFrames,
       "mpFrppMccIdRcvDeFrames": mpFrppMccIdRcvDeFrames,
       "mpFrppMccIdRcvInvalidFrames": mpFrppMccIdRcvInvalidFrames,
       "mpFrppMccIdRcvLongFrames": mpFrppMccIdRcvLongFrames,
       "mpFrppMccIdRcvShortFrames": mpFrppMccIdRcvShortFrames,
       "mpFrppMccIdXmtOctets": mpFrppMccIdXmtOctets,
       "mpFrppMccIdXmtFrames": mpFrppMccIdXmtFrames,
       "mpFrppMccIdXmtFrameMinSize": mpFrppMccIdXmtFrameMinSize,
       "mpFrppMccIdXmtFrameMaxSize": mpFrppMccIdXmtFrameMaxSize,
       "mpFrppMccIdXmtDiscardFrames": mpFrppMccIdXmtDiscardFrames,
       "mpFrppMccIdXmtFecnFrames": mpFrppMccIdXmtFecnFrames,
       "mpFrppMccIdXmtBecnFrames": mpFrppMccIdXmtBecnFrames,
       "mpFrppMccIdXmtDeFrames": mpFrppMccIdXmtDeFrames,
       "mpFrppMccIdRcvCllmFrames": mpFrppMccIdRcvCllmFrames,
       "mpFrppMccIdLmiStatTable": mpFrppMccIdLmiStatTable,
       "mpFrppMccIdLmiStatEntry": mpFrppMccIdLmiStatEntry,
       "mpFrppMccIdLmiStatIfIndex": mpFrppMccIdLmiStatIfIndex,
       "mpFrppMccIdRcvLmiStatEnqs": mpFrppMccIdRcvLmiStatEnqs,
       "mpFrppMccIdXmtLmiStatEnqs": mpFrppMccIdXmtLmiStatEnqs,
       "mpFrppMccIdRcvLmiStats": mpFrppMccIdRcvLmiStats,
       "mpFrppMccIdXmtLmiStats": mpFrppMccIdXmtLmiStats,
       "mpFrppMccIdUsrLmiLinkRelErrs": mpFrppMccIdUsrLmiLinkRelErrs,
       "mpFrppMccIdUsrLmiT391Tos": mpFrppMccIdUsrLmiT391Tos,
       "mpFrppMccIdUsrLmiSeqErrs": mpFrppMccIdUsrLmiSeqErrs,
       "mpFrppMccIdUsrLmiProtErrs": mpFrppMccIdUsrLmiProtErrs,
       "mpFrppMccIdUsrLmiChInacts": mpFrppMccIdUsrLmiChInacts,
       "mpFrppMccIdNetLmiLinkRelErrs": mpFrppMccIdNetLmiLinkRelErrs,
       "mpFrppMccIdNetLmiT392Tos": mpFrppMccIdNetLmiT392Tos,
       "mpFrppMccIdNetLmiSeqErrs": mpFrppMccIdNetLmiSeqErrs,
       "mpFrppMccIdNetLmiErrs": mpFrppMccIdNetLmiErrs,
       "mpFrppMccIdNetChInacts": mpFrppMccIdNetChInacts,
       "mpFrppMccIdRcvAsyncFrms": mpFrppMccIdRcvAsyncFrms,
       "mpFrppFrppStatTable": mpFrppFrppStatTable,
       "mpFrppFrppStatEntry": mpFrppFrppStatEntry,
       "mpFrppFrppStatIndex": mpFrppFrppStatIndex,
       "mpFrppFrppStatRcvFrames": mpFrppFrppStatRcvFrames,
       "mpFrppFrppStatXmtFrames": mpFrppFrppStatXmtFrames,
       "mpFrppFrppStatRcvDiscardFrames": mpFrppFrppStatRcvDiscardFrames,
       "mpFrppFrppStatXmtDiscardFrames": mpFrppFrppStatXmtDiscardFrames,
       "mpFrppFrppStatRcvEncapErrors": mpFrppFrppStatRcvEncapErrors,
       "mpFrppFrppStatXmtEncapErrors": mpFrppFrppStatXmtEncapErrors,
       "mpFrppFrppStatRcvArpTransErrors": mpFrppFrppStatRcvArpTransErrors,
       "mpFrppFrppStatXmtArpTransErrors": mpFrppFrppStatXmtArpTransErrors,
       "mpFrppFrppStatReassembleErrors": mpFrppFrppStatReassembleErrors,
       "mpFrppFrppStatPriorityQueues": mpFrppFrppStatPriorityQueues,
       "mpFrppFrppStatPriorityBytes": mpFrppFrppStatPriorityBytes,
       "mpFrppDlcStatTable": mpFrppDlcStatTable,
       "mpFrppDlcStatEntry": mpFrppDlcStatEntry,
       "mpFrppDlciStatIfIndex": mpFrppDlciStatIfIndex,
       "mpFrppDlciStatRcvOctets": mpFrppDlciStatRcvOctets,
       "mpFrppDlciStatRcvFrames": mpFrppDlciStatRcvFrames,
       "mpFrppDlciStatRcvFrameMinSize": mpFrppDlciStatRcvFrameMinSize,
       "mpFrppDlciStatRcvFrameMaxSize": mpFrppDlciStatRcvFrameMaxSize,
       "mpFrppDlciStatRcvFECNFrames": mpFrppDlciStatRcvFECNFrames,
       "mpFrppDlciStatRcvBECNFrames": mpFrppDlciStatRcvBECNFrames,
       "mpFrppDlciStatRcvDEFrames": mpFrppDlciStatRcvDEFrames,
       "mpFrppDlciStatRcvTaggedDEFrames": mpFrppDlciStatRcvTaggedDEFrames,
       "mpFrppDlciStatXmtOctets": mpFrppDlciStatXmtOctets,
       "mpFrppDlciStatXmtFrames": mpFrppDlciStatXmtFrames,
       "mpFrppDlciStatXmtFrameMinSize": mpFrppDlciStatXmtFrameMinSize,
       "mpFrppDlciStatXmtFrameMaxSize": mpFrppDlciStatXmtFrameMaxSize,
       "mpFrppDlciStatXmtDEDiscardFrames": mpFrppDlciStatXmtDEDiscardFrames,
       "mpFrppDlciStatXmtFECNFrames": mpFrppDlciStatXmtFECNFrames,
       "mpFrppDlciStatXmtBECNFrames": mpFrppDlciStatXmtBECNFrames,
       "mpFrppDlciStatXmtDEFrames": mpFrppDlciStatXmtDEFrames,
       "mpFrppDlciStatXmtTaggedDEFrames": mpFrppDlciStatXmtTaggedDEFrames,
       "mpFrppDlciStatRcvInArpReqFrms": mpFrppDlciStatRcvInArpReqFrms,
       "mpFrppDlciStatXmtInArpReqFrms": mpFrppDlciStatXmtInArpReqFrms,
       "mpFrppDlciStatRcvInArpRlyFrms": mpFrppDlciStatRcvInArpRlyFrms,
       "mpFrppDlciStatXmtInArpRlyFrms": mpFrppDlciStatXmtInArpRlyFrms,
       "mpFrppDlciStatFNUnrecognizHeaders": mpFrppDlciStatFNUnrecognizHeaders,
       "mpFrppDlciStatNFUnrecognizHeaders": mpFrppDlciStatNFUnrecognizHeaders,
       "mpFrppDlciStatFNArpTranslationErrs": mpFrppDlciStatFNArpTranslationErrs,
       "mpFrppDlciStatNFArpTranslationErrs": mpFrppDlciStatNFArpTranslationErrs,
       "mpFrppDlciStatXmtVQFrms": mpFrppDlciStatXmtVQFrms,
       "mpFrppDlciStatXmtUQFrms": mpFrppDlciStatXmtUQFrms,
       "mpFrppDlciStatXmtXceedUQLenFrms": mpFrppDlciStatXmtXceedUQLenFrms,
       "mpFrppDlciStatXmtXceedUQByteFrms": mpFrppDlciStatXmtXceedUQByteFrms,
       "mpFrppDlciStatXmtHQFrms": mpFrppDlciStatXmtHQFrms,
       "mpFrppDlciStatXmtXceedHQLenFrms": mpFrppDlciStatXmtXceedHQLenFrms,
       "mpFrppDlciStatXmtXceedHQByteFrms": mpFrppDlciStatXmtXceedHQByteFrms,
       "mpFrppDlciStatXmtNQFrms": mpFrppDlciStatXmtNQFrms,
       "mpFrppDlciStatXmtXceedNQLenFrms": mpFrppDlciStatXmtXceedNQLenFrms,
       "mpFrppDlciStatXmtXceedNQByteFrms": mpFrppDlciStatXmtXceedNQByteFrms,
       "mpFrppDlciStatXmtLQFrms": mpFrppDlciStatXmtLQFrms,
       "mpFrppDlciStatXmtXceedLQLenFrms": mpFrppDlciStatXmtXceedLQLenFrms,
       "mpFrppDlciStatXmtXceedLQByteFrms": mpFrppDlciStatXmtXceedLQByteFrms,
       "mpFrppDlciStatRcvNPBDe0Frms": mpFrppDlciStatRcvNPBDe0Frms,
       "mpFrppDlciStatRcvNPBDe1Frms": mpFrppDlciStatRcvNPBDe1Frms,
       "mpFrppDlciStatRcvNPBDiscardFrms": mpFrppDlciStatRcvNPBDiscardFrms,
       "mpFrppDlciStatXmtNPBFrms": mpFrppDlciStatXmtNPBFrms,
       "mpFrppDlciStatXmtNPBDiscardFrms": mpFrppDlciStatXmtNPBDiscardFrms,
       "mpFrppDlciWkStatTable": mpFrppDlciWkStatTable,
       "mpFrppDlciWkStatEntry": mpFrppDlciWkStatEntry,
       "mpFrppDlciWkStatIfIndex": mpFrppDlciWkStatIfIndex,
       "mpFrppDlciWkStatFNEncapNones": mpFrppDlciWkStatFNEncapNones,
       "mpFrppDlciWkStatFNEncapBridgeds": mpFrppDlciWkStatFNEncapBridgeds,
       "mpFrppDlciWkStatFNEncapBridgedFCSs": mpFrppDlciWkStatFNEncapBridgedFCSs,
       "mpFrppDlciWkStatFNEncapBPDUs": mpFrppDlciWkStatFNEncapBPDUs,
       "mpFrppDlciWkStatFNEncapRoutedIPs": mpFrppDlciWkStatFNEncapRoutedIPs,
       "mpFrppDlciWkStatFNEncapRoutedIPSNAPs": mpFrppDlciWkStatFNEncapRoutedIPSNAPs,
       "mpFrppDlciWkStatFNEncapVOIP0s": mpFrppDlciWkStatFNEncapVOIP0s,
       "mpFrppDlciWkStatFNEncapVOIP1s": mpFrppDlciWkStatFNEncapVOIP1s,
       "mpFrppDlciWkStatFNEncapVOIP2s": mpFrppDlciWkStatFNEncapVOIP2s,
       "mpFrppDlciWkStatFNEncapVOIP3s": mpFrppDlciWkStatFNEncapVOIP3s,
       "mpFrppDlciWkStatFNEncapVOIP4s": mpFrppDlciWkStatFNEncapVOIP4s,
       "mpFrppDlciWkStatFNEncapVOIP5s": mpFrppDlciWkStatFNEncapVOIP5s,
       "mpFrppDlciWkStatFNEncapVOIP6s": mpFrppDlciWkStatFNEncapVOIP6s,
       "mpFrppDlciWkStatFNEncapVOIP7s": mpFrppDlciWkStatFNEncapVOIP7s,
       "mpFrppDlciWkStatFNEncapVOIP8s": mpFrppDlciWkStatFNEncapVOIP8s,
       "mpFrppDlciWkStatFNEncapVOIP9s": mpFrppDlciWkStatFNEncapVOIP9s,
       "mpFrppDlciWkStatNFEncapNones": mpFrppDlciWkStatNFEncapNones,
       "mpFrppDlciWkStatNFEncapBridgeds": mpFrppDlciWkStatNFEncapBridgeds,
       "mpFrppDlciWkStatNFEncapBridgedFCSs": mpFrppDlciWkStatNFEncapBridgedFCSs,
       "mpFrppDlciWkStatNFEncapBPDUs": mpFrppDlciWkStatNFEncapBPDUs,
       "mpFrppDlciWkStatNFEncapRoutedIPs": mpFrppDlciWkStatNFEncapRoutedIPs,
       "mpFrppDlciWkStatNFEncapRoutedIPSNAPs": mpFrppDlciWkStatNFEncapRoutedIPSNAPs,
       "mpFrppDlciWkStatNFEncapVOIP0s": mpFrppDlciWkStatNFEncapVOIP0s,
       "mpFrppDlciWkStatNFEncapVOIP1s": mpFrppDlciWkStatNFEncapVOIP1s,
       "mpFrppDlciWkStatNFEncapVOIP2s": mpFrppDlciWkStatNFEncapVOIP2s,
       "mpFrppDlciWkStatNFEncapVOIP3s": mpFrppDlciWkStatNFEncapVOIP3s,
       "mpFrppDlciWkStatNFEncapVOIP4s": mpFrppDlciWkStatNFEncapVOIP4s,
       "mpFrppDlciWkStatNFEncapVOIP5s": mpFrppDlciWkStatNFEncapVOIP5s,
       "mpFrppDlciWkStatNFEncapVOIP6s": mpFrppDlciWkStatNFEncapVOIP6s,
       "mpFrppDlciWkStatNFEncapVOIP7s": mpFrppDlciWkStatNFEncapVOIP7s,
       "mpFrppDlciWkStatNFEncapVOIP8s": mpFrppDlciWkStatNFEncapVOIP8s,
       "mpFrppDlciWkStatNFEncapVOIP9s": mpFrppDlciWkStatNFEncapVOIP9s,
       "mpFrppDlciWkStatRcvFragFrms": mpFrppDlciWkStatRcvFragFrms,
       "mpFrppDlciWkStatRasmCompleteds": mpFrppDlciWkStatRasmCompleteds,
       "mpFrppDlciWkStatFragSequenceErrs": mpFrppDlciWkStatFragSequenceErrs,
       "mpFrppDlciWkStatFragBitErrs": mpFrppDlciWkStatFragBitErrs,
       "mpFrppDlciWkStatRasmFrmSizeErrs": mpFrppDlciWkStatRasmFrmSizeErrs,
       "mpFrppDlciWkStatInvalidFragFrms": mpFrppDlciWkStatInvalidFragFrms,
       "mpFrppDlciWkStatFragBufhuntNgs": mpFrppDlciWkStatFragBufhuntNgs,
       "mpFrppDlciWkStatFragSndNgs": mpFrppDlciWkStatFragSndNgs,
       "mpFrppDlciWkStatXmtFrames": mpFrppDlciWkStatXmtFrames,
       "mpFrppDlciWkStatXmtDiscardFrms": mpFrppDlciWkStatXmtDiscardFrms}
)
