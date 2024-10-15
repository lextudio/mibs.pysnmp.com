# SNMP MIB module (CHIPTRNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPTRNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:50 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




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


class _OlTRnetMapState_Type(Integer32):
    """Custom type olTRnetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRnetMapState_Type.__name__ = "Integer32"
_OlTRnetMapState_Object = MibScalar
olTRnetMapState = _OlTRnetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 1),
    _OlTRnetMapState_Type()
)
olTRnetMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapState.setStatus("mandatory")
_OlTRnetStatsTable_Object = MibTable
olTRnetStatsTable = _OlTRnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    olTRnetStatsTable.setStatus("mandatory")
_OlTRnetStatsEntry_Object = MibTableRow
olTRnetStatsEntry = _OlTRnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1)
)
olTRnetStatsEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRnetStatsNetID"),
)
if mibBuilder.loadTexts:
    olTRnetStatsEntry.setStatus("mandatory")


class _OlTRnetStatsNetID_Type(Integer32):
    """Custom type olTRnetStatsNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsNetID_Type.__name__ = "Integer32"
_OlTRnetStatsNetID_Object = MibTableColumn
olTRnetStatsNetID = _OlTRnetStatsNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 1),
    _OlTRnetStatsNetID_Type()
)
olTRnetStatsNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsNetID.setStatus("mandatory")
_OlTRnetStatsLineErrors_Type = Counter32
_OlTRnetStatsLineErrors_Object = MibTableColumn
olTRnetStatsLineErrors = _OlTRnetStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 2),
    _OlTRnetStatsLineErrors_Type()
)
olTRnetStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLineErrors.setStatus("mandatory")
_OlTRnetStatsBurstErrors_Type = Counter32
_OlTRnetStatsBurstErrors_Object = MibTableColumn
olTRnetStatsBurstErrors = _OlTRnetStatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 3),
    _OlTRnetStatsBurstErrors_Type()
)
olTRnetStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsBurstErrors.setStatus("mandatory")
_OlTRnetStatsACErrors_Type = Counter32
_OlTRnetStatsACErrors_Object = MibTableColumn
olTRnetStatsACErrors = _OlTRnetStatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 4),
    _OlTRnetStatsACErrors_Type()
)
olTRnetStatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsACErrors.setStatus("mandatory")
_OlTRnetStatsLostFrameErrors_Type = Counter32
_OlTRnetStatsLostFrameErrors_Object = MibTableColumn
olTRnetStatsLostFrameErrors = _OlTRnetStatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 5),
    _OlTRnetStatsLostFrameErrors_Type()
)
olTRnetStatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsCongestionErrors_Type = Counter32
_OlTRnetStatsCongestionErrors_Object = MibTableColumn
olTRnetStatsCongestionErrors = _OlTRnetStatsCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 6),
    _OlTRnetStatsCongestionErrors_Type()
)
olTRnetStatsCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsCongestionErrors.setStatus("mandatory")
_OlTRnetStatsFrameCopiedErrors_Type = Counter32
_OlTRnetStatsFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsFrameCopiedErrors = _OlTRnetStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 7),
    _OlTRnetStatsFrameCopiedErrors_Type()
)
olTRnetStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsTokenErrors_Type = Counter32
_OlTRnetStatsTokenErrors_Object = MibTableColumn
olTRnetStatsTokenErrors = _OlTRnetStatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 8),
    _OlTRnetStatsTokenErrors_Type()
)
olTRnetStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTokenErrors.setStatus("mandatory")
_OlTRnetStatsDuplicateAddresses_Type = Counter32
_OlTRnetStatsDuplicateAddresses_Object = MibTableColumn
olTRnetStatsDuplicateAddresses = _OlTRnetStatsDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 9),
    _OlTRnetStatsDuplicateAddresses_Type()
)
olTRnetStatsDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsDuplicateAddresses.setStatus("mandatory")
_OlTRnetStatsBeaconEvents_Type = Counter32
_OlTRnetStatsBeaconEvents_Object = MibTableColumn
olTRnetStatsBeaconEvents = _OlTRnetStatsBeaconEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 10),
    _OlTRnetStatsBeaconEvents_Type()
)
olTRnetStatsBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsBeaconEvents.setStatus("mandatory")


class _OlTRnetStatsLastBeaconSender_Type(OctetString):
    """Custom type olTRnetStatsLastBeaconSender based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsLastBeaconSender_Type.__name__ = "OctetString"
_OlTRnetStatsLastBeaconSender_Object = MibTableColumn
olTRnetStatsLastBeaconSender = _OlTRnetStatsLastBeaconSender_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 11),
    _OlTRnetStatsLastBeaconSender_Type()
)
olTRnetStatsLastBeaconSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconSender.setStatus("mandatory")


class _OlTRnetStatsLastBeaconNAUN_Type(OctetString):
    """Custom type olTRnetStatsLastBeaconNAUN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsLastBeaconNAUN_Type.__name__ = "OctetString"
_OlTRnetStatsLastBeaconNAUN_Object = MibTableColumn
olTRnetStatsLastBeaconNAUN = _OlTRnetStatsLastBeaconNAUN_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 12),
    _OlTRnetStatsLastBeaconNAUN_Type()
)
olTRnetStatsLastBeaconNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconNAUN.setStatus("mandatory")
_OlTRnetStatsLastBeaconTime_Type = TimeTicks
_OlTRnetStatsLastBeaconTime_Object = MibTableColumn
olTRnetStatsLastBeaconTime = _OlTRnetStatsLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 13),
    _OlTRnetStatsLastBeaconTime_Type()
)
olTRnetStatsLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconTime.setStatus("mandatory")


class _OlTRnetStatsLastBeaconAction_Type(Integer32):
    """Custom type olTRnetStatsLastBeaconAction based on Integer32"""
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
        *(("moduleIsolate", 4),
          ("noAction", 1),
          ("portDisable", 2),
          ("trunkDisable", 3))
    )


_OlTRnetStatsLastBeaconAction_Type.__name__ = "Integer32"
_OlTRnetStatsLastBeaconAction_Object = MibTableColumn
olTRnetStatsLastBeaconAction = _OlTRnetStatsLastBeaconAction_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 14),
    _OlTRnetStatsLastBeaconAction_Type()
)
olTRnetStatsLastBeaconAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsLastBeaconAction.setStatus("mandatory")


class _OlTRnetStatsTotalStations_Type(Integer32):
    """Custom type olTRnetStatsTotalStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlTRnetStatsTotalStations_Type.__name__ = "Integer32"
_OlTRnetStatsTotalStations_Object = MibTableColumn
olTRnetStatsTotalStations = _OlTRnetStatsTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 15),
    _OlTRnetStatsTotalStations_Type()
)
olTRnetStatsTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTotalStations.setStatus("mandatory")


class _OlTRnetStatsConcStations_Type(Integer32):
    """Custom type olTRnetStatsConcStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlTRnetStatsConcStations_Type.__name__ = "Integer32"
_OlTRnetStatsConcStations_Object = MibTableColumn
olTRnetStatsConcStations = _OlTRnetStatsConcStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 16),
    _OlTRnetStatsConcStations_Type()
)
olTRnetStatsConcStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsConcStations.setStatus("mandatory")
_OlTRnetStatsTotalPorts_Type = Integer32
_OlTRnetStatsTotalPorts_Object = MibTableColumn
olTRnetStatsTotalPorts = _OlTRnetStatsTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 17),
    _OlTRnetStatsTotalPorts_Type()
)
olTRnetStatsTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsTotalPorts.setStatus("mandatory")
_OlTRnetStatsEnabledPorts_Type = Integer32
_OlTRnetStatsEnabledPorts_Object = MibTableColumn
olTRnetStatsEnabledPorts = _OlTRnetStatsEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 18),
    _OlTRnetStatsEnabledPorts_Type()
)
olTRnetStatsEnabledPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsEnabledPorts.setStatus("mandatory")
_OlTRnetStatsActivePorts_Type = Integer32
_OlTRnetStatsActivePorts_Object = MibTableColumn
olTRnetStatsActivePorts = _OlTRnetStatsActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 2, 1, 19),
    _OlTRnetStatsActivePorts_Type()
)
olTRnetStatsActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsActivePorts.setStatus("mandatory")
_OlTRnetStatsStationTable_Object = MibTable
olTRnetStatsStationTable = _OlTRnetStatsStationTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    olTRnetStatsStationTable.setStatus("mandatory")
_OlTRnetStatsStationEntry_Object = MibTableRow
olTRnetStatsStationEntry = _OlTRnetStatsStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1)
)
olTRnetStatsStationEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRnetStatsStationNetID"),
    (0, "CHIPTRNET-MIB", "olTRnetStatsStationAddr"),
)
if mibBuilder.loadTexts:
    olTRnetStatsStationEntry.setStatus("mandatory")


class _OlTRnetStatsStationNetID_Type(Integer32):
    """Custom type olTRnetStatsStationNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsStationNetID_Type.__name__ = "Integer32"
_OlTRnetStatsStationNetID_Object = MibTableColumn
olTRnetStatsStationNetID = _OlTRnetStatsStationNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 1),
    _OlTRnetStatsStationNetID_Type()
)
olTRnetStatsStationNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationNetID.setStatus("mandatory")


class _OlTRnetStatsStationAddr_Type(OctetString):
    """Custom type olTRnetStatsStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsStationAddr_Type.__name__ = "OctetString"
_OlTRnetStatsStationAddr_Object = MibTableColumn
olTRnetStatsStationAddr = _OlTRnetStatsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 2),
    _OlTRnetStatsStationAddr_Type()
)
olTRnetStatsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationAddr.setStatus("mandatory")


class _OlTRnetStatsStationSlotIndex_Type(Integer32):
    """Custom type olTRnetStatsStationSlotIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRnetStatsStationSlotIndex_Type.__name__ = "Integer32"
_OlTRnetStatsStationSlotIndex_Object = MibTableColumn
olTRnetStatsStationSlotIndex = _OlTRnetStatsStationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 3),
    _OlTRnetStatsStationSlotIndex_Type()
)
olTRnetStatsStationSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationSlotIndex.setStatus("mandatory")
_OlTRnetStatsStationPortIndex_Type = Integer32
_OlTRnetStatsStationPortIndex_Object = MibTableColumn
olTRnetStatsStationPortIndex = _OlTRnetStatsStationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 4),
    _OlTRnetStatsStationPortIndex_Type()
)
olTRnetStatsStationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationPortIndex.setStatus("mandatory")


class _OlTRnetStatsStationNAUNAddress_Type(OctetString):
    """Custom type olTRnetStatsStationNAUNAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsStationNAUNAddress_Type.__name__ = "OctetString"
_OlTRnetStatsStationNAUNAddress_Object = MibTableColumn
olTRnetStatsStationNAUNAddress = _OlTRnetStatsStationNAUNAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 5),
    _OlTRnetStatsStationNAUNAddress_Type()
)
olTRnetStatsStationNAUNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationNAUNAddress.setStatus("mandatory")
_OlTRnetStatsStationLineErrors_Type = Counter32
_OlTRnetStatsStationLineErrors_Object = MibTableColumn
olTRnetStatsStationLineErrors = _OlTRnetStatsStationLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 6),
    _OlTRnetStatsStationLineErrors_Type()
)
olTRnetStatsStationLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationLineErrors.setStatus("mandatory")
_OlTRnetStatsStationBurstErrors_Type = Counter32
_OlTRnetStatsStationBurstErrors_Object = MibTableColumn
olTRnetStatsStationBurstErrors = _OlTRnetStatsStationBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 7),
    _OlTRnetStatsStationBurstErrors_Type()
)
olTRnetStatsStationBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationBurstErrors.setStatus("mandatory")
_OlTRnetStatsStationACErrors_Type = Counter32
_OlTRnetStatsStationACErrors_Object = MibTableColumn
olTRnetStatsStationACErrors = _OlTRnetStatsStationACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 8),
    _OlTRnetStatsStationACErrors_Type()
)
olTRnetStatsStationACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationACErrors.setStatus("mandatory")
_OlTRnetStatsStationLostFrameErrors_Type = Counter32
_OlTRnetStatsStationLostFrameErrors_Object = MibTableColumn
olTRnetStatsStationLostFrameErrors = _OlTRnetStatsStationLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 9),
    _OlTRnetStatsStationLostFrameErrors_Type()
)
olTRnetStatsStationLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsStationCongestionErrors_Type = Counter32
_OlTRnetStatsStationCongestionErrors_Object = MibTableColumn
olTRnetStatsStationCongestionErrors = _OlTRnetStatsStationCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 10),
    _OlTRnetStatsStationCongestionErrors_Type()
)
olTRnetStatsStationCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationCongestionErrors.setStatus("mandatory")
_OlTRnetStatsStationFrameCopiedErrors_Type = Counter32
_OlTRnetStatsStationFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsStationFrameCopiedErrors = _OlTRnetStatsStationFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 11),
    _OlTRnetStatsStationFrameCopiedErrors_Type()
)
olTRnetStatsStationFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsStationTokenErrors_Type = Counter32
_OlTRnetStatsStationTokenErrors_Object = MibTableColumn
olTRnetStatsStationTokenErrors = _OlTRnetStatsStationTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 12),
    _OlTRnetStatsStationTokenErrors_Type()
)
olTRnetStatsStationTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationTokenErrors.setStatus("mandatory")
_OlTRnetStatsStationDuplicateAddresses_Type = Counter32
_OlTRnetStatsStationDuplicateAddresses_Object = MibTableColumn
olTRnetStatsStationDuplicateAddresses = _OlTRnetStatsStationDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 3, 1, 13),
    _OlTRnetStatsStationDuplicateAddresses_Type()
)
olTRnetStatsStationDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsStationDuplicateAddresses.setStatus("mandatory")
_OlTRnetStatsPortTable_Object = MibTable
olTRnetStatsPortTable = _OlTRnetStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    olTRnetStatsPortTable.setStatus("mandatory")
_OlTRnetStatsPortEntry_Object = MibTableRow
olTRnetStatsPortEntry = _OlTRnetStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1)
)
olTRnetStatsPortEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRnetStatsPortSlotIndex"),
    (0, "CHIPTRNET-MIB", "olTRnetStatsPortIndex"),
)
if mibBuilder.loadTexts:
    olTRnetStatsPortEntry.setStatus("mandatory")
_OlTRnetStatsPortSlotIndex_Type = Integer32
_OlTRnetStatsPortSlotIndex_Object = MibTableColumn
olTRnetStatsPortSlotIndex = _OlTRnetStatsPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 1),
    _OlTRnetStatsPortSlotIndex_Type()
)
olTRnetStatsPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortSlotIndex.setStatus("mandatory")
_OlTRnetStatsPortIndex_Type = Integer32
_OlTRnetStatsPortIndex_Object = MibTableColumn
olTRnetStatsPortIndex = _OlTRnetStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 2),
    _OlTRnetStatsPortIndex_Type()
)
olTRnetStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortIndex.setStatus("mandatory")


class _OlTRnetStatsPortNetID_Type(Integer32):
    """Custom type olTRnetStatsPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetStatsPortNetID_Type.__name__ = "Integer32"
_OlTRnetStatsPortNetID_Object = MibTableColumn
olTRnetStatsPortNetID = _OlTRnetStatsPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 3),
    _OlTRnetStatsPortNetID_Type()
)
olTRnetStatsPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortNetID.setStatus("mandatory")
_OlTRnetStatsPortTotalStations_Type = Integer32
_OlTRnetStatsPortTotalStations_Object = MibTableColumn
olTRnetStatsPortTotalStations = _OlTRnetStatsPortTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 4),
    _OlTRnetStatsPortTotalStations_Type()
)
olTRnetStatsPortTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortTotalStations.setStatus("mandatory")


class _OlTRnetStatsPortAddress_Type(OctetString):
    """Custom type olTRnetStatsPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlTRnetStatsPortAddress_Type.__name__ = "OctetString"
_OlTRnetStatsPortAddress_Object = MibTableColumn
olTRnetStatsPortAddress = _OlTRnetStatsPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 5),
    _OlTRnetStatsPortAddress_Type()
)
olTRnetStatsPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortAddress.setStatus("mandatory")
_OlTRnetStatsPortLineErrors_Type = Counter32
_OlTRnetStatsPortLineErrors_Object = MibTableColumn
olTRnetStatsPortLineErrors = _OlTRnetStatsPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 6),
    _OlTRnetStatsPortLineErrors_Type()
)
olTRnetStatsPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortLineErrors.setStatus("mandatory")
_OlTRnetStatsPortBurstErrors_Type = Counter32
_OlTRnetStatsPortBurstErrors_Object = MibTableColumn
olTRnetStatsPortBurstErrors = _OlTRnetStatsPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 7),
    _OlTRnetStatsPortBurstErrors_Type()
)
olTRnetStatsPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortBurstErrors.setStatus("mandatory")
_OlTRnetStatsPortACErrors_Type = Counter32
_OlTRnetStatsPortACErrors_Object = MibTableColumn
olTRnetStatsPortACErrors = _OlTRnetStatsPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 8),
    _OlTRnetStatsPortACErrors_Type()
)
olTRnetStatsPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortACErrors.setStatus("mandatory")
_OlTRnetStatsPortLostFrameErrors_Type = Counter32
_OlTRnetStatsPortLostFrameErrors_Object = MibTableColumn
olTRnetStatsPortLostFrameErrors = _OlTRnetStatsPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 9),
    _OlTRnetStatsPortLostFrameErrors_Type()
)
olTRnetStatsPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortLostFrameErrors.setStatus("mandatory")
_OlTRnetStatsPortCongestionErrors_Type = Counter32
_OlTRnetStatsPortCongestionErrors_Object = MibTableColumn
olTRnetStatsPortCongestionErrors = _OlTRnetStatsPortCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 10),
    _OlTRnetStatsPortCongestionErrors_Type()
)
olTRnetStatsPortCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortCongestionErrors.setStatus("mandatory")
_OlTRnetStatsPortFrameCopiedErrors_Type = Counter32
_OlTRnetStatsPortFrameCopiedErrors_Object = MibTableColumn
olTRnetStatsPortFrameCopiedErrors = _OlTRnetStatsPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 11),
    _OlTRnetStatsPortFrameCopiedErrors_Type()
)
olTRnetStatsPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortFrameCopiedErrors.setStatus("mandatory")
_OlTRnetStatsPortTokenErrors_Type = Counter32
_OlTRnetStatsPortTokenErrors_Object = MibTableColumn
olTRnetStatsPortTokenErrors = _OlTRnetStatsPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 12),
    _OlTRnetStatsPortTokenErrors_Type()
)
olTRnetStatsPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortTokenErrors.setStatus("mandatory")
_OlTRnetStatsPortDuplicateAddresses_Type = Counter32
_OlTRnetStatsPortDuplicateAddresses_Object = MibTableColumn
olTRnetStatsPortDuplicateAddresses = _OlTRnetStatsPortDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 4, 1, 13),
    _OlTRnetStatsPortDuplicateAddresses_Type()
)
olTRnetStatsPortDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetStatsPortDuplicateAddresses.setStatus("mandatory")
_OlTRnetMapSummary_ObjectIdentity = ObjectIdentity
olTRnetMapSummary = _OlTRnetMapSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5)
)


class _OlTRnetMapSummaryLogicalState_Type(Integer32):
    """Custom type olTRnetMapSummaryLogicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRnetMapSummaryLogicalState_Type.__name__ = "Integer32"
_OlTRnetMapSummaryLogicalState_Object = MibScalar
olTRnetMapSummaryLogicalState = _OlTRnetMapSummaryLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 1),
    _OlTRnetMapSummaryLogicalState_Type()
)
olTRnetMapSummaryLogicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryLogicalState.setStatus("mandatory")


class _OlTRnetMapSummaryLogicalLock_Type(Integer32):
    """Custom type olTRnetMapSummaryLogicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_OlTRnetMapSummaryLogicalLock_Type.__name__ = "Integer32"
_OlTRnetMapSummaryLogicalLock_Object = MibScalar
olTRnetMapSummaryLogicalLock = _OlTRnetMapSummaryLogicalLock_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 2),
    _OlTRnetMapSummaryLogicalLock_Type()
)
olTRnetMapSummaryLogicalLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRnetMapSummaryLogicalLock.setStatus("mandatory")
_OlTRnetMapSummaryTable_Object = MibTable
olTRnetMapSummaryTable = _OlTRnetMapSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3)
)
if mibBuilder.loadTexts:
    olTRnetMapSummaryTable.setStatus("mandatory")
_OlTRnetMapSummaryEntry_Object = MibTableRow
olTRnetMapSummaryEntry = _OlTRnetMapSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1)
)
olTRnetMapSummaryEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRnetMapSummaryNetID"),
    (0, "CHIPTRNET-MIB", "olTRnetMapSummaryIndex"),
)
if mibBuilder.loadTexts:
    olTRnetMapSummaryEntry.setStatus("mandatory")


class _OlTRnetMapSummaryNetID_Type(Integer32):
    """Custom type olTRnetMapSummaryNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRnetMapSummaryNetID_Type.__name__ = "Integer32"
_OlTRnetMapSummaryNetID_Object = MibTableColumn
olTRnetMapSummaryNetID = _OlTRnetMapSummaryNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 1),
    _OlTRnetMapSummaryNetID_Type()
)
olTRnetMapSummaryNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryNetID.setStatus("mandatory")
_OlTRnetMapSummaryIndex_Type = Integer32
_OlTRnetMapSummaryIndex_Object = MibTableColumn
olTRnetMapSummaryIndex = _OlTRnetMapSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 2),
    _OlTRnetMapSummaryIndex_Type()
)
olTRnetMapSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummaryIndex.setStatus("mandatory")


class _OlTRnetMapSummary32Stations_Type(OctetString):
    """Custom type olTRnetMapSummary32Stations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 256),
    )


_OlTRnetMapSummary32Stations_Type.__name__ = "OctetString"
_OlTRnetMapSummary32Stations_Object = MibTableColumn
olTRnetMapSummary32Stations = _OlTRnetMapSummary32Stations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 5, 3, 1, 3),
    _OlTRnetMapSummary32Stations_Type()
)
olTRnetMapSummary32Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRnetMapSummary32Stations.setStatus("mandatory")
_OlTRTrafTable_Object = MibTable
olTRTrafTable = _OlTRTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    olTRTrafTable.setStatus("mandatory")
_OlTRTrafEntry_Object = MibTableRow
olTRTrafEntry = _OlTRTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1)
)
olTRTrafEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafNetID"),
)
if mibBuilder.loadTexts:
    olTRTrafEntry.setStatus("mandatory")


class _OlTRTrafNetID_Type(Integer32):
    """Custom type olTRTrafNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafNetID_Type.__name__ = "Integer32"
_OlTRTrafNetID_Object = MibTableColumn
olTRTrafNetID = _OlTRTrafNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 1),
    _OlTRTrafNetID_Type()
)
olTRTrafNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafNetID.setStatus("mandatory")
_OlTRTrafTokenRotationTime_Type = Integer32
_OlTRTrafTokenRotationTime_Object = MibTableColumn
olTRTrafTokenRotationTime = _OlTRTrafTokenRotationTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 2),
    _OlTRTrafTokenRotationTime_Type()
)
olTRTrafTokenRotationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTokenRotationTime.setStatus("mandatory")
_OlTRTrafDropEvents_Type = Counter32
_OlTRTrafDropEvents_Object = MibTableColumn
olTRTrafDropEvents = _OlTRTrafDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 3),
    _OlTRTrafDropEvents_Type()
)
olTRTrafDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafDropEvents.setStatus("mandatory")
_OlTRTrafOctets_Type = Counter32
_OlTRTrafOctets_Object = MibTableColumn
olTRTrafOctets = _OlTRTrafOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 4),
    _OlTRTrafOctets_Type()
)
olTRTrafOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafOctets.setStatus("mandatory")
_OlTRTrafFrames_Type = Counter32
_OlTRTrafFrames_Object = MibTableColumn
olTRTrafFrames = _OlTRTrafFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 5),
    _OlTRTrafFrames_Type()
)
olTRTrafFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames.setStatus("mandatory")
_OlTRTrafMacOctets_Type = Counter32
_OlTRTrafMacOctets_Object = MibTableColumn
olTRTrafMacOctets = _OlTRTrafMacOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 6),
    _OlTRTrafMacOctets_Type()
)
olTRTrafMacOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMacOctets.setStatus("mandatory")
_OlTRTrafMacFrames_Type = Counter32
_OlTRTrafMacFrames_Object = MibTableColumn
olTRTrafMacFrames = _OlTRTrafMacFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 7),
    _OlTRTrafMacFrames_Type()
)
olTRTrafMacFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMacFrames.setStatus("mandatory")
_OlTRTrafBroadcastFrames_Type = Counter32
_OlTRTrafBroadcastFrames_Object = MibTableColumn
olTRTrafBroadcastFrames = _OlTRTrafBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 8),
    _OlTRTrafBroadcastFrames_Type()
)
olTRTrafBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafBroadcastFrames.setStatus("mandatory")
_OlTRTrafMulticastFrames_Type = Counter32
_OlTRTrafMulticastFrames_Object = MibTableColumn
olTRTrafMulticastFrames = _OlTRTrafMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 9),
    _OlTRTrafMulticastFrames_Type()
)
olTRTrafMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafMulticastFrames.setStatus("mandatory")
_OlTRTrafFrames18to63Octets_Type = Counter32
_OlTRTrafFrames18to63Octets_Object = MibTableColumn
olTRTrafFrames18to63Octets = _OlTRTrafFrames18to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 10),
    _OlTRTrafFrames18to63Octets_Type()
)
olTRTrafFrames18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames18to63Octets.setStatus("mandatory")
_OlTRTrafFrames64to127Octets_Type = Counter32
_OlTRTrafFrames64to127Octets_Object = MibTableColumn
olTRTrafFrames64to127Octets = _OlTRTrafFrames64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 11),
    _OlTRTrafFrames64to127Octets_Type()
)
olTRTrafFrames64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames64to127Octets.setStatus("mandatory")
_OlTRTrafFrames128to255Octets_Type = Counter32
_OlTRTrafFrames128to255Octets_Object = MibTableColumn
olTRTrafFrames128to255Octets = _OlTRTrafFrames128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 12),
    _OlTRTrafFrames128to255Octets_Type()
)
olTRTrafFrames128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames128to255Octets.setStatus("mandatory")
_OlTRTrafFrames256to511Octets_Type = Counter32
_OlTRTrafFrames256to511Octets_Object = MibTableColumn
olTRTrafFrames256to511Octets = _OlTRTrafFrames256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 13),
    _OlTRTrafFrames256to511Octets_Type()
)
olTRTrafFrames256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames256to511Octets.setStatus("mandatory")
_OlTRTrafFrames512to1023Octets_Type = Counter32
_OlTRTrafFrames512to1023Octets_Object = MibTableColumn
olTRTrafFrames512to1023Octets = _OlTRTrafFrames512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 14),
    _OlTRTrafFrames512to1023Octets_Type()
)
olTRTrafFrames512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames512to1023Octets.setStatus("mandatory")
_OlTRTrafFrames1024to2047Octets_Type = Counter32
_OlTRTrafFrames1024to2047Octets_Object = MibTableColumn
olTRTrafFrames1024to2047Octets = _OlTRTrafFrames1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 15),
    _OlTRTrafFrames1024to2047Octets_Type()
)
olTRTrafFrames1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames1024to2047Octets.setStatus("mandatory")
_OlTRTrafFrames2048to4095Octets_Type = Counter32
_OlTRTrafFrames2048to4095Octets_Object = MibTableColumn
olTRTrafFrames2048to4095Octets = _OlTRTrafFrames2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 16),
    _OlTRTrafFrames2048to4095Octets_Type()
)
olTRTrafFrames2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames2048to4095Octets.setStatus("mandatory")
_OlTRTrafFrames4096to8191Octets_Type = Counter32
_OlTRTrafFrames4096to8191Octets_Object = MibTableColumn
olTRTrafFrames4096to8191Octets = _OlTRTrafFrames4096to8191Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 17),
    _OlTRTrafFrames4096to8191Octets_Type()
)
olTRTrafFrames4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames4096to8191Octets.setStatus("mandatory")
_OlTRTrafFrames8192to18000Octets_Type = Counter32
_OlTRTrafFrames8192to18000Octets_Object = MibTableColumn
olTRTrafFrames8192to18000Octets = _OlTRTrafFrames8192to18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 18),
    _OlTRTrafFrames8192to18000Octets_Type()
)
olTRTrafFrames8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFrames8192to18000Octets.setStatus("mandatory")
_OlTRTrafFramesGreaterThan18000Octets_Type = Counter32
_OlTRTrafFramesGreaterThan18000Octets_Object = MibTableColumn
olTRTrafFramesGreaterThan18000Octets = _OlTRTrafFramesGreaterThan18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 6, 1, 19),
    _OlTRTrafFramesGreaterThan18000Octets_Type()
)
olTRTrafFramesGreaterThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafFramesGreaterThan18000Octets.setStatus("mandatory")
_OlTRTrafControlTable_Object = MibTable
olTRTrafControlTable = _OlTRTrafControlTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    olTRTrafControlTable.setStatus("mandatory")
_OlTRTrafControlEntry_Object = MibTableRow
olTRTrafControlEntry = _OlTRTrafControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1)
)
olTRTrafControlEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafControlNetID"),
)
if mibBuilder.loadTexts:
    olTRTrafControlEntry.setStatus("mandatory")


class _OlTRTrafControlNetID_Type(Integer32):
    """Custom type olTRTrafControlNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafControlNetID_Type.__name__ = "Integer32"
_OlTRTrafControlNetID_Object = MibTableColumn
olTRTrafControlNetID = _OlTRTrafControlNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 1),
    _OlTRTrafControlNetID_Type()
)
olTRTrafControlNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlNetID.setStatus("mandatory")


class _OlTRTrafControlLogicalState_Type(Integer32):
    """Custom type olTRTrafControlLogicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 1),
          ("notChanging", 2))
    )


_OlTRTrafControlLogicalState_Type.__name__ = "Integer32"
_OlTRTrafControlLogicalState_Object = MibTableColumn
olTRTrafControlLogicalState = _OlTRTrafControlLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 2),
    _OlTRTrafControlLogicalState_Type()
)
olTRTrafControlLogicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlLogicalState.setStatus("mandatory")


class _OlTRTrafControlLogicalLock_Type(Integer32):
    """Custom type olTRTrafControlLogicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_OlTRTrafControlLogicalLock_Type.__name__ = "Integer32"
_OlTRTrafControlLogicalLock_Object = MibTableColumn
olTRTrafControlLogicalLock = _OlTRTrafControlLogicalLock_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 3),
    _OlTRTrafControlLogicalLock_Type()
)
olTRTrafControlLogicalLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlLogicalLock.setStatus("mandatory")


class _OlTRTrafControlClear_Type(Integer32):
    """Custom type olTRTrafControlClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("normal", 1))
    )


_OlTRTrafControlClear_Type.__name__ = "Integer32"
_OlTRTrafControlClear_Object = MibTableColumn
olTRTrafControlClear = _OlTRTrafControlClear_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 4),
    _OlTRTrafControlClear_Type()
)
olTRTrafControlClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlClear.setStatus("mandatory")
_OlTRTrafControlLastClearTime_Type = TimeTicks
_OlTRTrafControlLastClearTime_Object = MibTableColumn
olTRTrafControlLastClearTime = _OlTRTrafControlLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 5),
    _OlTRTrafControlLastClearTime_Type()
)
olTRTrafControlLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlLastClearTime.setStatus("mandatory")
_OlTRTrafControlTotalStations_Type = Integer32
_OlTRTrafControlTotalStations_Object = MibTableColumn
olTRTrafControlTotalStations = _OlTRTrafControlTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 6),
    _OlTRTrafControlTotalStations_Type()
)
olTRTrafControlTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTotalStations.setStatus("mandatory")
_OlTRTrafControlStationLastChangeTime_Type = TimeTicks
_OlTRTrafControlStationLastChangeTime_Object = MibTableColumn
olTRTrafControlStationLastChangeTime = _OlTRTrafControlStationLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 7),
    _OlTRTrafControlStationLastChangeTime_Type()
)
olTRTrafControlStationLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlStationLastChangeTime.setStatus("mandatory")
_OlTRTrafControlPortTotalStations_Type = Integer32
_OlTRTrafControlPortTotalStations_Object = MibTableColumn
olTRTrafControlPortTotalStations = _OlTRTrafControlPortTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 8),
    _OlTRTrafControlPortTotalStations_Type()
)
olTRTrafControlPortTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlPortTotalStations.setStatus("mandatory")
_OlTRTrafControlPortLastChangeTime_Type = TimeTicks
_OlTRTrafControlPortLastChangeTime_Object = MibTableColumn
olTRTrafControlPortLastChangeTime = _OlTRTrafControlPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 9),
    _OlTRTrafControlPortLastChangeTime_Type()
)
olTRTrafControlPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlPortLastChangeTime.setStatus("mandatory")
_OlTRTrafControlTopNMaxStations_Type = Integer32
_OlTRTrafControlTopNMaxStations_Object = MibTableColumn
olTRTrafControlTopNMaxStations = _OlTRTrafControlTopNMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 10),
    _OlTRTrafControlTopNMaxStations_Type()
)
olTRTrafControlTopNMaxStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlTopNMaxStations.setStatus("mandatory")
_OlTRTrafControlTopNTotalStations_Type = Integer32
_OlTRTrafControlTopNTotalStations_Object = MibTableColumn
olTRTrafControlTopNTotalStations = _OlTRTrafControlTopNTotalStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 11),
    _OlTRTrafControlTopNTotalStations_Type()
)
olTRTrafControlTopNTotalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTopNTotalStations.setStatus("mandatory")
_OlTRTrafControlTopNLastChangeTime_Type = TimeTicks
_OlTRTrafControlTopNLastChangeTime_Object = MibTableColumn
olTRTrafControlTopNLastChangeTime = _OlTRTrafControlTopNLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 12),
    _OlTRTrafControlTopNLastChangeTime_Type()
)
olTRTrafControlTopNLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafControlTopNLastChangeTime.setStatus("mandatory")
_OlTRTrafControlTopNInterval_Type = Integer32
_OlTRTrafControlTopNInterval_Object = MibTableColumn
olTRTrafControlTopNInterval = _OlTRTrafControlTopNInterval_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 7, 1, 13),
    _OlTRTrafControlTopNInterval_Type()
)
olTRTrafControlTopNInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafControlTopNInterval.setStatus("mandatory")
_OlTRTrafStationTable_Object = MibTable
olTRTrafStationTable = _OlTRTrafStationTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    olTRTrafStationTable.setStatus("mandatory")
_OlTRTrafStationEntry_Object = MibTableRow
olTRTrafStationEntry = _OlTRTrafStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1)
)
olTRTrafStationEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafStationNetID"),
    (0, "CHIPTRNET-MIB", "olTRTrafStationAddress"),
)
if mibBuilder.loadTexts:
    olTRTrafStationEntry.setStatus("mandatory")


class _OlTRTrafStationNetID_Type(Integer32):
    """Custom type olTRTrafStationNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafStationNetID_Type.__name__ = "Integer32"
_OlTRTrafStationNetID_Object = MibTableColumn
olTRTrafStationNetID = _OlTRTrafStationNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 1),
    _OlTRTrafStationNetID_Type()
)
olTRTrafStationNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationNetID.setStatus("mandatory")
_OlTRTrafStationAddress_Type = MacAddress
_OlTRTrafStationAddress_Object = MibTableColumn
olTRTrafStationAddress = _OlTRTrafStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 2),
    _OlTRTrafStationAddress_Type()
)
olTRTrafStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationAddress.setStatus("mandatory")


class _OlTRTrafStationSlotIndex_Type(Integer32):
    """Custom type olTRTrafStationSlotIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("remote-ring", 254),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRTrafStationSlotIndex_Type.__name__ = "Integer32"
_OlTRTrafStationSlotIndex_Object = MibTableColumn
olTRTrafStationSlotIndex = _OlTRTrafStationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 3),
    _OlTRTrafStationSlotIndex_Type()
)
olTRTrafStationSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationSlotIndex.setStatus("mandatory")
_OlTRTrafStationPortIndex_Type = Integer32
_OlTRTrafStationPortIndex_Object = MibTableColumn
olTRTrafStationPortIndex = _OlTRTrafStationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 4),
    _OlTRTrafStationPortIndex_Type()
)
olTRTrafStationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationPortIndex.setStatus("mandatory")
_OlTRTrafStationInFrames_Type = Counter32
_OlTRTrafStationInFrames_Object = MibTableColumn
olTRTrafStationInFrames = _OlTRTrafStationInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 5),
    _OlTRTrafStationInFrames_Type()
)
olTRTrafStationInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationInFrames.setStatus("mandatory")
_OlTRTrafStationOutFrames_Type = Counter32
_OlTRTrafStationOutFrames_Object = MibTableColumn
olTRTrafStationOutFrames = _OlTRTrafStationOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 6),
    _OlTRTrafStationOutFrames_Type()
)
olTRTrafStationOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutFrames.setStatus("mandatory")
_OlTRTrafStationInOctets_Type = Counter32
_OlTRTrafStationInOctets_Object = MibTableColumn
olTRTrafStationInOctets = _OlTRTrafStationInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 7),
    _OlTRTrafStationInOctets_Type()
)
olTRTrafStationInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationInOctets.setStatus("mandatory")
_OlTRTrafStationOutOctets_Type = Counter32
_OlTRTrafStationOutOctets_Object = MibTableColumn
olTRTrafStationOutOctets = _OlTRTrafStationOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 8),
    _OlTRTrafStationOutOctets_Type()
)
olTRTrafStationOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutOctets.setStatus("mandatory")
_OlTRTrafStationOutErrors_Type = Counter32
_OlTRTrafStationOutErrors_Object = MibTableColumn
olTRTrafStationOutErrors = _OlTRTrafStationOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 9),
    _OlTRTrafStationOutErrors_Type()
)
olTRTrafStationOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutErrors.setStatus("mandatory")
_OlTRTrafStationOutBroadcastFrames_Type = Counter32
_OlTRTrafStationOutBroadcastFrames_Object = MibTableColumn
olTRTrafStationOutBroadcastFrames = _OlTRTrafStationOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 10),
    _OlTRTrafStationOutBroadcastFrames_Type()
)
olTRTrafStationOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafStationOutMulticastFrames_Type = Counter32
_OlTRTrafStationOutMulticastFrames_Object = MibTableColumn
olTRTrafStationOutMulticastFrames = _OlTRTrafStationOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 8, 1, 11),
    _OlTRTrafStationOutMulticastFrames_Type()
)
olTRTrafStationOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafStationOutMulticastFrames.setStatus("mandatory")
_OlTRTrafPortTable_Object = MibTable
olTRTrafPortTable = _OlTRTrafPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    olTRTrafPortTable.setStatus("mandatory")
_OlTRTrafPortEntry_Object = MibTableRow
olTRTrafPortEntry = _OlTRTrafPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1)
)
olTRTrafPortEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafPortSlotIndex"),
    (0, "CHIPTRNET-MIB", "olTRTrafPortPortIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafPortEntry.setStatus("mandatory")
_OlTRTrafPortSlotIndex_Type = Integer32
_OlTRTrafPortSlotIndex_Object = MibTableColumn
olTRTrafPortSlotIndex = _OlTRTrafPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 1),
    _OlTRTrafPortSlotIndex_Type()
)
olTRTrafPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortSlotIndex.setStatus("mandatory")
_OlTRTrafPortPortIndex_Type = Integer32
_OlTRTrafPortPortIndex_Object = MibTableColumn
olTRTrafPortPortIndex = _OlTRTrafPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 2),
    _OlTRTrafPortPortIndex_Type()
)
olTRTrafPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortPortIndex.setStatus("mandatory")


class _OlTRTrafPortNetID_Type(Integer32):
    """Custom type olTRTrafPortNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafPortNetID_Type.__name__ = "Integer32"
_OlTRTrafPortNetID_Object = MibTableColumn
olTRTrafPortNetID = _OlTRTrafPortNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 3),
    _OlTRTrafPortNetID_Type()
)
olTRTrafPortNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortNetID.setStatus("mandatory")
_OlTRTrafPortAddress_Type = MacAddress
_OlTRTrafPortAddress_Object = MibTableColumn
olTRTrafPortAddress = _OlTRTrafPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 4),
    _OlTRTrafPortAddress_Type()
)
olTRTrafPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortAddress.setStatus("mandatory")
_OlTRTrafPortInFrames_Type = Counter32
_OlTRTrafPortInFrames_Object = MibTableColumn
olTRTrafPortInFrames = _OlTRTrafPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 5),
    _OlTRTrafPortInFrames_Type()
)
olTRTrafPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortInFrames.setStatus("mandatory")
_OlTRTrafPortOutFrames_Type = Counter32
_OlTRTrafPortOutFrames_Object = MibTableColumn
olTRTrafPortOutFrames = _OlTRTrafPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 6),
    _OlTRTrafPortOutFrames_Type()
)
olTRTrafPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutFrames.setStatus("mandatory")
_OlTRTrafPortInOctets_Type = Counter32
_OlTRTrafPortInOctets_Object = MibTableColumn
olTRTrafPortInOctets = _OlTRTrafPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 7),
    _OlTRTrafPortInOctets_Type()
)
olTRTrafPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortInOctets.setStatus("mandatory")
_OlTRTrafPortOutOctets_Type = Counter32
_OlTRTrafPortOutOctets_Object = MibTableColumn
olTRTrafPortOutOctets = _OlTRTrafPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 8),
    _OlTRTrafPortOutOctets_Type()
)
olTRTrafPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutOctets.setStatus("mandatory")
_OlTRTrafPortOutErrors_Type = Counter32
_OlTRTrafPortOutErrors_Object = MibTableColumn
olTRTrafPortOutErrors = _OlTRTrafPortOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 9),
    _OlTRTrafPortOutErrors_Type()
)
olTRTrafPortOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutErrors.setStatus("mandatory")
_OlTRTrafPortOutBroadcastFrames_Type = Counter32
_OlTRTrafPortOutBroadcastFrames_Object = MibTableColumn
olTRTrafPortOutBroadcastFrames = _OlTRTrafPortOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 10),
    _OlTRTrafPortOutBroadcastFrames_Type()
)
olTRTrafPortOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafPortOutMulticastFrames_Type = Counter32
_OlTRTrafPortOutMulticastFrames_Object = MibTableColumn
olTRTrafPortOutMulticastFrames = _OlTRTrafPortOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 9, 1, 11),
    _OlTRTrafPortOutMulticastFrames_Type()
)
olTRTrafPortOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafPortOutMulticastFrames.setStatus("mandatory")
_OlTRTrafTopNTable_Object = MibTable
olTRTrafTopNTable = _OlTRTrafTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10)
)
if mibBuilder.loadTexts:
    olTRTrafTopNTable.setStatus("mandatory")
_OlTRTrafTopNEntry_Object = MibTableRow
olTRTrafTopNEntry = _OlTRTrafTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1)
)
olTRTrafTopNEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafTopNNetID"),
    (0, "CHIPTRNET-MIB", "olTRTrafTopNStatistic"),
    (0, "CHIPTRNET-MIB", "olTRTrafTopNIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafTopNEntry.setStatus("mandatory")


class _OlTRTrafTopNNetID_Type(Integer32):
    """Custom type olTRTrafTopNNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafTopNNetID_Type.__name__ = "Integer32"
_OlTRTrafTopNNetID_Object = MibTableColumn
olTRTrafTopNNetID = _OlTRTrafTopNNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 1),
    _OlTRTrafTopNNetID_Type()
)
olTRTrafTopNNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNNetID.setStatus("mandatory")


class _OlTRTrafTopNStatistic_Type(Integer32):
    """Custom type olTRTrafTopNStatistic based on Integer32"""
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
        *(("olTRTrafTopNInFrames", 1),
          ("olTRTrafTopNInOctets", 3),
          ("olTRTrafTopNOutBroadcastFrames", 6),
          ("olTRTrafTopNOutErrors", 5),
          ("olTRTrafTopNOutFrames", 2),
          ("olTRTrafTopNOutMulticastFrames", 7),
          ("olTRTrafTopNOutOctets", 4))
    )


_OlTRTrafTopNStatistic_Type.__name__ = "Integer32"
_OlTRTrafTopNStatistic_Object = MibTableColumn
olTRTrafTopNStatistic = _OlTRTrafTopNStatistic_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 2),
    _OlTRTrafTopNStatistic_Type()
)
olTRTrafTopNStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafTopNStatistic.setStatus("mandatory")
_OlTRTrafTopNIndex_Type = Integer32
_OlTRTrafTopNIndex_Object = MibTableColumn
olTRTrafTopNIndex = _OlTRTrafTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 3),
    _OlTRTrafTopNIndex_Type()
)
olTRTrafTopNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNIndex.setStatus("mandatory")
_OlTRTrafTopNAddress_Type = MacAddress
_OlTRTrafTopNAddress_Object = MibTableColumn
olTRTrafTopNAddress = _OlTRTrafTopNAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 4),
    _OlTRTrafTopNAddress_Type()
)
olTRTrafTopNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNAddress.setStatus("mandatory")


class _OlTRTrafTopNSlotIndex_Type(Integer32):
    """Custom type olTRTrafTopNSlotIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("remote-ring", 254),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTRTrafTopNSlotIndex_Type.__name__ = "Integer32"
_OlTRTrafTopNSlotIndex_Object = MibTableColumn
olTRTrafTopNSlotIndex = _OlTRTrafTopNSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 5),
    _OlTRTrafTopNSlotIndex_Type()
)
olTRTrafTopNSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSlotIndex.setStatus("mandatory")
_OlTRTrafTopNPortIndex_Type = Integer32
_OlTRTrafTopNPortIndex_Object = MibTableColumn
olTRTrafTopNPortIndex = _OlTRTrafTopNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 6),
    _OlTRTrafTopNPortIndex_Type()
)
olTRTrafTopNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNPortIndex.setStatus("mandatory")
_OlTRTrafTopNInFrames_Type = Counter32
_OlTRTrafTopNInFrames_Object = MibTableColumn
olTRTrafTopNInFrames = _OlTRTrafTopNInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 7),
    _OlTRTrafTopNInFrames_Type()
)
olTRTrafTopNInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNInFrames.setStatus("mandatory")
_OlTRTrafTopNOutFrames_Type = Counter32
_OlTRTrafTopNOutFrames_Object = MibTableColumn
olTRTrafTopNOutFrames = _OlTRTrafTopNOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 8),
    _OlTRTrafTopNOutFrames_Type()
)
olTRTrafTopNOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutFrames.setStatus("mandatory")
_OlTRTrafTopNInOctets_Type = Counter32
_OlTRTrafTopNInOctets_Object = MibTableColumn
olTRTrafTopNInOctets = _OlTRTrafTopNInOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 9),
    _OlTRTrafTopNInOctets_Type()
)
olTRTrafTopNInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNInOctets.setStatus("mandatory")
_OlTRTrafTopNOutOctets_Type = Counter32
_OlTRTrafTopNOutOctets_Object = MibTableColumn
olTRTrafTopNOutOctets = _OlTRTrafTopNOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 10),
    _OlTRTrafTopNOutOctets_Type()
)
olTRTrafTopNOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutOctets.setStatus("mandatory")
_OlTRTrafTopNOutErrors_Type = Counter32
_OlTRTrafTopNOutErrors_Object = MibTableColumn
olTRTrafTopNOutErrors = _OlTRTrafTopNOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 11),
    _OlTRTrafTopNOutErrors_Type()
)
olTRTrafTopNOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutErrors.setStatus("mandatory")
_OlTRTrafTopNOutBroadcastFrames_Type = Counter32
_OlTRTrafTopNOutBroadcastFrames_Object = MibTableColumn
olTRTrafTopNOutBroadcastFrames = _OlTRTrafTopNOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 12),
    _OlTRTrafTopNOutBroadcastFrames_Type()
)
olTRTrafTopNOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutBroadcastFrames.setStatus("mandatory")
_OlTRTrafTopNOutMulticastFrames_Type = Counter32
_OlTRTrafTopNOutMulticastFrames_Object = MibTableColumn
olTRTrafTopNOutMulticastFrames = _OlTRTrafTopNOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 10, 1, 13),
    _OlTRTrafTopNOutMulticastFrames_Type()
)
olTRTrafTopNOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNOutMulticastFrames.setStatus("mandatory")
_OlTRTrafTopNSummaryTable_Object = MibTable
olTRTrafTopNSummaryTable = _OlTRTrafTopNSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11)
)
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryTable.setStatus("mandatory")
_OlTRTrafTopNSummaryEntry_Object = MibTableRow
olTRTrafTopNSummaryEntry = _OlTRTrafTopNSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1)
)
olTRTrafTopNSummaryEntry.setIndexNames(
    (0, "CHIPTRNET-MIB", "olTRTrafTopNSummaryNetID"),
    (0, "CHIPTRNET-MIB", "olTRTrafTopNSummaryStatistic"),
    (0, "CHIPTRNET-MIB", "olTRTrafTopNSummaryIndex"),
)
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryEntry.setStatus("mandatory")


class _OlTRTrafTopNSummaryNetID_Type(Integer32):
    """Custom type olTRTrafTopNSummaryNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 2),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlTRTrafTopNSummaryNetID_Type.__name__ = "Integer32"
_OlTRTrafTopNSummaryNetID_Object = MibTableColumn
olTRTrafTopNSummaryNetID = _OlTRTrafTopNSummaryNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 1),
    _OlTRTrafTopNSummaryNetID_Type()
)
olTRTrafTopNSummaryNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryNetID.setStatus("mandatory")


class _OlTRTrafTopNSummaryStatistic_Type(Integer32):
    """Custom type olTRTrafTopNSummaryStatistic based on Integer32"""
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
        *(("olTRTrafTopNSummaryInFrames", 1),
          ("olTRTrafTopNSummaryInOctets", 3),
          ("olTRTrafTopNSummaryOutBroadcastFrames", 6),
          ("olTRTrafTopNSummaryOutErrors", 5),
          ("olTRTrafTopNSummaryOutFrames", 2),
          ("olTRTrafTopNSummaryOutMulticastFrames", 7),
          ("olTRTrafTopNSummaryOutOctets", 4))
    )


_OlTRTrafTopNSummaryStatistic_Type.__name__ = "Integer32"
_OlTRTrafTopNSummaryStatistic_Object = MibTableColumn
olTRTrafTopNSummaryStatistic = _OlTRTrafTopNSummaryStatistic_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 2),
    _OlTRTrafTopNSummaryStatistic_Type()
)
olTRTrafTopNSummaryStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryStatistic.setStatus("mandatory")
_OlTRTrafTopNSummaryIndex_Type = Integer32
_OlTRTrafTopNSummaryIndex_Object = MibTableColumn
olTRTrafTopNSummaryIndex = _OlTRTrafTopNSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 3),
    _OlTRTrafTopNSummaryIndex_Type()
)
olTRTrafTopNSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryIndex.setStatus("mandatory")
_OlTRTrafTopNSummaryStations_Type = OctetString
_OlTRTrafTopNSummaryStations_Object = MibTableColumn
olTRTrafTopNSummaryStations = _OlTRTrafTopNSummaryStations_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3, 11, 1, 4),
    _OlTRTrafTopNSummaryStations_Type()
)
olTRTrafTopNSummaryStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTRTrafTopNSummaryStations.setStatus("mandatory")
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
    "CHIPTRNET-MIB",
    **{"MacAddress": MacAddress,
       "chipcom": chipcom,
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
       "olTRnetMapState": olTRnetMapState,
       "olTRnetStatsTable": olTRnetStatsTable,
       "olTRnetStatsEntry": olTRnetStatsEntry,
       "olTRnetStatsNetID": olTRnetStatsNetID,
       "olTRnetStatsLineErrors": olTRnetStatsLineErrors,
       "olTRnetStatsBurstErrors": olTRnetStatsBurstErrors,
       "olTRnetStatsACErrors": olTRnetStatsACErrors,
       "olTRnetStatsLostFrameErrors": olTRnetStatsLostFrameErrors,
       "olTRnetStatsCongestionErrors": olTRnetStatsCongestionErrors,
       "olTRnetStatsFrameCopiedErrors": olTRnetStatsFrameCopiedErrors,
       "olTRnetStatsTokenErrors": olTRnetStatsTokenErrors,
       "olTRnetStatsDuplicateAddresses": olTRnetStatsDuplicateAddresses,
       "olTRnetStatsBeaconEvents": olTRnetStatsBeaconEvents,
       "olTRnetStatsLastBeaconSender": olTRnetStatsLastBeaconSender,
       "olTRnetStatsLastBeaconNAUN": olTRnetStatsLastBeaconNAUN,
       "olTRnetStatsLastBeaconTime": olTRnetStatsLastBeaconTime,
       "olTRnetStatsLastBeaconAction": olTRnetStatsLastBeaconAction,
       "olTRnetStatsTotalStations": olTRnetStatsTotalStations,
       "olTRnetStatsConcStations": olTRnetStatsConcStations,
       "olTRnetStatsTotalPorts": olTRnetStatsTotalPorts,
       "olTRnetStatsEnabledPorts": olTRnetStatsEnabledPorts,
       "olTRnetStatsActivePorts": olTRnetStatsActivePorts,
       "olTRnetStatsStationTable": olTRnetStatsStationTable,
       "olTRnetStatsStationEntry": olTRnetStatsStationEntry,
       "olTRnetStatsStationNetID": olTRnetStatsStationNetID,
       "olTRnetStatsStationAddr": olTRnetStatsStationAddr,
       "olTRnetStatsStationSlotIndex": olTRnetStatsStationSlotIndex,
       "olTRnetStatsStationPortIndex": olTRnetStatsStationPortIndex,
       "olTRnetStatsStationNAUNAddress": olTRnetStatsStationNAUNAddress,
       "olTRnetStatsStationLineErrors": olTRnetStatsStationLineErrors,
       "olTRnetStatsStationBurstErrors": olTRnetStatsStationBurstErrors,
       "olTRnetStatsStationACErrors": olTRnetStatsStationACErrors,
       "olTRnetStatsStationLostFrameErrors": olTRnetStatsStationLostFrameErrors,
       "olTRnetStatsStationCongestionErrors": olTRnetStatsStationCongestionErrors,
       "olTRnetStatsStationFrameCopiedErrors": olTRnetStatsStationFrameCopiedErrors,
       "olTRnetStatsStationTokenErrors": olTRnetStatsStationTokenErrors,
       "olTRnetStatsStationDuplicateAddresses": olTRnetStatsStationDuplicateAddresses,
       "olTRnetStatsPortTable": olTRnetStatsPortTable,
       "olTRnetStatsPortEntry": olTRnetStatsPortEntry,
       "olTRnetStatsPortSlotIndex": olTRnetStatsPortSlotIndex,
       "olTRnetStatsPortIndex": olTRnetStatsPortIndex,
       "olTRnetStatsPortNetID": olTRnetStatsPortNetID,
       "olTRnetStatsPortTotalStations": olTRnetStatsPortTotalStations,
       "olTRnetStatsPortAddress": olTRnetStatsPortAddress,
       "olTRnetStatsPortLineErrors": olTRnetStatsPortLineErrors,
       "olTRnetStatsPortBurstErrors": olTRnetStatsPortBurstErrors,
       "olTRnetStatsPortACErrors": olTRnetStatsPortACErrors,
       "olTRnetStatsPortLostFrameErrors": olTRnetStatsPortLostFrameErrors,
       "olTRnetStatsPortCongestionErrors": olTRnetStatsPortCongestionErrors,
       "olTRnetStatsPortFrameCopiedErrors": olTRnetStatsPortFrameCopiedErrors,
       "olTRnetStatsPortTokenErrors": olTRnetStatsPortTokenErrors,
       "olTRnetStatsPortDuplicateAddresses": olTRnetStatsPortDuplicateAddresses,
       "olTRnetMapSummary": olTRnetMapSummary,
       "olTRnetMapSummaryLogicalState": olTRnetMapSummaryLogicalState,
       "olTRnetMapSummaryLogicalLock": olTRnetMapSummaryLogicalLock,
       "olTRnetMapSummaryTable": olTRnetMapSummaryTable,
       "olTRnetMapSummaryEntry": olTRnetMapSummaryEntry,
       "olTRnetMapSummaryNetID": olTRnetMapSummaryNetID,
       "olTRnetMapSummaryIndex": olTRnetMapSummaryIndex,
       "olTRnetMapSummary32Stations": olTRnetMapSummary32Stations,
       "olTRTrafTable": olTRTrafTable,
       "olTRTrafEntry": olTRTrafEntry,
       "olTRTrafNetID": olTRTrafNetID,
       "olTRTrafTokenRotationTime": olTRTrafTokenRotationTime,
       "olTRTrafDropEvents": olTRTrafDropEvents,
       "olTRTrafOctets": olTRTrafOctets,
       "olTRTrafFrames": olTRTrafFrames,
       "olTRTrafMacOctets": olTRTrafMacOctets,
       "olTRTrafMacFrames": olTRTrafMacFrames,
       "olTRTrafBroadcastFrames": olTRTrafBroadcastFrames,
       "olTRTrafMulticastFrames": olTRTrafMulticastFrames,
       "olTRTrafFrames18to63Octets": olTRTrafFrames18to63Octets,
       "olTRTrafFrames64to127Octets": olTRTrafFrames64to127Octets,
       "olTRTrafFrames128to255Octets": olTRTrafFrames128to255Octets,
       "olTRTrafFrames256to511Octets": olTRTrafFrames256to511Octets,
       "olTRTrafFrames512to1023Octets": olTRTrafFrames512to1023Octets,
       "olTRTrafFrames1024to2047Octets": olTRTrafFrames1024to2047Octets,
       "olTRTrafFrames2048to4095Octets": olTRTrafFrames2048to4095Octets,
       "olTRTrafFrames4096to8191Octets": olTRTrafFrames4096to8191Octets,
       "olTRTrafFrames8192to18000Octets": olTRTrafFrames8192to18000Octets,
       "olTRTrafFramesGreaterThan18000Octets": olTRTrafFramesGreaterThan18000Octets,
       "olTRTrafControlTable": olTRTrafControlTable,
       "olTRTrafControlEntry": olTRTrafControlEntry,
       "olTRTrafControlNetID": olTRTrafControlNetID,
       "olTRTrafControlLogicalState": olTRTrafControlLogicalState,
       "olTRTrafControlLogicalLock": olTRTrafControlLogicalLock,
       "olTRTrafControlClear": olTRTrafControlClear,
       "olTRTrafControlLastClearTime": olTRTrafControlLastClearTime,
       "olTRTrafControlTotalStations": olTRTrafControlTotalStations,
       "olTRTrafControlStationLastChangeTime": olTRTrafControlStationLastChangeTime,
       "olTRTrafControlPortTotalStations": olTRTrafControlPortTotalStations,
       "olTRTrafControlPortLastChangeTime": olTRTrafControlPortLastChangeTime,
       "olTRTrafControlTopNMaxStations": olTRTrafControlTopNMaxStations,
       "olTRTrafControlTopNTotalStations": olTRTrafControlTopNTotalStations,
       "olTRTrafControlTopNLastChangeTime": olTRTrafControlTopNLastChangeTime,
       "olTRTrafControlTopNInterval": olTRTrafControlTopNInterval,
       "olTRTrafStationTable": olTRTrafStationTable,
       "olTRTrafStationEntry": olTRTrafStationEntry,
       "olTRTrafStationNetID": olTRTrafStationNetID,
       "olTRTrafStationAddress": olTRTrafStationAddress,
       "olTRTrafStationSlotIndex": olTRTrafStationSlotIndex,
       "olTRTrafStationPortIndex": olTRTrafStationPortIndex,
       "olTRTrafStationInFrames": olTRTrafStationInFrames,
       "olTRTrafStationOutFrames": olTRTrafStationOutFrames,
       "olTRTrafStationInOctets": olTRTrafStationInOctets,
       "olTRTrafStationOutOctets": olTRTrafStationOutOctets,
       "olTRTrafStationOutErrors": olTRTrafStationOutErrors,
       "olTRTrafStationOutBroadcastFrames": olTRTrafStationOutBroadcastFrames,
       "olTRTrafStationOutMulticastFrames": olTRTrafStationOutMulticastFrames,
       "olTRTrafPortTable": olTRTrafPortTable,
       "olTRTrafPortEntry": olTRTrafPortEntry,
       "olTRTrafPortSlotIndex": olTRTrafPortSlotIndex,
       "olTRTrafPortPortIndex": olTRTrafPortPortIndex,
       "olTRTrafPortNetID": olTRTrafPortNetID,
       "olTRTrafPortAddress": olTRTrafPortAddress,
       "olTRTrafPortInFrames": olTRTrafPortInFrames,
       "olTRTrafPortOutFrames": olTRTrafPortOutFrames,
       "olTRTrafPortInOctets": olTRTrafPortInOctets,
       "olTRTrafPortOutOctets": olTRTrafPortOutOctets,
       "olTRTrafPortOutErrors": olTRTrafPortOutErrors,
       "olTRTrafPortOutBroadcastFrames": olTRTrafPortOutBroadcastFrames,
       "olTRTrafPortOutMulticastFrames": olTRTrafPortOutMulticastFrames,
       "olTRTrafTopNTable": olTRTrafTopNTable,
       "olTRTrafTopNEntry": olTRTrafTopNEntry,
       "olTRTrafTopNNetID": olTRTrafTopNNetID,
       "olTRTrafTopNStatistic": olTRTrafTopNStatistic,
       "olTRTrafTopNIndex": olTRTrafTopNIndex,
       "olTRTrafTopNAddress": olTRTrafTopNAddress,
       "olTRTrafTopNSlotIndex": olTRTrafTopNSlotIndex,
       "olTRTrafTopNPortIndex": olTRTrafTopNPortIndex,
       "olTRTrafTopNInFrames": olTRTrafTopNInFrames,
       "olTRTrafTopNOutFrames": olTRTrafTopNOutFrames,
       "olTRTrafTopNInOctets": olTRTrafTopNInOctets,
       "olTRTrafTopNOutOctets": olTRTrafTopNOutOctets,
       "olTRTrafTopNOutErrors": olTRTrafTopNOutErrors,
       "olTRTrafTopNOutBroadcastFrames": olTRTrafTopNOutBroadcastFrames,
       "olTRTrafTopNOutMulticastFrames": olTRTrafTopNOutMulticastFrames,
       "olTRTrafTopNSummaryTable": olTRTrafTopNSummaryTable,
       "olTRTrafTopNSummaryEntry": olTRTrafTopNSummaryEntry,
       "olTRTrafTopNSummaryNetID": olTRTrafTopNSummaryNetID,
       "olTRTrafTopNSummaryStatistic": olTRTrafTopNSummaryStatistic,
       "olTRTrafTopNSummaryIndex": olTRTrafTopNSummaryIndex,
       "olTRTrafTopNSummaryStations": olTRTrafTopNSummaryStations,
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
