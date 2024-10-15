# SNMP MIB module (CHIPENET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPENET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:47 2024
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
_OlEnetStatsTable_Object = MibTable
olEnetStatsTable = _OlEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    olEnetStatsTable.setStatus("mandatory")
_OlEnetStatsEntry_Object = MibTableRow
olEnetStatsEntry = _OlEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1)
)
olEnetStatsEntry.setIndexNames(
    (0, "CHIPENET-MIB", "olEnetStatsNetID"),
)
if mibBuilder.loadTexts:
    olEnetStatsEntry.setStatus("mandatory")


class _OlEnetStatsNetID_Type(Integer32):
    """Custom type olEnetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8))
    )


_OlEnetStatsNetID_Type.__name__ = "Integer32"
_OlEnetStatsNetID_Object = MibTableColumn
olEnetStatsNetID = _OlEnetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 1),
    _OlEnetStatsNetID_Type()
)
olEnetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsNetID.setStatus("mandatory")
_OlEnetStatsFramesRcvdOks_Type = Counter32
_OlEnetStatsFramesRcvdOks_Object = MibTableColumn
olEnetStatsFramesRcvdOks = _OlEnetStatsFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 2),
    _OlEnetStatsFramesRcvdOks_Type()
)
olEnetStatsFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsOctetsRcvdOks_Type = Counter32
_OlEnetStatsOctetsRcvdOks_Object = MibTableColumn
olEnetStatsOctetsRcvdOks = _OlEnetStatsOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 3),
    _OlEnetStatsOctetsRcvdOks_Type()
)
olEnetStatsOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsMcastRcvdOks_Type = Counter32
_OlEnetStatsMcastRcvdOks_Object = MibTableColumn
olEnetStatsMcastRcvdOks = _OlEnetStatsMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 4),
    _OlEnetStatsMcastRcvdOks_Type()
)
olEnetStatsMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsBcastRcvdOks_Type = Counter32
_OlEnetStatsBcastRcvdOks_Object = MibTableColumn
olEnetStatsBcastRcvdOks = _OlEnetStatsBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 5),
    _OlEnetStatsBcastRcvdOks_Type()
)
olEnetStatsBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsFrameTooLongs_Type = Counter32
_OlEnetStatsFrameTooLongs_Object = MibTableColumn
olEnetStatsFrameTooLongs = _OlEnetStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 6),
    _OlEnetStatsFrameTooLongs_Type()
)
olEnetStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFrameTooLongs.setStatus("mandatory")
_OlEnetStatsAlignmentErrors_Type = Counter32
_OlEnetStatsAlignmentErrors_Object = MibTableColumn
olEnetStatsAlignmentErrors = _OlEnetStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 7),
    _OlEnetStatsAlignmentErrors_Type()
)
olEnetStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsAlignmentErrors.setStatus("mandatory")
_OlEnetStatsFCSErrors_Type = Counter32
_OlEnetStatsFCSErrors_Object = MibTableColumn
olEnetStatsFCSErrors = _OlEnetStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 8),
    _OlEnetStatsFCSErrors_Type()
)
olEnetStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsFCSErrors.setStatus("mandatory")
_OlEnetStatsRunts_Type = Counter32
_OlEnetStatsRunts_Object = MibTableColumn
olEnetStatsRunts = _OlEnetStatsRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 9),
    _OlEnetStatsRunts_Type()
)
olEnetStatsRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsRunts.setStatus("mandatory")
_OlEnetStatsLocalColls_Type = Counter32
_OlEnetStatsLocalColls_Object = MibTableColumn
olEnetStatsLocalColls = _OlEnetStatsLocalColls_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 10),
    _OlEnetStatsLocalColls_Type()
)
olEnetStatsLocalColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsLocalColls.setStatus("mandatory")
_OlEnetStatsModTable_Object = MibTable
olEnetStatsModTable = _OlEnetStatsModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    olEnetStatsModTable.setStatus("mandatory")
_OlEnetStatsModEntry_Object = MibTableRow
olEnetStatsModEntry = _OlEnetStatsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1)
)
olEnetStatsModEntry.setIndexNames(
    (0, "CHIPENET-MIB", "olEnetStatsModNetID"),
    (0, "CHIPENET-MIB", "olEnetStatsModSlotIndex"),
)
if mibBuilder.loadTexts:
    olEnetStatsModEntry.setStatus("mandatory")


class _OlEnetStatsModNetID_Type(Integer32):
    """Custom type olEnetStatsModNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8))
    )


_OlEnetStatsModNetID_Type.__name__ = "Integer32"
_OlEnetStatsModNetID_Object = MibTableColumn
olEnetStatsModNetID = _OlEnetStatsModNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 1),
    _OlEnetStatsModNetID_Type()
)
olEnetStatsModNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModNetID.setStatus("mandatory")
_OlEnetStatsModSlotIndex_Type = Integer32
_OlEnetStatsModSlotIndex_Object = MibTableColumn
olEnetStatsModSlotIndex = _OlEnetStatsModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 2),
    _OlEnetStatsModSlotIndex_Type()
)
olEnetStatsModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModSlotIndex.setStatus("mandatory")
_OlEnetStatsModFramesRcvdOks_Type = Counter32
_OlEnetStatsModFramesRcvdOks_Object = MibTableColumn
olEnetStatsModFramesRcvdOks = _OlEnetStatsModFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 3),
    _OlEnetStatsModFramesRcvdOks_Type()
)
olEnetStatsModFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsModOctetsRcvdOks_Type = Counter32
_OlEnetStatsModOctetsRcvdOks_Object = MibTableColumn
olEnetStatsModOctetsRcvdOks = _OlEnetStatsModOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 4),
    _OlEnetStatsModOctetsRcvdOks_Type()
)
olEnetStatsModOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsModMcastRcvdOks_Type = Counter32
_OlEnetStatsModMcastRcvdOks_Object = MibTableColumn
olEnetStatsModMcastRcvdOks = _OlEnetStatsModMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 5),
    _OlEnetStatsModMcastRcvdOks_Type()
)
olEnetStatsModMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsModBcastRcvdOks_Type = Counter32
_OlEnetStatsModBcastRcvdOks_Object = MibTableColumn
olEnetStatsModBcastRcvdOks = _OlEnetStatsModBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 6),
    _OlEnetStatsModBcastRcvdOks_Type()
)
olEnetStatsModBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsModFrameTooLongs_Type = Counter32
_OlEnetStatsModFrameTooLongs_Object = MibTableColumn
olEnetStatsModFrameTooLongs = _OlEnetStatsModFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 7),
    _OlEnetStatsModFrameTooLongs_Type()
)
olEnetStatsModFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFrameTooLongs.setStatus("mandatory")
_OlEnetStatsModAlignmentErrors_Type = Counter32
_OlEnetStatsModAlignmentErrors_Object = MibTableColumn
olEnetStatsModAlignmentErrors = _OlEnetStatsModAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 8),
    _OlEnetStatsModAlignmentErrors_Type()
)
olEnetStatsModAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModAlignmentErrors.setStatus("mandatory")
_OlEnetStatsModFCSErrors_Type = Counter32
_OlEnetStatsModFCSErrors_Object = MibTableColumn
olEnetStatsModFCSErrors = _OlEnetStatsModFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 9),
    _OlEnetStatsModFCSErrors_Type()
)
olEnetStatsModFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModFCSErrors.setStatus("mandatory")
_OlEnetStatsModRunts_Type = Counter32
_OlEnetStatsModRunts_Object = MibTableColumn
olEnetStatsModRunts = _OlEnetStatsModRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 10),
    _OlEnetStatsModRunts_Type()
)
olEnetStatsModRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsModRunts.setStatus("mandatory")
_OlEnetStatsPortTable_Object = MibTable
olEnetStatsPortTable = _OlEnetStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    olEnetStatsPortTable.setStatus("mandatory")
_OlEnetStatsPortEntry_Object = MibTableRow
olEnetStatsPortEntry = _OlEnetStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1)
)
olEnetStatsPortEntry.setIndexNames(
    (0, "CHIPENET-MIB", "olEnetStatsPortSlotIndex"),
    (0, "CHIPENET-MIB", "olEnetStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olEnetStatsPortEntry.setStatus("mandatory")


class _OlEnetStatsPortNetID_Type(Integer32):
    """Custom type olEnetStatsPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8))
    )


_OlEnetStatsPortNetID_Type.__name__ = "Integer32"
_OlEnetStatsPortNetID_Object = MibTableColumn
olEnetStatsPortNetID = _OlEnetStatsPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 1),
    _OlEnetStatsPortNetID_Type()
)
olEnetStatsPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortNetID.setStatus("mandatory")
_OlEnetStatsPortSlotIndex_Type = Integer32
_OlEnetStatsPortSlotIndex_Object = MibTableColumn
olEnetStatsPortSlotIndex = _OlEnetStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 2),
    _OlEnetStatsPortSlotIndex_Type()
)
olEnetStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortSlotIndex.setStatus("mandatory")
_OlEnetStatsPortIndex_Type = Integer32
_OlEnetStatsPortIndex_Object = MibTableColumn
olEnetStatsPortIndex = _OlEnetStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 3),
    _OlEnetStatsPortIndex_Type()
)
olEnetStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortIndex.setStatus("mandatory")
_OlEnetStatsPortFramesRcvdOks_Type = Counter32
_OlEnetStatsPortFramesRcvdOks_Object = MibTableColumn
olEnetStatsPortFramesRcvdOks = _OlEnetStatsPortFramesRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 4),
    _OlEnetStatsPortFramesRcvdOks_Type()
)
olEnetStatsPortFramesRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFramesRcvdOks.setStatus("mandatory")
_OlEnetStatsPortOctetsRcvdOks_Type = Counter32
_OlEnetStatsPortOctetsRcvdOks_Object = MibTableColumn
olEnetStatsPortOctetsRcvdOks = _OlEnetStatsPortOctetsRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 5),
    _OlEnetStatsPortOctetsRcvdOks_Type()
)
olEnetStatsPortOctetsRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortOctetsRcvdOks.setStatus("mandatory")
_OlEnetStatsPortMcastRcvdOks_Type = Counter32
_OlEnetStatsPortMcastRcvdOks_Object = MibTableColumn
olEnetStatsPortMcastRcvdOks = _OlEnetStatsPortMcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 6),
    _OlEnetStatsPortMcastRcvdOks_Type()
)
olEnetStatsPortMcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortMcastRcvdOks.setStatus("mandatory")
_OlEnetStatsPortBcastRcvdOks_Type = Counter32
_OlEnetStatsPortBcastRcvdOks_Object = MibTableColumn
olEnetStatsPortBcastRcvdOks = _OlEnetStatsPortBcastRcvdOks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 7),
    _OlEnetStatsPortBcastRcvdOks_Type()
)
olEnetStatsPortBcastRcvdOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortBcastRcvdOks.setStatus("mandatory")
_OlEnetStatsPortFrameTooLongs_Type = Counter32
_OlEnetStatsPortFrameTooLongs_Object = MibTableColumn
olEnetStatsPortFrameTooLongs = _OlEnetStatsPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 8),
    _OlEnetStatsPortFrameTooLongs_Type()
)
olEnetStatsPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFrameTooLongs.setStatus("mandatory")
_OlEnetStatsPortAlignmentErrors_Type = Counter32
_OlEnetStatsPortAlignmentErrors_Object = MibTableColumn
olEnetStatsPortAlignmentErrors = _OlEnetStatsPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 9),
    _OlEnetStatsPortAlignmentErrors_Type()
)
olEnetStatsPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortAlignmentErrors.setStatus("mandatory")
_OlEnetStatsPortFCSErrors_Type = Counter32
_OlEnetStatsPortFCSErrors_Object = MibTableColumn
olEnetStatsPortFCSErrors = _OlEnetStatsPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 10),
    _OlEnetStatsPortFCSErrors_Type()
)
olEnetStatsPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortFCSErrors.setStatus("mandatory")
_OlEnetStatsPortRunts_Type = Counter32
_OlEnetStatsPortRunts_Object = MibTableColumn
olEnetStatsPortRunts = _OlEnetStatsPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 11),
    _OlEnetStatsPortRunts_Type()
)
olEnetStatsPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortRunts.setStatus("mandatory")
_OlEnetStatsPortSrcAddrChanges_Type = Counter32
_OlEnetStatsPortSrcAddrChanges_Object = MibTableColumn
olEnetStatsPortSrcAddrChanges = _OlEnetStatsPortSrcAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 12),
    _OlEnetStatsPortSrcAddrChanges_Type()
)
olEnetStatsPortSrcAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortSrcAddrChanges.setStatus("mandatory")


class _OlEnetStatsPortLastSrcAddr_Type(OctetString):
    """Custom type olEnetStatsPortLastSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetStatsPortLastSrcAddr_Type.__name__ = "OctetString"
_OlEnetStatsPortLastSrcAddr_Object = MibTableColumn
olEnetStatsPortLastSrcAddr = _OlEnetStatsPortLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 13),
    _OlEnetStatsPortLastSrcAddr_Type()
)
olEnetStatsPortLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortLastSrcAddr.setStatus("mandatory")


class _OlEnetStatsPortLastErrAddr_Type(OctetString):
    """Custom type olEnetStatsPortLastErrAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetStatsPortLastErrAddr_Type.__name__ = "OctetString"
_OlEnetStatsPortLastErrAddr_Object = MibTableColumn
olEnetStatsPortLastErrAddr = _OlEnetStatsPortLastErrAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 14),
    _OlEnetStatsPortLastErrAddr_Type()
)
olEnetStatsPortLastErrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetStatsPortLastErrAddr.setStatus("mandatory")
_OlEnetMapTable_Object = MibTable
olEnetMapTable = _OlEnetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    olEnetMapTable.setStatus("mandatory")
_OlEnetMapEntry_Object = MibTableRow
olEnetMapEntry = _OlEnetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1)
)
olEnetMapEntry.setIndexNames(
    (0, "CHIPENET-MIB", "olEnetMapNetID"),
    (0, "CHIPENET-MIB", "olEnetMapAddress"),
)
if mibBuilder.loadTexts:
    olEnetMapEntry.setStatus("mandatory")


class _OlEnetMapNetID_Type(Integer32):
    """Custom type olEnetMapNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8))
    )


_OlEnetMapNetID_Type.__name__ = "Integer32"
_OlEnetMapNetID_Object = MibTableColumn
olEnetMapNetID = _OlEnetMapNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 1),
    _OlEnetMapNetID_Type()
)
olEnetMapNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapNetID.setStatus("mandatory")


class _OlEnetMapAddress_Type(OctetString):
    """Custom type olEnetMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlEnetMapAddress_Type.__name__ = "OctetString"
_OlEnetMapAddress_Object = MibTableColumn
olEnetMapAddress = _OlEnetMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 2),
    _OlEnetMapAddress_Type()
)
olEnetMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapAddress.setStatus("mandatory")
_OlEnetMapSlotIndex_Type = Integer32
_OlEnetMapSlotIndex_Object = MibTableColumn
olEnetMapSlotIndex = _OlEnetMapSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 3),
    _OlEnetMapSlotIndex_Type()
)
olEnetMapSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapSlotIndex.setStatus("mandatory")
_OlEnetMapPortIndex_Type = Integer32
_OlEnetMapPortIndex_Object = MibTableColumn
olEnetMapPortIndex = _OlEnetMapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 4),
    _OlEnetMapPortIndex_Type()
)
olEnetMapPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapPortIndex.setStatus("mandatory")
_OlEnetMapFrames_Type = Counter32
_OlEnetMapFrames_Object = MibTableColumn
olEnetMapFrames = _OlEnetMapFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 5),
    _OlEnetMapFrames_Type()
)
olEnetMapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapFrames.setStatus("mandatory")
_OlEnetMapOctets_Type = Counter32
_OlEnetMapOctets_Object = MibTableColumn
olEnetMapOctets = _OlEnetMapOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 6),
    _OlEnetMapOctets_Type()
)
olEnetMapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapOctets.setStatus("mandatory")
_OlEnetMapTime_Type = TimeTicks
_OlEnetMapTime_Object = MibTableColumn
olEnetMapTime = _OlEnetMapTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 7),
    _OlEnetMapTime_Type()
)
olEnetMapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnetMapTime.setStatus("mandatory")
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
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
    "CHIPENET-MIB",
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
       "olEnetStatsTable": olEnetStatsTable,
       "olEnetStatsEntry": olEnetStatsEntry,
       "olEnetStatsNetID": olEnetStatsNetID,
       "olEnetStatsFramesRcvdOks": olEnetStatsFramesRcvdOks,
       "olEnetStatsOctetsRcvdOks": olEnetStatsOctetsRcvdOks,
       "olEnetStatsMcastRcvdOks": olEnetStatsMcastRcvdOks,
       "olEnetStatsBcastRcvdOks": olEnetStatsBcastRcvdOks,
       "olEnetStatsFrameTooLongs": olEnetStatsFrameTooLongs,
       "olEnetStatsAlignmentErrors": olEnetStatsAlignmentErrors,
       "olEnetStatsFCSErrors": olEnetStatsFCSErrors,
       "olEnetStatsRunts": olEnetStatsRunts,
       "olEnetStatsLocalColls": olEnetStatsLocalColls,
       "olEnetStatsModTable": olEnetStatsModTable,
       "olEnetStatsModEntry": olEnetStatsModEntry,
       "olEnetStatsModNetID": olEnetStatsModNetID,
       "olEnetStatsModSlotIndex": olEnetStatsModSlotIndex,
       "olEnetStatsModFramesRcvdOks": olEnetStatsModFramesRcvdOks,
       "olEnetStatsModOctetsRcvdOks": olEnetStatsModOctetsRcvdOks,
       "olEnetStatsModMcastRcvdOks": olEnetStatsModMcastRcvdOks,
       "olEnetStatsModBcastRcvdOks": olEnetStatsModBcastRcvdOks,
       "olEnetStatsModFrameTooLongs": olEnetStatsModFrameTooLongs,
       "olEnetStatsModAlignmentErrors": olEnetStatsModAlignmentErrors,
       "olEnetStatsModFCSErrors": olEnetStatsModFCSErrors,
       "olEnetStatsModRunts": olEnetStatsModRunts,
       "olEnetStatsPortTable": olEnetStatsPortTable,
       "olEnetStatsPortEntry": olEnetStatsPortEntry,
       "olEnetStatsPortNetID": olEnetStatsPortNetID,
       "olEnetStatsPortSlotIndex": olEnetStatsPortSlotIndex,
       "olEnetStatsPortIndex": olEnetStatsPortIndex,
       "olEnetStatsPortFramesRcvdOks": olEnetStatsPortFramesRcvdOks,
       "olEnetStatsPortOctetsRcvdOks": olEnetStatsPortOctetsRcvdOks,
       "olEnetStatsPortMcastRcvdOks": olEnetStatsPortMcastRcvdOks,
       "olEnetStatsPortBcastRcvdOks": olEnetStatsPortBcastRcvdOks,
       "olEnetStatsPortFrameTooLongs": olEnetStatsPortFrameTooLongs,
       "olEnetStatsPortAlignmentErrors": olEnetStatsPortAlignmentErrors,
       "olEnetStatsPortFCSErrors": olEnetStatsPortFCSErrors,
       "olEnetStatsPortRunts": olEnetStatsPortRunts,
       "olEnetStatsPortSrcAddrChanges": olEnetStatsPortSrcAddrChanges,
       "olEnetStatsPortLastSrcAddr": olEnetStatsPortLastSrcAddr,
       "olEnetStatsPortLastErrAddr": olEnetStatsPortLastErrAddr,
       "olEnetMapTable": olEnetMapTable,
       "olEnetMapEntry": olEnetMapEntry,
       "olEnetMapNetID": olEnetMapNetID,
       "olEnetMapAddress": olEnetMapAddress,
       "olEnetMapSlotIndex": olEnetMapSlotIndex,
       "olEnetMapPortIndex": olEnetMapPortIndex,
       "olEnetMapFrames": olEnetMapFrames,
       "olEnetMapOctets": olEnetMapOctets,
       "olEnetMapTime": olEnetMapTime,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
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
