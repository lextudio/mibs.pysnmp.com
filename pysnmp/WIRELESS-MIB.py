# SNMP MIB module (WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:01 2024
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

(Timeticks,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "Timeticks")

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibmwlan_ObjectIdentity = ObjectIdentity
ibmwlan = _Ibmwlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 10)
)
_WrBase_ObjectIdentity = ObjectIdentity
wrBase = _WrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1)
)
_BaseName_Type = DisplayString
_BaseName_Object = MibScalar
baseName = _BaseName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 1),
    _BaseName_Type()
)
baseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseName.setStatus("mandatory")
_BaseNetworkName_Type = DisplayString
_BaseNetworkName_Object = MibScalar
baseNetworkName = _BaseNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 2),
    _BaseNetworkName_Type()
)
baseNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseNetworkName.setStatus("mandatory")
_BaseAdminIPAddr_Type = IpAddress
_BaseAdminIPAddr_Object = MibScalar
baseAdminIPAddr = _BaseAdminIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 3),
    _BaseAdminIPAddr_Type()
)
baseAdminIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseAdminIPAddr.setStatus("mandatory")
_WrBaseTable_Object = MibTable
wrBaseTable = _WrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4)
)
if mibBuilder.loadTexts:
    wrBaseTable.setStatus("mandatory")
_WrBaseEntry_Object = MibTableRow
wrBaseEntry = _WrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1)
)
wrBaseEntry.setIndexNames(
    (0, "WIRELESS-MIB", "baseIfIndex"),
)
if mibBuilder.loadTexts:
    wrBaseEntry.setStatus("mandatory")
_BaseIfIndex_Type = Integer32
_BaseIfIndex_Object = MibTableColumn
baseIfIndex = _BaseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 1),
    _BaseIfIndex_Type()
)
baseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseIfIndex.setStatus("mandatory")
_BaseHDLCaddress_Type = OctetString
_BaseHDLCaddress_Object = MibTableColumn
baseHDLCaddress = _BaseHDLCaddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 2),
    _BaseHDLCaddress_Type()
)
baseHDLCaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseHDLCaddress.setStatus("mandatory")
_BaseNbOFRemote_Type = Integer32
_BaseNbOFRemote_Object = MibTableColumn
baseNbOFRemote = _BaseNbOFRemote_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 3),
    _BaseNbOFRemote_Type()
)
baseNbOFRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseNbOFRemote.setStatus("mandatory")
_BaseCellIdentifier_Type = Integer32
_BaseCellIdentifier_Object = MibTableColumn
baseCellIdentifier = _BaseCellIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 4),
    _BaseCellIdentifier_Type()
)
baseCellIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseCellIdentifier.setStatus("mandatory")


class _BaseAdapterStatus_Type(Integer32):
    """Custom type baseAdapterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-operational", 2),
          ("operational", 1))
    )


_BaseAdapterStatus_Type.__name__ = "Integer32"
_BaseAdapterStatus_Object = MibTableColumn
baseAdapterStatus = _BaseAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 5),
    _BaseAdapterStatus_Type()
)
baseAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseAdapterStatus.setStatus("mandatory")
_BaseEmittedPower_Type = Integer32
_BaseEmittedPower_Object = MibTableColumn
baseEmittedPower = _BaseEmittedPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 6),
    _BaseEmittedPower_Type()
)
baseEmittedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseEmittedPower.setStatus("mandatory")
_BaseControllerCardDesc_Type = DisplayString
_BaseControllerCardDesc_Object = MibTableColumn
baseControllerCardDesc = _BaseControllerCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 7),
    _BaseControllerCardDesc_Type()
)
baseControllerCardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseControllerCardDesc.setStatus("mandatory")
_BaseUnivAddress_Type = MacAddress
_BaseUnivAddress_Object = MibTableColumn
baseUnivAddress = _BaseUnivAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 8),
    _BaseUnivAddress_Type()
)
baseUnivAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseUnivAddress.setStatus("mandatory")
_BaseModemDesc_Type = DisplayString
_BaseModemDesc_Object = MibTableColumn
baseModemDesc = _BaseModemDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 9),
    _BaseModemDesc_Type()
)
baseModemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseModemDesc.setStatus("mandatory")


class _BaseTopologyTrapActive_Type(Integer32):
    """Custom type baseTopologyTrapActive based on Integer32"""
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


_BaseTopologyTrapActive_Type.__name__ = "Integer32"
_BaseTopologyTrapActive_Object = MibTableColumn
baseTopologyTrapActive = _BaseTopologyTrapActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 10),
    _BaseTopologyTrapActive_Type()
)
baseTopologyTrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseTopologyTrapActive.setStatus("mandatory")
_WrBaseStatsTable_Object = MibTable
wrBaseStatsTable = _WrBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5)
)
if mibBuilder.loadTexts:
    wrBaseStatsTable.setStatus("mandatory")
_WrBaseStatsEntry_Object = MibTableRow
wrBaseStatsEntry = _WrBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1)
)
wrBaseStatsEntry.setIndexNames(
    (0, "WIRELESS-MIB", "baseStatsIfIndex"),
)
if mibBuilder.loadTexts:
    wrBaseStatsEntry.setStatus("mandatory")
_BaseStatsIfIndex_Type = Integer32
_BaseStatsIfIndex_Object = MibTableColumn
baseStatsIfIndex = _BaseStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 1),
    _BaseStatsIfIndex_Type()
)
baseStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsIfIndex.setStatus("mandatory")
_BaseStatsXmit_Type = Counter32
_BaseStatsXmit_Object = MibTableColumn
baseStatsXmit = _BaseStatsXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 2),
    _BaseStatsXmit_Type()
)
baseStatsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsXmit.setStatus("mandatory")
_BaseStatsRxmit_Type = Counter32
_BaseStatsRxmit_Object = MibTableColumn
baseStatsRxmit = _BaseStatsRxmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 3),
    _BaseStatsRxmit_Type()
)
baseStatsRxmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsRxmit.setStatus("mandatory")
_BaseStatsNegAckRcv_Type = Counter32
_BaseStatsNegAckRcv_Object = MibTableColumn
baseStatsNegAckRcv = _BaseStatsNegAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 4),
    _BaseStatsNegAckRcv_Type()
)
baseStatsNegAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsNegAckRcv.setStatus("mandatory")
_BaseStatsRcv_Type = Counter32
_BaseStatsRcv_Object = MibTableColumn
baseStatsRcv = _BaseStatsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 5),
    _BaseStatsRcv_Type()
)
baseStatsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsRcv.setStatus("mandatory")
_BaseStatsLineErrors_Type = Counter32
_BaseStatsLineErrors_Object = MibTableColumn
baseStatsLineErrors = _BaseStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 6),
    _BaseStatsLineErrors_Type()
)
baseStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsLineErrors.setStatus("mandatory")
_BaseStatsNegAckXmit_Type = Counter32
_BaseStatsNegAckXmit_Object = MibTableColumn
baseStatsNegAckXmit = _BaseStatsNegAckXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 7),
    _BaseStatsNegAckXmit_Type()
)
baseStatsNegAckXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsNegAckXmit.setStatus("mandatory")
_BaseStatsFramePurged_Type = Counter32
_BaseStatsFramePurged_Object = MibTableColumn
baseStatsFramePurged = _BaseStatsFramePurged_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 8),
    _BaseStatsFramePurged_Type()
)
baseStatsFramePurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsFramePurged.setStatus("mandatory")
_BaseStatsFreqDelete_Type = Counter32
_BaseStatsFreqDelete_Object = MibTableColumn
baseStatsFreqDelete = _BaseStatsFreqDelete_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 9),
    _BaseStatsFreqDelete_Type()
)
baseStatsFreqDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsFreqDelete.setStatus("mandatory")
_BaseStatsHopAdvance_Type = Counter32
_BaseStatsHopAdvance_Object = MibTableColumn
baseStatsHopAdvance = _BaseStatsHopAdvance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 10),
    _BaseStatsHopAdvance_Type()
)
baseStatsHopAdvance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsHopAdvance.setStatus("mandatory")
_BaseStatsCLineErrors_Type = Counter32
_BaseStatsCLineErrors_Object = MibTableColumn
baseStatsCLineErrors = _BaseStatsCLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 11),
    _BaseStatsCLineErrors_Type()
)
baseStatsCLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsCLineErrors.setStatus("mandatory")
_BaseStatsRcvICRFrame_Type = Counter32
_BaseStatsRcvICRFrame_Object = MibTableColumn
baseStatsRcvICRFrame = _BaseStatsRcvICRFrame_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 12),
    _BaseStatsRcvICRFrame_Type()
)
baseStatsRcvICRFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsRcvICRFrame.setStatus("mandatory")
_BaseStatsXmitICRFrame_Type = Counter32
_BaseStatsXmitICRFrame_Object = MibTableColumn
baseStatsXmitICRFrame = _BaseStatsXmitICRFrame_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 13),
    _BaseStatsXmitICRFrame_Type()
)
baseStatsXmitICRFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsXmitICRFrame.setStatus("mandatory")
_BaseStatsNoICRBufferAvail_Type = Counter32
_BaseStatsNoICRBufferAvail_Object = MibTableColumn
baseStatsNoICRBufferAvail = _BaseStatsNoICRBufferAvail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 14),
    _BaseStatsNoICRBufferAvail_Type()
)
baseStatsNoICRBufferAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsNoICRBufferAvail.setStatus("mandatory")
_BaseStatsNotRoutedICRFrame_Type = Counter32
_BaseStatsNotRoutedICRFrame_Object = MibTableColumn
baseStatsNotRoutedICRFrame = _BaseStatsNotRoutedICRFrame_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 15),
    _BaseStatsNotRoutedICRFrame_Type()
)
baseStatsNotRoutedICRFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsNotRoutedICRFrame.setStatus("mandatory")
_BaseStatsNbCUserEst_Type = Gauge32
_BaseStatsNbCUserEst_Object = MibTableColumn
baseStatsNbCUserEst = _BaseStatsNbCUserEst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 16),
    _BaseStatsNbCUserEst_Type()
)
baseStatsNbCUserEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatsNbCUserEst.setStatus("mandatory")
_WrRemote_ObjectIdentity = ObjectIdentity
wrRemote = _WrRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2)
)
_WrRemoteTable_Object = MibTable
wrRemoteTable = _WrRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1)
)
if mibBuilder.loadTexts:
    wrRemoteTable.setStatus("mandatory")
_WrRemoteEntry_Object = MibTableRow
wrRemoteEntry = _WrRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1)
)
wrRemoteEntry.setIndexNames(
    (0, "WIRELESS-MIB", "remIfIndex"),
    (0, "WIRELESS-MIB", "remIndex"),
)
if mibBuilder.loadTexts:
    wrRemoteEntry.setStatus("mandatory")
_RemIfIndex_Type = Integer32
_RemIfIndex_Object = MibTableColumn
remIfIndex = _RemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 1),
    _RemIfIndex_Type()
)
remIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remIfIndex.setStatus("mandatory")
_RemIndex_Type = Integer32
_RemIndex_Object = MibTableColumn
remIndex = _RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 2),
    _RemIndex_Type()
)
remIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remIndex.setStatus("mandatory")
_RemMacAddress_Type = MacAddress
_RemMacAddress_Object = MibTableColumn
remMacAddress = _RemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 3),
    _RemMacAddress_Type()
)
remMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMacAddress.setStatus("mandatory")
_RemName_Type = DisplayString
_RemName_Object = MibTableColumn
remName = _RemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 4),
    _RemName_Type()
)
remName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remName.setStatus("mandatory")
_RemControllerCardDesc_Type = DisplayString
_RemControllerCardDesc_Object = MibTableColumn
remControllerCardDesc = _RemControllerCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 5),
    _RemControllerCardDesc_Type()
)
remControllerCardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remControllerCardDesc.setStatus("mandatory")
_RemUnivAddress_Type = MacAddress
_RemUnivAddress_Object = MibTableColumn
remUnivAddress = _RemUnivAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 6),
    _RemUnivAddress_Type()
)
remUnivAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remUnivAddress.setStatus("mandatory")
_RemModemDesc_Type = DisplayString
_RemModemDesc_Object = MibTableColumn
remModemDesc = _RemModemDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 7),
    _RemModemDesc_Type()
)
remModemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remModemDesc.setStatus("mandatory")
_WrRemoteStatsTable_Object = MibTable
wrRemoteStatsTable = _WrRemoteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2)
)
if mibBuilder.loadTexts:
    wrRemoteStatsTable.setStatus("mandatory")
_WrRemStatsEntry_Object = MibTableRow
wrRemStatsEntry = _WrRemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1)
)
wrRemStatsEntry.setIndexNames(
    (0, "WIRELESS-MIB", "remStatsIfIndex"),
    (0, "WIRELESS-MIB", "remStatsIndex"),
)
if mibBuilder.loadTexts:
    wrRemStatsEntry.setStatus("mandatory")
_RemStatsIfIndex_Type = Integer32
_RemStatsIfIndex_Object = MibTableColumn
remStatsIfIndex = _RemStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 1),
    _RemStatsIfIndex_Type()
)
remStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsIfIndex.setStatus("mandatory")
_RemStatsIndex_Type = Integer32
_RemStatsIndex_Object = MibTableColumn
remStatsIndex = _RemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 2),
    _RemStatsIndex_Type()
)
remStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsIndex.setStatus("mandatory")
_RemStatsXmit_Type = Counter32
_RemStatsXmit_Object = MibTableColumn
remStatsXmit = _RemStatsXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 3),
    _RemStatsXmit_Type()
)
remStatsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsXmit.setStatus("mandatory")
_RemStatsRxmit_Type = Counter32
_RemStatsRxmit_Object = MibTableColumn
remStatsRxmit = _RemStatsRxmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 4),
    _RemStatsRxmit_Type()
)
remStatsRxmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsRxmit.setStatus("mandatory")
_RemStatsNegAckRcv_Type = Counter32
_RemStatsNegAckRcv_Object = MibTableColumn
remStatsNegAckRcv = _RemStatsNegAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 5),
    _RemStatsNegAckRcv_Type()
)
remStatsNegAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsNegAckRcv.setStatus("mandatory")
_RemStatsRcv_Type = Counter32
_RemStatsRcv_Object = MibTableColumn
remStatsRcv = _RemStatsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 6),
    _RemStatsRcv_Type()
)
remStatsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsRcv.setStatus("mandatory")
_RemStatsLineErrors_Type = Counter32
_RemStatsLineErrors_Object = MibTableColumn
remStatsLineErrors = _RemStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 7),
    _RemStatsLineErrors_Type()
)
remStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsLineErrors.setStatus("mandatory")
_RemStatsNegAckXmit_Type = Counter32
_RemStatsNegAckXmit_Object = MibTableColumn
remStatsNegAckXmit = _RemStatsNegAckXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 8),
    _RemStatsNegAckXmit_Type()
)
remStatsNegAckXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remStatsNegAckXmit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WIRELESS-MIB",
    **{"MacAddress": MacAddress,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibmwlan": ibmwlan,
       "wrBase": wrBase,
       "baseName": baseName,
       "baseNetworkName": baseNetworkName,
       "baseAdminIPAddr": baseAdminIPAddr,
       "wrBaseTable": wrBaseTable,
       "wrBaseEntry": wrBaseEntry,
       "baseIfIndex": baseIfIndex,
       "baseHDLCaddress": baseHDLCaddress,
       "baseNbOFRemote": baseNbOFRemote,
       "baseCellIdentifier": baseCellIdentifier,
       "baseAdapterStatus": baseAdapterStatus,
       "baseEmittedPower": baseEmittedPower,
       "baseControllerCardDesc": baseControllerCardDesc,
       "baseUnivAddress": baseUnivAddress,
       "baseModemDesc": baseModemDesc,
       "baseTopologyTrapActive": baseTopologyTrapActive,
       "wrBaseStatsTable": wrBaseStatsTable,
       "wrBaseStatsEntry": wrBaseStatsEntry,
       "baseStatsIfIndex": baseStatsIfIndex,
       "baseStatsXmit": baseStatsXmit,
       "baseStatsRxmit": baseStatsRxmit,
       "baseStatsNegAckRcv": baseStatsNegAckRcv,
       "baseStatsRcv": baseStatsRcv,
       "baseStatsLineErrors": baseStatsLineErrors,
       "baseStatsNegAckXmit": baseStatsNegAckXmit,
       "baseStatsFramePurged": baseStatsFramePurged,
       "baseStatsFreqDelete": baseStatsFreqDelete,
       "baseStatsHopAdvance": baseStatsHopAdvance,
       "baseStatsCLineErrors": baseStatsCLineErrors,
       "baseStatsRcvICRFrame": baseStatsRcvICRFrame,
       "baseStatsXmitICRFrame": baseStatsXmitICRFrame,
       "baseStatsNoICRBufferAvail": baseStatsNoICRBufferAvail,
       "baseStatsNotRoutedICRFrame": baseStatsNotRoutedICRFrame,
       "baseStatsNbCUserEst": baseStatsNbCUserEst,
       "wrRemote": wrRemote,
       "wrRemoteTable": wrRemoteTable,
       "wrRemoteEntry": wrRemoteEntry,
       "remIfIndex": remIfIndex,
       "remIndex": remIndex,
       "remMacAddress": remMacAddress,
       "remName": remName,
       "remControllerCardDesc": remControllerCardDesc,
       "remUnivAddress": remUnivAddress,
       "remModemDesc": remModemDesc,
       "wrRemoteStatsTable": wrRemoteStatsTable,
       "wrRemStatsEntry": wrRemStatsEntry,
       "remStatsIfIndex": remStatsIfIndex,
       "remStatsIndex": remStatsIndex,
       "remStatsXmit": remStatsXmit,
       "remStatsRxmit": remStatsRxmit,
       "remStatsNegAckRcv": remStatsNegAckRcv,
       "remStatsRcv": remStatsRcv,
       "remStatsLineErrors": remStatsLineErrors,
       "remStatsNegAckXmit": remStatsNegAckXmit}
)
