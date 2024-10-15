# SNMP MIB module (CHIPFDDINET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPFDDINET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:48 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlFDDIStatsModTable_Object = MibTable
olFDDIStatsModTable = _OlFDDIStatsModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    olFDDIStatsModTable.setStatus("mandatory")
_OlFDDIStatsModEntry_Object = MibTableRow
olFDDIStatsModEntry = _OlFDDIStatsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1)
)
olFDDIStatsModEntry.setIndexNames(
    (0, "CHIPFDDINET-MIB", "olFDDIStatsModSlotIndex"),
)
if mibBuilder.loadTexts:
    olFDDIStatsModEntry.setStatus("mandatory")
_OlFDDIStatsModSlotIndex_Type = Integer32
_OlFDDIStatsModSlotIndex_Object = MibTableColumn
olFDDIStatsModSlotIndex = _OlFDDIStatsModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 1),
    _OlFDDIStatsModSlotIndex_Type()
)
olFDDIStatsModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModSlotIndex.setStatus("mandatory")
_OlFDDIStatsModMgtRcvErrs_Type = Counter32
_OlFDDIStatsModMgtRcvErrs_Object = MibTableColumn
olFDDIStatsModMgtRcvErrs = _OlFDDIStatsModMgtRcvErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 2),
    _OlFDDIStatsModMgtRcvErrs_Type()
)
olFDDIStatsModMgtRcvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModMgtRcvErrs.setStatus("mandatory")
_OlFDDIStatsModMgtXmitErrs_Type = Counter32
_OlFDDIStatsModMgtXmitErrs_Object = MibTableColumn
olFDDIStatsModMgtXmitErrs = _OlFDDIStatsModMgtXmitErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 3),
    _OlFDDIStatsModMgtXmitErrs_Type()
)
olFDDIStatsModMgtXmitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModMgtXmitErrs.setStatus("mandatory")
_OlFDDIStatsModBackplaneErrs_Type = Counter32
_OlFDDIStatsModBackplaneErrs_Object = MibTableColumn
olFDDIStatsModBackplaneErrs = _OlFDDIStatsModBackplaneErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 4),
    _OlFDDIStatsModBackplaneErrs_Type()
)
olFDDIStatsModBackplaneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModBackplaneErrs.setStatus("mandatory")
_OlFDDIStatsModPllUnlockErrs_Type = Counter32
_OlFDDIStatsModPllUnlockErrs_Object = MibTableColumn
olFDDIStatsModPllUnlockErrs = _OlFDDIStatsModPllUnlockErrs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 2, 1, 5),
    _OlFDDIStatsModPllUnlockErrs_Type()
)
olFDDIStatsModPllUnlockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsModPllUnlockErrs.setStatus("mandatory")
_OlFDDIStatsPortTable_Object = MibTable
olFDDIStatsPortTable = _OlFDDIStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    olFDDIStatsPortTable.setStatus("mandatory")
_OlFDDIStatsPortEntry_Object = MibTableRow
olFDDIStatsPortEntry = _OlFDDIStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1)
)
olFDDIStatsPortEntry.setIndexNames(
    (0, "CHIPFDDINET-MIB", "olFDDIStatsPortSlotIndex"),
    (0, "CHIPFDDINET-MIB", "olFDDIStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olFDDIStatsPortEntry.setStatus("mandatory")
_OlFDDIStatsPortSlotIndex_Type = Integer32
_OlFDDIStatsPortSlotIndex_Object = MibTableColumn
olFDDIStatsPortSlotIndex = _OlFDDIStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 1),
    _OlFDDIStatsPortSlotIndex_Type()
)
olFDDIStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortSlotIndex.setStatus("mandatory")
_OlFDDIStatsPortIndex_Type = Integer32
_OlFDDIStatsPortIndex_Object = MibTableColumn
olFDDIStatsPortIndex = _OlFDDIStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 2),
    _OlFDDIStatsPortIndex_Type()
)
olFDDIStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortIndex.setStatus("mandatory")
_OlFDDIStatsPortLCTFailCts_Type = Counter32
_OlFDDIStatsPortLCTFailCts_Object = MibTableColumn
olFDDIStatsPortLCTFailCts = _OlFDDIStatsPortLCTFailCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 3),
    _OlFDDIStatsPortLCTFailCts_Type()
)
olFDDIStatsPortLCTFailCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLCTFailCts.setStatus("mandatory")
_OlFDDIStatsPortLerEstimate_Type = Gauge32
_OlFDDIStatsPortLerEstimate_Object = MibTableColumn
olFDDIStatsPortLerEstimate = _OlFDDIStatsPortLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 4),
    _OlFDDIStatsPortLerEstimate_Type()
)
olFDDIStatsPortLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLerEstimate.setStatus("mandatory")
_OlFDDIStatsPortLemRejectCts_Type = Counter32
_OlFDDIStatsPortLemRejectCts_Object = MibTableColumn
olFDDIStatsPortLemRejectCts = _OlFDDIStatsPortLemRejectCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 5),
    _OlFDDIStatsPortLemRejectCts_Type()
)
olFDDIStatsPortLemRejectCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLemRejectCts.setStatus("mandatory")
_OlFDDIStatsPortLemCts_Type = Counter32
_OlFDDIStatsPortLemCts_Object = MibTableColumn
olFDDIStatsPortLemCts = _OlFDDIStatsPortLemCts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 3, 1, 6),
    _OlFDDIStatsPortLemCts_Type()
)
olFDDIStatsPortLemCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDIStatsPortLemCts.setStatus("mandatory")
_OlFDDInetStatsTable_Object = MibTable
olFDDInetStatsTable = _OlFDDInetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4)
)
if mibBuilder.loadTexts:
    olFDDInetStatsTable.setStatus("mandatory")
_OlFDDInetStatsEntry_Object = MibTableRow
olFDDInetStatsEntry = _OlFDDInetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1)
)
olFDDInetStatsEntry.setIndexNames(
    (0, "CHIPFDDINET-MIB", "olFDDInetStatsNetID"),
)
if mibBuilder.loadTexts:
    olFDDInetStatsEntry.setStatus("mandatory")


class _OlFDDInetStatsNetID_Type(Integer32):
    """Custom type olFDDInetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("isolated", 2))
    )


_OlFDDInetStatsNetID_Type.__name__ = "Integer32"
_OlFDDInetStatsNetID_Object = MibTableColumn
olFDDInetStatsNetID = _OlFDDInetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 1),
    _OlFDDInetStatsNetID_Type()
)
olFDDInetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsNetID.setStatus("mandatory")
_OlFDDInetStatsRingOpCounts_Type = Counter32
_OlFDDInetStatsRingOpCounts_Object = MibTableColumn
olFDDInetStatsRingOpCounts = _OlFDDInetStatsRingOpCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 2),
    _OlFDDInetStatsRingOpCounts_Type()
)
olFDDInetStatsRingOpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsRingOpCounts.setStatus("mandatory")
_OlFDDInetStatsFrameCounts_Type = Counter32
_OlFDDInetStatsFrameCounts_Object = MibTableColumn
olFDDInetStatsFrameCounts = _OlFDDInetStatsFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 3),
    _OlFDDInetStatsFrameCounts_Type()
)
olFDDInetStatsFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsFrameCounts.setStatus("mandatory")
_OlFDDInetStatsErrorCounts_Type = Counter32
_OlFDDInetStatsErrorCounts_Object = MibTableColumn
olFDDInetStatsErrorCounts = _OlFDDInetStatsErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 4),
    _OlFDDInetStatsErrorCounts_Type()
)
olFDDInetStatsErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsErrorCounts.setStatus("mandatory")
_OlFDDInetStatsLostCounts_Type = Counter32
_OlFDDInetStatsLostCounts_Object = MibTableColumn
olFDDInetStatsLostCounts = _OlFDDInetStatsLostCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 5),
    _OlFDDInetStatsLostCounts_Type()
)
olFDDInetStatsLostCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsLostCounts.setStatus("mandatory")


class _OlFDDInetStatsFrameErrorRatio_Type(Integer32):
    """Custom type olFDDInetStatsFrameErrorRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OlFDDInetStatsFrameErrorRatio_Type.__name__ = "Integer32"
_OlFDDInetStatsFrameErrorRatio_Object = MibTableColumn
olFDDInetStatsFrameErrorRatio = _OlFDDInetStatsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4, 4, 1, 6),
    _OlFDDInetStatsFrameErrorRatio_Type()
)
olFDDInetStatsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olFDDInetStatsFrameErrorRatio.setStatus("mandatory")
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPFDDINET-MIB",
    **{"chipcom": chipcom,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipEcho": chipEcho,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olConc": olConc,
       "olEnv": olEnv,
       "olModules": olModules,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnRES": ol51nnRES,
       "ol51nnREE": ol51nnREE,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol5208MTP": ol5208MTP,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMFR": ol52nnMFR,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMFL": ol51nnMFL,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol51nnMFB": ol51nnMFB,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMSTP": ol53nnMSTP,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol52nnBTT": ol52nnBTT,
       "ol51nnIx": ol51nnIx,
       "ol52nnMMGT": ol52nnMMGT,
       "ol50nnMHCTL": ol50nnMHCTL,
       "olNets": olNets,
       "olNet": olNet,
       "olEnet": olEnet,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
       "olFDDIStatsModTable": olFDDIStatsModTable,
       "olFDDIStatsModEntry": olFDDIStatsModEntry,
       "olFDDIStatsModSlotIndex": olFDDIStatsModSlotIndex,
       "olFDDIStatsModMgtRcvErrs": olFDDIStatsModMgtRcvErrs,
       "olFDDIStatsModMgtXmitErrs": olFDDIStatsModMgtXmitErrs,
       "olFDDIStatsModBackplaneErrs": olFDDIStatsModBackplaneErrs,
       "olFDDIStatsModPllUnlockErrs": olFDDIStatsModPllUnlockErrs,
       "olFDDIStatsPortTable": olFDDIStatsPortTable,
       "olFDDIStatsPortEntry": olFDDIStatsPortEntry,
       "olFDDIStatsPortSlotIndex": olFDDIStatsPortSlotIndex,
       "olFDDIStatsPortIndex": olFDDIStatsPortIndex,
       "olFDDIStatsPortLCTFailCts": olFDDIStatsPortLCTFailCts,
       "olFDDIStatsPortLerEstimate": olFDDIStatsPortLerEstimate,
       "olFDDIStatsPortLemRejectCts": olFDDIStatsPortLemRejectCts,
       "olFDDIStatsPortLemCts": olFDDIStatsPortLemCts,
       "olFDDInetStatsTable": olFDDInetStatsTable,
       "olFDDInetStatsEntry": olFDDInetStatsEntry,
       "olFDDInetStatsNetID": olFDDInetStatsNetID,
       "olFDDInetStatsRingOpCounts": olFDDInetStatsRingOpCounts,
       "olFDDInetStatsFrameCounts": olFDDInetStatsFrameCounts,
       "olFDDInetStatsErrorCounts": olFDDInetStatsErrorCounts,
       "olFDDInetStatsLostCounts": olFDDInetStatsLostCounts,
       "olFDDInetStatsFrameErrorRatio": olFDDInetStatsFrameErrorRatio,
       "olGroups": olGroups,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTFTP": chipTFTP,
       "chipDownload": chipDownload}
)
