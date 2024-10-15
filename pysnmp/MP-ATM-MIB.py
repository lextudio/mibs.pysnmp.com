# SNMP MIB module (MP-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MP-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:43 2024
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

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





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





class AtmAddr(OctetString):
    """Custom type AtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )





class MpAtmCCCladType(Integer32):
    """Custom type MpAtmCCCladType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("atm-trunk", 4),
          ("atm-trunk-cdm", 13),
          ("atm-uni", 3),
          ("atm-uni-vmc", 5),
          ("ces", 9),
          ("com", 1),
          ("eth", 12),
          ("ffr", 7),
          ("ins", 10),
          ("lvc", 6),
          ("mux", 2),
          ("odt", 8),
          ("sel", 11))
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
_MpAtmCCBaseGroup_ObjectIdentity = ObjectIdentity
mpAtmCCBaseGroup = _MpAtmCCBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 1)
)
_MpAtmCCNextTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCNextTrafficDescrIndex_Object = MibScalar
mpAtmCCNextTrafficDescrIndex = _MpAtmCCNextTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 1, 1),
    _MpAtmCCNextTrafficDescrIndex_Type()
)
mpAtmCCNextTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCNextTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCNextNodeVci_Type = Integer32
_MpAtmCCNextNodeVci_Object = MibScalar
mpAtmCCNextNodeVci = _MpAtmCCNextNodeVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 1, 2),
    _MpAtmCCNextNodeVci_Type()
)
mpAtmCCNextNodeVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCNextNodeVci.setStatus("mandatory")
_MpAtmCCStaticPVPC_ObjectIdentity = ObjectIdentity
mpAtmCCStaticPVPC = _MpAtmCCStaticPVPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2)
)
_MpAtmCCStaticPvpTable_Object = MibTable
mpAtmCCStaticPvpTable = _MpAtmCCStaticPvpTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpTable.setStatus("mandatory")
_MpAtmCCStaticPvpEntry_Object = MibTableRow
mpAtmCCStaticPvpEntry = _MpAtmCCStaticPvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1)
)
mpAtmCCStaticPvpEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvpIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvpLowIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvpLowVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvpHighIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvpHighVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpEntry.setStatus("mandatory")


class _MpAtmCCStaticPvpIndex_Type(Integer32):
    """Custom type mpAtmCCStaticPvpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpAtmCCStaticPvpIndex_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpIndex_Object = MibTableColumn
mpAtmCCStaticPvpIndex = _MpAtmCCStaticPvpIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 1),
    _MpAtmCCStaticPvpIndex_Type()
)
mpAtmCCStaticPvpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpIndex.setStatus("mandatory")
_MpAtmCCStaticPvpLowIfIndex_Type = Integer32
_MpAtmCCStaticPvpLowIfIndex_Object = MibTableColumn
mpAtmCCStaticPvpLowIfIndex = _MpAtmCCStaticPvpLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 2),
    _MpAtmCCStaticPvpLowIfIndex_Type()
)
mpAtmCCStaticPvpLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpLowIfIndex.setStatus("mandatory")


class _MpAtmCCStaticPvpLowVpi_Type(Integer32):
    """Custom type mpAtmCCStaticPvpLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCStaticPvpLowVpi_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpLowVpi_Object = MibTableColumn
mpAtmCCStaticPvpLowVpi = _MpAtmCCStaticPvpLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 3),
    _MpAtmCCStaticPvpLowVpi_Type()
)
mpAtmCCStaticPvpLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpLowVpi.setStatus("mandatory")
_MpAtmCCStaticPvpHighIfIndex_Type = Integer32
_MpAtmCCStaticPvpHighIfIndex_Object = MibTableColumn
mpAtmCCStaticPvpHighIfIndex = _MpAtmCCStaticPvpHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 4),
    _MpAtmCCStaticPvpHighIfIndex_Type()
)
mpAtmCCStaticPvpHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpHighIfIndex.setStatus("mandatory")


class _MpAtmCCStaticPvpHighVpi_Type(Integer32):
    """Custom type mpAtmCCStaticPvpHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCStaticPvpHighVpi_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpHighVpi_Object = MibTableColumn
mpAtmCCStaticPvpHighVpi = _MpAtmCCStaticPvpHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 5),
    _MpAtmCCStaticPvpHighVpi_Type()
)
mpAtmCCStaticPvpHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpHighVpi.setStatus("mandatory")
_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvpLowReceiveTrafficDescrIndex = _MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 6),
    _MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Type()
)
mpAtmCCStaticPvpLowReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpLowReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvpLowTransmitTrafficDescrIndex = _MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 7),
    _MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Type()
)
mpAtmCCStaticPvpLowTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpLowTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvpHighReceiveTrafficDescrIndex = _MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 8),
    _MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Type()
)
mpAtmCCStaticPvpHighReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpHighReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvpHighTransmitTrafficDescrIndex = _MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 9),
    _MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Type()
)
mpAtmCCStaticPvpHighTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpHighTransmitTrafficDescrIndex.setStatus("mandatory")


class _MpAtmCCStaticPvpPriority_Type(Integer32):
    """Custom type mpAtmCCStaticPvpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCStaticPvpPriority_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpPriority_Object = MibTableColumn
mpAtmCCStaticPvpPriority = _MpAtmCCStaticPvpPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 10),
    _MpAtmCCStaticPvpPriority_Type()
)
mpAtmCCStaticPvpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpPriority.setStatus("mandatory")
_MpAtmCCStaticPvpLowCladType_Type = MpAtmCCCladType
_MpAtmCCStaticPvpLowCladType_Object = MibTableColumn
mpAtmCCStaticPvpLowCladType = _MpAtmCCStaticPvpLowCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 11),
    _MpAtmCCStaticPvpLowCladType_Type()
)
mpAtmCCStaticPvpLowCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpLowCladType.setStatus("mandatory")
_MpAtmCCStaticPvpHighCladType_Type = MpAtmCCCladType
_MpAtmCCStaticPvpHighCladType_Object = MibTableColumn
mpAtmCCStaticPvpHighCladType = _MpAtmCCStaticPvpHighCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 12),
    _MpAtmCCStaticPvpHighCladType_Type()
)
mpAtmCCStaticPvpHighCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpHighCladType.setStatus("mandatory")


class _MpAtmCCStaticPvpAdminStatus_Type(Integer32):
    """Custom type mpAtmCCStaticPvpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCStaticPvpAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpAdminStatus_Object = MibTableColumn
mpAtmCCStaticPvpAdminStatus = _MpAtmCCStaticPvpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 13),
    _MpAtmCCStaticPvpAdminStatus_Type()
)
mpAtmCCStaticPvpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpAdminStatus.setStatus("mandatory")
_MpAtmCCStaticPvpOperStatus_Type = Integer32
_MpAtmCCStaticPvpOperStatus_Object = MibTableColumn
mpAtmCCStaticPvpOperStatus = _MpAtmCCStaticPvpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 14),
    _MpAtmCCStaticPvpOperStatus_Type()
)
mpAtmCCStaticPvpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpOperStatus.setStatus("mandatory")
_MpAtmCCStaticPvpPvpId_Type = Integer32
_MpAtmCCStaticPvpPvpId_Object = MibTableColumn
mpAtmCCStaticPvpPvpId = _MpAtmCCStaticPvpPvpId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 15),
    _MpAtmCCStaticPvpPvpId_Type()
)
mpAtmCCStaticPvpPvpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpPvpId.setStatus("mandatory")
_MpAtmCCStaticPvpSeqNo_Type = Integer32
_MpAtmCCStaticPvpSeqNo_Object = MibTableColumn
mpAtmCCStaticPvpSeqNo = _MpAtmCCStaticPvpSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 16),
    _MpAtmCCStaticPvpSeqNo_Type()
)
mpAtmCCStaticPvpSeqNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpSeqNo.setStatus("mandatory")
_MpAtmCCStaticPvpPgcRequest_Type = Integer32
_MpAtmCCStaticPvpPgcRequest_Object = MibTableColumn
mpAtmCCStaticPvpPgcRequest = _MpAtmCCStaticPvpPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 17),
    _MpAtmCCStaticPvpPgcRequest_Type()
)
mpAtmCCStaticPvpPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpPgcRequest.setStatus("mandatory")


class _MpAtmCCStaticPvpCfgStatus_Type(Integer32):
    """Custom type mpAtmCCStaticPvpCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCStaticPvpCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCStaticPvpCfgStatus_Object = MibTableColumn
mpAtmCCStaticPvpCfgStatus = _MpAtmCCStaticPvpCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 98),
    _MpAtmCCStaticPvpCfgStatus_Type()
)
mpAtmCCStaticPvpCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpCfgStatus.setStatus("mandatory")
_MpAtmCCStaticPvpErrInfo_Type = Integer32
_MpAtmCCStaticPvpErrInfo_Object = MibTableColumn
mpAtmCCStaticPvpErrInfo = _MpAtmCCStaticPvpErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 1, 1, 99),
    _MpAtmCCStaticPvpErrInfo_Type()
)
mpAtmCCStaticPvpErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvpErrInfo.setStatus("mandatory")
_MpAtmCCStaticPvcTable_Object = MibTable
mpAtmCCStaticPvcTable = _MpAtmCCStaticPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcTable.setStatus("mandatory")
_MpAtmCCStaticPvcEntry_Object = MibTableRow
mpAtmCCStaticPvcEntry = _MpAtmCCStaticPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1)
)
mpAtmCCStaticPvcEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcLowIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcLowVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcLowVci"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcHighIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcHighVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCStaticPvcHighVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcEntry.setStatus("mandatory")


class _MpAtmCCStaticPvcIndex_Type(Integer32):
    """Custom type mpAtmCCStaticPvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpAtmCCStaticPvcIndex_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcIndex_Object = MibTableColumn
mpAtmCCStaticPvcIndex = _MpAtmCCStaticPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 1),
    _MpAtmCCStaticPvcIndex_Type()
)
mpAtmCCStaticPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcIndex.setStatus("mandatory")
_MpAtmCCStaticPvcLowIfIndex_Type = Integer32
_MpAtmCCStaticPvcLowIfIndex_Object = MibTableColumn
mpAtmCCStaticPvcLowIfIndex = _MpAtmCCStaticPvcLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 2),
    _MpAtmCCStaticPvcLowIfIndex_Type()
)
mpAtmCCStaticPvcLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowIfIndex.setStatus("mandatory")


class _MpAtmCCStaticPvcLowVpi_Type(Integer32):
    """Custom type mpAtmCCStaticPvcLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCStaticPvcLowVpi_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcLowVpi_Object = MibTableColumn
mpAtmCCStaticPvcLowVpi = _MpAtmCCStaticPvcLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 3),
    _MpAtmCCStaticPvcLowVpi_Type()
)
mpAtmCCStaticPvcLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowVpi.setStatus("mandatory")


class _MpAtmCCStaticPvcLowVci_Type(Integer32):
    """Custom type mpAtmCCStaticPvcLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpAtmCCStaticPvcLowVci_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcLowVci_Object = MibTableColumn
mpAtmCCStaticPvcLowVci = _MpAtmCCStaticPvcLowVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 4),
    _MpAtmCCStaticPvcLowVci_Type()
)
mpAtmCCStaticPvcLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowVci.setStatus("mandatory")
_MpAtmCCStaticPvcHighIfIndex_Type = Integer32
_MpAtmCCStaticPvcHighIfIndex_Object = MibTableColumn
mpAtmCCStaticPvcHighIfIndex = _MpAtmCCStaticPvcHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 5),
    _MpAtmCCStaticPvcHighIfIndex_Type()
)
mpAtmCCStaticPvcHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighIfIndex.setStatus("mandatory")


class _MpAtmCCStaticPvcHighVpi_Type(Integer32):
    """Custom type mpAtmCCStaticPvcHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCStaticPvcHighVpi_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcHighVpi_Object = MibTableColumn
mpAtmCCStaticPvcHighVpi = _MpAtmCCStaticPvcHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 6),
    _MpAtmCCStaticPvcHighVpi_Type()
)
mpAtmCCStaticPvcHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighVpi.setStatus("mandatory")


class _MpAtmCCStaticPvcHighVci_Type(Integer32):
    """Custom type mpAtmCCStaticPvcHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpAtmCCStaticPvcHighVci_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcHighVci_Object = MibTableColumn
mpAtmCCStaticPvcHighVci = _MpAtmCCStaticPvcHighVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 7),
    _MpAtmCCStaticPvcHighVci_Type()
)
mpAtmCCStaticPvcHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighVci.setStatus("mandatory")
_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvcLowReceiveTrafficDescrIndex = _MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 8),
    _MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Type()
)
mpAtmCCStaticPvcLowReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvcLowTransmitTrafficDescrIndex = _MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 9),
    _MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Type()
)
mpAtmCCStaticPvcLowTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvcHighReceiveTrafficDescrIndex = _MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 10),
    _MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Type()
)
mpAtmCCStaticPvcHighReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCStaticPvcHighTransmitTrafficDescrIndex = _MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 11),
    _MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Type()
)
mpAtmCCStaticPvcHighTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighTransmitTrafficDescrIndex.setStatus("mandatory")


class _MpAtmCCStaticPvcPriority_Type(Integer32):
    """Custom type mpAtmCCStaticPvcPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCStaticPvcPriority_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcPriority_Object = MibTableColumn
mpAtmCCStaticPvcPriority = _MpAtmCCStaticPvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 12),
    _MpAtmCCStaticPvcPriority_Type()
)
mpAtmCCStaticPvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcPriority.setStatus("mandatory")
_MpAtmCCStaticPvcLowCladType_Type = MpAtmCCCladType
_MpAtmCCStaticPvcLowCladType_Object = MibTableColumn
mpAtmCCStaticPvcLowCladType = _MpAtmCCStaticPvcLowCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 13),
    _MpAtmCCStaticPvcLowCladType_Type()
)
mpAtmCCStaticPvcLowCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcLowCladType.setStatus("mandatory")
_MpAtmCCStaticPvcHighCladType_Type = MpAtmCCCladType
_MpAtmCCStaticPvcHighCladType_Object = MibTableColumn
mpAtmCCStaticPvcHighCladType = _MpAtmCCStaticPvcHighCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 14),
    _MpAtmCCStaticPvcHighCladType_Type()
)
mpAtmCCStaticPvcHighCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcHighCladType.setStatus("mandatory")


class _MpAtmCCStaticPvcAdminStatus_Type(Integer32):
    """Custom type mpAtmCCStaticPvcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCStaticPvcAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcAdminStatus_Object = MibTableColumn
mpAtmCCStaticPvcAdminStatus = _MpAtmCCStaticPvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 15),
    _MpAtmCCStaticPvcAdminStatus_Type()
)
mpAtmCCStaticPvcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcAdminStatus.setStatus("mandatory")
_MpAtmCCStaticPvcOperStatus_Type = Integer32
_MpAtmCCStaticPvcOperStatus_Object = MibTableColumn
mpAtmCCStaticPvcOperStatus = _MpAtmCCStaticPvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 16),
    _MpAtmCCStaticPvcOperStatus_Type()
)
mpAtmCCStaticPvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcOperStatus.setStatus("mandatory")
_MpAtmCCStaticPvcPvcId_Type = Integer32
_MpAtmCCStaticPvcPvcId_Object = MibTableColumn
mpAtmCCStaticPvcPvcId = _MpAtmCCStaticPvcPvcId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 17),
    _MpAtmCCStaticPvcPvcId_Type()
)
mpAtmCCStaticPvcPvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcPvcId.setStatus("mandatory")
_MpAtmCCStaticPvcSeqNo_Type = Integer32
_MpAtmCCStaticPvcSeqNo_Object = MibTableColumn
mpAtmCCStaticPvcSeqNo = _MpAtmCCStaticPvcSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 18),
    _MpAtmCCStaticPvcSeqNo_Type()
)
mpAtmCCStaticPvcSeqNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcSeqNo.setStatus("mandatory")
_MpAtmCCStaticPvcPgcRequest_Type = Integer32
_MpAtmCCStaticPvcPgcRequest_Object = MibTableColumn
mpAtmCCStaticPvcPgcRequest = _MpAtmCCStaticPvcPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 19),
    _MpAtmCCStaticPvcPgcRequest_Type()
)
mpAtmCCStaticPvcPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcPgcRequest.setStatus("mandatory")


class _MpAtmCCStaticPvcCfgStatus_Type(Integer32):
    """Custom type mpAtmCCStaticPvcCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCStaticPvcCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCStaticPvcCfgStatus_Object = MibTableColumn
mpAtmCCStaticPvcCfgStatus = _MpAtmCCStaticPvcCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 98),
    _MpAtmCCStaticPvcCfgStatus_Type()
)
mpAtmCCStaticPvcCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcCfgStatus.setStatus("mandatory")
_MpAtmCCStaticPvcErrInfo_Type = Integer32
_MpAtmCCStaticPvcErrInfo_Object = MibTableColumn
mpAtmCCStaticPvcErrInfo = _MpAtmCCStaticPvcErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 2, 2, 1, 99),
    _MpAtmCCStaticPvcErrInfo_Type()
)
mpAtmCCStaticPvcErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCStaticPvcErrInfo.setStatus("mandatory")
_MpAtmCCSoftPVPC_ObjectIdentity = ObjectIdentity
mpAtmCCSoftPVPC = _MpAtmCCSoftPVPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3)
)
_MpAtmCCSoftPvpTable_Object = MibTable
mpAtmCCSoftPvpTable = _MpAtmCCSoftPvpTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpTable.setStatus("mandatory")
_MpAtmCCSoftPvpEntry_Object = MibTableRow
mpAtmCCSoftPvpEntry = _MpAtmCCSoftPvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1)
)
mpAtmCCSoftPvpEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpLeafReference"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpEntry.setStatus("mandatory")


class _MpAtmCCSoftPvpLeafReference_Type(Integer32):
    """Custom type mpAtmCCSoftPvpLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpAtmCCSoftPvpLeafReference_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpLeafReference_Object = MibTableColumn
mpAtmCCSoftPvpLeafReference = _MpAtmCCSoftPvpLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 1),
    _MpAtmCCSoftPvpLeafReference_Type()
)
mpAtmCCSoftPvpLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpLeafReference.setStatus("mandatory")
_MpAtmCCSoftPvpIfIndex_Type = Integer32
_MpAtmCCSoftPvpIfIndex_Object = MibTableColumn
mpAtmCCSoftPvpIfIndex = _MpAtmCCSoftPvpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 2),
    _MpAtmCCSoftPvpIfIndex_Type()
)
mpAtmCCSoftPvpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpIfIndex.setStatus("mandatory")
_MpAtmCCSoftPvpVpi_Type = Integer32
_MpAtmCCSoftPvpVpi_Object = MibTableColumn
mpAtmCCSoftPvpVpi = _MpAtmCCSoftPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 3),
    _MpAtmCCSoftPvpVpi_Type()
)
mpAtmCCSoftPvpVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpVpi.setStatus("mandatory")
_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvpReceiveTrafficDescrIndex = _MpAtmCCSoftPvpReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 4),
    _MpAtmCCSoftPvpReceiveTrafficDescrIndex_Type()
)
mpAtmCCSoftPvpReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvpTransmitTrafficDescrIndex = _MpAtmCCSoftPvpTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 5),
    _MpAtmCCSoftPvpTransmitTrafficDescrIndex_Type()
)
mpAtmCCSoftPvpTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvpTargetAddress_Type = AtmAddr
_MpAtmCCSoftPvpTargetAddress_Object = MibTableColumn
mpAtmCCSoftPvpTargetAddress = _MpAtmCCSoftPvpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 6),
    _MpAtmCCSoftPvpTargetAddress_Type()
)
mpAtmCCSoftPvpTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpTargetAddress.setStatus("mandatory")


class _MpAtmCCSoftPvpTargetVpi_Type(Integer32):
    """Custom type mpAtmCCSoftPvpTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCSoftPvpTargetVpi_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpTargetVpi_Object = MibTableColumn
mpAtmCCSoftPvpTargetVpi = _MpAtmCCSoftPvpTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 7),
    _MpAtmCCSoftPvpTargetVpi_Type()
)
mpAtmCCSoftPvpTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpTargetVpi.setStatus("mandatory")


class _MpAtmCCSoftPvpLastReleaseCause_Type(Integer32):
    """Custom type mpAtmCCSoftPvpLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MpAtmCCSoftPvpLastReleaseCause_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpLastReleaseCause_Object = MibTableColumn
mpAtmCCSoftPvpLastReleaseCause = _MpAtmCCSoftPvpLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 8),
    _MpAtmCCSoftPvpLastReleaseCause_Type()
)
mpAtmCCSoftPvpLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpLastReleaseCause.setStatus("mandatory")


class _MpAtmCCSoftPvpLastReleaseDiagnostic_Type(OctetString):
    """Custom type mpAtmCCSoftPvpLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpAtmCCSoftPvpLastReleaseDiagnostic_Type.__name__ = "OctetString"
_MpAtmCCSoftPvpLastReleaseDiagnostic_Object = MibTableColumn
mpAtmCCSoftPvpLastReleaseDiagnostic = _MpAtmCCSoftPvpLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 9),
    _MpAtmCCSoftPvpLastReleaseDiagnostic_Type()
)
mpAtmCCSoftPvpLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpLastReleaseDiagnostic.setStatus("mandatory")


class _MpAtmCCSoftPvpPriority_Type(Integer32):
    """Custom type mpAtmCCSoftPvpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCSoftPvpPriority_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpPriority_Object = MibTableColumn
mpAtmCCSoftPvpPriority = _MpAtmCCSoftPvpPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 10),
    _MpAtmCCSoftPvpPriority_Type()
)
mpAtmCCSoftPvpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpPriority.setStatus("mandatory")
_MpAtmCCSoftPvpCladType_Type = MpAtmCCCladType
_MpAtmCCSoftPvpCladType_Object = MibTableColumn
mpAtmCCSoftPvpCladType = _MpAtmCCSoftPvpCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 11),
    _MpAtmCCSoftPvpCladType_Type()
)
mpAtmCCSoftPvpCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCladType.setStatus("mandatory")
_MpAtmCCSoftPvpOriginalAddress_Type = AtmAddr
_MpAtmCCSoftPvpOriginalAddress_Object = MibTableColumn
mpAtmCCSoftPvpOriginalAddress = _MpAtmCCSoftPvpOriginalAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 12),
    _MpAtmCCSoftPvpOriginalAddress_Type()
)
mpAtmCCSoftPvpOriginalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpOriginalAddress.setStatus("mandatory")


class _MpAtmCCSoftPvpAdminStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCSoftPvpAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpAdminStatus_Object = MibTableColumn
mpAtmCCSoftPvpAdminStatus = _MpAtmCCSoftPvpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 13),
    _MpAtmCCSoftPvpAdminStatus_Type()
)
mpAtmCCSoftPvpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpAdminStatus.setStatus("mandatory")
_MpAtmCCSoftPvpOperStatus_Type = Integer32
_MpAtmCCSoftPvpOperStatus_Object = MibTableColumn
mpAtmCCSoftPvpOperStatus = _MpAtmCCSoftPvpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 14),
    _MpAtmCCSoftPvpOperStatus_Type()
)
mpAtmCCSoftPvpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpOperStatus.setStatus("mandatory")
_MpAtmCCSoftPvpPgcRequest_Type = Integer32
_MpAtmCCSoftPvpPgcRequest_Object = MibTableColumn
mpAtmCCSoftPvpPgcRequest = _MpAtmCCSoftPvpPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 15),
    _MpAtmCCSoftPvpPgcRequest_Type()
)
mpAtmCCSoftPvpPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpPgcRequest.setStatus("mandatory")


class _MpAtmCCSoftPvpCfgStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCSoftPvpCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCfgStatus_Object = MibTableColumn
mpAtmCCSoftPvpCfgStatus = _MpAtmCCSoftPvpCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 98),
    _MpAtmCCSoftPvpCfgStatus_Type()
)
mpAtmCCSoftPvpCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCfgStatus.setStatus("mandatory")
_MpAtmCCSoftPvpErrInfo_Type = Integer32
_MpAtmCCSoftPvpErrInfo_Object = MibTableColumn
mpAtmCCSoftPvpErrInfo = _MpAtmCCSoftPvpErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 1, 1, 99),
    _MpAtmCCSoftPvpErrInfo_Type()
)
mpAtmCCSoftPvpErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpErrInfo.setStatus("mandatory")
_MpAtmCCSoftPvcTable_Object = MibTable
mpAtmCCSoftPvcTable = _MpAtmCCSoftPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcTable.setStatus("mandatory")
_MpAtmCCSoftPvcEntry_Object = MibTableRow
mpAtmCCSoftPvcEntry = _MpAtmCCSoftPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1)
)
mpAtmCCSoftPvcEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcLeafReference"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcEntry.setStatus("mandatory")


class _MpAtmCCSoftPvcLeafReference_Type(Integer32):
    """Custom type mpAtmCCSoftPvcLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpAtmCCSoftPvcLeafReference_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcLeafReference_Object = MibTableColumn
mpAtmCCSoftPvcLeafReference = _MpAtmCCSoftPvcLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 1),
    _MpAtmCCSoftPvcLeafReference_Type()
)
mpAtmCCSoftPvcLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcLeafReference.setStatus("mandatory")
_MpAtmCCSoftPvcIfIndex_Type = Integer32
_MpAtmCCSoftPvcIfIndex_Object = MibTableColumn
mpAtmCCSoftPvcIfIndex = _MpAtmCCSoftPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 2),
    _MpAtmCCSoftPvcIfIndex_Type()
)
mpAtmCCSoftPvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcIfIndex.setStatus("mandatory")
_MpAtmCCSoftPvcVpi_Type = Integer32
_MpAtmCCSoftPvcVpi_Object = MibTableColumn
mpAtmCCSoftPvcVpi = _MpAtmCCSoftPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 3),
    _MpAtmCCSoftPvcVpi_Type()
)
mpAtmCCSoftPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcVpi.setStatus("mandatory")
_MpAtmCCSoftPvcVci_Type = Integer32
_MpAtmCCSoftPvcVci_Object = MibTableColumn
mpAtmCCSoftPvcVci = _MpAtmCCSoftPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 4),
    _MpAtmCCSoftPvcVci_Type()
)
mpAtmCCSoftPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcVci.setStatus("mandatory")
_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvcReceiveTrafficDescrIndex = _MpAtmCCSoftPvcReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 5),
    _MpAtmCCSoftPvcReceiveTrafficDescrIndex_Type()
)
mpAtmCCSoftPvcReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvcTransmitTrafficDescrIndex = _MpAtmCCSoftPvcTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 6),
    _MpAtmCCSoftPvcTransmitTrafficDescrIndex_Type()
)
mpAtmCCSoftPvcTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvcTargetAddress_Type = AtmAddr
_MpAtmCCSoftPvcTargetAddress_Object = MibTableColumn
mpAtmCCSoftPvcTargetAddress = _MpAtmCCSoftPvcTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 7),
    _MpAtmCCSoftPvcTargetAddress_Type()
)
mpAtmCCSoftPvcTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcTargetAddress.setStatus("mandatory")


class _MpAtmCCSoftPvcTargetVpi_Type(Integer32):
    """Custom type mpAtmCCSoftPvcTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCSoftPvcTargetVpi_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcTargetVpi_Object = MibTableColumn
mpAtmCCSoftPvcTargetVpi = _MpAtmCCSoftPvcTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 8),
    _MpAtmCCSoftPvcTargetVpi_Type()
)
mpAtmCCSoftPvcTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcTargetVpi.setStatus("mandatory")


class _MpAtmCCSoftPvcTargetVci_Type(Integer32):
    """Custom type mpAtmCCSoftPvcTargetVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpAtmCCSoftPvcTargetVci_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcTargetVci_Object = MibTableColumn
mpAtmCCSoftPvcTargetVci = _MpAtmCCSoftPvcTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 9),
    _MpAtmCCSoftPvcTargetVci_Type()
)
mpAtmCCSoftPvcTargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcTargetVci.setStatus("mandatory")


class _MpAtmCCSoftPvcLastReleaseCause_Type(Integer32):
    """Custom type mpAtmCCSoftPvcLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MpAtmCCSoftPvcLastReleaseCause_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcLastReleaseCause_Object = MibTableColumn
mpAtmCCSoftPvcLastReleaseCause = _MpAtmCCSoftPvcLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 10),
    _MpAtmCCSoftPvcLastReleaseCause_Type()
)
mpAtmCCSoftPvcLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcLastReleaseCause.setStatus("mandatory")


class _MpAtmCCSoftPvcLastReleaseDiagnostic_Type(OctetString):
    """Custom type mpAtmCCSoftPvcLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpAtmCCSoftPvcLastReleaseDiagnostic_Type.__name__ = "OctetString"
_MpAtmCCSoftPvcLastReleaseDiagnostic_Object = MibTableColumn
mpAtmCCSoftPvcLastReleaseDiagnostic = _MpAtmCCSoftPvcLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 11),
    _MpAtmCCSoftPvcLastReleaseDiagnostic_Type()
)
mpAtmCCSoftPvcLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcLastReleaseDiagnostic.setStatus("mandatory")


class _MpAtmCCSoftPvcPriority_Type(Integer32):
    """Custom type mpAtmCCSoftPvcPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCSoftPvcPriority_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcPriority_Object = MibTableColumn
mpAtmCCSoftPvcPriority = _MpAtmCCSoftPvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 12),
    _MpAtmCCSoftPvcPriority_Type()
)
mpAtmCCSoftPvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcPriority.setStatus("mandatory")
_MpAtmCCSoftPvcCladType_Type = MpAtmCCCladType
_MpAtmCCSoftPvcCladType_Object = MibTableColumn
mpAtmCCSoftPvcCladType = _MpAtmCCSoftPvcCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 13),
    _MpAtmCCSoftPvcCladType_Type()
)
mpAtmCCSoftPvcCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCladType.setStatus("mandatory")
_MpAtmCCSoftPvcOriginalAddress_Type = AtmAddr
_MpAtmCCSoftPvcOriginalAddress_Object = MibTableColumn
mpAtmCCSoftPvcOriginalAddress = _MpAtmCCSoftPvcOriginalAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 14),
    _MpAtmCCSoftPvcOriginalAddress_Type()
)
mpAtmCCSoftPvcOriginalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcOriginalAddress.setStatus("mandatory")


class _MpAtmCCSoftPvcAdminStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCSoftPvcAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcAdminStatus_Object = MibTableColumn
mpAtmCCSoftPvcAdminStatus = _MpAtmCCSoftPvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 15),
    _MpAtmCCSoftPvcAdminStatus_Type()
)
mpAtmCCSoftPvcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcAdminStatus.setStatus("mandatory")
_MpAtmCCSoftPvcOperStatus_Type = Integer32
_MpAtmCCSoftPvcOperStatus_Object = MibTableColumn
mpAtmCCSoftPvcOperStatus = _MpAtmCCSoftPvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 16),
    _MpAtmCCSoftPvcOperStatus_Type()
)
mpAtmCCSoftPvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcOperStatus.setStatus("mandatory")
_MpAtmCCSoftPvcPgcRequest_Type = Integer32
_MpAtmCCSoftPvcPgcRequest_Object = MibTableColumn
mpAtmCCSoftPvcPgcRequest = _MpAtmCCSoftPvcPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 17),
    _MpAtmCCSoftPvcPgcRequest_Type()
)
mpAtmCCSoftPvcPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcPgcRequest.setStatus("mandatory")


class _MpAtmCCSoftPvcCfgStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCSoftPvcCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCfgStatus_Object = MibTableColumn
mpAtmCCSoftPvcCfgStatus = _MpAtmCCSoftPvcCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 98),
    _MpAtmCCSoftPvcCfgStatus_Type()
)
mpAtmCCSoftPvcCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCfgStatus.setStatus("mandatory")
_MpAtmCCSoftPvcErrInfo_Type = Integer32
_MpAtmCCSoftPvcErrInfo_Object = MibTableColumn
mpAtmCCSoftPvcErrInfo = _MpAtmCCSoftPvcErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 2, 1, 99),
    _MpAtmCCSoftPvcErrInfo_Type()
)
mpAtmCCSoftPvcErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcErrInfo.setStatus("mandatory")
_MpAtmCCSoftPvpCalledTable_Object = MibTable
mpAtmCCSoftPvpCalledTable = _MpAtmCCSoftPvpCalledTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledTable.setStatus("mandatory")
_MpAtmCCSoftPvpCalledEntry_Object = MibTableRow
mpAtmCCSoftPvpCalledEntry = _MpAtmCCSoftPvpCalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1)
)
mpAtmCCSoftPvpCalledEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpCalledLeafReference"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpCalledIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvpCalledVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledEntry.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledLeafReference_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpAtmCCSoftPvpCalledLeafReference_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledLeafReference_Object = MibTableColumn
mpAtmCCSoftPvpCalledLeafReference = _MpAtmCCSoftPvpCalledLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 1),
    _MpAtmCCSoftPvpCalledLeafReference_Type()
)
mpAtmCCSoftPvpCalledLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledLeafReference.setStatus("mandatory")
_MpAtmCCSoftPvpCalledIfIndex_Type = Integer32
_MpAtmCCSoftPvpCalledIfIndex_Object = MibTableColumn
mpAtmCCSoftPvpCalledIfIndex = _MpAtmCCSoftPvpCalledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 2),
    _MpAtmCCSoftPvpCalledIfIndex_Type()
)
mpAtmCCSoftPvpCalledIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledIfIndex.setStatus("mandatory")
_MpAtmCCSoftPvpCalledVpi_Type = Integer32
_MpAtmCCSoftPvpCalledVpi_Object = MibTableColumn
mpAtmCCSoftPvpCalledVpi = _MpAtmCCSoftPvpCalledVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 3),
    _MpAtmCCSoftPvpCalledVpi_Type()
)
mpAtmCCSoftPvpCalledVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledVpi.setStatus("mandatory")
_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex = _MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 4),
    _MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Type()
)
mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex = _MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 5),
    _MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Type()
)
mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvpCalledTargetAddress_Type = AtmAddr
_MpAtmCCSoftPvpCalledTargetAddress_Object = MibTableColumn
mpAtmCCSoftPvpCalledTargetAddress = _MpAtmCCSoftPvpCalledTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 6),
    _MpAtmCCSoftPvpCalledTargetAddress_Type()
)
mpAtmCCSoftPvpCalledTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledTargetAddress.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledTargetVpi_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCSoftPvpCalledTargetVpi_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledTargetVpi_Object = MibTableColumn
mpAtmCCSoftPvpCalledTargetVpi = _MpAtmCCSoftPvpCalledTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 7),
    _MpAtmCCSoftPvpCalledTargetVpi_Type()
)
mpAtmCCSoftPvpCalledTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledTargetVpi.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledLastReleaseCause_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MpAtmCCSoftPvpCalledLastReleaseCause_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledLastReleaseCause_Object = MibTableColumn
mpAtmCCSoftPvpCalledLastReleaseCause = _MpAtmCCSoftPvpCalledLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 8),
    _MpAtmCCSoftPvpCalledLastReleaseCause_Type()
)
mpAtmCCSoftPvpCalledLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledLastReleaseCause.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type(OctetString):
    """Custom type mpAtmCCSoftPvpCalledLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type.__name__ = "OctetString"
_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Object = MibTableColumn
mpAtmCCSoftPvpCalledLastReleaseDiagnostic = _MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 9),
    _MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type()
)
mpAtmCCSoftPvpCalledLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledLastReleaseDiagnostic.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledPriority_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCSoftPvpCalledPriority_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledPriority_Object = MibTableColumn
mpAtmCCSoftPvpCalledPriority = _MpAtmCCSoftPvpCalledPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 10),
    _MpAtmCCSoftPvpCalledPriority_Type()
)
mpAtmCCSoftPvpCalledPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledPriority.setStatus("mandatory")
_MpAtmCCSoftPvpCalledCladType_Type = MpAtmCCCladType
_MpAtmCCSoftPvpCalledCladType_Object = MibTableColumn
mpAtmCCSoftPvpCalledCladType = _MpAtmCCSoftPvpCalledCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 11),
    _MpAtmCCSoftPvpCalledCladType_Type()
)
mpAtmCCSoftPvpCalledCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledCladType.setStatus("mandatory")
_MpAtmCCSoftPvpCalledOriginalAddress_Type = AtmAddr
_MpAtmCCSoftPvpCalledOriginalAddress_Object = MibTableColumn
mpAtmCCSoftPvpCalledOriginalAddress = _MpAtmCCSoftPvpCalledOriginalAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 12),
    _MpAtmCCSoftPvpCalledOriginalAddress_Type()
)
mpAtmCCSoftPvpCalledOriginalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledOriginalAddress.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledAdminStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCSoftPvpCalledAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledAdminStatus_Object = MibTableColumn
mpAtmCCSoftPvpCalledAdminStatus = _MpAtmCCSoftPvpCalledAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 13),
    _MpAtmCCSoftPvpCalledAdminStatus_Type()
)
mpAtmCCSoftPvpCalledAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledAdminStatus.setStatus("mandatory")
_MpAtmCCSoftPvpCalledOperStatus_Type = Integer32
_MpAtmCCSoftPvpCalledOperStatus_Object = MibTableColumn
mpAtmCCSoftPvpCalledOperStatus = _MpAtmCCSoftPvpCalledOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 14),
    _MpAtmCCSoftPvpCalledOperStatus_Type()
)
mpAtmCCSoftPvpCalledOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledOperStatus.setStatus("mandatory")
_MpAtmCCSoftPvpCalledPgcRequest_Type = Integer32
_MpAtmCCSoftPvpCalledPgcRequest_Object = MibTableColumn
mpAtmCCSoftPvpCalledPgcRequest = _MpAtmCCSoftPvpCalledPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 15),
    _MpAtmCCSoftPvpCalledPgcRequest_Type()
)
mpAtmCCSoftPvpCalledPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledPgcRequest.setStatus("mandatory")


class _MpAtmCCSoftPvpCalledCfgStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvpCalledCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCSoftPvpCalledCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvpCalledCfgStatus_Object = MibTableColumn
mpAtmCCSoftPvpCalledCfgStatus = _MpAtmCCSoftPvpCalledCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 98),
    _MpAtmCCSoftPvpCalledCfgStatus_Type()
)
mpAtmCCSoftPvpCalledCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledCfgStatus.setStatus("mandatory")
_MpAtmCCSoftPvpCalledErrInfo_Type = Integer32
_MpAtmCCSoftPvpCalledErrInfo_Object = MibTableColumn
mpAtmCCSoftPvpCalledErrInfo = _MpAtmCCSoftPvpCalledErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 3, 1, 99),
    _MpAtmCCSoftPvpCalledErrInfo_Type()
)
mpAtmCCSoftPvpCalledErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvpCalledErrInfo.setStatus("mandatory")
_MpAtmCCSoftPvcCalledTable_Object = MibTable
mpAtmCCSoftPvcCalledTable = _MpAtmCCSoftPvcCalledTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4)
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledTable.setStatus("mandatory")
_MpAtmCCSoftPvcCalledEntry_Object = MibTableRow
mpAtmCCSoftPvcCalledEntry = _MpAtmCCSoftPvcCalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1)
)
mpAtmCCSoftPvcCalledEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcCalledLeafReference"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcCalledIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcCalledVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCSoftPvcCalledVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledEntry.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledLeafReference_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpAtmCCSoftPvcCalledLeafReference_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledLeafReference_Object = MibTableColumn
mpAtmCCSoftPvcCalledLeafReference = _MpAtmCCSoftPvcCalledLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 1),
    _MpAtmCCSoftPvcCalledLeafReference_Type()
)
mpAtmCCSoftPvcCalledLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledLeafReference.setStatus("mandatory")
_MpAtmCCSoftPvcCalledIfIndex_Type = Integer32
_MpAtmCCSoftPvcCalledIfIndex_Object = MibTableColumn
mpAtmCCSoftPvcCalledIfIndex = _MpAtmCCSoftPvcCalledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 2),
    _MpAtmCCSoftPvcCalledIfIndex_Type()
)
mpAtmCCSoftPvcCalledIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledIfIndex.setStatus("mandatory")
_MpAtmCCSoftPvcCalledVpi_Type = Integer32
_MpAtmCCSoftPvcCalledVpi_Object = MibTableColumn
mpAtmCCSoftPvcCalledVpi = _MpAtmCCSoftPvcCalledVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 3),
    _MpAtmCCSoftPvcCalledVpi_Type()
)
mpAtmCCSoftPvcCalledVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledVpi.setStatus("mandatory")
_MpAtmCCSoftPvcCalledVci_Type = Integer32
_MpAtmCCSoftPvcCalledVci_Object = MibTableColumn
mpAtmCCSoftPvcCalledVci = _MpAtmCCSoftPvcCalledVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 4),
    _MpAtmCCSoftPvcCalledVci_Type()
)
mpAtmCCSoftPvcCalledVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledVci.setStatus("mandatory")
_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex = _MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 5),
    _MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Type()
)
mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex = _MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 6),
    _MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Type()
)
mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCSoftPvcCalledTargetAddress_Type = AtmAddr
_MpAtmCCSoftPvcCalledTargetAddress_Object = MibTableColumn
mpAtmCCSoftPvcCalledTargetAddress = _MpAtmCCSoftPvcCalledTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 7),
    _MpAtmCCSoftPvcCalledTargetAddress_Type()
)
mpAtmCCSoftPvcCalledTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledTargetAddress.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledTargetVpi_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpAtmCCSoftPvcCalledTargetVpi_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledTargetVpi_Object = MibTableColumn
mpAtmCCSoftPvcCalledTargetVpi = _MpAtmCCSoftPvcCalledTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 8),
    _MpAtmCCSoftPvcCalledTargetVpi_Type()
)
mpAtmCCSoftPvcCalledTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledTargetVpi.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledTargetVci_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledTargetVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpAtmCCSoftPvcCalledTargetVci_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledTargetVci_Object = MibTableColumn
mpAtmCCSoftPvcCalledTargetVci = _MpAtmCCSoftPvcCalledTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 9),
    _MpAtmCCSoftPvcCalledTargetVci_Type()
)
mpAtmCCSoftPvcCalledTargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledTargetVci.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledLastReleaseCause_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MpAtmCCSoftPvcCalledLastReleaseCause_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledLastReleaseCause_Object = MibTableColumn
mpAtmCCSoftPvcCalledLastReleaseCause = _MpAtmCCSoftPvcCalledLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 10),
    _MpAtmCCSoftPvcCalledLastReleaseCause_Type()
)
mpAtmCCSoftPvcCalledLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledLastReleaseCause.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type(OctetString):
    """Custom type mpAtmCCSoftPvcCalledLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type.__name__ = "OctetString"
_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Object = MibTableColumn
mpAtmCCSoftPvcCalledLastReleaseDiagnostic = _MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 11),
    _MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type()
)
mpAtmCCSoftPvcCalledLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledLastReleaseDiagnostic.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledPriority_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCSoftPvcCalledPriority_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledPriority_Object = MibTableColumn
mpAtmCCSoftPvcCalledPriority = _MpAtmCCSoftPvcCalledPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 12),
    _MpAtmCCSoftPvcCalledPriority_Type()
)
mpAtmCCSoftPvcCalledPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledPriority.setStatus("mandatory")
_MpAtmCCSoftPvcCalledCladType_Type = MpAtmCCCladType
_MpAtmCCSoftPvcCalledCladType_Object = MibTableColumn
mpAtmCCSoftPvcCalledCladType = _MpAtmCCSoftPvcCalledCladType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 13),
    _MpAtmCCSoftPvcCalledCladType_Type()
)
mpAtmCCSoftPvcCalledCladType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledCladType.setStatus("mandatory")
_MpAtmCCSoftPvcCalledOriginalAddress_Type = AtmAddr
_MpAtmCCSoftPvcCalledOriginalAddress_Object = MibTableColumn
mpAtmCCSoftPvcCalledOriginalAddress = _MpAtmCCSoftPvcCalledOriginalAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 14),
    _MpAtmCCSoftPvcCalledOriginalAddress_Type()
)
mpAtmCCSoftPvcCalledOriginalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledOriginalAddress.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledAdminStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCSoftPvcCalledAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledAdminStatus_Object = MibTableColumn
mpAtmCCSoftPvcCalledAdminStatus = _MpAtmCCSoftPvcCalledAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 15),
    _MpAtmCCSoftPvcCalledAdminStatus_Type()
)
mpAtmCCSoftPvcCalledAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledAdminStatus.setStatus("mandatory")
_MpAtmCCSoftPvcCalledOperStatus_Type = Integer32
_MpAtmCCSoftPvcCalledOperStatus_Object = MibTableColumn
mpAtmCCSoftPvcCalledOperStatus = _MpAtmCCSoftPvcCalledOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 16),
    _MpAtmCCSoftPvcCalledOperStatus_Type()
)
mpAtmCCSoftPvcCalledOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledOperStatus.setStatus("mandatory")
_MpAtmCCSoftPvcCalledPgcRequest_Type = Integer32
_MpAtmCCSoftPvcCalledPgcRequest_Object = MibTableColumn
mpAtmCCSoftPvcCalledPgcRequest = _MpAtmCCSoftPvcCalledPgcRequest_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 17),
    _MpAtmCCSoftPvcCalledPgcRequest_Type()
)
mpAtmCCSoftPvcCalledPgcRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledPgcRequest.setStatus("mandatory")


class _MpAtmCCSoftPvcCalledCfgStatus_Type(Integer32):
    """Custom type mpAtmCCSoftPvcCalledCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCSoftPvcCalledCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCSoftPvcCalledCfgStatus_Object = MibTableColumn
mpAtmCCSoftPvcCalledCfgStatus = _MpAtmCCSoftPvcCalledCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 98),
    _MpAtmCCSoftPvcCalledCfgStatus_Type()
)
mpAtmCCSoftPvcCalledCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledCfgStatus.setStatus("mandatory")
_MpAtmCCSoftPvcCalledErrInfo_Type = Integer32
_MpAtmCCSoftPvcCalledErrInfo_Object = MibTableColumn
mpAtmCCSoftPvcCalledErrInfo = _MpAtmCCSoftPvcCalledErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 3, 4, 1, 99),
    _MpAtmCCSoftPvcCalledErrInfo_Type()
)
mpAtmCCSoftPvcCalledErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSoftPvcCalledErrInfo.setStatus("mandatory")
_MpAtmCCStatistics_ObjectIdentity = ObjectIdentity
mpAtmCCStatistics = _MpAtmCCStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4)
)
_MpAtmCCVpStatisticsTable_Object = MibTable
mpAtmCCVpStatisticsTable = _MpAtmCCVpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCVpStatisticsTable.setStatus("mandatory")
_MpAtmCCVpStatisticsEntry_Object = MibTableRow
mpAtmCCVpStatisticsEntry = _MpAtmCCVpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1)
)
mpAtmCCVpStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCVpStatVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCVpStatisticsEntry.setStatus("mandatory")
_MpAtmCCVpStatVpi_Type = Integer32
_MpAtmCCVpStatVpi_Object = MibTableColumn
mpAtmCCVpStatVpi = _MpAtmCCVpStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 1),
    _MpAtmCCVpStatVpi_Type()
)
mpAtmCCVpStatVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVpStatVpi.setStatus("mandatory")
_MpAtmCCVpStatInCells_Type = OctetString
_MpAtmCCVpStatInCells_Object = MibTableColumn
mpAtmCCVpStatInCells = _MpAtmCCVpStatInCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 2),
    _MpAtmCCVpStatInCells_Type()
)
mpAtmCCVpStatInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatInCells.setStatus("mandatory")
_MpAtmCCVpStatInCellsCounters_Type = Counter32
_MpAtmCCVpStatInCellsCounters_Object = MibTableColumn
mpAtmCCVpStatInCellsCounters = _MpAtmCCVpStatInCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 3),
    _MpAtmCCVpStatInCellsCounters_Type()
)
mpAtmCCVpStatInCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatInCellsCounters.setStatus("mandatory")
_MpAtmCCVpStatOutCells_Type = OctetString
_MpAtmCCVpStatOutCells_Object = MibTableColumn
mpAtmCCVpStatOutCells = _MpAtmCCVpStatOutCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 4),
    _MpAtmCCVpStatOutCells_Type()
)
mpAtmCCVpStatOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatOutCells.setStatus("mandatory")
_MpAtmCCVpStatOutCellsCounters_Type = Counter32
_MpAtmCCVpStatOutCellsCounters_Object = MibTableColumn
mpAtmCCVpStatOutCellsCounters = _MpAtmCCVpStatOutCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 5),
    _MpAtmCCVpStatOutCellsCounters_Type()
)
mpAtmCCVpStatOutCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatOutCellsCounters.setStatus("mandatory")
_MpAtmCCVpStatInDropCells_Type = OctetString
_MpAtmCCVpStatInDropCells_Object = MibTableColumn
mpAtmCCVpStatInDropCells = _MpAtmCCVpStatInDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 6),
    _MpAtmCCVpStatInDropCells_Type()
)
mpAtmCCVpStatInDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatInDropCells.setStatus("mandatory")
_MpAtmCCVpStatInDropCellsCounters_Type = Counter32
_MpAtmCCVpStatInDropCellsCounters_Object = MibTableColumn
mpAtmCCVpStatInDropCellsCounters = _MpAtmCCVpStatInDropCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 1, 1, 7),
    _MpAtmCCVpStatInDropCellsCounters_Type()
)
mpAtmCCVpStatInDropCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpStatInDropCellsCounters.setStatus("mandatory")
_MpAtmCCVcStatisticsTable_Object = MibTable
mpAtmCCVcStatisticsTable = _MpAtmCCVcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCVcStatisticsTable.setStatus("mandatory")
_MpAtmCCVcStatisticsEntry_Object = MibTableRow
mpAtmCCVcStatisticsEntry = _MpAtmCCVcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1)
)
mpAtmCCVcStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCVcStatVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCVcStatVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCVcStatisticsEntry.setStatus("mandatory")
_MpAtmCCVcStatVpi_Type = Integer32
_MpAtmCCVcStatVpi_Object = MibTableColumn
mpAtmCCVcStatVpi = _MpAtmCCVcStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 1),
    _MpAtmCCVcStatVpi_Type()
)
mpAtmCCVcStatVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVcStatVpi.setStatus("mandatory")
_MpAtmCCVcStatVci_Type = Integer32
_MpAtmCCVcStatVci_Object = MibTableColumn
mpAtmCCVcStatVci = _MpAtmCCVcStatVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 2),
    _MpAtmCCVcStatVci_Type()
)
mpAtmCCVcStatVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVcStatVci.setStatus("mandatory")
_MpAtmCCVcStatInCells_Type = OctetString
_MpAtmCCVcStatInCells_Object = MibTableColumn
mpAtmCCVcStatInCells = _MpAtmCCVcStatInCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 3),
    _MpAtmCCVcStatInCells_Type()
)
mpAtmCCVcStatInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatInCells.setStatus("mandatory")
_MpAtmCCVcStatInCellsCounters_Type = Counter32
_MpAtmCCVcStatInCellsCounters_Object = MibTableColumn
mpAtmCCVcStatInCellsCounters = _MpAtmCCVcStatInCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 4),
    _MpAtmCCVcStatInCellsCounters_Type()
)
mpAtmCCVcStatInCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatInCellsCounters.setStatus("mandatory")
_MpAtmCCVcStatOutCells_Type = OctetString
_MpAtmCCVcStatOutCells_Object = MibTableColumn
mpAtmCCVcStatOutCells = _MpAtmCCVcStatOutCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 5),
    _MpAtmCCVcStatOutCells_Type()
)
mpAtmCCVcStatOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatOutCells.setStatus("mandatory")
_MpAtmCCVcStatOutCellsCounters_Type = Counter32
_MpAtmCCVcStatOutCellsCounters_Object = MibTableColumn
mpAtmCCVcStatOutCellsCounters = _MpAtmCCVcStatOutCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 6),
    _MpAtmCCVcStatOutCellsCounters_Type()
)
mpAtmCCVcStatOutCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatOutCellsCounters.setStatus("mandatory")
_MpAtmCCVcStatInDropCells_Type = OctetString
_MpAtmCCVcStatInDropCells_Object = MibTableColumn
mpAtmCCVcStatInDropCells = _MpAtmCCVcStatInDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 7),
    _MpAtmCCVcStatInDropCells_Type()
)
mpAtmCCVcStatInDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatInDropCells.setStatus("mandatory")
_MpAtmCCVcStatInDropCellsCounters_Type = Counter32
_MpAtmCCVcStatInDropCellsCounters_Object = MibTableColumn
mpAtmCCVcStatInDropCellsCounters = _MpAtmCCVcStatInDropCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 2, 1, 8),
    _MpAtmCCVcStatInDropCellsCounters_Type()
)
mpAtmCCVcStatInDropCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVcStatInDropCellsCounters.setStatus("mandatory")
_MpAtmCCOuspStatisticsTable_Object = MibTable
mpAtmCCOuspStatisticsTable = _MpAtmCCOuspStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCOuspStatisticsTable.setStatus("mandatory")
_MpAtmCCOuspStatisticsEntry_Object = MibTableRow
mpAtmCCOuspStatisticsEntry = _MpAtmCCOuspStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1)
)
mpAtmCCOuspStatisticsEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCOuspStatIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCOuspStatisticsEntry.setStatus("mandatory")
_MpAtmCCOuspStatIndex_Type = Integer32
_MpAtmCCOuspStatIndex_Object = MibTableColumn
mpAtmCCOuspStatIndex = _MpAtmCCOuspStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 1),
    _MpAtmCCOuspStatIndex_Type()
)
mpAtmCCOuspStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatIndex.setStatus("mandatory")
_MpAtmCCOuspStatRcvCrcErrCellsCounters_Type = Counter32
_MpAtmCCOuspStatRcvCrcErrCellsCounters_Object = MibTableColumn
mpAtmCCOuspStatRcvCrcErrCellsCounters = _MpAtmCCOuspStatRcvCrcErrCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 2),
    _MpAtmCCOuspStatRcvCrcErrCellsCounters_Type()
)
mpAtmCCOuspStatRcvCrcErrCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatRcvCrcErrCellsCounters.setStatus("mandatory")
_MpAtmCCOuspStatSendOfifoFullCounters_Type = Counter32
_MpAtmCCOuspStatSendOfifoFullCounters_Object = MibTableColumn
mpAtmCCOuspStatSendOfifoFullCounters = _MpAtmCCOuspStatSendOfifoFullCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 3),
    _MpAtmCCOuspStatSendOfifoFullCounters_Type()
)
mpAtmCCOuspStatSendOfifoFullCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatSendOfifoFullCounters.setStatus("mandatory")
_MpAtmCCOuspStatRcvBufOverCounters_Type = Counter32
_MpAtmCCOuspStatRcvBufOverCounters_Object = MibTableColumn
mpAtmCCOuspStatRcvBufOverCounters = _MpAtmCCOuspStatRcvBufOverCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 4),
    _MpAtmCCOuspStatRcvBufOverCounters_Type()
)
mpAtmCCOuspStatRcvBufOverCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatRcvBufOverCounters.setStatus("mandatory")
_MpAtmCCOuspStatRcvUnknownCellsCounters_Type = Counter32
_MpAtmCCOuspStatRcvUnknownCellsCounters_Object = MibTableColumn
mpAtmCCOuspStatRcvUnknownCellsCounters = _MpAtmCCOuspStatRcvUnknownCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 5),
    _MpAtmCCOuspStatRcvUnknownCellsCounters_Type()
)
mpAtmCCOuspStatRcvUnknownCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatRcvUnknownCellsCounters.setStatus("mandatory")
_MpAtmCCOuspStatRcvInvalidCellsCounters_Type = Counter32
_MpAtmCCOuspStatRcvInvalidCellsCounters_Object = MibTableColumn
mpAtmCCOuspStatRcvInvalidCellsCounters = _MpAtmCCOuspStatRcvInvalidCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 6),
    _MpAtmCCOuspStatRcvInvalidCellsCounters_Type()
)
mpAtmCCOuspStatRcvInvalidCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatRcvInvalidCellsCounters.setStatus("mandatory")
_MpAtmCCOuspStatSendScheduleErrorCounters_Type = Counter32
_MpAtmCCOuspStatSendScheduleErrorCounters_Object = MibTableColumn
mpAtmCCOuspStatSendScheduleErrorCounters = _MpAtmCCOuspStatSendScheduleErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 7),
    _MpAtmCCOuspStatSendScheduleErrorCounters_Type()
)
mpAtmCCOuspStatSendScheduleErrorCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatSendScheduleErrorCounters.setStatus("mandatory")
_MpAtmCCOuspStatRcvScheduleErrorCounters_Type = Counter32
_MpAtmCCOuspStatRcvScheduleErrorCounters_Object = MibTableColumn
mpAtmCCOuspStatRcvScheduleErrorCounters = _MpAtmCCOuspStatRcvScheduleErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 8),
    _MpAtmCCOuspStatRcvScheduleErrorCounters_Type()
)
mpAtmCCOuspStatRcvScheduleErrorCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatRcvScheduleErrorCounters.setStatus("mandatory")
_MpAtmCCOuspStatSendInvalidCdvCounters_Type = Counter32
_MpAtmCCOuspStatSendInvalidCdvCounters_Object = MibTableColumn
mpAtmCCOuspStatSendInvalidCdvCounters = _MpAtmCCOuspStatSendInvalidCdvCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 3, 1, 9),
    _MpAtmCCOuspStatSendInvalidCdvCounters_Type()
)
mpAtmCCOuspStatSendInvalidCdvCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCOuspStatSendInvalidCdvCounters.setStatus("mandatory")
_MpAtmCCPhyStatisticsTable_Object = MibTable
mpAtmCCPhyStatisticsTable = _MpAtmCCPhyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4)
)
if mibBuilder.loadTexts:
    mpAtmCCPhyStatisticsTable.setStatus("mandatory")
_MpAtmCCPhyStatisticsEntry_Object = MibTableRow
mpAtmCCPhyStatisticsEntry = _MpAtmCCPhyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1)
)
mpAtmCCPhyStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPhyStatisticsEntry.setStatus("mandatory")
_MpAtmCCPhyStatTmtCellsCounters_Type = Counter32
_MpAtmCCPhyStatTmtCellsCounters_Object = MibTableColumn
mpAtmCCPhyStatTmtCellsCounters = _MpAtmCCPhyStatTmtCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 1),
    _MpAtmCCPhyStatTmtCellsCounters_Type()
)
mpAtmCCPhyStatTmtCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatTmtCellsCounters.setStatus("mandatory")
_MpAtmCCPhyStatRcvCellsCounters_Type = Counter32
_MpAtmCCPhyStatRcvCellsCounters_Object = MibTableColumn
mpAtmCCPhyStatRcvCellsCounters = _MpAtmCCPhyStatRcvCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 2),
    _MpAtmCCPhyStatRcvCellsCounters_Type()
)
mpAtmCCPhyStatRcvCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatRcvCellsCounters.setStatus("mandatory")
_MpAtmCCPhyStatCorrectHecErrCounters_Type = Counter32
_MpAtmCCPhyStatCorrectHecErrCounters_Object = MibTableColumn
mpAtmCCPhyStatCorrectHecErrCounters = _MpAtmCCPhyStatCorrectHecErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 3),
    _MpAtmCCPhyStatCorrectHecErrCounters_Type()
)
mpAtmCCPhyStatCorrectHecErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatCorrectHecErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatUncorrectHecErrCounters_Type = Counter32
_MpAtmCCPhyStatUncorrectHecErrCounters_Object = MibTableColumn
mpAtmCCPhyStatUncorrectHecErrCounters = _MpAtmCCPhyStatUncorrectHecErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 4),
    _MpAtmCCPhyStatUncorrectHecErrCounters_Type()
)
mpAtmCCPhyStatUncorrectHecErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatUncorrectHecErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatB1ErrCounters_Type = Counter32
_MpAtmCCPhyStatB1ErrCounters_Object = MibTableColumn
mpAtmCCPhyStatB1ErrCounters = _MpAtmCCPhyStatB1ErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 5),
    _MpAtmCCPhyStatB1ErrCounters_Type()
)
mpAtmCCPhyStatB1ErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatB1ErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatB2ErrCounters_Type = Counter32
_MpAtmCCPhyStatB2ErrCounters_Object = MibTableColumn
mpAtmCCPhyStatB2ErrCounters = _MpAtmCCPhyStatB2ErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 6),
    _MpAtmCCPhyStatB2ErrCounters_Type()
)
mpAtmCCPhyStatB2ErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatB2ErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatB3ErrCounters_Type = Counter32
_MpAtmCCPhyStatB3ErrCounters_Object = MibTableColumn
mpAtmCCPhyStatB3ErrCounters = _MpAtmCCPhyStatB3ErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 7),
    _MpAtmCCPhyStatB3ErrCounters_Type()
)
mpAtmCCPhyStatB3ErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatB3ErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatFebeCounters_Type = Counter32
_MpAtmCCPhyStatFebeCounters_Object = MibTableColumn
mpAtmCCPhyStatFebeCounters = _MpAtmCCPhyStatFebeCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 8),
    _MpAtmCCPhyStatFebeCounters_Type()
)
mpAtmCCPhyStatFebeCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatFebeCounters.setStatus("mandatory")
_MpAtmCCPhyStatSymbolErrCounters_Type = Counter32
_MpAtmCCPhyStatSymbolErrCounters_Object = MibTableColumn
mpAtmCCPhyStatSymbolErrCounters = _MpAtmCCPhyStatSymbolErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 9),
    _MpAtmCCPhyStatSymbolErrCounters_Type()
)
mpAtmCCPhyStatSymbolErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatSymbolErrCounters.setStatus("mandatory")
_MpAtmCCPhyStatParityErrCounters_Type = Counter32
_MpAtmCCPhyStatParityErrCounters_Object = MibTableColumn
mpAtmCCPhyStatParityErrCounters = _MpAtmCCPhyStatParityErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 4, 1, 10),
    _MpAtmCCPhyStatParityErrCounters_Type()
)
mpAtmCCPhyStatParityErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPhyStatParityErrCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatisticsTable_Object = MibTable
mpAtmCCPortAlarmStatisticsTable = _MpAtmCCPortAlarmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5)
)
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatisticsTable.setStatus("mandatory")
_MpAtmCCPortAlarmStatisticsEntry_Object = MibTableRow
mpAtmCCPortAlarmStatisticsEntry = _MpAtmCCPortAlarmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1)
)
mpAtmCCPortAlarmStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatisticsEntry.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLosCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLosCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLosCounters = _MpAtmCCPortAlarmStatRedLosCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 1),
    _MpAtmCCPortAlarmStatRedLosCounters_Type()
)
mpAtmCCPortAlarmStatRedLosCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLosCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLofCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLofCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLofCounters = _MpAtmCCPortAlarmStatRedLofCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 2),
    _MpAtmCCPortAlarmStatRedLofCounters_Type()
)
mpAtmCCPortAlarmStatRedLofCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLofCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedMsAisCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedMsAisCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedMsAisCounters = _MpAtmCCPortAlarmStatRedMsAisCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 3),
    _MpAtmCCPortAlarmStatRedMsAisCounters_Type()
)
mpAtmCCPortAlarmStatRedMsAisCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedMsAisCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLopCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLopCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLopCounters = _MpAtmCCPortAlarmStatRedLopCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 4),
    _MpAtmCCPortAlarmStatRedLopCounters_Type()
)
mpAtmCCPortAlarmStatRedLopCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLopCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedPAisCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedPAisCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedPAisCounters = _MpAtmCCPortAlarmStatRedPAisCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 5),
    _MpAtmCCPortAlarmStatRedPAisCounters_Type()
)
mpAtmCCPortAlarmStatRedPAisCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedPAisCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLocCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLocCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLocCounters = _MpAtmCCPortAlarmStatRedLocCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 6),
    _MpAtmCCPortAlarmStatRedLocCounters_Type()
)
mpAtmCCPortAlarmStatRedLocCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLocCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedResetCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedResetCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedResetCounters = _MpAtmCCPortAlarmStatRedResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 7),
    _MpAtmCCPortAlarmStatRedResetCounters_Type()
)
mpAtmCCPortAlarmStatRedResetCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedResetCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedCcRedCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedCcRedCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedCcRedCounters = _MpAtmCCPortAlarmStatRedCcRedCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 8),
    _MpAtmCCPortAlarmStatRedCcRedCounters_Type()
)
mpAtmCCPortAlarmStatRedCcRedCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedCcRedCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedOofCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedOofCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedOofCounters = _MpAtmCCPortAlarmStatRedOofCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 9),
    _MpAtmCCPortAlarmStatRedOofCounters_Type()
)
mpAtmCCPortAlarmStatRedOofCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedOofCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedAisCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedAisCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedAisCounters = _MpAtmCCPortAlarmStatRedAisCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 10),
    _MpAtmCCPortAlarmStatRedAisCounters_Type()
)
mpAtmCCPortAlarmStatRedAisCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedAisCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedPOofCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedPOofCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedPOofCounters = _MpAtmCCPortAlarmStatRedPOofCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 11),
    _MpAtmCCPortAlarmStatRedPOofCounters_Type()
)
mpAtmCCPortAlarmStatRedPOofCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedPOofCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedBadSigCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedBadSigCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedBadSigCounters = _MpAtmCCPortAlarmStatRedBadSigCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 12),
    _MpAtmCCPortAlarmStatRedBadSigCounters_Type()
)
mpAtmCCPortAlarmStatRedBadSigCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedBadSigCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLcdCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLcdCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLcdCounters = _MpAtmCCPortAlarmStatRedLcdCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 13),
    _MpAtmCCPortAlarmStatRedLcdCounters_Type()
)
mpAtmCCPortAlarmStatRedLcdCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLcdCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedLinkAisCounters_Type = Counter32
_MpAtmCCPortAlarmStatRedLinkAisCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedLinkAisCounters = _MpAtmCCPortAlarmStatRedLinkAisCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 14),
    _MpAtmCCPortAlarmStatRedLinkAisCounters_Type()
)
mpAtmCCPortAlarmStatRedLinkAisCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedLinkAisCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatRedInfo0Counters_Type = Counter32
_MpAtmCCPortAlarmStatRedInfo0Counters_Object = MibTableColumn
mpAtmCCPortAlarmStatRedInfo0Counters = _MpAtmCCPortAlarmStatRedInfo0Counters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 15),
    _MpAtmCCPortAlarmStatRedInfo0Counters_Type()
)
mpAtmCCPortAlarmStatRedInfo0Counters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatRedInfo0Counters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelMsRdiCounters_Type = Counter32
_MpAtmCCPortAlarmStatYelMsRdiCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelMsRdiCounters = _MpAtmCCPortAlarmStatYelMsRdiCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 16),
    _MpAtmCCPortAlarmStatYelMsRdiCounters_Type()
)
mpAtmCCPortAlarmStatYelMsRdiCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelMsRdiCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelPRdiCounters_Type = Counter32
_MpAtmCCPortAlarmStatYelPRdiCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelPRdiCounters = _MpAtmCCPortAlarmStatYelPRdiCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 17),
    _MpAtmCCPortAlarmStatYelPRdiCounters_Type()
)
mpAtmCCPortAlarmStatYelPRdiCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelPRdiCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelCcYelCounters_Type = Counter32
_MpAtmCCPortAlarmStatYelCcYelCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelCcYelCounters = _MpAtmCCPortAlarmStatYelCcYelCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 18),
    _MpAtmCCPortAlarmStatYelCcYelCounters_Type()
)
mpAtmCCPortAlarmStatYelCcYelCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelCcYelCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelRaiCounters_Type = Counter32
_MpAtmCCPortAlarmStatYelRaiCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelRaiCounters = _MpAtmCCPortAlarmStatYelRaiCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 19),
    _MpAtmCCPortAlarmStatYelRaiCounters_Type()
)
mpAtmCCPortAlarmStatYelRaiCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelRaiCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelPRaiCounters_Type = Counter32
_MpAtmCCPortAlarmStatYelPRaiCounters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelPRaiCounters = _MpAtmCCPortAlarmStatYelPRaiCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 20),
    _MpAtmCCPortAlarmStatYelPRaiCounters_Type()
)
mpAtmCCPortAlarmStatYelPRaiCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelPRaiCounters.setStatus("mandatory")
_MpAtmCCPortAlarmStatYelInfo2Counters_Type = Counter32
_MpAtmCCPortAlarmStatYelInfo2Counters_Object = MibTableColumn
mpAtmCCPortAlarmStatYelInfo2Counters = _MpAtmCCPortAlarmStatYelInfo2Counters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 5, 1, 21),
    _MpAtmCCPortAlarmStatYelInfo2Counters_Type()
)
mpAtmCCPortAlarmStatYelInfo2Counters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortAlarmStatYelInfo2Counters.setStatus("mandatory")
_MpAtmCCVpTunnellingStatisticsTable_Object = MibTable
mpAtmCCVpTunnellingStatisticsTable = _MpAtmCCVpTunnellingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 6)
)
if mibBuilder.loadTexts:
    mpAtmCCVpTunnellingStatisticsTable.setStatus("mandatory")
_MpAtmCCVpTunnellingStatisticsEntry_Object = MibTableRow
mpAtmCCVpTunnellingStatisticsEntry = _MpAtmCCVpTunnellingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 6, 1)
)
mpAtmCCVpTunnellingStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCVpTunnellingStatisticsEntry.setStatus("mandatory")
_MpAtmCCVpTunStatTmtCellsCounters_Type = Counter32
_MpAtmCCVpTunStatTmtCellsCounters_Object = MibTableColumn
mpAtmCCVpTunStatTmtCellsCounters = _MpAtmCCVpTunStatTmtCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 6, 1, 1),
    _MpAtmCCVpTunStatTmtCellsCounters_Type()
)
mpAtmCCVpTunStatTmtCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunStatTmtCellsCounters.setStatus("mandatory")
_MpAtmCCVpTunStatRcvCellsCounters_Type = Counter32
_MpAtmCCVpTunStatRcvCellsCounters_Object = MibTableColumn
mpAtmCCVpTunStatRcvCellsCounters = _MpAtmCCVpTunStatRcvCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 6, 1, 2),
    _MpAtmCCVpTunStatRcvCellsCounters_Type()
)
mpAtmCCVpTunStatRcvCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunStatRcvCellsCounters.setStatus("mandatory")
_MpAtmCCVccStatisticsRegTable_Object = MibTable
mpAtmCCVccStatisticsRegTable = _MpAtmCCVccStatisticsRegTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7)
)
if mibBuilder.loadTexts:
    mpAtmCCVccStatisticsRegTable.setStatus("mandatory")
_MpAtmCCVccStatisticsRegEntry_Object = MibTableRow
mpAtmCCVccStatisticsRegEntry = _MpAtmCCVccStatisticsRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1)
)
mpAtmCCVccStatisticsRegEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCVccStatRegVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCVccStatRegVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCVccStatisticsRegEntry.setStatus("mandatory")
_MpAtmCCVccStatRegVpi_Type = Integer32
_MpAtmCCVccStatRegVpi_Object = MibTableColumn
mpAtmCCVccStatRegVpi = _MpAtmCCVccStatRegVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 1),
    _MpAtmCCVccStatRegVpi_Type()
)
mpAtmCCVccStatRegVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegVpi.setStatus("mandatory")
_MpAtmCCVccStatRegVci_Type = Integer32
_MpAtmCCVccStatRegVci_Object = MibTableColumn
mpAtmCCVccStatRegVci = _MpAtmCCVccStatRegVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 2),
    _MpAtmCCVccStatRegVci_Type()
)
mpAtmCCVccStatRegVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegVci.setStatus("mandatory")
_MpAtmCCVccStatRegInCellsCounters_Type = Counter32
_MpAtmCCVccStatRegInCellsCounters_Object = MibTableColumn
mpAtmCCVccStatRegInCellsCounters = _MpAtmCCVccStatRegInCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 3),
    _MpAtmCCVccStatRegInCellsCounters_Type()
)
mpAtmCCVccStatRegInCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegInCellsCounters.setStatus("mandatory")
_MpAtmCCVccStatRegOutCellsCounters_Type = Counter32
_MpAtmCCVccStatRegOutCellsCounters_Object = MibTableColumn
mpAtmCCVccStatRegOutCellsCounters = _MpAtmCCVccStatRegOutCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 4),
    _MpAtmCCVccStatRegOutCellsCounters_Type()
)
mpAtmCCVccStatRegOutCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegOutCellsCounters.setStatus("mandatory")


class _MpAtmCCVccStatRegStatus_Type(Integer32):
    """Custom type mpAtmCCVccStatRegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_MpAtmCCVccStatRegStatus_Type.__name__ = "Integer32"
_MpAtmCCVccStatRegStatus_Object = MibTableColumn
mpAtmCCVccStatRegStatus = _MpAtmCCVccStatRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 5),
    _MpAtmCCVccStatRegStatus_Type()
)
mpAtmCCVccStatRegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegStatus.setStatus("mandatory")
_MpAtmCCVccStatRegErrInfo_Type = Integer32
_MpAtmCCVccStatRegErrInfo_Object = MibTableColumn
mpAtmCCVccStatRegErrInfo = _MpAtmCCVccStatRegErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 4, 7, 1, 99),
    _MpAtmCCVccStatRegErrInfo_Type()
)
mpAtmCCVccStatRegErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatRegErrInfo.setStatus("mandatory")
_MpAtmCCResourceControl_ObjectIdentity = ObjectIdentity
mpAtmCCResourceControl = _MpAtmCCResourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5)
)
_MpAtmCCPortResourceInfomationTable_Object = MibTable
mpAtmCCPortResourceInfomationTable = _MpAtmCCPortResourceInfomationTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCPortResourceInfomationTable.setStatus("mandatory")
_MpAtmCCPortResourceInfomationEntry_Object = MibTableRow
mpAtmCCPortResourceInfomationEntry = _MpAtmCCPortResourceInfomationEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1)
)
mpAtmCCPortResourceInfomationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPortResourceInfomationEntry.setStatus("mandatory")
_MpAtmCCPortResInfoPortSpeed_Type = Gauge32
_MpAtmCCPortResInfoPortSpeed_Object = MibTableColumn
mpAtmCCPortResInfoPortSpeed = _MpAtmCCPortResInfoPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 1),
    _MpAtmCCPortResInfoPortSpeed_Type()
)
mpAtmCCPortResInfoPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoPortSpeed.setStatus("mandatory")
_MpAtmCCPortResInfoMaxVpiBits_Type = Integer32
_MpAtmCCPortResInfoMaxVpiBits_Object = MibTableColumn
mpAtmCCPortResInfoMaxVpiBits = _MpAtmCCPortResInfoMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 2),
    _MpAtmCCPortResInfoMaxVpiBits_Type()
)
mpAtmCCPortResInfoMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxVpiBits.setStatus("mandatory")
_MpAtmCCPortResInfoMaxVciBits_Type = Integer32
_MpAtmCCPortResInfoMaxVciBits_Object = MibTableColumn
mpAtmCCPortResInfoMaxVciBits = _MpAtmCCPortResInfoMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 3),
    _MpAtmCCPortResInfoMaxVciBits_Type()
)
mpAtmCCPortResInfoMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxVciBits.setStatus("mandatory")
_MpAtmCCPortResInfoMaxVPC_Type = Integer32
_MpAtmCCPortResInfoMaxVPC_Object = MibTableColumn
mpAtmCCPortResInfoMaxVPC = _MpAtmCCPortResInfoMaxVPC_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 4),
    _MpAtmCCPortResInfoMaxVPC_Type()
)
mpAtmCCPortResInfoMaxVPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxVPC.setStatus("mandatory")
_MpAtmCCPortResInfoMaxVCC_Type = Integer32
_MpAtmCCPortResInfoMaxVCC_Object = MibTableColumn
mpAtmCCPortResInfoMaxVCC = _MpAtmCCPortResInfoMaxVCC_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 5),
    _MpAtmCCPortResInfoMaxVCC_Type()
)
mpAtmCCPortResInfoMaxVCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxVCC.setStatus("mandatory")
_MpAtmCCPortResInfoMaxSvpcVpi_Type = Integer32
_MpAtmCCPortResInfoMaxSvpcVpi_Object = MibTableColumn
mpAtmCCPortResInfoMaxSvpcVpi = _MpAtmCCPortResInfoMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 6),
    _MpAtmCCPortResInfoMaxSvpcVpi_Type()
)
mpAtmCCPortResInfoMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxSvpcVpi.setStatus("mandatory")
_MpAtmCCPortResInfoMaxSvccVpi_Type = Integer32
_MpAtmCCPortResInfoMaxSvccVpi_Object = MibTableColumn
mpAtmCCPortResInfoMaxSvccVpi = _MpAtmCCPortResInfoMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 7),
    _MpAtmCCPortResInfoMaxSvccVpi_Type()
)
mpAtmCCPortResInfoMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMaxSvccVpi.setStatus("mandatory")
_MpAtmCCPortResInfoMinSvccVci_Type = Integer32
_MpAtmCCPortResInfoMinSvccVci_Object = MibTableColumn
mpAtmCCPortResInfoMinSvccVci = _MpAtmCCPortResInfoMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 8),
    _MpAtmCCPortResInfoMinSvccVci_Type()
)
mpAtmCCPortResInfoMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoMinSvccVci.setStatus("mandatory")


class _MpAtmCCPortResInfoShaperKind_Type(Integer32):
    """Custom type mpAtmCCPortResInfoShaperKind based on Integer32"""
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
        *(("none", 1),
          ("vc", 3),
          ("vp", 2),
          ("vpAndVc", 4))
    )


_MpAtmCCPortResInfoShaperKind_Type.__name__ = "Integer32"
_MpAtmCCPortResInfoShaperKind_Object = MibTableColumn
mpAtmCCPortResInfoShaperKind = _MpAtmCCPortResInfoShaperKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 9),
    _MpAtmCCPortResInfoShaperKind_Type()
)
mpAtmCCPortResInfoShaperKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoShaperKind.setStatus("mandatory")


class _MpAtmCCPortResInfoVpTunnellingConfig_Type(Integer32):
    """Custom type mpAtmCCPortResInfoVpTunnellingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("notConfigured", 1))
    )


_MpAtmCCPortResInfoVpTunnellingConfig_Type.__name__ = "Integer32"
_MpAtmCCPortResInfoVpTunnellingConfig_Object = MibTableColumn
mpAtmCCPortResInfoVpTunnellingConfig = _MpAtmCCPortResInfoVpTunnellingConfig_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 10),
    _MpAtmCCPortResInfoVpTunnellingConfig_Type()
)
mpAtmCCPortResInfoVpTunnellingConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoVpTunnellingConfig.setStatus("mandatory")


class _MpAtmCCPortResInfoSvccVciHuntWay_Type(Integer32):
    """Custom type mpAtmCCPortResInfoSvccVciHuntWay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high2low", 2),
          ("low2high", 1))
    )


_MpAtmCCPortResInfoSvccVciHuntWay_Type.__name__ = "Integer32"
_MpAtmCCPortResInfoSvccVciHuntWay_Object = MibTableColumn
mpAtmCCPortResInfoSvccVciHuntWay = _MpAtmCCPortResInfoSvccVciHuntWay_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 11),
    _MpAtmCCPortResInfoSvccVciHuntWay_Type()
)
mpAtmCCPortResInfoSvccVciHuntWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoSvccVciHuntWay.setStatus("mandatory")
_MpAtmCCPortResInfoVpiCounters_Type = Counter32
_MpAtmCCPortResInfoVpiCounters_Object = MibTableColumn
mpAtmCCPortResInfoVpiCounters = _MpAtmCCPortResInfoVpiCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 12),
    _MpAtmCCPortResInfoVpiCounters_Type()
)
mpAtmCCPortResInfoVpiCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoVpiCounters.setStatus("mandatory")
_MpAtmCCPortResInfoVpcCounters_Type = Counter32
_MpAtmCCPortResInfoVpcCounters_Object = MibTableColumn
mpAtmCCPortResInfoVpcCounters = _MpAtmCCPortResInfoVpcCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 13),
    _MpAtmCCPortResInfoVpcCounters_Type()
)
mpAtmCCPortResInfoVpcCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoVpcCounters.setStatus("mandatory")
_MpAtmCCPortResInfoVccCounters_Type = Counter32
_MpAtmCCPortResInfoVccCounters_Object = MibTableColumn
mpAtmCCPortResInfoVccCounters = _MpAtmCCPortResInfoVccCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 1, 1, 14),
    _MpAtmCCPortResInfoVccCounters_Type()
)
mpAtmCCPortResInfoVccCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortResInfoVccCounters.setStatus("mandatory")
_MpAtmCCPortBandwidthInfomationTable_Object = MibTable
mpAtmCCPortBandwidthInfomationTable = _MpAtmCCPortBandwidthInfomationTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCPortBandwidthInfomationTable.setStatus("mandatory")
_MpAtmCCPortBandwidthInfomationEntry_Object = MibTableRow
mpAtmCCPortBandwidthInfomationEntry = _MpAtmCCPortBandwidthInfomationEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1)
)
mpAtmCCPortBandwidthInfomationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCPortBwInfoVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCPortBandwidthInfomationEntry.setStatus("mandatory")
_MpAtmCCPortBwInfoVpi_Type = Integer32
_MpAtmCCPortBwInfoVpi_Object = MibTableColumn
mpAtmCCPortBwInfoVpi = _MpAtmCCPortBwInfoVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 1),
    _MpAtmCCPortBwInfoVpi_Type()
)
mpAtmCCPortBwInfoVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoVpi.setStatus("mandatory")
_MpAtmCCPortBwInfoRawBandwidthBps_Type = Integer32
_MpAtmCCPortBwInfoRawBandwidthBps_Object = MibTableColumn
mpAtmCCPortBwInfoRawBandwidthBps = _MpAtmCCPortBwInfoRawBandwidthBps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 2),
    _MpAtmCCPortBwInfoRawBandwidthBps_Type()
)
mpAtmCCPortBwInfoRawBandwidthBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoRawBandwidthBps.setStatus("mandatory")
_MpAtmCCPortBwInfoRawBandwidthCps_Type = Integer32
_MpAtmCCPortBwInfoRawBandwidthCps_Object = MibTableColumn
mpAtmCCPortBwInfoRawBandwidthCps = _MpAtmCCPortBwInfoRawBandwidthCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 3),
    _MpAtmCCPortBwInfoRawBandwidthCps_Type()
)
mpAtmCCPortBwInfoRawBandwidthCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoRawBandwidthCps.setStatus("mandatory")
_MpAtmCCPortBwInfoTmitUsedBwCps_Type = Integer32
_MpAtmCCPortBwInfoTmitUsedBwCps_Object = MibTableColumn
mpAtmCCPortBwInfoTmitUsedBwCps = _MpAtmCCPortBwInfoTmitUsedBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 4),
    _MpAtmCCPortBwInfoTmitUsedBwCps_Type()
)
mpAtmCCPortBwInfoTmitUsedBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoTmitUsedBwCps.setStatus("mandatory")
_MpAtmCCPortBwInfoRcvUsedBwCps_Type = Integer32
_MpAtmCCPortBwInfoRcvUsedBwCps_Object = MibTableColumn
mpAtmCCPortBwInfoRcvUsedBwCps = _MpAtmCCPortBwInfoRcvUsedBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 5),
    _MpAtmCCPortBwInfoRcvUsedBwCps_Type()
)
mpAtmCCPortBwInfoRcvUsedBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoRcvUsedBwCps.setStatus("mandatory")
_MpAtmCCPortBwInfoVciCounters_Type = Integer32
_MpAtmCCPortBwInfoVciCounters_Object = MibTableColumn
mpAtmCCPortBwInfoVciCounters = _MpAtmCCPortBwInfoVciCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 2, 1, 6),
    _MpAtmCCPortBwInfoVciCounters_Type()
)
mpAtmCCPortBwInfoVciCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPortBwInfoVciCounters.setStatus("mandatory")
_MpAtmCCBwInfoPortTable_Object = MibTable
mpAtmCCBwInfoPortTable = _MpAtmCCBwInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortTable.setStatus("mandatory")
_MpAtmCCBwInfoPortEntry_Object = MibTableRow
mpAtmCCBwInfoPortEntry = _MpAtmCCBwInfoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1)
)
mpAtmCCBwInfoPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortEntry.setStatus("mandatory")
_MpAtmCCBwInfoPortRawBandwidthBps_Type = Integer32
_MpAtmCCBwInfoPortRawBandwidthBps_Object = MibTableColumn
mpAtmCCBwInfoPortRawBandwidthBps = _MpAtmCCBwInfoPortRawBandwidthBps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 1),
    _MpAtmCCBwInfoPortRawBandwidthBps_Type()
)
mpAtmCCBwInfoPortRawBandwidthBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortRawBandwidthBps.setStatus("mandatory")
_MpAtmCCBwInfoPortRawBandwidthCps_Type = Integer32
_MpAtmCCBwInfoPortRawBandwidthCps_Object = MibTableColumn
mpAtmCCBwInfoPortRawBandwidthCps = _MpAtmCCBwInfoPortRawBandwidthCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 2),
    _MpAtmCCBwInfoPortRawBandwidthCps_Type()
)
mpAtmCCBwInfoPortRawBandwidthCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortRawBandwidthCps.setStatus("mandatory")
_MpAtmCCBwInfoPortTmitUsedBwCps_Type = Integer32
_MpAtmCCBwInfoPortTmitUsedBwCps_Object = MibTableColumn
mpAtmCCBwInfoPortTmitUsedBwCps = _MpAtmCCBwInfoPortTmitUsedBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 3),
    _MpAtmCCBwInfoPortTmitUsedBwCps_Type()
)
mpAtmCCBwInfoPortTmitUsedBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortTmitUsedBwCps.setStatus("mandatory")
_MpAtmCCBwInfoPortRcvUsedBwCps_Type = Integer32
_MpAtmCCBwInfoPortRcvUsedBwCps_Object = MibTableColumn
mpAtmCCBwInfoPortRcvUsedBwCps = _MpAtmCCBwInfoPortRcvUsedBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 4),
    _MpAtmCCBwInfoPortRcvUsedBwCps_Type()
)
mpAtmCCBwInfoPortRcvUsedBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortRcvUsedBwCps.setStatus("mandatory")
_MpAtmCCBwInfoPortTmitRemainBwCps_Type = Integer32
_MpAtmCCBwInfoPortTmitRemainBwCps_Object = MibTableColumn
mpAtmCCBwInfoPortTmitRemainBwCps = _MpAtmCCBwInfoPortTmitRemainBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 5),
    _MpAtmCCBwInfoPortTmitRemainBwCps_Type()
)
mpAtmCCBwInfoPortTmitRemainBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortTmitRemainBwCps.setStatus("mandatory")
_MpAtmCCBwInfoPortRcvRemainBwCps_Type = Integer32
_MpAtmCCBwInfoPortRcvRemainBwCps_Object = MibTableColumn
mpAtmCCBwInfoPortRcvRemainBwCps = _MpAtmCCBwInfoPortRcvRemainBwCps_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 6),
    _MpAtmCCBwInfoPortRcvRemainBwCps_Type()
)
mpAtmCCBwInfoPortRcvRemainBwCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortRcvRemainBwCps.setStatus("mandatory")


class _MpAtmCCBwInfoPortVpTunneling_Type(Integer32):
    """Custom type mpAtmCCBwInfoPortVpTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpAtmCCBwInfoPortVpTunneling_Type.__name__ = "Integer32"
_MpAtmCCBwInfoPortVpTunneling_Object = MibTableColumn
mpAtmCCBwInfoPortVpTunneling = _MpAtmCCBwInfoPortVpTunneling_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 5, 3, 1, 7),
    _MpAtmCCBwInfoPortVpTunneling_Type()
)
mpAtmCCBwInfoPortVpTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCBwInfoPortVpTunneling.setStatus("mandatory")
_MpAtmCCProtocol_ObjectIdentity = ObjectIdentity
mpAtmCCProtocol = _MpAtmCCProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6)
)
_MpAtmCCSscopTable_Object = MibTable
mpAtmCCSscopTable = _MpAtmCCSscopTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCSscopTable.setStatus("mandatory")
_MpAtmCCSscopEntry_Object = MibTableRow
mpAtmCCSscopEntry = _MpAtmCCSscopEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1)
)
mpAtmCCSscopEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCSscopEntry.setStatus("mandatory")


class _MpAtmCCSscopTimerPoll_Type(Integer32):
    """Custom type mpAtmCCSscopTimerPoll based on Integer32"""
    defaultValue = 750


_MpAtmCCSscopTimerPoll_Object = MibTableColumn
mpAtmCCSscopTimerPoll = _MpAtmCCSscopTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 1),
    _MpAtmCCSscopTimerPoll_Type()
)
mpAtmCCSscopTimerPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopTimerPoll.setStatus("mandatory")


class _MpAtmCCSscopTimerNoResponce_Type(Integer32):
    """Custom type mpAtmCCSscopTimerNoResponce based on Integer32"""
    defaultValue = 7000


_MpAtmCCSscopTimerNoResponce_Object = MibTableColumn
mpAtmCCSscopTimerNoResponce = _MpAtmCCSscopTimerNoResponce_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 2),
    _MpAtmCCSscopTimerNoResponce_Type()
)
mpAtmCCSscopTimerNoResponce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopTimerNoResponce.setStatus("mandatory")


class _MpAtmCCSscopTimerKeepAlive_Type(Integer32):
    """Custom type mpAtmCCSscopTimerKeepAlive based on Integer32"""
    defaultValue = 2000


_MpAtmCCSscopTimerKeepAlive_Object = MibTableColumn
mpAtmCCSscopTimerKeepAlive = _MpAtmCCSscopTimerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 3),
    _MpAtmCCSscopTimerKeepAlive_Type()
)
mpAtmCCSscopTimerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopTimerKeepAlive.setStatus("mandatory")


class _MpAtmCCSscopTimerIdle_Type(Integer32):
    """Custom type mpAtmCCSscopTimerIdle based on Integer32"""
    defaultValue = 15000


_MpAtmCCSscopTimerIdle_Object = MibTableColumn
mpAtmCCSscopTimerIdle = _MpAtmCCSscopTimerIdle_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 4),
    _MpAtmCCSscopTimerIdle_Type()
)
mpAtmCCSscopTimerIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopTimerIdle.setStatus("mandatory")


class _MpAtmCCSscopTimerCc_Type(Integer32):
    """Custom type mpAtmCCSscopTimerCc based on Integer32"""
    defaultValue = 1000


_MpAtmCCSscopTimerCc_Object = MibTableColumn
mpAtmCCSscopTimerCc = _MpAtmCCSscopTimerCc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 5),
    _MpAtmCCSscopTimerCc_Type()
)
mpAtmCCSscopTimerCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopTimerCc.setStatus("mandatory")


class _MpAtmCCSscopMaxCc_Type(Integer32):
    """Custom type mpAtmCCSscopMaxCc based on Integer32"""
    defaultValue = 4


_MpAtmCCSscopMaxCc_Object = MibTableColumn
mpAtmCCSscopMaxCc = _MpAtmCCSscopMaxCc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 6),
    _MpAtmCCSscopMaxCc_Type()
)
mpAtmCCSscopMaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopMaxCc.setStatus("mandatory")


class _MpAtmCCSscopMaxPd_Type(Integer32):
    """Custom type mpAtmCCSscopMaxPd based on Integer32"""
    defaultValue = 25


_MpAtmCCSscopMaxPd_Object = MibTableColumn
mpAtmCCSscopMaxPd = _MpAtmCCSscopMaxPd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 7),
    _MpAtmCCSscopMaxPd_Type()
)
mpAtmCCSscopMaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopMaxPd.setStatus("mandatory")


class _MpAtmCCSscopMaxStat_Type(Integer32):
    """Custom type mpAtmCCSscopMaxStat based on Integer32"""
    defaultValue = 67


_MpAtmCCSscopMaxStat_Object = MibTableColumn
mpAtmCCSscopMaxStat = _MpAtmCCSscopMaxStat_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 8),
    _MpAtmCCSscopMaxStat_Type()
)
mpAtmCCSscopMaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSscopMaxStat.setStatus("mandatory")


class _MpAtmCCSscopClearBuffs_Type(Integer32):
    """Custom type mpAtmCCSscopClearBuffs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MpAtmCCSscopClearBuffs_Type.__name__ = "Integer32"
_MpAtmCCSscopClearBuffs_Object = MibTableColumn
mpAtmCCSscopClearBuffs = _MpAtmCCSscopClearBuffs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 9),
    _MpAtmCCSscopClearBuffs_Type()
)
mpAtmCCSscopClearBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSscopClearBuffs.setStatus("mandatory")


class _MpAtmCCSscopCredit_Type(Integer32):
    """Custom type mpAtmCCSscopCredit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MpAtmCCSscopCredit_Type.__name__ = "Integer32"
_MpAtmCCSscopCredit_Object = MibTableColumn
mpAtmCCSscopCredit = _MpAtmCCSscopCredit_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 1, 1, 10),
    _MpAtmCCSscopCredit_Type()
)
mpAtmCCSscopCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCSscopCredit.setStatus("mandatory")
_MpAtmCCIlmiTable_Object = MibTable
mpAtmCCIlmiTable = _MpAtmCCIlmiTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCIlmiTable.setStatus("mandatory")
_MpAtmCCIlmiEntry_Object = MibTableRow
mpAtmCCIlmiEntry = _MpAtmCCIlmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 2, 1)
)
mpAtmCCIlmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCIlmiEntry.setStatus("mandatory")


class _MpAtmCCIlmiConfigStatus_Type(Integer32):
    """Custom type mpAtmCCIlmiConfigStatus based on Integer32"""
    defaultValue = 1

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


_MpAtmCCIlmiConfigStatus_Type.__name__ = "Integer32"
_MpAtmCCIlmiConfigStatus_Object = MibTableColumn
mpAtmCCIlmiConfigStatus = _MpAtmCCIlmiConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 2, 1, 1),
    _MpAtmCCIlmiConfigStatus_Type()
)
mpAtmCCIlmiConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCIlmiConfigStatus.setStatus("mandatory")


class _MpAtmCClmiMaxTransmissions_Type(Integer32):
    """Custom type mpAtmCClmiMaxTransmissions based on Integer32"""
    defaultValue = 4


_MpAtmCClmiMaxTransmissions_Object = MibTableColumn
mpAtmCClmiMaxTransmissions = _MpAtmCClmiMaxTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 2, 1, 2),
    _MpAtmCClmiMaxTransmissions_Type()
)
mpAtmCClmiMaxTransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCClmiMaxTransmissions.setStatus("mandatory")


class _MpAtmCCIlmiRetransmitInterval_Type(Integer32):
    """Custom type mpAtmCCIlmiRetransmitInterval based on Integer32"""
    defaultValue = 5


_MpAtmCCIlmiRetransmitInterval_Object = MibTableColumn
mpAtmCCIlmiRetransmitInterval = _MpAtmCCIlmiRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 2, 1, 3),
    _MpAtmCCIlmiRetransmitInterval_Type()
)
mpAtmCCIlmiRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCIlmiRetransmitInterval.setStatus("mandatory")
_MpAtmCCSignallingTable_Object = MibTable
mpAtmCCSignallingTable = _MpAtmCCSignallingTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCSignallingTable.setStatus("mandatory")
_MpAtmCCSignallingEntry_Object = MibTableRow
mpAtmCCSignallingEntry = _MpAtmCCSignallingEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1)
)
mpAtmCCSignallingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCSignallingEntry.setStatus("mandatory")


class _MpAtmCCSignallingT301_Type(Integer32):
    """Custom type mpAtmCCSignallingT301 based on Integer32"""
    defaultValue = 180


_MpAtmCCSignallingT301_Object = MibTableColumn
mpAtmCCSignallingT301 = _MpAtmCCSignallingT301_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 1),
    _MpAtmCCSignallingT301_Type()
)
mpAtmCCSignallingT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT301.setStatus("mandatory")


class _MpAtmCCSignallingT303_Type(Integer32):
    """Custom type mpAtmCCSignallingT303 based on Integer32"""
    defaultValue = 4


_MpAtmCCSignallingT303_Object = MibTableColumn
mpAtmCCSignallingT303 = _MpAtmCCSignallingT303_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 2),
    _MpAtmCCSignallingT303_Type()
)
mpAtmCCSignallingT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT303.setStatus("mandatory")


class _MpAtmCCSignallingT308_Type(Integer32):
    """Custom type mpAtmCCSignallingT308 based on Integer32"""
    defaultValue = 30


_MpAtmCCSignallingT308_Object = MibTableColumn
mpAtmCCSignallingT308 = _MpAtmCCSignallingT308_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 3),
    _MpAtmCCSignallingT308_Type()
)
mpAtmCCSignallingT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT308.setStatus("mandatory")


class _MpAtmCCSignallingT309_Type(Integer32):
    """Custom type mpAtmCCSignallingT309 based on Integer32"""
    defaultValue = 10


_MpAtmCCSignallingT309_Object = MibTableColumn
mpAtmCCSignallingT309 = _MpAtmCCSignallingT309_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 4),
    _MpAtmCCSignallingT309_Type()
)
mpAtmCCSignallingT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT309.setStatus("mandatory")


class _MpAtmCCSignallingT310_Type(Integer32):
    """Custom type mpAtmCCSignallingT310 based on Integer32"""
    defaultValue = 30


_MpAtmCCSignallingT310_Object = MibTableColumn
mpAtmCCSignallingT310 = _MpAtmCCSignallingT310_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 5),
    _MpAtmCCSignallingT310_Type()
)
mpAtmCCSignallingT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT310.setStatus("mandatory")


class _MpAtmCCSignallingT313_Type(Integer32):
    """Custom type mpAtmCCSignallingT313 based on Integer32"""
    defaultValue = 4


_MpAtmCCSignallingT313_Object = MibTableColumn
mpAtmCCSignallingT313 = _MpAtmCCSignallingT313_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 6),
    _MpAtmCCSignallingT313_Type()
)
mpAtmCCSignallingT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT313.setStatus("mandatory")


class _MpAtmCCSignallingT316_Type(Integer32):
    """Custom type mpAtmCCSignallingT316 based on Integer32"""
    defaultValue = 120


_MpAtmCCSignallingT316_Object = MibTableColumn
mpAtmCCSignallingT316 = _MpAtmCCSignallingT316_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 7),
    _MpAtmCCSignallingT316_Type()
)
mpAtmCCSignallingT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT316.setStatus("mandatory")


class _MpAtmCCSignallingT317_Type(Integer32):
    """Custom type mpAtmCCSignallingT317 based on Integer32"""
    defaultValue = 180


_MpAtmCCSignallingT317_Object = MibTableColumn
mpAtmCCSignallingT317 = _MpAtmCCSignallingT317_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 8),
    _MpAtmCCSignallingT317_Type()
)
mpAtmCCSignallingT317.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT317.setStatus("mandatory")


class _MpAtmCCSignallingT322_Type(Integer32):
    """Custom type mpAtmCCSignallingT322 based on Integer32"""
    defaultValue = 4


_MpAtmCCSignallingT322_Object = MibTableColumn
mpAtmCCSignallingT322 = _MpAtmCCSignallingT322_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 9),
    _MpAtmCCSignallingT322_Type()
)
mpAtmCCSignallingT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT322.setStatus("mandatory")


class _MpAtmCCSignallingT331_Type(Integer32):
    """Custom type mpAtmCCSignallingT331 based on Integer32"""
    defaultValue = 60


_MpAtmCCSignallingT331_Object = MibTableColumn
mpAtmCCSignallingT331 = _MpAtmCCSignallingT331_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 10),
    _MpAtmCCSignallingT331_Type()
)
mpAtmCCSignallingT331.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT331.setStatus("mandatory")


class _MpAtmCCSignallingT397_Type(Integer32):
    """Custom type mpAtmCCSignallingT397 based on Integer32"""
    defaultValue = 180


_MpAtmCCSignallingT397_Object = MibTableColumn
mpAtmCCSignallingT397 = _MpAtmCCSignallingT397_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 11),
    _MpAtmCCSignallingT397_Type()
)
mpAtmCCSignallingT397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT397.setStatus("mandatory")


class _MpAtmCCSignallingT398_Type(Integer32):
    """Custom type mpAtmCCSignallingT398 based on Integer32"""
    defaultValue = 4


_MpAtmCCSignallingT398_Object = MibTableColumn
mpAtmCCSignallingT398 = _MpAtmCCSignallingT398_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 12),
    _MpAtmCCSignallingT398_Type()
)
mpAtmCCSignallingT398.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT398.setStatus("mandatory")


class _MpAtmCCSignallingT399_Type(Integer32):
    """Custom type mpAtmCCSignallingT399 based on Integer32"""
    defaultValue = 34


_MpAtmCCSignallingT399_Object = MibTableColumn
mpAtmCCSignallingT399 = _MpAtmCCSignallingT399_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 3, 1, 13),
    _MpAtmCCSignallingT399_Type()
)
mpAtmCCSignallingT399.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCSignallingT399.setStatus("mandatory")
_MpAtmCCProtocolTrapInfoTable_Object = MibTable
mpAtmCCProtocolTrapInfoTable = _MpAtmCCProtocolTrapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 4)
)
if mibBuilder.loadTexts:
    mpAtmCCProtocolTrapInfoTable.setStatus("mandatory")
_MpAtmCCProtocolTrapInfoEntry_Object = MibTableRow
mpAtmCCProtocolTrapInfoEntry = _MpAtmCCProtocolTrapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 4, 1)
)
mpAtmCCProtocolTrapInfoEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCProtocolTrapInfoIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCProtocolTrapInfoEntry.setStatus("mandatory")
_MpAtmCCProtocolTrapInfoIndex_Type = Integer32
_MpAtmCCProtocolTrapInfoIndex_Object = MibTableColumn
mpAtmCCProtocolTrapInfoIndex = _MpAtmCCProtocolTrapInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 4, 1, 1),
    _MpAtmCCProtocolTrapInfoIndex_Type()
)
mpAtmCCProtocolTrapInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCProtocolTrapInfoIndex.setStatus("mandatory")
_MpAtmCCProtocolTrapInfoCause_Type = Integer32
_MpAtmCCProtocolTrapInfoCause_Object = MibTableColumn
mpAtmCCProtocolTrapInfoCause = _MpAtmCCProtocolTrapInfoCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 6, 4, 1, 2),
    _MpAtmCCProtocolTrapInfoCause_Type()
)
mpAtmCCProtocolTrapInfoCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCProtocolTrapInfoCause.setStatus("mandatory")
_MpAtmCCPathTrace_ObjectIdentity = ObjectIdentity
mpAtmCCPathTrace = _MpAtmCCPathTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7)
)
_MpAtmCCVccStatusTable_Object = MibTable
mpAtmCCVccStatusTable = _MpAtmCCVccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCVccStatusTable.setStatus("mandatory")
_MpAtmCCVccStatusEntry_Object = MibTableRow
mpAtmCCVccStatusEntry = _MpAtmCCVccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1)
)
mpAtmCCVccStatusEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCVccStatusOrgPort"),
    (0, "MP-ATM-MIB", "mpAtmCCVccStatusOrgVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCVccStatusOrgVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCVccStatusEntry.setStatus("mandatory")
_MpAtmCCVccStatusOrgPort_Type = Integer32
_MpAtmCCVccStatusOrgPort_Object = MibTableColumn
mpAtmCCVccStatusOrgPort = _MpAtmCCVccStatusOrgPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 1),
    _MpAtmCCVccStatusOrgPort_Type()
)
mpAtmCCVccStatusOrgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOrgPort.setStatus("mandatory")
_MpAtmCCVccStatusOrgVpi_Type = Integer32
_MpAtmCCVccStatusOrgVpi_Object = MibTableColumn
mpAtmCCVccStatusOrgVpi = _MpAtmCCVccStatusOrgVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 2),
    _MpAtmCCVccStatusOrgVpi_Type()
)
mpAtmCCVccStatusOrgVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOrgVpi.setStatus("mandatory")
_MpAtmCCVccStatusOrgVci_Type = Integer32
_MpAtmCCVccStatusOrgVci_Object = MibTableColumn
mpAtmCCVccStatusOrgVci = _MpAtmCCVccStatusOrgVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 3),
    _MpAtmCCVccStatusOrgVci_Type()
)
mpAtmCCVccStatusOrgVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOrgVci.setStatus("mandatory")
_MpAtmCCVccStatusDestPort_Type = Integer32
_MpAtmCCVccStatusDestPort_Object = MibTableColumn
mpAtmCCVccStatusDestPort = _MpAtmCCVccStatusDestPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 4),
    _MpAtmCCVccStatusDestPort_Type()
)
mpAtmCCVccStatusDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusDestPort.setStatus("mandatory")
_MpAtmCCVccStatusDestVpi_Type = Integer32
_MpAtmCCVccStatusDestVpi_Object = MibTableColumn
mpAtmCCVccStatusDestVpi = _MpAtmCCVccStatusDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 5),
    _MpAtmCCVccStatusDestVpi_Type()
)
mpAtmCCVccStatusDestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusDestVpi.setStatus("mandatory")
_MpAtmCCVccStatusDestVci_Type = Integer32
_MpAtmCCVccStatusDestVci_Object = MibTableColumn
mpAtmCCVccStatusDestVci = _MpAtmCCVccStatusDestVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 6),
    _MpAtmCCVccStatusDestVci_Type()
)
mpAtmCCVccStatusDestVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusDestVci.setStatus("mandatory")


class _MpAtmCCVccStatusPathKind_Type(Integer32):
    """Custom type mpAtmCCVccStatusPathKind based on Integer32"""
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
        *(("insPvc", 3),
          ("pvc", 1),
          ("pvp", 4),
          ("softpvc", 2),
          ("softpvp", 5))
    )


_MpAtmCCVccStatusPathKind_Type.__name__ = "Integer32"
_MpAtmCCVccStatusPathKind_Object = MibTableColumn
mpAtmCCVccStatusPathKind = _MpAtmCCVccStatusPathKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 7),
    _MpAtmCCVccStatusPathKind_Type()
)
mpAtmCCVccStatusPathKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusPathKind.setStatus("mandatory")


class _MpAtmCCVccStatusOrgCallKind_Type(Integer32):
    """Custom type mpAtmCCVccStatusOrgCallKind based on Integer32"""
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
        *(("called", 4),
          ("calling", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_MpAtmCCVccStatusOrgCallKind_Type.__name__ = "Integer32"
_MpAtmCCVccStatusOrgCallKind_Object = MibTableColumn
mpAtmCCVccStatusOrgCallKind = _MpAtmCCVccStatusOrgCallKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 8),
    _MpAtmCCVccStatusOrgCallKind_Type()
)
mpAtmCCVccStatusOrgCallKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOrgCallKind.setStatus("mandatory")


class _MpAtmCCVccStatusDestCallKind_Type(Integer32):
    """Custom type mpAtmCCVccStatusDestCallKind based on Integer32"""
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
        *(("called", 4),
          ("calling", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_MpAtmCCVccStatusDestCallKind_Type.__name__ = "Integer32"
_MpAtmCCVccStatusDestCallKind_Object = MibTableColumn
mpAtmCCVccStatusDestCallKind = _MpAtmCCVccStatusDestCallKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 9),
    _MpAtmCCVccStatusDestCallKind_Type()
)
mpAtmCCVccStatusDestCallKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusDestCallKind.setStatus("mandatory")


class _MpAtmCCVccStatusAdminStatus_Type(Integer32):
    """Custom type mpAtmCCVccStatusAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCVccStatusAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCVccStatusAdminStatus_Object = MibTableColumn
mpAtmCCVccStatusAdminStatus = _MpAtmCCVccStatusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 10),
    _MpAtmCCVccStatusAdminStatus_Type()
)
mpAtmCCVccStatusAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusAdminStatus.setStatus("mandatory")


class _MpAtmCCVccStatusOperStatus_Type(Integer32):
    """Custom type mpAtmCCVccStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCVccStatusOperStatus_Type.__name__ = "Integer32"
_MpAtmCCVccStatusOperStatus_Object = MibTableColumn
mpAtmCCVccStatusOperStatus = _MpAtmCCVccStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 11),
    _MpAtmCCVccStatusOperStatus_Type()
)
mpAtmCCVccStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOperStatus.setStatus("mandatory")


class _MpAtmCCVccStatusInsStatus_Type(Integer32):
    """Custom type mpAtmCCVccStatusInsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insPort", 2),
          ("trunkPort", 1))
    )


_MpAtmCCVccStatusInsStatus_Type.__name__ = "Integer32"
_MpAtmCCVccStatusInsStatus_Object = MibTableColumn
mpAtmCCVccStatusInsStatus = _MpAtmCCVccStatusInsStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 12),
    _MpAtmCCVccStatusInsStatus_Type()
)
mpAtmCCVccStatusInsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusInsStatus.setStatus("mandatory")


class _MpAtmCCVccStatusOrgPortVpTunneling_Type(Integer32):
    """Custom type mpAtmCCVccStatusOrgPortVpTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpAtmCCVccStatusOrgPortVpTunneling_Type.__name__ = "Integer32"
_MpAtmCCVccStatusOrgPortVpTunneling_Object = MibTableColumn
mpAtmCCVccStatusOrgPortVpTunneling = _MpAtmCCVccStatusOrgPortVpTunneling_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 13),
    _MpAtmCCVccStatusOrgPortVpTunneling_Type()
)
mpAtmCCVccStatusOrgPortVpTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusOrgPortVpTunneling.setStatus("mandatory")


class _MpAtmCCVccStatusDestPortVpTunneling_Type(Integer32):
    """Custom type mpAtmCCVccStatusDestPortVpTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpAtmCCVccStatusDestPortVpTunneling_Type.__name__ = "Integer32"
_MpAtmCCVccStatusDestPortVpTunneling_Object = MibTableColumn
mpAtmCCVccStatusDestPortVpTunneling = _MpAtmCCVccStatusDestPortVpTunneling_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 14),
    _MpAtmCCVccStatusDestPortVpTunneling_Type()
)
mpAtmCCVccStatusDestPortVpTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusDestPortVpTunneling.setStatus("mandatory")


class _MpAtmCCVccStatusConnCastType_Type(Integer32):
    """Custom type mpAtmCCVccStatusConnCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p2mpLeaf", 3),
          ("p2mpRoot", 2),
          ("p2p", 1))
    )


_MpAtmCCVccStatusConnCastType_Type.__name__ = "Integer32"
_MpAtmCCVccStatusConnCastType_Object = MibTableColumn
mpAtmCCVccStatusConnCastType = _MpAtmCCVccStatusConnCastType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 1, 1, 15),
    _MpAtmCCVccStatusConnCastType_Type()
)
mpAtmCCVccStatusConnCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVccStatusConnCastType.setStatus("mandatory")
_MpAtmCCPvcTraceControlTable_Object = MibTable
mpAtmCCPvcTraceControlTable = _MpAtmCCPvcTraceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceControlTable.setStatus("mandatory")
_MpAtmCCPvcTraceCtlEntry_Object = MibTableRow
mpAtmCCPvcTraceCtlEntry = _MpAtmCCPvcTraceCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1)
)
mpAtmCCPvcTraceCtlEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCPvcTraceIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlEntry.setStatus("mandatory")


class _MpAtmCCPvcTraceIndex_Type(Integer32):
    """Custom type mpAtmCCPvcTraceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MpAtmCCPvcTraceIndex_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceIndex_Object = MibTableColumn
mpAtmCCPvcTraceIndex = _MpAtmCCPvcTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 1),
    _MpAtmCCPvcTraceIndex_Type()
)
mpAtmCCPvcTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceIndex.setStatus("mandatory")


class _MpAtmCCPvcTraceCtlPathKind_Type(Integer32):
    """Custom type mpAtmCCPvcTraceCtlPathKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 1),
          ("vpc", 2))
    )


_MpAtmCCPvcTraceCtlPathKind_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceCtlPathKind_Object = MibTableColumn
mpAtmCCPvcTraceCtlPathKind = _MpAtmCCPvcTraceCtlPathKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 2),
    _MpAtmCCPvcTraceCtlPathKind_Type()
)
mpAtmCCPvcTraceCtlPathKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlPathKind.setStatus("mandatory")
_MpAtmCCPvcTraceCtlIfIndex_Type = Integer32
_MpAtmCCPvcTraceCtlIfIndex_Object = MibTableColumn
mpAtmCCPvcTraceCtlIfIndex = _MpAtmCCPvcTraceCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 3),
    _MpAtmCCPvcTraceCtlIfIndex_Type()
)
mpAtmCCPvcTraceCtlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlIfIndex.setStatus("mandatory")
_MpAtmCCPvcTraceCtlVpi_Type = Integer32
_MpAtmCCPvcTraceCtlVpi_Object = MibTableColumn
mpAtmCCPvcTraceCtlVpi = _MpAtmCCPvcTraceCtlVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 4),
    _MpAtmCCPvcTraceCtlVpi_Type()
)
mpAtmCCPvcTraceCtlVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlVpi.setStatus("mandatory")
_MpAtmCCPvcTraceCtlVci_Type = Integer32
_MpAtmCCPvcTraceCtlVci_Object = MibTableColumn
mpAtmCCPvcTraceCtlVci = _MpAtmCCPvcTraceCtlVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 5),
    _MpAtmCCPvcTraceCtlVci_Type()
)
mpAtmCCPvcTraceCtlVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlVci.setStatus("mandatory")


class _MpAtmCCPvcTraceCtlStatus_Type(Integer32):
    """Custom type mpAtmCCPvcTraceCtlStatus based on Integer32"""
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
        *(("cancel", 5),
          ("collecting", 3),
          ("done", 4),
          ("idle", 1),
          ("start", 2),
          ("unknown", 6))
    )


_MpAtmCCPvcTraceCtlStatus_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceCtlStatus_Object = MibTableColumn
mpAtmCCPvcTraceCtlStatus = _MpAtmCCPvcTraceCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 2, 1, 6),
    _MpAtmCCPvcTraceCtlStatus_Type()
)
mpAtmCCPvcTraceCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceCtlStatus.setStatus("mandatory")
_MpAtmCCPvcTraceInfoTable_Object = MibTable
mpAtmCCPvcTraceInfoTable = _MpAtmCCPvcTraceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoTable.setStatus("mandatory")
_MpAtmCCPvcTraceInfoEntry_Object = MibTableRow
mpAtmCCPvcTraceInfoEntry = _MpAtmCCPvcTraceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1)
)
mpAtmCCPvcTraceInfoEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCPvcTraceIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCPvcTraceEntryIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoEntry.setStatus("mandatory")


class _MpAtmCCPvcTraceEntryIndex_Type(Integer32):
    """Custom type mpAtmCCPvcTraceEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MpAtmCCPvcTraceEntryIndex_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceEntryIndex_Object = MibTableColumn
mpAtmCCPvcTraceEntryIndex = _MpAtmCCPvcTraceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 1),
    _MpAtmCCPvcTraceEntryIndex_Type()
)
mpAtmCCPvcTraceEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceEntryIndex.setStatus("mandatory")


class _MpAtmCCPvcTraceInfoSysName_Type(DisplayString):
    """Custom type mpAtmCCPvcTraceInfoSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpAtmCCPvcTraceInfoSysName_Type.__name__ = "DisplayString"
_MpAtmCCPvcTraceInfoSysName_Object = MibTableColumn
mpAtmCCPvcTraceInfoSysName = _MpAtmCCPvcTraceInfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 2),
    _MpAtmCCPvcTraceInfoSysName_Type()
)
mpAtmCCPvcTraceInfoSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoSysName.setStatus("mandatory")
_MpAtmCCPvcTraceInfoIfIndex_Type = Integer32
_MpAtmCCPvcTraceInfoIfIndex_Object = MibTableColumn
mpAtmCCPvcTraceInfoIfIndex = _MpAtmCCPvcTraceInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 3),
    _MpAtmCCPvcTraceInfoIfIndex_Type()
)
mpAtmCCPvcTraceInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoIfIndex.setStatus("mandatory")
_MpAtmCCPvcTraceInfoVpi_Type = Integer32
_MpAtmCCPvcTraceInfoVpi_Object = MibTableColumn
mpAtmCCPvcTraceInfoVpi = _MpAtmCCPvcTraceInfoVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 4),
    _MpAtmCCPvcTraceInfoVpi_Type()
)
mpAtmCCPvcTraceInfoVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoVpi.setStatus("mandatory")
_MpAtmCCPvcTraceInfoVci_Type = Integer32
_MpAtmCCPvcTraceInfoVci_Object = MibTableColumn
mpAtmCCPvcTraceInfoVci = _MpAtmCCPvcTraceInfoVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 5),
    _MpAtmCCPvcTraceInfoVci_Type()
)
mpAtmCCPvcTraceInfoVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoVci.setStatus("mandatory")


class _MpAtmCCPvcTraceInfoPathKind_Type(Integer32):
    """Custom type mpAtmCCPvcTraceInfoPathKind based on Integer32"""
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
        *(("inspvc", 3),
          ("pvc", 1),
          ("pvp", 4),
          ("softpvc", 2),
          ("softpvp", 5))
    )


_MpAtmCCPvcTraceInfoPathKind_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceInfoPathKind_Object = MibTableColumn
mpAtmCCPvcTraceInfoPathKind = _MpAtmCCPvcTraceInfoPathKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 6),
    _MpAtmCCPvcTraceInfoPathKind_Type()
)
mpAtmCCPvcTraceInfoPathKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoPathKind.setStatus("mandatory")


class _MpAtmCCPvcTraceInfoCallKind_Type(Integer32):
    """Custom type mpAtmCCPvcTraceInfoCallKind based on Integer32"""
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
        *(("called", 4),
          ("calling", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_MpAtmCCPvcTraceInfoCallKind_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceInfoCallKind_Object = MibTableColumn
mpAtmCCPvcTraceInfoCallKind = _MpAtmCCPvcTraceInfoCallKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 7),
    _MpAtmCCPvcTraceInfoCallKind_Type()
)
mpAtmCCPvcTraceInfoCallKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoCallKind.setStatus("mandatory")


class _MpAtmCCPvcTraceInfoLastSegment_Type(Integer32):
    """Custom type mpAtmCCPvcTraceInfoLastSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("last", 2),
          ("notlast", 1))
    )


_MpAtmCCPvcTraceInfoLastSegment_Type.__name__ = "Integer32"
_MpAtmCCPvcTraceInfoLastSegment_Object = MibTableColumn
mpAtmCCPvcTraceInfoLastSegment = _MpAtmCCPvcTraceInfoLastSegment_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 7, 3, 1, 8),
    _MpAtmCCPvcTraceInfoLastSegment_Type()
)
mpAtmCCPvcTraceInfoLastSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcTraceInfoLastSegment.setStatus("mandatory")
_MpAtmCCMuxMib_ObjectIdentity = ObjectIdentity
mpAtmCCMuxMib = _MpAtmCCMuxMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8)
)
_MpAtmCCMuxStatistics_ObjectIdentity = ObjectIdentity
mpAtmCCMuxStatistics = _MpAtmCCMuxStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1)
)
_MpAtmCCMuxStatReceiveCellsCounters_Type = Counter32
_MpAtmCCMuxStatReceiveCellsCounters_Object = MibScalar
mpAtmCCMuxStatReceiveCellsCounters = _MpAtmCCMuxStatReceiveCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 1),
    _MpAtmCCMuxStatReceiveCellsCounters_Type()
)
mpAtmCCMuxStatReceiveCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatReceiveCellsCounters.setStatus("mandatory")
_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Type = Counter32
_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Object = MibScalar
mpAtmCCMuxStatReceiveCellsCntOvfCounters = _MpAtmCCMuxStatReceiveCellsCntOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 2),
    _MpAtmCCMuxStatReceiveCellsCntOvfCounters_Type()
)
mpAtmCCMuxStatReceiveCellsCntOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatReceiveCellsCntOvfCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsBufOvfCounters = _MpAtmCCMuxStatDiscardCellsBufOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 3),
    _MpAtmCCMuxStatDiscardCellsBufOvfCounters_Type()
)
mpAtmCCMuxStatDiscardCellsBufOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsBufOvfCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters = _MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 4),
    _MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Type()
)
mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsHTErrCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsHTErrCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsHTErrCounters = _MpAtmCCMuxStatDiscardCellsHTErrCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 5),
    _MpAtmCCMuxStatDiscardCellsHTErrCounters_Type()
)
mpAtmCCMuxStatDiscardCellsHTErrCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsHTErrCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters = _MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 6),
    _MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Type()
)
mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsThresholdOvfCounters = _MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 7),
    _MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Type()
)
mpAtmCCMuxStatDiscardCellsThresholdOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsThresholdOvfCounters.setStatus("mandatory")
_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Type = Counter32
_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Object = MibScalar
mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters = _MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 8, 1, 8),
    _MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Type()
)
mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters.setStatus("mandatory")
_MpAtmCCVpTunneling_ObjectIdentity = ObjectIdentity
mpAtmCCVpTunneling = _MpAtmCCVpTunneling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9)
)
_MpAtmCCVpTunnelingTable_Object = MibTable
mpAtmCCVpTunnelingTable = _MpAtmCCVpTunnelingTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingTable.setStatus("mandatory")
_MpAtmCCVpTunnelingEntry_Object = MibTableRow
mpAtmCCVpTunnelingEntry = _MpAtmCCVpTunnelingEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1)
)
mpAtmCCVpTunnelingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCVpTunnelingVpi"),
)
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingEntry.setStatus("mandatory")
_MpAtmCCVpTunnelingVpi_Type = Integer32
_MpAtmCCVpTunnelingVpi_Object = MibTableColumn
mpAtmCCVpTunnelingVpi = _MpAtmCCVpTunnelingVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 1),
    _MpAtmCCVpTunnelingVpi_Type()
)
mpAtmCCVpTunnelingVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingVpi.setStatus("mandatory")


class _MpAtmCCVpTunnelingAdminStatus_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCVpTunnelingAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingAdminStatus_Object = MibTableColumn
mpAtmCCVpTunnelingAdminStatus = _MpAtmCCVpTunnelingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 2),
    _MpAtmCCVpTunnelingAdminStatus_Type()
)
mpAtmCCVpTunnelingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingAdminStatus.setStatus("mandatory")


class _MpAtmCCVpTunnelingOperStatus_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCVpTunnelingOperStatus_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingOperStatus_Object = MibTableColumn
mpAtmCCVpTunnelingOperStatus = _MpAtmCCVpTunnelingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 3),
    _MpAtmCCVpTunnelingOperStatus_Type()
)
mpAtmCCVpTunnelingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingOperStatus.setStatus("mandatory")
_MpAtmCCVpTunnelingSpeed_Type = Integer32
_MpAtmCCVpTunnelingSpeed_Object = MibTableColumn
mpAtmCCVpTunnelingSpeed = _MpAtmCCVpTunnelingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 4),
    _MpAtmCCVpTunnelingSpeed_Type()
)
mpAtmCCVpTunnelingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingSpeed.setStatus("mandatory")
_MpAtmCCVpTunnelingNeighborInfo_Type = Integer32
_MpAtmCCVpTunnelingNeighborInfo_Object = MibTableColumn
mpAtmCCVpTunnelingNeighborInfo = _MpAtmCCVpTunnelingNeighborInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 5),
    _MpAtmCCVpTunnelingNeighborInfo_Type()
)
mpAtmCCVpTunnelingNeighborInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingNeighborInfo.setStatus("mandatory")
_MpAtmCCVpTunnelingPnniVer_Type = Integer32
_MpAtmCCVpTunnelingPnniVer_Object = MibTableColumn
mpAtmCCVpTunnelingPnniVer = _MpAtmCCVpTunnelingPnniVer_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 6),
    _MpAtmCCVpTunnelingPnniVer_Type()
)
mpAtmCCVpTunnelingPnniVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingPnniVer.setStatus("mandatory")


class _MpAtmCCVpTunnelingContinuityCheck_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingContinuityCheck based on Integer32"""
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


_MpAtmCCVpTunnelingContinuityCheck_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingContinuityCheck_Object = MibTableColumn
mpAtmCCVpTunnelingContinuityCheck = _MpAtmCCVpTunnelingContinuityCheck_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 7),
    _MpAtmCCVpTunnelingContinuityCheck_Type()
)
mpAtmCCVpTunnelingContinuityCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingContinuityCheck.setStatus("mandatory")


class _MpAtmCCVpTunnelingTrapState_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingTrapState based on Integer32"""
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


_MpAtmCCVpTunnelingTrapState_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingTrapState_Object = MibTableColumn
mpAtmCCVpTunnelingTrapState = _MpAtmCCVpTunnelingTrapState_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 8),
    _MpAtmCCVpTunnelingTrapState_Type()
)
mpAtmCCVpTunnelingTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingTrapState.setStatus("mandatory")


class _MpAtmCCVpTunnelingSeverity_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingSeverity based on Integer32"""
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
        *(("critical", 1),
          ("informational", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_MpAtmCCVpTunnelingSeverity_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingSeverity_Object = MibTableColumn
mpAtmCCVpTunnelingSeverity = _MpAtmCCVpTunnelingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 9),
    _MpAtmCCVpTunnelingSeverity_Type()
)
mpAtmCCVpTunnelingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingSeverity.setStatus("mandatory")


class _MpAtmCCVpTunnelingCfgStatus_Type(Integer32):
    """Custom type mpAtmCCVpTunnelingCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCVpTunnelingCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCVpTunnelingCfgStatus_Object = MibTableColumn
mpAtmCCVpTunnelingCfgStatus = _MpAtmCCVpTunnelingCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 98),
    _MpAtmCCVpTunnelingCfgStatus_Type()
)
mpAtmCCVpTunnelingCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingCfgStatus.setStatus("mandatory")
_MpAtmCCVpTunnelingErrInfo_Type = Integer32
_MpAtmCCVpTunnelingErrInfo_Object = MibTableColumn
mpAtmCCVpTunnelingErrInfo = _MpAtmCCVpTunnelingErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 9, 1, 1, 99),
    _MpAtmCCVpTunnelingErrInfo_Type()
)
mpAtmCCVpTunnelingErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCVpTunnelingErrInfo.setStatus("mandatory")
_MpAtmCCPathTest_ObjectIdentity = ObjectIdentity
mpAtmCCPathTest = _MpAtmCCPathTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10)
)
_MpAtmCCPathTestTable_Object = MibTable
mpAtmCCPathTestTable = _MpAtmCCPathTestTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1)
)
if mibBuilder.loadTexts:
    mpAtmCCPathTestTable.setStatus("mandatory")
_MpAtmCCPathTestEntry_Object = MibTableRow
mpAtmCCPathTestEntry = _MpAtmCCPathTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1)
)
mpAtmCCPathTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCPathTestVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCPathTestVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCPathTestEntry.setStatus("mandatory")
_MpAtmCCPathTestVpi_Type = Integer32
_MpAtmCCPathTestVpi_Object = MibTableColumn
mpAtmCCPathTestVpi = _MpAtmCCPathTestVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 1),
    _MpAtmCCPathTestVpi_Type()
)
mpAtmCCPathTestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPathTestVpi.setStatus("mandatory")
_MpAtmCCPathTestVci_Type = Integer32
_MpAtmCCPathTestVci_Object = MibTableColumn
mpAtmCCPathTestVci = _MpAtmCCPathTestVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 2),
    _MpAtmCCPathTestVci_Type()
)
mpAtmCCPathTestVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPathTestVci.setStatus("mandatory")


class _MpAtmCCPathTestStatus_Type(Integer32):
    """Custom type mpAtmCCPathTestStatus based on Integer32"""
    defaultValue = 7

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
        *(("delete", 6),
          ("loopRelease", 5),
          ("loopSet", 4),
          ("sendStart", 2),
          ("sendStop", 3),
          ("testReq", 1),
          ("unknown", 7))
    )


_MpAtmCCPathTestStatus_Type.__name__ = "Integer32"
_MpAtmCCPathTestStatus_Object = MibTableColumn
mpAtmCCPathTestStatus = _MpAtmCCPathTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 3),
    _MpAtmCCPathTestStatus_Type()
)
mpAtmCCPathTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPathTestStatus.setStatus("mandatory")


class _MpAtmCCPathTestSendDirection_Type(Integer32):
    """Custom type mpAtmCCPathTestSendDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mux", 2),
          ("port", 1))
    )


_MpAtmCCPathTestSendDirection_Type.__name__ = "Integer32"
_MpAtmCCPathTestSendDirection_Object = MibTableColumn
mpAtmCCPathTestSendDirection = _MpAtmCCPathTestSendDirection_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 4),
    _MpAtmCCPathTestSendDirection_Type()
)
mpAtmCCPathTestSendDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPathTestSendDirection.setStatus("mandatory")


class _MpAtmCCPathTestSendTime_Type(Integer32):
    """Custom type mpAtmCCPathTestSendTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 68400),
    )


_MpAtmCCPathTestSendTime_Type.__name__ = "Integer32"
_MpAtmCCPathTestSendTime_Object = MibTableColumn
mpAtmCCPathTestSendTime = _MpAtmCCPathTestSendTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 5),
    _MpAtmCCPathTestSendTime_Type()
)
mpAtmCCPathTestSendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPathTestSendTime.setStatus("mandatory")
_MpAtmCCPathTestSendCellsCounters_Type = Counter32
_MpAtmCCPathTestSendCellsCounters_Object = MibTableColumn
mpAtmCCPathTestSendCellsCounters = _MpAtmCCPathTestSendCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 6),
    _MpAtmCCPathTestSendCellsCounters_Type()
)
mpAtmCCPathTestSendCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPathTestSendCellsCounters.setStatus("mandatory")
_MpAtmCCPathTestRcvCellsCounters_Type = Counter32
_MpAtmCCPathTestRcvCellsCounters_Object = MibTableColumn
mpAtmCCPathTestRcvCellsCounters = _MpAtmCCPathTestRcvCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 7),
    _MpAtmCCPathTestRcvCellsCounters_Type()
)
mpAtmCCPathTestRcvCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPathTestRcvCellsCounters.setStatus("mandatory")
_MpAtmCCPathTestErrInfo_Type = Integer32
_MpAtmCCPathTestErrInfo_Object = MibTableColumn
mpAtmCCPathTestErrInfo = _MpAtmCCPathTestErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 10, 1, 1, 99),
    _MpAtmCCPathTestErrInfo_Type()
)
mpAtmCCPathTestErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPathTestErrInfo.setStatus("mandatory")
_MpAtmCCPvcGroupCutover_ObjectIdentity = ObjectIdentity
mpAtmCCPvcGroupCutover = _MpAtmCCPvcGroupCutover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11)
)
_MpAtmCCPvcGroupCutoverBaseInfo_ObjectIdentity = ObjectIdentity
mpAtmCCPvcGroupCutoverBaseInfo = _MpAtmCCPvcGroupCutoverBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 1)
)


class _MpAtmCCPvcGroupCutoverEnable_Type(Integer32):
    """Custom type mpAtmCCPvcGroupCutoverEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ture", 1))
    )


_MpAtmCCPvcGroupCutoverEnable_Type.__name__ = "Integer32"
_MpAtmCCPvcGroupCutoverEnable_Object = MibScalar
mpAtmCCPvcGroupCutoverEnable = _MpAtmCCPvcGroupCutoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 1, 1),
    _MpAtmCCPvcGroupCutoverEnable_Type()
)
mpAtmCCPvcGroupCutoverEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcGroupCutoverEnable.setStatus("mandatory")


class _MpAtmCCPvcGroupCutoverStatus_Type(Integer32):
    """Custom type mpAtmCCPvcGroupCutoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("underAvtivate", 2),
          ("underDeactivate", 3))
    )


_MpAtmCCPvcGroupCutoverStatus_Type.__name__ = "Integer32"
_MpAtmCCPvcGroupCutoverStatus_Object = MibScalar
mpAtmCCPvcGroupCutoverStatus = _MpAtmCCPvcGroupCutoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 1, 2),
    _MpAtmCCPvcGroupCutoverStatus_Type()
)
mpAtmCCPvcGroupCutoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPvcGroupCutoverStatus.setStatus("mandatory")
_MpAtmCCUnitePvcGroup_ObjectIdentity = ObjectIdentity
mpAtmCCUnitePvcGroup = _MpAtmCCUnitePvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2)
)
_MpAtmCCUpgcBaseInfo_ObjectIdentity = ObjectIdentity
mpAtmCCUpgcBaseInfo = _MpAtmCCUpgcBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 1)
)
_MpAtmCCUpgcTotalGroupNumber_Type = Integer32
_MpAtmCCUpgcTotalGroupNumber_Object = MibScalar
mpAtmCCUpgcTotalGroupNumber = _MpAtmCCUpgcTotalGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 1, 1),
    _MpAtmCCUpgcTotalGroupNumber_Type()
)
mpAtmCCUpgcTotalGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcTotalGroupNumber.setStatus("mandatory")
_MpAtmCCUpgcBaseActiveGroupNumber_Type = Integer32
_MpAtmCCUpgcBaseActiveGroupNumber_Object = MibScalar
mpAtmCCUpgcBaseActiveGroupNumber = _MpAtmCCUpgcBaseActiveGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 1, 2),
    _MpAtmCCUpgcBaseActiveGroupNumber_Type()
)
mpAtmCCUpgcBaseActiveGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcBaseActiveGroupNumber.setStatus("mandatory")
_MpAtmCCUnitePvcGroupControlTable_Object = MibTable
mpAtmCCUnitePvcGroupControlTable = _MpAtmCCUnitePvcGroupControlTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCUnitePvcGroupControlTable.setStatus("mandatory")
_MpAtmCCUpgcCtlEntry_Object = MibTableRow
mpAtmCCUpgcCtlEntry = _MpAtmCCUpgcCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2, 1)
)
mpAtmCCUpgcCtlEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCUpgcIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCUpgcCtlEntry.setStatus("mandatory")


class _MpAtmCCUpgcIndex_Type(Integer32):
    """Custom type mpAtmCCUpgcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MpAtmCCUpgcIndex_Type.__name__ = "Integer32"
_MpAtmCCUpgcIndex_Object = MibTableColumn
mpAtmCCUpgcIndex = _MpAtmCCUpgcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2, 1, 1),
    _MpAtmCCUpgcIndex_Type()
)
mpAtmCCUpgcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcIndex.setStatus("mandatory")


class _MpAtmCCUpgcCtlStatus_Type(Integer32):
    """Custom type mpAtmCCUpgcCtlStatus based on Integer32"""
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
        *(("active", 2),
          ("delete", 4),
          ("inactive", 3),
          ("register", 1),
          ("stsInactive", 5),
          ("underDeactivate", 7),
          ("underEstablish", 6))
    )


_MpAtmCCUpgcCtlStatus_Type.__name__ = "Integer32"
_MpAtmCCUpgcCtlStatus_Object = MibTableColumn
mpAtmCCUpgcCtlStatus = _MpAtmCCUpgcCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2, 1, 2),
    _MpAtmCCUpgcCtlStatus_Type()
)
mpAtmCCUpgcCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCUpgcCtlStatus.setStatus("mandatory")
_MpAtmCCUpgcCtlCountPgc_Type = Integer32
_MpAtmCCUpgcCtlCountPgc_Object = MibTableColumn
mpAtmCCUpgcCtlCountPgc = _MpAtmCCUpgcCtlCountPgc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2, 1, 3),
    _MpAtmCCUpgcCtlCountPgc_Type()
)
mpAtmCCUpgcCtlCountPgc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcCtlCountPgc.setStatus("mandatory")
_MpAtmCCUpgcCtlResult_Type = Integer32
_MpAtmCCUpgcCtlResult_Object = MibTableColumn
mpAtmCCUpgcCtlResult = _MpAtmCCUpgcCtlResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 2, 1, 4),
    _MpAtmCCUpgcCtlResult_Type()
)
mpAtmCCUpgcCtlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcCtlResult.setStatus("mandatory")
_MpAtmCCUnitePvcGroupRegisterTable_Object = MibTable
mpAtmCCUnitePvcGroupRegisterTable = _MpAtmCCUnitePvcGroupRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCUnitePvcGroupRegisterTable.setStatus("mandatory")
_MpAtmCCUpgcRegiEntry_Object = MibTableRow
mpAtmCCUpgcRegiEntry = _MpAtmCCUpgcRegiEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 3, 1)
)
mpAtmCCUpgcRegiEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCUpgcIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCUpgcPgcIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCUpgcRegiEntry.setStatus("mandatory")


class _MpAtmCCUpgcPgcIndex_Type(Integer32):
    """Custom type mpAtmCCUpgcPgcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MpAtmCCUpgcPgcIndex_Type.__name__ = "Integer32"
_MpAtmCCUpgcPgcIndex_Object = MibTableColumn
mpAtmCCUpgcPgcIndex = _MpAtmCCUpgcPgcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 3, 1, 1),
    _MpAtmCCUpgcPgcIndex_Type()
)
mpAtmCCUpgcPgcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCUpgcPgcIndex.setStatus("mandatory")


class _MpAtmCCUpgcRegiStatus_Type(Integer32):
    """Custom type mpAtmCCUpgcRegiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("enable", 3))
    )


_MpAtmCCUpgcRegiStatus_Type.__name__ = "Integer32"
_MpAtmCCUpgcRegiStatus_Object = MibTableColumn
mpAtmCCUpgcRegiStatus = _MpAtmCCUpgcRegiStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 2, 3, 1, 2),
    _MpAtmCCUpgcRegiStatus_Type()
)
mpAtmCCUpgcRegiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCUpgcRegiStatus.setStatus("mandatory")
_MpAtmCCPvcGroup_ObjectIdentity = ObjectIdentity
mpAtmCCPvcGroup = _MpAtmCCPvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3)
)
_MpAtmCCPgcBaseInfo_ObjectIdentity = ObjectIdentity
mpAtmCCPgcBaseInfo = _MpAtmCCPgcBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 1)
)
_MpAtmCCPgcTotalGroupNumber_Type = Integer32
_MpAtmCCPgcTotalGroupNumber_Object = MibScalar
mpAtmCCPgcTotalGroupNumber = _MpAtmCCPgcTotalGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 1, 1),
    _MpAtmCCPgcTotalGroupNumber_Type()
)
mpAtmCCPgcTotalGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcTotalGroupNumber.setStatus("mandatory")
_MpAtmCCPvcGroupControlTable_Object = MibTable
mpAtmCCPvcGroupControlTable = _MpAtmCCPvcGroupControlTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCPvcGroupControlTable.setStatus("mandatory")
_MpAtmCCPgcCtlEntry_Object = MibTableRow
mpAtmCCPgcCtlEntry = _MpAtmCCPgcCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2, 1)
)
mpAtmCCPgcCtlEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCPgcIndex"),
)
if mibBuilder.loadTexts:
    mpAtmCCPgcCtlEntry.setStatus("mandatory")


class _MpAtmCCPgcIndex_Type(Integer32):
    """Custom type mpAtmCCPgcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MpAtmCCPgcIndex_Type.__name__ = "Integer32"
_MpAtmCCPgcIndex_Object = MibTableColumn
mpAtmCCPgcIndex = _MpAtmCCPgcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2, 1, 1),
    _MpAtmCCPgcIndex_Type()
)
mpAtmCCPgcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcIndex.setStatus("mandatory")


class _MpAtmCCPgcCtlStatus_Type(Integer32):
    """Custom type mpAtmCCPgcCtlStatus based on Integer32"""
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
        *(("active", 2),
          ("delete", 4),
          ("inactive", 3),
          ("register", 1),
          ("stsInactive", 5),
          ("underDeactivate", 7),
          ("underEstablish", 6))
    )


_MpAtmCCPgcCtlStatus_Type.__name__ = "Integer32"
_MpAtmCCPgcCtlStatus_Object = MibTableColumn
mpAtmCCPgcCtlStatus = _MpAtmCCPgcCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2, 1, 2),
    _MpAtmCCPgcCtlStatus_Type()
)
mpAtmCCPgcCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcCtlStatus.setStatus("mandatory")
_MpAtmCCPgcCtlCountPvc_Type = Integer32
_MpAtmCCPgcCtlCountPvc_Object = MibTableColumn
mpAtmCCPgcCtlCountPvc = _MpAtmCCPgcCtlCountPvc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2, 1, 3),
    _MpAtmCCPgcCtlCountPvc_Type()
)
mpAtmCCPgcCtlCountPvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcCtlCountPvc.setStatus("mandatory")
_MpAtmCCPgcCtlResult_Type = Integer32
_MpAtmCCPgcCtlResult_Object = MibTableColumn
mpAtmCCPgcCtlResult = _MpAtmCCPgcCtlResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 2, 1, 4),
    _MpAtmCCPgcCtlResult_Type()
)
mpAtmCCPgcCtlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcCtlResult.setStatus("mandatory")
_MpAtmCCPvcGroupRegisterTable_Object = MibTable
mpAtmCCPvcGroupRegisterTable = _MpAtmCCPvcGroupRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCPvcGroupRegisterTable.setStatus("mandatory")
_MpAtmCCPgcRegiEntry_Object = MibTableRow
mpAtmCCPgcRegiEntry = _MpAtmCCPgcRegiEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1)
)
mpAtmCCPgcRegiEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCPgcIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCPgcPvcIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCPgcPvcVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCPgcPvcVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCPgcRegiEntry.setStatus("mandatory")
_MpAtmCCPgcPvcIfIndex_Type = Integer32
_MpAtmCCPgcPvcIfIndex_Object = MibTableColumn
mpAtmCCPgcPvcIfIndex = _MpAtmCCPgcPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 1),
    _MpAtmCCPgcPvcIfIndex_Type()
)
mpAtmCCPgcPvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcIfIndex.setStatus("mandatory")
_MpAtmCCPgcPvcVpi_Type = Integer32
_MpAtmCCPgcPvcVpi_Object = MibTableColumn
mpAtmCCPgcPvcVpi = _MpAtmCCPgcPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 2),
    _MpAtmCCPgcPvcVpi_Type()
)
mpAtmCCPgcPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcVpi.setStatus("mandatory")
_MpAtmCCPgcPvcVci_Type = Integer32
_MpAtmCCPgcPvcVci_Object = MibTableColumn
mpAtmCCPgcPvcVci = _MpAtmCCPgcPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 3),
    _MpAtmCCPgcPvcVci_Type()
)
mpAtmCCPgcPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcVci.setStatus("mandatory")


class _MpAtmCCPgcPvcKind_Type(Integer32):
    """Custom type mpAtmCCPgcPvcKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("softPvc", 2),
          ("staticPvc", 1))
    )


_MpAtmCCPgcPvcKind_Type.__name__ = "Integer32"
_MpAtmCCPgcPvcKind_Object = MibTableColumn
mpAtmCCPgcPvcKind = _MpAtmCCPgcPvcKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 4),
    _MpAtmCCPgcPvcKind_Type()
)
mpAtmCCPgcPvcKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcKind.setStatus("mandatory")
_MpAtmCCPgcStaticPvcDestIfIndex_Type = Integer32
_MpAtmCCPgcStaticPvcDestIfIndex_Object = MibTableColumn
mpAtmCCPgcStaticPvcDestIfIndex = _MpAtmCCPgcStaticPvcDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 5),
    _MpAtmCCPgcStaticPvcDestIfIndex_Type()
)
mpAtmCCPgcStaticPvcDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcStaticPvcDestIfIndex.setStatus("mandatory")
_MpAtmCCPgcSoftPvcDestAtmAddress_Type = AtmAddr
_MpAtmCCPgcSoftPvcDestAtmAddress_Object = MibTableColumn
mpAtmCCPgcSoftPvcDestAtmAddress = _MpAtmCCPgcSoftPvcDestAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 6),
    _MpAtmCCPgcSoftPvcDestAtmAddress_Type()
)
mpAtmCCPgcSoftPvcDestAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcSoftPvcDestAtmAddress.setStatus("mandatory")
_MpAtmCCPgcPvcDestVpi_Type = Integer32
_MpAtmCCPgcPvcDestVpi_Object = MibTableColumn
mpAtmCCPgcPvcDestVpi = _MpAtmCCPgcPvcDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 7),
    _MpAtmCCPgcPvcDestVpi_Type()
)
mpAtmCCPgcPvcDestVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcDestVpi.setStatus("mandatory")
_MpAtmCCPgcPvcDestVci_Type = Integer32
_MpAtmCCPgcPvcDestVci_Object = MibTableColumn
mpAtmCCPgcPvcDestVci = _MpAtmCCPgcPvcDestVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 8),
    _MpAtmCCPgcPvcDestVci_Type()
)
mpAtmCCPgcPvcDestVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcDestVci.setStatus("mandatory")
_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Object = MibTableColumn
mpAtmCCPgcPvcReceiveTrafficDescrIndex = _MpAtmCCPgcPvcReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 9),
    _MpAtmCCPgcPvcReceiveTrafficDescrIndex_Type()
)
mpAtmCCPgcPvcReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcReceiveTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Object = MibTableColumn
mpAtmCCPgcPvcTransmitTrafficDescrIndex = _MpAtmCCPgcPvcTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 10),
    _MpAtmCCPgcPvcTransmitTrafficDescrIndex_Type()
)
mpAtmCCPgcPvcTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcTransmitTrafficDescrIndex.setStatus("mandatory")


class _MpAtmCCPgcPvcPriority_Type(Integer32):
    """Custom type mpAtmCCPgcPvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpAtmCCPgcPvcPriority_Type.__name__ = "Integer32"
_MpAtmCCPgcPvcPriority_Object = MibTableColumn
mpAtmCCPgcPvcPriority = _MpAtmCCPgcPvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 11),
    _MpAtmCCPgcPvcPriority_Type()
)
mpAtmCCPgcPvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcPvcPriority.setStatus("mandatory")
_MpAtmCCPgcStaticPvcId_Type = Integer32
_MpAtmCCPgcStaticPvcId_Object = MibTableColumn
mpAtmCCPgcStaticPvcId = _MpAtmCCPgcStaticPvcId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 12),
    _MpAtmCCPgcStaticPvcId_Type()
)
mpAtmCCPgcStaticPvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcStaticPvcId.setStatus("mandatory")
_MpAtmCCPgcStaticPvcSeqNo_Type = Integer32
_MpAtmCCPgcStaticPvcSeqNo_Object = MibTableColumn
mpAtmCCPgcStaticPvcSeqNo = _MpAtmCCPgcStaticPvcSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 13),
    _MpAtmCCPgcStaticPvcSeqNo_Type()
)
mpAtmCCPgcStaticPvcSeqNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcStaticPvcSeqNo.setStatus("mandatory")


class _MpAtmCCPgcSoftPvcCallKind_Type(Integer32):
    """Custom type mpAtmCCPgcSoftPvcCallKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("calling", 1))
    )


_MpAtmCCPgcSoftPvcCallKind_Type.__name__ = "Integer32"
_MpAtmCCPgcSoftPvcCallKind_Object = MibTableColumn
mpAtmCCPgcSoftPvcCallKind = _MpAtmCCPgcSoftPvcCallKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 14),
    _MpAtmCCPgcSoftPvcCallKind_Type()
)
mpAtmCCPgcSoftPvcCallKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcSoftPvcCallKind.setStatus("mandatory")


class _MpAtmCCPgcRegiAdminStatus_Type(Integer32):
    """Custom type mpAtmCCPgcRegiAdminStatus based on Integer32"""
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
        *(("active", 2),
          ("connectWait", 4),
          ("disconnectWait", 5),
          ("inactive", 1),
          ("stsInactive", 3))
    )


_MpAtmCCPgcRegiAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCPgcRegiAdminStatus_Object = MibTableColumn
mpAtmCCPgcRegiAdminStatus = _MpAtmCCPgcRegiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 15),
    _MpAtmCCPgcRegiAdminStatus_Type()
)
mpAtmCCPgcRegiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcRegiAdminStatus.setStatus("mandatory")


class _MpAtmCCPgcRegiCfgStatus_Type(Integer32):
    """Custom type mpAtmCCPgcRegiCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCPgcRegiCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCPgcRegiCfgStatus_Object = MibTableColumn
mpAtmCCPgcRegiCfgStatus = _MpAtmCCPgcRegiCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 16),
    _MpAtmCCPgcRegiCfgStatus_Type()
)
mpAtmCCPgcRegiCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCPgcRegiCfgStatus.setStatus("mandatory")
_MpAtmCCPgcRegiErrInfo_Type = Integer32
_MpAtmCCPgcRegiErrInfo_Object = MibTableColumn
mpAtmCCPgcRegiErrInfo = _MpAtmCCPgcRegiErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 3, 1, 17),
    _MpAtmCCPgcRegiErrInfo_Type()
)
mpAtmCCPgcRegiErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcRegiErrInfo.setStatus("mandatory")
_MpAtmCCPvcGroupActiveInfoTable_Object = MibTable
mpAtmCCPvcGroupActiveInfoTable = _MpAtmCCPvcGroupActiveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 4)
)
if mibBuilder.loadTexts:
    mpAtmCCPvcGroupActiveInfoTable.setStatus("mandatory")
_MpAtmCCPgcActInfoEntry_Object = MibTableRow
mpAtmCCPgcActInfoEntry = _MpAtmCCPgcActInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 4, 1)
)
mpAtmCCPgcActInfoEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCPgcActGrpNum"),
)
if mibBuilder.loadTexts:
    mpAtmCCPgcActInfoEntry.setStatus("mandatory")
_MpAtmCCPgcActGrpNum_Type = Integer32
_MpAtmCCPgcActGrpNum_Object = MibTableColumn
mpAtmCCPgcActGrpNum = _MpAtmCCPgcActGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 11, 3, 4, 1, 1),
    _MpAtmCCPgcActGrpNum_Type()
)
mpAtmCCPgcActGrpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCPgcActGrpNum.setStatus("mandatory")
_MpAtmCCAtmMulticast_ObjectIdentity = ObjectIdentity
mpAtmCCAtmMulticast = _MpAtmCCAtmMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12)
)
_MpAtmCCAtmMulticastRegistration_ObjectIdentity = ObjectIdentity
mpAtmCCAtmMulticastRegistration = _MpAtmCCAtmMulticastRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1)
)
_MpAtmCCAtmMultiRootIfIndex_Type = Integer32
_MpAtmCCAtmMultiRootIfIndex_Object = MibScalar
mpAtmCCAtmMultiRootIfIndex = _MpAtmCCAtmMultiRootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 1),
    _MpAtmCCAtmMultiRootIfIndex_Type()
)
mpAtmCCAtmMultiRootIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiRootIfIndex.setStatus("mandatory")
_MpAtmCCAtmMultiRootVpi_Type = Integer32
_MpAtmCCAtmMultiRootVpi_Object = MibScalar
mpAtmCCAtmMultiRootVpi = _MpAtmCCAtmMultiRootVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 2),
    _MpAtmCCAtmMultiRootVpi_Type()
)
mpAtmCCAtmMultiRootVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiRootVpi.setStatus("mandatory")
_MpAtmCCAtmMultiRootVci_Type = Integer32
_MpAtmCCAtmMultiRootVci_Object = MibScalar
mpAtmCCAtmMultiRootVci = _MpAtmCCAtmMultiRootVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 3),
    _MpAtmCCAtmMultiRootVci_Type()
)
mpAtmCCAtmMultiRootVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiRootVci.setStatus("mandatory")
_MpAtmCCAtmMultiLeafIfIndex_Type = Integer32
_MpAtmCCAtmMultiLeafIfIndex_Object = MibScalar
mpAtmCCAtmMultiLeafIfIndex = _MpAtmCCAtmMultiLeafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 4),
    _MpAtmCCAtmMultiLeafIfIndex_Type()
)
mpAtmCCAtmMultiLeafIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiLeafIfIndex.setStatus("mandatory")
_MpAtmCCAtmMultiLeafVpi_Type = Integer32
_MpAtmCCAtmMultiLeafVpi_Object = MibScalar
mpAtmCCAtmMultiLeafVpi = _MpAtmCCAtmMultiLeafVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 5),
    _MpAtmCCAtmMultiLeafVpi_Type()
)
mpAtmCCAtmMultiLeafVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiLeafVpi.setStatus("mandatory")
_MpAtmCCAtmMultiLeafVci_Type = Integer32
_MpAtmCCAtmMultiLeafVci_Object = MibScalar
mpAtmCCAtmMultiLeafVci = _MpAtmCCAtmMultiLeafVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 6),
    _MpAtmCCAtmMultiLeafVci_Type()
)
mpAtmCCAtmMultiLeafVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiLeafVci.setStatus("mandatory")
_MpAtmCCAtmMultiTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCAtmMultiTrafficDescrIndex_Object = MibScalar
mpAtmCCAtmMultiTrafficDescrIndex = _MpAtmCCAtmMultiTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 7),
    _MpAtmCCAtmMultiTrafficDescrIndex_Type()
)
mpAtmCCAtmMultiTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCAtmMultiSlotNumber_Type = Integer32
_MpAtmCCAtmMultiSlotNumber_Object = MibScalar
mpAtmCCAtmMultiSlotNumber = _MpAtmCCAtmMultiSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 8),
    _MpAtmCCAtmMultiSlotNumber_Type()
)
mpAtmCCAtmMultiSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiSlotNumber.setStatus("mandatory")


class _MpAtmCCAtmMultiVcRdiResponse_Type(Integer32):
    """Custom type mpAtmCCAtmMultiVcRdiResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ture", 1))
    )


_MpAtmCCAtmMultiVcRdiResponse_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiVcRdiResponse_Object = MibScalar
mpAtmCCAtmMultiVcRdiResponse = _MpAtmCCAtmMultiVcRdiResponse_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 9),
    _MpAtmCCAtmMultiVcRdiResponse_Type()
)
mpAtmCCAtmMultiVcRdiResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiVcRdiResponse.setStatus("mandatory")
_MpAtmCCAtmMultiPvcId_Type = Integer32
_MpAtmCCAtmMultiPvcId_Object = MibScalar
mpAtmCCAtmMultiPvcId = _MpAtmCCAtmMultiPvcId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 10),
    _MpAtmCCAtmMultiPvcId_Type()
)
mpAtmCCAtmMultiPvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiPvcId.setStatus("mandatory")
_MpAtmCCAtmMultiSeqNo_Type = Integer32
_MpAtmCCAtmMultiSeqNo_Object = MibScalar
mpAtmCCAtmMultiSeqNo = _MpAtmCCAtmMultiSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 11),
    _MpAtmCCAtmMultiSeqNo_Type()
)
mpAtmCCAtmMultiSeqNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiSeqNo.setStatus("mandatory")


class _MpAtmCCAtmMultiCfgStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiCfgStatus based on Integer32"""
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
        *(("cancel", 2),
          ("delete", 3),
          ("enable", 1),
          ("unknown", 4))
    )


_MpAtmCCAtmMultiCfgStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiCfgStatus_Object = MibScalar
mpAtmCCAtmMultiCfgStatus = _MpAtmCCAtmMultiCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 98),
    _MpAtmCCAtmMultiCfgStatus_Type()
)
mpAtmCCAtmMultiCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiCfgStatus.setStatus("mandatory")
_MpAtmCCAtmMultiRegErrInfo_Type = Integer32
_MpAtmCCAtmMultiRegErrInfo_Object = MibScalar
mpAtmCCAtmMultiRegErrInfo = _MpAtmCCAtmMultiRegErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 1, 99),
    _MpAtmCCAtmMultiRegErrInfo_Type()
)
mpAtmCCAtmMultiRegErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiRegErrInfo.setStatus("mandatory")
_MpAtmCCAtmMulticastCtlTable_Object = MibTable
mpAtmCCAtmMulticastCtlTable = _MpAtmCCAtmMulticastCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2)
)
if mibBuilder.loadTexts:
    mpAtmCCAtmMulticastCtlTable.setStatus("mandatory")
_MpAtmCCAtmMultiCtlEntry_Object = MibTableRow
mpAtmCCAtmMultiCtlEntry = _MpAtmCCAtmMultiCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1)
)
mpAtmCCAtmMultiCtlEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiCtlEntry.setStatus("mandatory")
_MpAtmCCAtmMultiIfIndex_Type = Integer32
_MpAtmCCAtmMultiIfIndex_Object = MibTableColumn
mpAtmCCAtmMultiIfIndex = _MpAtmCCAtmMultiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 1),
    _MpAtmCCAtmMultiIfIndex_Type()
)
mpAtmCCAtmMultiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiIfIndex.setStatus("mandatory")
_MpAtmCCAtmMultiVpi_Type = Integer32
_MpAtmCCAtmMultiVpi_Object = MibTableColumn
mpAtmCCAtmMultiVpi = _MpAtmCCAtmMultiVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 2),
    _MpAtmCCAtmMultiVpi_Type()
)
mpAtmCCAtmMultiVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiVpi.setStatus("mandatory")
_MpAtmCCAtmMultiVci_Type = Integer32
_MpAtmCCAtmMultiVci_Object = MibTableColumn
mpAtmCCAtmMultiVci = _MpAtmCCAtmMultiVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 3),
    _MpAtmCCAtmMultiVci_Type()
)
mpAtmCCAtmMultiVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiVci.setStatus("mandatory")


class _MpAtmCCAtmMultiAdminStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiAdminStatus_Object = MibTableColumn
mpAtmCCAtmMultiAdminStatus = _MpAtmCCAtmMultiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 4),
    _MpAtmCCAtmMultiAdminStatus_Type()
)
mpAtmCCAtmMultiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiAdminStatus.setStatus("mandatory")


class _MpAtmCCAtmMultiOperStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiOperStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiOperStatus_Object = MibTableColumn
mpAtmCCAtmMultiOperStatus = _MpAtmCCAtmMultiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 5),
    _MpAtmCCAtmMultiOperStatus_Type()
)
mpAtmCCAtmMultiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiOperStatus.setStatus("mandatory")
_MpAtmCCAtmMultiErrInfo_Type = Integer32
_MpAtmCCAtmMultiErrInfo_Object = MibTableColumn
mpAtmCCAtmMultiErrInfo = _MpAtmCCAtmMultiErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 2, 1, 99),
    _MpAtmCCAtmMultiErrInfo_Type()
)
mpAtmCCAtmMultiErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiErrInfo.setStatus("mandatory")
_MpAtmCCAtmMulticastConfTable_Object = MibTable
mpAtmCCAtmMulticastConfTable = _MpAtmCCAtmMulticastConfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3)
)
if mibBuilder.loadTexts:
    mpAtmCCAtmMulticastConfTable.setStatus("mandatory")
_MpAtmCCAtmMultiConfEntry_Object = MibTableRow
mpAtmCCAtmMultiConfEntry = _MpAtmCCAtmMultiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1)
)
mpAtmCCAtmMultiConfEntry.setIndexNames(
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiRootIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiRootVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiRootVci"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiLeafIfIndex"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiLeafVpi"),
    (0, "MP-ATM-MIB", "mpAtmCCAtmMultiLeafVci"),
)
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfEntry.setStatus("mandatory")
_MpAtmCCAtmMultiConfRootIfIndex_Type = Integer32
_MpAtmCCAtmMultiConfRootIfIndex_Object = MibTableColumn
mpAtmCCAtmMultiConfRootIfIndex = _MpAtmCCAtmMultiConfRootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 1),
    _MpAtmCCAtmMultiConfRootIfIndex_Type()
)
mpAtmCCAtmMultiConfRootIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootIfIndex.setStatus("mandatory")
_MpAtmCCAtmMultiConfRootVpi_Type = Integer32
_MpAtmCCAtmMultiConfRootVpi_Object = MibTableColumn
mpAtmCCAtmMultiConfRootVpi = _MpAtmCCAtmMultiConfRootVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 2),
    _MpAtmCCAtmMultiConfRootVpi_Type()
)
mpAtmCCAtmMultiConfRootVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootVpi.setStatus("mandatory")
_MpAtmCCAtmMultiConfRootVci_Type = Integer32
_MpAtmCCAtmMultiConfRootVci_Object = MibTableColumn
mpAtmCCAtmMultiConfRootVci = _MpAtmCCAtmMultiConfRootVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 3),
    _MpAtmCCAtmMultiConfRootVci_Type()
)
mpAtmCCAtmMultiConfRootVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootVci.setStatus("mandatory")
_MpAtmCCAtmMultiConfLeafIfIndex_Type = Integer32
_MpAtmCCAtmMultiConfLeafIfIndex_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafIfIndex = _MpAtmCCAtmMultiConfLeafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 4),
    _MpAtmCCAtmMultiConfLeafIfIndex_Type()
)
mpAtmCCAtmMultiConfLeafIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafIfIndex.setStatus("mandatory")
_MpAtmCCAtmMultiConfLeafVpi_Type = Integer32
_MpAtmCCAtmMultiConfLeafVpi_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafVpi = _MpAtmCCAtmMultiConfLeafVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 5),
    _MpAtmCCAtmMultiConfLeafVpi_Type()
)
mpAtmCCAtmMultiConfLeafVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafVpi.setStatus("mandatory")
_MpAtmCCAtmMultiConfLeafVci_Type = Integer32
_MpAtmCCAtmMultiConfLeafVci_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafVci = _MpAtmCCAtmMultiConfLeafVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 6),
    _MpAtmCCAtmMultiConfLeafVci_Type()
)
mpAtmCCAtmMultiConfLeafVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafVci.setStatus("mandatory")


class _MpAtmCCAtmMultiConfRootAdminStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfRootAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiConfRootAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfRootAdminStatus_Object = MibTableColumn
mpAtmCCAtmMultiConfRootAdminStatus = _MpAtmCCAtmMultiConfRootAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 7),
    _MpAtmCCAtmMultiConfRootAdminStatus_Type()
)
mpAtmCCAtmMultiConfRootAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootAdminStatus.setStatus("mandatory")


class _MpAtmCCAtmMultiConfRootOperStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfRootOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiConfRootOperStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfRootOperStatus_Object = MibTableColumn
mpAtmCCAtmMultiConfRootOperStatus = _MpAtmCCAtmMultiConfRootOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 8),
    _MpAtmCCAtmMultiConfRootOperStatus_Type()
)
mpAtmCCAtmMultiConfRootOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootOperStatus.setStatus("mandatory")


class _MpAtmCCAtmMultiConfLeafAdminStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfLeafAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiConfLeafAdminStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfLeafAdminStatus_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafAdminStatus = _MpAtmCCAtmMultiConfLeafAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 9),
    _MpAtmCCAtmMultiConfLeafAdminStatus_Type()
)
mpAtmCCAtmMultiConfLeafAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafAdminStatus.setStatus("mandatory")


class _MpAtmCCAtmMultiConfLeafOperStatus_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfLeafOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpAtmCCAtmMultiConfLeafOperStatus_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfLeafOperStatus_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafOperStatus = _MpAtmCCAtmMultiConfLeafOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 10),
    _MpAtmCCAtmMultiConfLeafOperStatus_Type()
)
mpAtmCCAtmMultiConfLeafOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafOperStatus.setStatus("mandatory")
_MpAtmCCAtmMultiConfTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_MpAtmCCAtmMultiConfTrafficDescrIndex_Object = MibTableColumn
mpAtmCCAtmMultiConfTrafficDescrIndex = _MpAtmCCAtmMultiConfTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 11),
    _MpAtmCCAtmMultiConfTrafficDescrIndex_Type()
)
mpAtmCCAtmMultiConfTrafficDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfTrafficDescrIndex.setStatus("mandatory")
_MpAtmCCAtmMultiConfSlotNumber_Type = Integer32
_MpAtmCCAtmMultiConfSlotNumber_Object = MibTableColumn
mpAtmCCAtmMultiConfSlotNumber = _MpAtmCCAtmMultiConfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 12),
    _MpAtmCCAtmMultiConfSlotNumber_Type()
)
mpAtmCCAtmMultiConfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfSlotNumber.setStatus("mandatory")


class _MpAtmCCAtmMultiConfVcRdiResponse_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfVcRdiResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MpAtmCCAtmMultiConfVcRdiResponse_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfVcRdiResponse_Object = MibTableColumn
mpAtmCCAtmMultiConfVcRdiResponse = _MpAtmCCAtmMultiConfVcRdiResponse_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 13),
    _MpAtmCCAtmMultiConfVcRdiResponse_Type()
)
mpAtmCCAtmMultiConfVcRdiResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfVcRdiResponse.setStatus("mandatory")
_MpAtmCCAtmMultiConfPvcId_Type = Integer32
_MpAtmCCAtmMultiConfPvcId_Object = MibTableColumn
mpAtmCCAtmMultiConfPvcId = _MpAtmCCAtmMultiConfPvcId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 14),
    _MpAtmCCAtmMultiConfPvcId_Type()
)
mpAtmCCAtmMultiConfPvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfPvcId.setStatus("mandatory")
_MpAtmCCAtmMultiConfSeqNo_Type = Integer32
_MpAtmCCAtmMultiConfSeqNo_Object = MibTableColumn
mpAtmCCAtmMultiConfSeqNo = _MpAtmCCAtmMultiConfSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 15),
    _MpAtmCCAtmMultiConfSeqNo_Type()
)
mpAtmCCAtmMultiConfSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfSeqNo.setStatus("mandatory")
_MpAtmCCAtmMultiConfShaperRate_Type = Integer32
_MpAtmCCAtmMultiConfShaperRate_Object = MibTableColumn
mpAtmCCAtmMultiConfShaperRate = _MpAtmCCAtmMultiConfShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 16),
    _MpAtmCCAtmMultiConfShaperRate_Type()
)
mpAtmCCAtmMultiConfShaperRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfShaperRate.setStatus("mandatory")


class _MpAtmCCAtmMultiConfRootVpTunneling_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfRootVpTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ture", 1))
    )


_MpAtmCCAtmMultiConfRootVpTunneling_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfRootVpTunneling_Object = MibTableColumn
mpAtmCCAtmMultiConfRootVpTunneling = _MpAtmCCAtmMultiConfRootVpTunneling_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 17),
    _MpAtmCCAtmMultiConfRootVpTunneling_Type()
)
mpAtmCCAtmMultiConfRootVpTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfRootVpTunneling.setStatus("mandatory")


class _MpAtmCCAtmMultiConfLeafVpTunneling_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfLeafVpTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ture", 1))
    )


_MpAtmCCAtmMultiConfLeafVpTunneling_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfLeafVpTunneling_Object = MibTableColumn
mpAtmCCAtmMultiConfLeafVpTunneling = _MpAtmCCAtmMultiConfLeafVpTunneling_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 18),
    _MpAtmCCAtmMultiConfLeafVpTunneling_Type()
)
mpAtmCCAtmMultiConfLeafVpTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfLeafVpTunneling.setStatus("mandatory")


class _MpAtmCCAtmMultiConfNextLeaf_Type(Integer32):
    """Custom type mpAtmCCAtmMultiConfNextLeaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("ture", 1))
    )


_MpAtmCCAtmMultiConfNextLeaf_Type.__name__ = "Integer32"
_MpAtmCCAtmMultiConfNextLeaf_Object = MibTableColumn
mpAtmCCAtmMultiConfNextLeaf = _MpAtmCCAtmMultiConfNextLeaf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 110, 12, 3, 1, 19),
    _MpAtmCCAtmMultiConfNextLeaf_Type()
)
mpAtmCCAtmMultiConfNextLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAtmCCAtmMultiConfNextLeaf.setStatus("mandatory")
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MP-ATM-MIB",
    **{"RowStatus": RowStatus,
       "NetPrefix": NetPrefix,
       "DisplayString": DisplayString,
       "DateAndTime": DateAndTime,
       "MacAddress": MacAddress,
       "PhysAddress": PhysAddress,
       "AtmAddr": AtmAddr,
       "MpAtmCCCladType": MpAtmCCCladType,
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
       "mpAtmCCBaseGroup": mpAtmCCBaseGroup,
       "mpAtmCCNextTrafficDescrIndex": mpAtmCCNextTrafficDescrIndex,
       "mpAtmCCNextNodeVci": mpAtmCCNextNodeVci,
       "mpAtmCCStaticPVPC": mpAtmCCStaticPVPC,
       "mpAtmCCStaticPvpTable": mpAtmCCStaticPvpTable,
       "mpAtmCCStaticPvpEntry": mpAtmCCStaticPvpEntry,
       "mpAtmCCStaticPvpIndex": mpAtmCCStaticPvpIndex,
       "mpAtmCCStaticPvpLowIfIndex": mpAtmCCStaticPvpLowIfIndex,
       "mpAtmCCStaticPvpLowVpi": mpAtmCCStaticPvpLowVpi,
       "mpAtmCCStaticPvpHighIfIndex": mpAtmCCStaticPvpHighIfIndex,
       "mpAtmCCStaticPvpHighVpi": mpAtmCCStaticPvpHighVpi,
       "mpAtmCCStaticPvpLowReceiveTrafficDescrIndex": mpAtmCCStaticPvpLowReceiveTrafficDescrIndex,
       "mpAtmCCStaticPvpLowTransmitTrafficDescrIndex": mpAtmCCStaticPvpLowTransmitTrafficDescrIndex,
       "mpAtmCCStaticPvpHighReceiveTrafficDescrIndex": mpAtmCCStaticPvpHighReceiveTrafficDescrIndex,
       "mpAtmCCStaticPvpHighTransmitTrafficDescrIndex": mpAtmCCStaticPvpHighTransmitTrafficDescrIndex,
       "mpAtmCCStaticPvpPriority": mpAtmCCStaticPvpPriority,
       "mpAtmCCStaticPvpLowCladType": mpAtmCCStaticPvpLowCladType,
       "mpAtmCCStaticPvpHighCladType": mpAtmCCStaticPvpHighCladType,
       "mpAtmCCStaticPvpAdminStatus": mpAtmCCStaticPvpAdminStatus,
       "mpAtmCCStaticPvpOperStatus": mpAtmCCStaticPvpOperStatus,
       "mpAtmCCStaticPvpPvpId": mpAtmCCStaticPvpPvpId,
       "mpAtmCCStaticPvpSeqNo": mpAtmCCStaticPvpSeqNo,
       "mpAtmCCStaticPvpPgcRequest": mpAtmCCStaticPvpPgcRequest,
       "mpAtmCCStaticPvpCfgStatus": mpAtmCCStaticPvpCfgStatus,
       "mpAtmCCStaticPvpErrInfo": mpAtmCCStaticPvpErrInfo,
       "mpAtmCCStaticPvcTable": mpAtmCCStaticPvcTable,
       "mpAtmCCStaticPvcEntry": mpAtmCCStaticPvcEntry,
       "mpAtmCCStaticPvcIndex": mpAtmCCStaticPvcIndex,
       "mpAtmCCStaticPvcLowIfIndex": mpAtmCCStaticPvcLowIfIndex,
       "mpAtmCCStaticPvcLowVpi": mpAtmCCStaticPvcLowVpi,
       "mpAtmCCStaticPvcLowVci": mpAtmCCStaticPvcLowVci,
       "mpAtmCCStaticPvcHighIfIndex": mpAtmCCStaticPvcHighIfIndex,
       "mpAtmCCStaticPvcHighVpi": mpAtmCCStaticPvcHighVpi,
       "mpAtmCCStaticPvcHighVci": mpAtmCCStaticPvcHighVci,
       "mpAtmCCStaticPvcLowReceiveTrafficDescrIndex": mpAtmCCStaticPvcLowReceiveTrafficDescrIndex,
       "mpAtmCCStaticPvcLowTransmitTrafficDescrIndex": mpAtmCCStaticPvcLowTransmitTrafficDescrIndex,
       "mpAtmCCStaticPvcHighReceiveTrafficDescrIndex": mpAtmCCStaticPvcHighReceiveTrafficDescrIndex,
       "mpAtmCCStaticPvcHighTransmitTrafficDescrIndex": mpAtmCCStaticPvcHighTransmitTrafficDescrIndex,
       "mpAtmCCStaticPvcPriority": mpAtmCCStaticPvcPriority,
       "mpAtmCCStaticPvcLowCladType": mpAtmCCStaticPvcLowCladType,
       "mpAtmCCStaticPvcHighCladType": mpAtmCCStaticPvcHighCladType,
       "mpAtmCCStaticPvcAdminStatus": mpAtmCCStaticPvcAdminStatus,
       "mpAtmCCStaticPvcOperStatus": mpAtmCCStaticPvcOperStatus,
       "mpAtmCCStaticPvcPvcId": mpAtmCCStaticPvcPvcId,
       "mpAtmCCStaticPvcSeqNo": mpAtmCCStaticPvcSeqNo,
       "mpAtmCCStaticPvcPgcRequest": mpAtmCCStaticPvcPgcRequest,
       "mpAtmCCStaticPvcCfgStatus": mpAtmCCStaticPvcCfgStatus,
       "mpAtmCCStaticPvcErrInfo": mpAtmCCStaticPvcErrInfo,
       "mpAtmCCSoftPVPC": mpAtmCCSoftPVPC,
       "mpAtmCCSoftPvpTable": mpAtmCCSoftPvpTable,
       "mpAtmCCSoftPvpEntry": mpAtmCCSoftPvpEntry,
       "mpAtmCCSoftPvpLeafReference": mpAtmCCSoftPvpLeafReference,
       "mpAtmCCSoftPvpIfIndex": mpAtmCCSoftPvpIfIndex,
       "mpAtmCCSoftPvpVpi": mpAtmCCSoftPvpVpi,
       "mpAtmCCSoftPvpReceiveTrafficDescrIndex": mpAtmCCSoftPvpReceiveTrafficDescrIndex,
       "mpAtmCCSoftPvpTransmitTrafficDescrIndex": mpAtmCCSoftPvpTransmitTrafficDescrIndex,
       "mpAtmCCSoftPvpTargetAddress": mpAtmCCSoftPvpTargetAddress,
       "mpAtmCCSoftPvpTargetVpi": mpAtmCCSoftPvpTargetVpi,
       "mpAtmCCSoftPvpLastReleaseCause": mpAtmCCSoftPvpLastReleaseCause,
       "mpAtmCCSoftPvpLastReleaseDiagnostic": mpAtmCCSoftPvpLastReleaseDiagnostic,
       "mpAtmCCSoftPvpPriority": mpAtmCCSoftPvpPriority,
       "mpAtmCCSoftPvpCladType": mpAtmCCSoftPvpCladType,
       "mpAtmCCSoftPvpOriginalAddress": mpAtmCCSoftPvpOriginalAddress,
       "mpAtmCCSoftPvpAdminStatus": mpAtmCCSoftPvpAdminStatus,
       "mpAtmCCSoftPvpOperStatus": mpAtmCCSoftPvpOperStatus,
       "mpAtmCCSoftPvpPgcRequest": mpAtmCCSoftPvpPgcRequest,
       "mpAtmCCSoftPvpCfgStatus": mpAtmCCSoftPvpCfgStatus,
       "mpAtmCCSoftPvpErrInfo": mpAtmCCSoftPvpErrInfo,
       "mpAtmCCSoftPvcTable": mpAtmCCSoftPvcTable,
       "mpAtmCCSoftPvcEntry": mpAtmCCSoftPvcEntry,
       "mpAtmCCSoftPvcLeafReference": mpAtmCCSoftPvcLeafReference,
       "mpAtmCCSoftPvcIfIndex": mpAtmCCSoftPvcIfIndex,
       "mpAtmCCSoftPvcVpi": mpAtmCCSoftPvcVpi,
       "mpAtmCCSoftPvcVci": mpAtmCCSoftPvcVci,
       "mpAtmCCSoftPvcReceiveTrafficDescrIndex": mpAtmCCSoftPvcReceiveTrafficDescrIndex,
       "mpAtmCCSoftPvcTransmitTrafficDescrIndex": mpAtmCCSoftPvcTransmitTrafficDescrIndex,
       "mpAtmCCSoftPvcTargetAddress": mpAtmCCSoftPvcTargetAddress,
       "mpAtmCCSoftPvcTargetVpi": mpAtmCCSoftPvcTargetVpi,
       "mpAtmCCSoftPvcTargetVci": mpAtmCCSoftPvcTargetVci,
       "mpAtmCCSoftPvcLastReleaseCause": mpAtmCCSoftPvcLastReleaseCause,
       "mpAtmCCSoftPvcLastReleaseDiagnostic": mpAtmCCSoftPvcLastReleaseDiagnostic,
       "mpAtmCCSoftPvcPriority": mpAtmCCSoftPvcPriority,
       "mpAtmCCSoftPvcCladType": mpAtmCCSoftPvcCladType,
       "mpAtmCCSoftPvcOriginalAddress": mpAtmCCSoftPvcOriginalAddress,
       "mpAtmCCSoftPvcAdminStatus": mpAtmCCSoftPvcAdminStatus,
       "mpAtmCCSoftPvcOperStatus": mpAtmCCSoftPvcOperStatus,
       "mpAtmCCSoftPvcPgcRequest": mpAtmCCSoftPvcPgcRequest,
       "mpAtmCCSoftPvcCfgStatus": mpAtmCCSoftPvcCfgStatus,
       "mpAtmCCSoftPvcErrInfo": mpAtmCCSoftPvcErrInfo,
       "mpAtmCCSoftPvpCalledTable": mpAtmCCSoftPvpCalledTable,
       "mpAtmCCSoftPvpCalledEntry": mpAtmCCSoftPvpCalledEntry,
       "mpAtmCCSoftPvpCalledLeafReference": mpAtmCCSoftPvpCalledLeafReference,
       "mpAtmCCSoftPvpCalledIfIndex": mpAtmCCSoftPvpCalledIfIndex,
       "mpAtmCCSoftPvpCalledVpi": mpAtmCCSoftPvpCalledVpi,
       "mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex": mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex,
       "mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex": mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex,
       "mpAtmCCSoftPvpCalledTargetAddress": mpAtmCCSoftPvpCalledTargetAddress,
       "mpAtmCCSoftPvpCalledTargetVpi": mpAtmCCSoftPvpCalledTargetVpi,
       "mpAtmCCSoftPvpCalledLastReleaseCause": mpAtmCCSoftPvpCalledLastReleaseCause,
       "mpAtmCCSoftPvpCalledLastReleaseDiagnostic": mpAtmCCSoftPvpCalledLastReleaseDiagnostic,
       "mpAtmCCSoftPvpCalledPriority": mpAtmCCSoftPvpCalledPriority,
       "mpAtmCCSoftPvpCalledCladType": mpAtmCCSoftPvpCalledCladType,
       "mpAtmCCSoftPvpCalledOriginalAddress": mpAtmCCSoftPvpCalledOriginalAddress,
       "mpAtmCCSoftPvpCalledAdminStatus": mpAtmCCSoftPvpCalledAdminStatus,
       "mpAtmCCSoftPvpCalledOperStatus": mpAtmCCSoftPvpCalledOperStatus,
       "mpAtmCCSoftPvpCalledPgcRequest": mpAtmCCSoftPvpCalledPgcRequest,
       "mpAtmCCSoftPvpCalledCfgStatus": mpAtmCCSoftPvpCalledCfgStatus,
       "mpAtmCCSoftPvpCalledErrInfo": mpAtmCCSoftPvpCalledErrInfo,
       "mpAtmCCSoftPvcCalledTable": mpAtmCCSoftPvcCalledTable,
       "mpAtmCCSoftPvcCalledEntry": mpAtmCCSoftPvcCalledEntry,
       "mpAtmCCSoftPvcCalledLeafReference": mpAtmCCSoftPvcCalledLeafReference,
       "mpAtmCCSoftPvcCalledIfIndex": mpAtmCCSoftPvcCalledIfIndex,
       "mpAtmCCSoftPvcCalledVpi": mpAtmCCSoftPvcCalledVpi,
       "mpAtmCCSoftPvcCalledVci": mpAtmCCSoftPvcCalledVci,
       "mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex": mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex,
       "mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex": mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex,
       "mpAtmCCSoftPvcCalledTargetAddress": mpAtmCCSoftPvcCalledTargetAddress,
       "mpAtmCCSoftPvcCalledTargetVpi": mpAtmCCSoftPvcCalledTargetVpi,
       "mpAtmCCSoftPvcCalledTargetVci": mpAtmCCSoftPvcCalledTargetVci,
       "mpAtmCCSoftPvcCalledLastReleaseCause": mpAtmCCSoftPvcCalledLastReleaseCause,
       "mpAtmCCSoftPvcCalledLastReleaseDiagnostic": mpAtmCCSoftPvcCalledLastReleaseDiagnostic,
       "mpAtmCCSoftPvcCalledPriority": mpAtmCCSoftPvcCalledPriority,
       "mpAtmCCSoftPvcCalledCladType": mpAtmCCSoftPvcCalledCladType,
       "mpAtmCCSoftPvcCalledOriginalAddress": mpAtmCCSoftPvcCalledOriginalAddress,
       "mpAtmCCSoftPvcCalledAdminStatus": mpAtmCCSoftPvcCalledAdminStatus,
       "mpAtmCCSoftPvcCalledOperStatus": mpAtmCCSoftPvcCalledOperStatus,
       "mpAtmCCSoftPvcCalledPgcRequest": mpAtmCCSoftPvcCalledPgcRequest,
       "mpAtmCCSoftPvcCalledCfgStatus": mpAtmCCSoftPvcCalledCfgStatus,
       "mpAtmCCSoftPvcCalledErrInfo": mpAtmCCSoftPvcCalledErrInfo,
       "mpAtmCCStatistics": mpAtmCCStatistics,
       "mpAtmCCVpStatisticsTable": mpAtmCCVpStatisticsTable,
       "mpAtmCCVpStatisticsEntry": mpAtmCCVpStatisticsEntry,
       "mpAtmCCVpStatVpi": mpAtmCCVpStatVpi,
       "mpAtmCCVpStatInCells": mpAtmCCVpStatInCells,
       "mpAtmCCVpStatInCellsCounters": mpAtmCCVpStatInCellsCounters,
       "mpAtmCCVpStatOutCells": mpAtmCCVpStatOutCells,
       "mpAtmCCVpStatOutCellsCounters": mpAtmCCVpStatOutCellsCounters,
       "mpAtmCCVpStatInDropCells": mpAtmCCVpStatInDropCells,
       "mpAtmCCVpStatInDropCellsCounters": mpAtmCCVpStatInDropCellsCounters,
       "mpAtmCCVcStatisticsTable": mpAtmCCVcStatisticsTable,
       "mpAtmCCVcStatisticsEntry": mpAtmCCVcStatisticsEntry,
       "mpAtmCCVcStatVpi": mpAtmCCVcStatVpi,
       "mpAtmCCVcStatVci": mpAtmCCVcStatVci,
       "mpAtmCCVcStatInCells": mpAtmCCVcStatInCells,
       "mpAtmCCVcStatInCellsCounters": mpAtmCCVcStatInCellsCounters,
       "mpAtmCCVcStatOutCells": mpAtmCCVcStatOutCells,
       "mpAtmCCVcStatOutCellsCounters": mpAtmCCVcStatOutCellsCounters,
       "mpAtmCCVcStatInDropCells": mpAtmCCVcStatInDropCells,
       "mpAtmCCVcStatInDropCellsCounters": mpAtmCCVcStatInDropCellsCounters,
       "mpAtmCCOuspStatisticsTable": mpAtmCCOuspStatisticsTable,
       "mpAtmCCOuspStatisticsEntry": mpAtmCCOuspStatisticsEntry,
       "mpAtmCCOuspStatIndex": mpAtmCCOuspStatIndex,
       "mpAtmCCOuspStatRcvCrcErrCellsCounters": mpAtmCCOuspStatRcvCrcErrCellsCounters,
       "mpAtmCCOuspStatSendOfifoFullCounters": mpAtmCCOuspStatSendOfifoFullCounters,
       "mpAtmCCOuspStatRcvBufOverCounters": mpAtmCCOuspStatRcvBufOverCounters,
       "mpAtmCCOuspStatRcvUnknownCellsCounters": mpAtmCCOuspStatRcvUnknownCellsCounters,
       "mpAtmCCOuspStatRcvInvalidCellsCounters": mpAtmCCOuspStatRcvInvalidCellsCounters,
       "mpAtmCCOuspStatSendScheduleErrorCounters": mpAtmCCOuspStatSendScheduleErrorCounters,
       "mpAtmCCOuspStatRcvScheduleErrorCounters": mpAtmCCOuspStatRcvScheduleErrorCounters,
       "mpAtmCCOuspStatSendInvalidCdvCounters": mpAtmCCOuspStatSendInvalidCdvCounters,
       "mpAtmCCPhyStatisticsTable": mpAtmCCPhyStatisticsTable,
       "mpAtmCCPhyStatisticsEntry": mpAtmCCPhyStatisticsEntry,
       "mpAtmCCPhyStatTmtCellsCounters": mpAtmCCPhyStatTmtCellsCounters,
       "mpAtmCCPhyStatRcvCellsCounters": mpAtmCCPhyStatRcvCellsCounters,
       "mpAtmCCPhyStatCorrectHecErrCounters": mpAtmCCPhyStatCorrectHecErrCounters,
       "mpAtmCCPhyStatUncorrectHecErrCounters": mpAtmCCPhyStatUncorrectHecErrCounters,
       "mpAtmCCPhyStatB1ErrCounters": mpAtmCCPhyStatB1ErrCounters,
       "mpAtmCCPhyStatB2ErrCounters": mpAtmCCPhyStatB2ErrCounters,
       "mpAtmCCPhyStatB3ErrCounters": mpAtmCCPhyStatB3ErrCounters,
       "mpAtmCCPhyStatFebeCounters": mpAtmCCPhyStatFebeCounters,
       "mpAtmCCPhyStatSymbolErrCounters": mpAtmCCPhyStatSymbolErrCounters,
       "mpAtmCCPhyStatParityErrCounters": mpAtmCCPhyStatParityErrCounters,
       "mpAtmCCPortAlarmStatisticsTable": mpAtmCCPortAlarmStatisticsTable,
       "mpAtmCCPortAlarmStatisticsEntry": mpAtmCCPortAlarmStatisticsEntry,
       "mpAtmCCPortAlarmStatRedLosCounters": mpAtmCCPortAlarmStatRedLosCounters,
       "mpAtmCCPortAlarmStatRedLofCounters": mpAtmCCPortAlarmStatRedLofCounters,
       "mpAtmCCPortAlarmStatRedMsAisCounters": mpAtmCCPortAlarmStatRedMsAisCounters,
       "mpAtmCCPortAlarmStatRedLopCounters": mpAtmCCPortAlarmStatRedLopCounters,
       "mpAtmCCPortAlarmStatRedPAisCounters": mpAtmCCPortAlarmStatRedPAisCounters,
       "mpAtmCCPortAlarmStatRedLocCounters": mpAtmCCPortAlarmStatRedLocCounters,
       "mpAtmCCPortAlarmStatRedResetCounters": mpAtmCCPortAlarmStatRedResetCounters,
       "mpAtmCCPortAlarmStatRedCcRedCounters": mpAtmCCPortAlarmStatRedCcRedCounters,
       "mpAtmCCPortAlarmStatRedOofCounters": mpAtmCCPortAlarmStatRedOofCounters,
       "mpAtmCCPortAlarmStatRedAisCounters": mpAtmCCPortAlarmStatRedAisCounters,
       "mpAtmCCPortAlarmStatRedPOofCounters": mpAtmCCPortAlarmStatRedPOofCounters,
       "mpAtmCCPortAlarmStatRedBadSigCounters": mpAtmCCPortAlarmStatRedBadSigCounters,
       "mpAtmCCPortAlarmStatRedLcdCounters": mpAtmCCPortAlarmStatRedLcdCounters,
       "mpAtmCCPortAlarmStatRedLinkAisCounters": mpAtmCCPortAlarmStatRedLinkAisCounters,
       "mpAtmCCPortAlarmStatRedInfo0Counters": mpAtmCCPortAlarmStatRedInfo0Counters,
       "mpAtmCCPortAlarmStatYelMsRdiCounters": mpAtmCCPortAlarmStatYelMsRdiCounters,
       "mpAtmCCPortAlarmStatYelPRdiCounters": mpAtmCCPortAlarmStatYelPRdiCounters,
       "mpAtmCCPortAlarmStatYelCcYelCounters": mpAtmCCPortAlarmStatYelCcYelCounters,
       "mpAtmCCPortAlarmStatYelRaiCounters": mpAtmCCPortAlarmStatYelRaiCounters,
       "mpAtmCCPortAlarmStatYelPRaiCounters": mpAtmCCPortAlarmStatYelPRaiCounters,
       "mpAtmCCPortAlarmStatYelInfo2Counters": mpAtmCCPortAlarmStatYelInfo2Counters,
       "mpAtmCCVpTunnellingStatisticsTable": mpAtmCCVpTunnellingStatisticsTable,
       "mpAtmCCVpTunnellingStatisticsEntry": mpAtmCCVpTunnellingStatisticsEntry,
       "mpAtmCCVpTunStatTmtCellsCounters": mpAtmCCVpTunStatTmtCellsCounters,
       "mpAtmCCVpTunStatRcvCellsCounters": mpAtmCCVpTunStatRcvCellsCounters,
       "mpAtmCCVccStatisticsRegTable": mpAtmCCVccStatisticsRegTable,
       "mpAtmCCVccStatisticsRegEntry": mpAtmCCVccStatisticsRegEntry,
       "mpAtmCCVccStatRegVpi": mpAtmCCVccStatRegVpi,
       "mpAtmCCVccStatRegVci": mpAtmCCVccStatRegVci,
       "mpAtmCCVccStatRegInCellsCounters": mpAtmCCVccStatRegInCellsCounters,
       "mpAtmCCVccStatRegOutCellsCounters": mpAtmCCVccStatRegOutCellsCounters,
       "mpAtmCCVccStatRegStatus": mpAtmCCVccStatRegStatus,
       "mpAtmCCVccStatRegErrInfo": mpAtmCCVccStatRegErrInfo,
       "mpAtmCCResourceControl": mpAtmCCResourceControl,
       "mpAtmCCPortResourceInfomationTable": mpAtmCCPortResourceInfomationTable,
       "mpAtmCCPortResourceInfomationEntry": mpAtmCCPortResourceInfomationEntry,
       "mpAtmCCPortResInfoPortSpeed": mpAtmCCPortResInfoPortSpeed,
       "mpAtmCCPortResInfoMaxVpiBits": mpAtmCCPortResInfoMaxVpiBits,
       "mpAtmCCPortResInfoMaxVciBits": mpAtmCCPortResInfoMaxVciBits,
       "mpAtmCCPortResInfoMaxVPC": mpAtmCCPortResInfoMaxVPC,
       "mpAtmCCPortResInfoMaxVCC": mpAtmCCPortResInfoMaxVCC,
       "mpAtmCCPortResInfoMaxSvpcVpi": mpAtmCCPortResInfoMaxSvpcVpi,
       "mpAtmCCPortResInfoMaxSvccVpi": mpAtmCCPortResInfoMaxSvccVpi,
       "mpAtmCCPortResInfoMinSvccVci": mpAtmCCPortResInfoMinSvccVci,
       "mpAtmCCPortResInfoShaperKind": mpAtmCCPortResInfoShaperKind,
       "mpAtmCCPortResInfoVpTunnellingConfig": mpAtmCCPortResInfoVpTunnellingConfig,
       "mpAtmCCPortResInfoSvccVciHuntWay": mpAtmCCPortResInfoSvccVciHuntWay,
       "mpAtmCCPortResInfoVpiCounters": mpAtmCCPortResInfoVpiCounters,
       "mpAtmCCPortResInfoVpcCounters": mpAtmCCPortResInfoVpcCounters,
       "mpAtmCCPortResInfoVccCounters": mpAtmCCPortResInfoVccCounters,
       "mpAtmCCPortBandwidthInfomationTable": mpAtmCCPortBandwidthInfomationTable,
       "mpAtmCCPortBandwidthInfomationEntry": mpAtmCCPortBandwidthInfomationEntry,
       "mpAtmCCPortBwInfoVpi": mpAtmCCPortBwInfoVpi,
       "mpAtmCCPortBwInfoRawBandwidthBps": mpAtmCCPortBwInfoRawBandwidthBps,
       "mpAtmCCPortBwInfoRawBandwidthCps": mpAtmCCPortBwInfoRawBandwidthCps,
       "mpAtmCCPortBwInfoTmitUsedBwCps": mpAtmCCPortBwInfoTmitUsedBwCps,
       "mpAtmCCPortBwInfoRcvUsedBwCps": mpAtmCCPortBwInfoRcvUsedBwCps,
       "mpAtmCCPortBwInfoVciCounters": mpAtmCCPortBwInfoVciCounters,
       "mpAtmCCBwInfoPortTable": mpAtmCCBwInfoPortTable,
       "mpAtmCCBwInfoPortEntry": mpAtmCCBwInfoPortEntry,
       "mpAtmCCBwInfoPortRawBandwidthBps": mpAtmCCBwInfoPortRawBandwidthBps,
       "mpAtmCCBwInfoPortRawBandwidthCps": mpAtmCCBwInfoPortRawBandwidthCps,
       "mpAtmCCBwInfoPortTmitUsedBwCps": mpAtmCCBwInfoPortTmitUsedBwCps,
       "mpAtmCCBwInfoPortRcvUsedBwCps": mpAtmCCBwInfoPortRcvUsedBwCps,
       "mpAtmCCBwInfoPortTmitRemainBwCps": mpAtmCCBwInfoPortTmitRemainBwCps,
       "mpAtmCCBwInfoPortRcvRemainBwCps": mpAtmCCBwInfoPortRcvRemainBwCps,
       "mpAtmCCBwInfoPortVpTunneling": mpAtmCCBwInfoPortVpTunneling,
       "mpAtmCCProtocol": mpAtmCCProtocol,
       "mpAtmCCSscopTable": mpAtmCCSscopTable,
       "mpAtmCCSscopEntry": mpAtmCCSscopEntry,
       "mpAtmCCSscopTimerPoll": mpAtmCCSscopTimerPoll,
       "mpAtmCCSscopTimerNoResponce": mpAtmCCSscopTimerNoResponce,
       "mpAtmCCSscopTimerKeepAlive": mpAtmCCSscopTimerKeepAlive,
       "mpAtmCCSscopTimerIdle": mpAtmCCSscopTimerIdle,
       "mpAtmCCSscopTimerCc": mpAtmCCSscopTimerCc,
       "mpAtmCCSscopMaxCc": mpAtmCCSscopMaxCc,
       "mpAtmCCSscopMaxPd": mpAtmCCSscopMaxPd,
       "mpAtmCCSscopMaxStat": mpAtmCCSscopMaxStat,
       "mpAtmCCSscopClearBuffs": mpAtmCCSscopClearBuffs,
       "mpAtmCCSscopCredit": mpAtmCCSscopCredit,
       "mpAtmCCIlmiTable": mpAtmCCIlmiTable,
       "mpAtmCCIlmiEntry": mpAtmCCIlmiEntry,
       "mpAtmCCIlmiConfigStatus": mpAtmCCIlmiConfigStatus,
       "mpAtmCClmiMaxTransmissions": mpAtmCClmiMaxTransmissions,
       "mpAtmCCIlmiRetransmitInterval": mpAtmCCIlmiRetransmitInterval,
       "mpAtmCCSignallingTable": mpAtmCCSignallingTable,
       "mpAtmCCSignallingEntry": mpAtmCCSignallingEntry,
       "mpAtmCCSignallingT301": mpAtmCCSignallingT301,
       "mpAtmCCSignallingT303": mpAtmCCSignallingT303,
       "mpAtmCCSignallingT308": mpAtmCCSignallingT308,
       "mpAtmCCSignallingT309": mpAtmCCSignallingT309,
       "mpAtmCCSignallingT310": mpAtmCCSignallingT310,
       "mpAtmCCSignallingT313": mpAtmCCSignallingT313,
       "mpAtmCCSignallingT316": mpAtmCCSignallingT316,
       "mpAtmCCSignallingT317": mpAtmCCSignallingT317,
       "mpAtmCCSignallingT322": mpAtmCCSignallingT322,
       "mpAtmCCSignallingT331": mpAtmCCSignallingT331,
       "mpAtmCCSignallingT397": mpAtmCCSignallingT397,
       "mpAtmCCSignallingT398": mpAtmCCSignallingT398,
       "mpAtmCCSignallingT399": mpAtmCCSignallingT399,
       "mpAtmCCProtocolTrapInfoTable": mpAtmCCProtocolTrapInfoTable,
       "mpAtmCCProtocolTrapInfoEntry": mpAtmCCProtocolTrapInfoEntry,
       "mpAtmCCProtocolTrapInfoIndex": mpAtmCCProtocolTrapInfoIndex,
       "mpAtmCCProtocolTrapInfoCause": mpAtmCCProtocolTrapInfoCause,
       "mpAtmCCPathTrace": mpAtmCCPathTrace,
       "mpAtmCCVccStatusTable": mpAtmCCVccStatusTable,
       "mpAtmCCVccStatusEntry": mpAtmCCVccStatusEntry,
       "mpAtmCCVccStatusOrgPort": mpAtmCCVccStatusOrgPort,
       "mpAtmCCVccStatusOrgVpi": mpAtmCCVccStatusOrgVpi,
       "mpAtmCCVccStatusOrgVci": mpAtmCCVccStatusOrgVci,
       "mpAtmCCVccStatusDestPort": mpAtmCCVccStatusDestPort,
       "mpAtmCCVccStatusDestVpi": mpAtmCCVccStatusDestVpi,
       "mpAtmCCVccStatusDestVci": mpAtmCCVccStatusDestVci,
       "mpAtmCCVccStatusPathKind": mpAtmCCVccStatusPathKind,
       "mpAtmCCVccStatusOrgCallKind": mpAtmCCVccStatusOrgCallKind,
       "mpAtmCCVccStatusDestCallKind": mpAtmCCVccStatusDestCallKind,
       "mpAtmCCVccStatusAdminStatus": mpAtmCCVccStatusAdminStatus,
       "mpAtmCCVccStatusOperStatus": mpAtmCCVccStatusOperStatus,
       "mpAtmCCVccStatusInsStatus": mpAtmCCVccStatusInsStatus,
       "mpAtmCCVccStatusOrgPortVpTunneling": mpAtmCCVccStatusOrgPortVpTunneling,
       "mpAtmCCVccStatusDestPortVpTunneling": mpAtmCCVccStatusDestPortVpTunneling,
       "mpAtmCCVccStatusConnCastType": mpAtmCCVccStatusConnCastType,
       "mpAtmCCPvcTraceControlTable": mpAtmCCPvcTraceControlTable,
       "mpAtmCCPvcTraceCtlEntry": mpAtmCCPvcTraceCtlEntry,
       "mpAtmCCPvcTraceIndex": mpAtmCCPvcTraceIndex,
       "mpAtmCCPvcTraceCtlPathKind": mpAtmCCPvcTraceCtlPathKind,
       "mpAtmCCPvcTraceCtlIfIndex": mpAtmCCPvcTraceCtlIfIndex,
       "mpAtmCCPvcTraceCtlVpi": mpAtmCCPvcTraceCtlVpi,
       "mpAtmCCPvcTraceCtlVci": mpAtmCCPvcTraceCtlVci,
       "mpAtmCCPvcTraceCtlStatus": mpAtmCCPvcTraceCtlStatus,
       "mpAtmCCPvcTraceInfoTable": mpAtmCCPvcTraceInfoTable,
       "mpAtmCCPvcTraceInfoEntry": mpAtmCCPvcTraceInfoEntry,
       "mpAtmCCPvcTraceEntryIndex": mpAtmCCPvcTraceEntryIndex,
       "mpAtmCCPvcTraceInfoSysName": mpAtmCCPvcTraceInfoSysName,
       "mpAtmCCPvcTraceInfoIfIndex": mpAtmCCPvcTraceInfoIfIndex,
       "mpAtmCCPvcTraceInfoVpi": mpAtmCCPvcTraceInfoVpi,
       "mpAtmCCPvcTraceInfoVci": mpAtmCCPvcTraceInfoVci,
       "mpAtmCCPvcTraceInfoPathKind": mpAtmCCPvcTraceInfoPathKind,
       "mpAtmCCPvcTraceInfoCallKind": mpAtmCCPvcTraceInfoCallKind,
       "mpAtmCCPvcTraceInfoLastSegment": mpAtmCCPvcTraceInfoLastSegment,
       "mpAtmCCMuxMib": mpAtmCCMuxMib,
       "mpAtmCCMuxStatistics": mpAtmCCMuxStatistics,
       "mpAtmCCMuxStatReceiveCellsCounters": mpAtmCCMuxStatReceiveCellsCounters,
       "mpAtmCCMuxStatReceiveCellsCntOvfCounters": mpAtmCCMuxStatReceiveCellsCntOvfCounters,
       "mpAtmCCMuxStatDiscardCellsBufOvfCounters": mpAtmCCMuxStatDiscardCellsBufOvfCounters,
       "mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters": mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters,
       "mpAtmCCMuxStatDiscardCellsHTErrCounters": mpAtmCCMuxStatDiscardCellsHTErrCounters,
       "mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters": mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters,
       "mpAtmCCMuxStatDiscardCellsThresholdOvfCounters": mpAtmCCMuxStatDiscardCellsThresholdOvfCounters,
       "mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters": mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters,
       "mpAtmCCVpTunneling": mpAtmCCVpTunneling,
       "mpAtmCCVpTunnelingTable": mpAtmCCVpTunnelingTable,
       "mpAtmCCVpTunnelingEntry": mpAtmCCVpTunnelingEntry,
       "mpAtmCCVpTunnelingVpi": mpAtmCCVpTunnelingVpi,
       "mpAtmCCVpTunnelingAdminStatus": mpAtmCCVpTunnelingAdminStatus,
       "mpAtmCCVpTunnelingOperStatus": mpAtmCCVpTunnelingOperStatus,
       "mpAtmCCVpTunnelingSpeed": mpAtmCCVpTunnelingSpeed,
       "mpAtmCCVpTunnelingNeighborInfo": mpAtmCCVpTunnelingNeighborInfo,
       "mpAtmCCVpTunnelingPnniVer": mpAtmCCVpTunnelingPnniVer,
       "mpAtmCCVpTunnelingContinuityCheck": mpAtmCCVpTunnelingContinuityCheck,
       "mpAtmCCVpTunnelingTrapState": mpAtmCCVpTunnelingTrapState,
       "mpAtmCCVpTunnelingSeverity": mpAtmCCVpTunnelingSeverity,
       "mpAtmCCVpTunnelingCfgStatus": mpAtmCCVpTunnelingCfgStatus,
       "mpAtmCCVpTunnelingErrInfo": mpAtmCCVpTunnelingErrInfo,
       "mpAtmCCPathTest": mpAtmCCPathTest,
       "mpAtmCCPathTestTable": mpAtmCCPathTestTable,
       "mpAtmCCPathTestEntry": mpAtmCCPathTestEntry,
       "mpAtmCCPathTestVpi": mpAtmCCPathTestVpi,
       "mpAtmCCPathTestVci": mpAtmCCPathTestVci,
       "mpAtmCCPathTestStatus": mpAtmCCPathTestStatus,
       "mpAtmCCPathTestSendDirection": mpAtmCCPathTestSendDirection,
       "mpAtmCCPathTestSendTime": mpAtmCCPathTestSendTime,
       "mpAtmCCPathTestSendCellsCounters": mpAtmCCPathTestSendCellsCounters,
       "mpAtmCCPathTestRcvCellsCounters": mpAtmCCPathTestRcvCellsCounters,
       "mpAtmCCPathTestErrInfo": mpAtmCCPathTestErrInfo,
       "mpAtmCCPvcGroupCutover": mpAtmCCPvcGroupCutover,
       "mpAtmCCPvcGroupCutoverBaseInfo": mpAtmCCPvcGroupCutoverBaseInfo,
       "mpAtmCCPvcGroupCutoverEnable": mpAtmCCPvcGroupCutoverEnable,
       "mpAtmCCPvcGroupCutoverStatus": mpAtmCCPvcGroupCutoverStatus,
       "mpAtmCCUnitePvcGroup": mpAtmCCUnitePvcGroup,
       "mpAtmCCUpgcBaseInfo": mpAtmCCUpgcBaseInfo,
       "mpAtmCCUpgcTotalGroupNumber": mpAtmCCUpgcTotalGroupNumber,
       "mpAtmCCUpgcBaseActiveGroupNumber": mpAtmCCUpgcBaseActiveGroupNumber,
       "mpAtmCCUnitePvcGroupControlTable": mpAtmCCUnitePvcGroupControlTable,
       "mpAtmCCUpgcCtlEntry": mpAtmCCUpgcCtlEntry,
       "mpAtmCCUpgcIndex": mpAtmCCUpgcIndex,
       "mpAtmCCUpgcCtlStatus": mpAtmCCUpgcCtlStatus,
       "mpAtmCCUpgcCtlCountPgc": mpAtmCCUpgcCtlCountPgc,
       "mpAtmCCUpgcCtlResult": mpAtmCCUpgcCtlResult,
       "mpAtmCCUnitePvcGroupRegisterTable": mpAtmCCUnitePvcGroupRegisterTable,
       "mpAtmCCUpgcRegiEntry": mpAtmCCUpgcRegiEntry,
       "mpAtmCCUpgcPgcIndex": mpAtmCCUpgcPgcIndex,
       "mpAtmCCUpgcRegiStatus": mpAtmCCUpgcRegiStatus,
       "mpAtmCCPvcGroup": mpAtmCCPvcGroup,
       "mpAtmCCPgcBaseInfo": mpAtmCCPgcBaseInfo,
       "mpAtmCCPgcTotalGroupNumber": mpAtmCCPgcTotalGroupNumber,
       "mpAtmCCPvcGroupControlTable": mpAtmCCPvcGroupControlTable,
       "mpAtmCCPgcCtlEntry": mpAtmCCPgcCtlEntry,
       "mpAtmCCPgcIndex": mpAtmCCPgcIndex,
       "mpAtmCCPgcCtlStatus": mpAtmCCPgcCtlStatus,
       "mpAtmCCPgcCtlCountPvc": mpAtmCCPgcCtlCountPvc,
       "mpAtmCCPgcCtlResult": mpAtmCCPgcCtlResult,
       "mpAtmCCPvcGroupRegisterTable": mpAtmCCPvcGroupRegisterTable,
       "mpAtmCCPgcRegiEntry": mpAtmCCPgcRegiEntry,
       "mpAtmCCPgcPvcIfIndex": mpAtmCCPgcPvcIfIndex,
       "mpAtmCCPgcPvcVpi": mpAtmCCPgcPvcVpi,
       "mpAtmCCPgcPvcVci": mpAtmCCPgcPvcVci,
       "mpAtmCCPgcPvcKind": mpAtmCCPgcPvcKind,
       "mpAtmCCPgcStaticPvcDestIfIndex": mpAtmCCPgcStaticPvcDestIfIndex,
       "mpAtmCCPgcSoftPvcDestAtmAddress": mpAtmCCPgcSoftPvcDestAtmAddress,
       "mpAtmCCPgcPvcDestVpi": mpAtmCCPgcPvcDestVpi,
       "mpAtmCCPgcPvcDestVci": mpAtmCCPgcPvcDestVci,
       "mpAtmCCPgcPvcReceiveTrafficDescrIndex": mpAtmCCPgcPvcReceiveTrafficDescrIndex,
       "mpAtmCCPgcPvcTransmitTrafficDescrIndex": mpAtmCCPgcPvcTransmitTrafficDescrIndex,
       "mpAtmCCPgcPvcPriority": mpAtmCCPgcPvcPriority,
       "mpAtmCCPgcStaticPvcId": mpAtmCCPgcStaticPvcId,
       "mpAtmCCPgcStaticPvcSeqNo": mpAtmCCPgcStaticPvcSeqNo,
       "mpAtmCCPgcSoftPvcCallKind": mpAtmCCPgcSoftPvcCallKind,
       "mpAtmCCPgcRegiAdminStatus": mpAtmCCPgcRegiAdminStatus,
       "mpAtmCCPgcRegiCfgStatus": mpAtmCCPgcRegiCfgStatus,
       "mpAtmCCPgcRegiErrInfo": mpAtmCCPgcRegiErrInfo,
       "mpAtmCCPvcGroupActiveInfoTable": mpAtmCCPvcGroupActiveInfoTable,
       "mpAtmCCPgcActInfoEntry": mpAtmCCPgcActInfoEntry,
       "mpAtmCCPgcActGrpNum": mpAtmCCPgcActGrpNum,
       "mpAtmCCAtmMulticast": mpAtmCCAtmMulticast,
       "mpAtmCCAtmMulticastRegistration": mpAtmCCAtmMulticastRegistration,
       "mpAtmCCAtmMultiRootIfIndex": mpAtmCCAtmMultiRootIfIndex,
       "mpAtmCCAtmMultiRootVpi": mpAtmCCAtmMultiRootVpi,
       "mpAtmCCAtmMultiRootVci": mpAtmCCAtmMultiRootVci,
       "mpAtmCCAtmMultiLeafIfIndex": mpAtmCCAtmMultiLeafIfIndex,
       "mpAtmCCAtmMultiLeafVpi": mpAtmCCAtmMultiLeafVpi,
       "mpAtmCCAtmMultiLeafVci": mpAtmCCAtmMultiLeafVci,
       "mpAtmCCAtmMultiTrafficDescrIndex": mpAtmCCAtmMultiTrafficDescrIndex,
       "mpAtmCCAtmMultiSlotNumber": mpAtmCCAtmMultiSlotNumber,
       "mpAtmCCAtmMultiVcRdiResponse": mpAtmCCAtmMultiVcRdiResponse,
       "mpAtmCCAtmMultiPvcId": mpAtmCCAtmMultiPvcId,
       "mpAtmCCAtmMultiSeqNo": mpAtmCCAtmMultiSeqNo,
       "mpAtmCCAtmMultiCfgStatus": mpAtmCCAtmMultiCfgStatus,
       "mpAtmCCAtmMultiRegErrInfo": mpAtmCCAtmMultiRegErrInfo,
       "mpAtmCCAtmMulticastCtlTable": mpAtmCCAtmMulticastCtlTable,
       "mpAtmCCAtmMultiCtlEntry": mpAtmCCAtmMultiCtlEntry,
       "mpAtmCCAtmMultiIfIndex": mpAtmCCAtmMultiIfIndex,
       "mpAtmCCAtmMultiVpi": mpAtmCCAtmMultiVpi,
       "mpAtmCCAtmMultiVci": mpAtmCCAtmMultiVci,
       "mpAtmCCAtmMultiAdminStatus": mpAtmCCAtmMultiAdminStatus,
       "mpAtmCCAtmMultiOperStatus": mpAtmCCAtmMultiOperStatus,
       "mpAtmCCAtmMultiErrInfo": mpAtmCCAtmMultiErrInfo,
       "mpAtmCCAtmMulticastConfTable": mpAtmCCAtmMulticastConfTable,
       "mpAtmCCAtmMultiConfEntry": mpAtmCCAtmMultiConfEntry,
       "mpAtmCCAtmMultiConfRootIfIndex": mpAtmCCAtmMultiConfRootIfIndex,
       "mpAtmCCAtmMultiConfRootVpi": mpAtmCCAtmMultiConfRootVpi,
       "mpAtmCCAtmMultiConfRootVci": mpAtmCCAtmMultiConfRootVci,
       "mpAtmCCAtmMultiConfLeafIfIndex": mpAtmCCAtmMultiConfLeafIfIndex,
       "mpAtmCCAtmMultiConfLeafVpi": mpAtmCCAtmMultiConfLeafVpi,
       "mpAtmCCAtmMultiConfLeafVci": mpAtmCCAtmMultiConfLeafVci,
       "mpAtmCCAtmMultiConfRootAdminStatus": mpAtmCCAtmMultiConfRootAdminStatus,
       "mpAtmCCAtmMultiConfRootOperStatus": mpAtmCCAtmMultiConfRootOperStatus,
       "mpAtmCCAtmMultiConfLeafAdminStatus": mpAtmCCAtmMultiConfLeafAdminStatus,
       "mpAtmCCAtmMultiConfLeafOperStatus": mpAtmCCAtmMultiConfLeafOperStatus,
       "mpAtmCCAtmMultiConfTrafficDescrIndex": mpAtmCCAtmMultiConfTrafficDescrIndex,
       "mpAtmCCAtmMultiConfSlotNumber": mpAtmCCAtmMultiConfSlotNumber,
       "mpAtmCCAtmMultiConfVcRdiResponse": mpAtmCCAtmMultiConfVcRdiResponse,
       "mpAtmCCAtmMultiConfPvcId": mpAtmCCAtmMultiConfPvcId,
       "mpAtmCCAtmMultiConfSeqNo": mpAtmCCAtmMultiConfSeqNo,
       "mpAtmCCAtmMultiConfShaperRate": mpAtmCCAtmMultiConfShaperRate,
       "mpAtmCCAtmMultiConfRootVpTunneling": mpAtmCCAtmMultiConfRootVpTunneling,
       "mpAtmCCAtmMultiConfLeafVpTunneling": mpAtmCCAtmMultiConfLeafVpTunneling,
       "mpAtmCCAtmMultiConfNextLeaf": mpAtmCCAtmMultiConfNextLeaf,
       "mpCes": mpCes,
       "mpIpsw": mpIpsw,
       "mpInsCtl": mpInsCtl,
       "mpFfr": mpFfr}
)
