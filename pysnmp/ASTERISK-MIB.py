# SNMP MIB module (ASTERISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASTERISK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:53 2024
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

(digium,) = mibBuilder.importSymbols(
    "DIGIUM-MIB",
    "digium")

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

asterisk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1)
)
asterisk.setRevisions(
        ("2008-06-20 20:25",
         "2007-08-21 14:50",
         "2006-03-06 18:40",
         "2006-02-04 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsteriskVersion_ObjectIdentity = ObjectIdentity
asteriskVersion = _AsteriskVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 1)
)
_AstVersionString_Type = DisplayString
_AstVersionString_Object = MibScalar
astVersionString = _AstVersionString_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 1, 1),
    _AstVersionString_Type()
)
astVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astVersionString.setStatus("current")
_AstVersionTag_Type = Unsigned32
_AstVersionTag_Object = MibScalar
astVersionTag = _AstVersionTag_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 1, 2),
    _AstVersionTag_Type()
)
astVersionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astVersionTag.setStatus("current")
_AsteriskConfiguration_ObjectIdentity = ObjectIdentity
asteriskConfiguration = _AsteriskConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2)
)
_AstConfigUpTime_Type = TimeTicks
_AstConfigUpTime_Object = MibScalar
astConfigUpTime = _AstConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 1),
    _AstConfigUpTime_Type()
)
astConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigUpTime.setStatus("current")
_AstConfigReloadTime_Type = TimeTicks
_AstConfigReloadTime_Object = MibScalar
astConfigReloadTime = _AstConfigReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 2),
    _AstConfigReloadTime_Type()
)
astConfigReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigReloadTime.setStatus("current")
_AstConfigPid_Type = Integer32
_AstConfigPid_Object = MibScalar
astConfigPid = _AstConfigPid_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 3),
    _AstConfigPid_Type()
)
astConfigPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigPid.setStatus("current")
_AstConfigSocket_Type = DisplayString
_AstConfigSocket_Object = MibScalar
astConfigSocket = _AstConfigSocket_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 4),
    _AstConfigSocket_Type()
)
astConfigSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigSocket.setStatus("current")
_AstConfigCallsActive_Type = Gauge32
_AstConfigCallsActive_Object = MibScalar
astConfigCallsActive = _AstConfigCallsActive_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 5),
    _AstConfigCallsActive_Type()
)
astConfigCallsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigCallsActive.setStatus("current")
_AstConfigCallsProcessed_Type = Counter32
_AstConfigCallsProcessed_Object = MibScalar
astConfigCallsProcessed = _AstConfigCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 2, 6),
    _AstConfigCallsProcessed_Type()
)
astConfigCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astConfigCallsProcessed.setStatus("current")
_AsteriskModules_ObjectIdentity = ObjectIdentity
asteriskModules = _AsteriskModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 3)
)
_AstNumModules_Type = Integer32
_AstNumModules_Object = MibScalar
astNumModules = _AstNumModules_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 3, 1),
    _AstNumModules_Type()
)
astNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astNumModules.setStatus("current")
_AsteriskIndications_ObjectIdentity = ObjectIdentity
asteriskIndications = _AsteriskIndications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4)
)
_AstNumIndications_Type = Integer32
_AstNumIndications_Object = MibScalar
astNumIndications = _AstNumIndications_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 1),
    _AstNumIndications_Type()
)
astNumIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astNumIndications.setStatus("current")
_AstCurrentIndication_Type = DisplayString
_AstCurrentIndication_Object = MibScalar
astCurrentIndication = _AstCurrentIndication_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 2),
    _AstCurrentIndication_Type()
)
astCurrentIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astCurrentIndication.setStatus("current")
_AstIndicationsTable_Object = MibTable
astIndicationsTable = _AstIndicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3)
)
if mibBuilder.loadTexts:
    astIndicationsTable.setStatus("current")
_AstIndicationsEntry_Object = MibTableRow
astIndicationsEntry = _AstIndicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1)
)
astIndicationsEntry.setIndexNames(
    (0, "ASTERISK-MIB", "astIndIndex"),
)
if mibBuilder.loadTexts:
    astIndicationsEntry.setStatus("current")


class _AstIndIndex_Type(Integer32):
    """Custom type astIndIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AstIndIndex_Type.__name__ = "Integer32"
_AstIndIndex_Object = MibTableColumn
astIndIndex = _AstIndIndex_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 1),
    _AstIndIndex_Type()
)
astIndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astIndIndex.setStatus("current")
_AstIndCountry_Type = DisplayString
_AstIndCountry_Object = MibTableColumn
astIndCountry = _AstIndCountry_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 2),
    _AstIndCountry_Type()
)
astIndCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astIndCountry.setStatus("current")
_AstIndAlias_Type = DisplayString
_AstIndAlias_Object = MibTableColumn
astIndAlias = _AstIndAlias_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 3),
    _AstIndAlias_Type()
)
astIndAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astIndAlias.setStatus("current")
_AstIndDescription_Type = DisplayString
_AstIndDescription_Object = MibTableColumn
astIndDescription = _AstIndDescription_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 4),
    _AstIndDescription_Type()
)
astIndDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astIndDescription.setStatus("current")
_AsteriskChannels_ObjectIdentity = ObjectIdentity
asteriskChannels = _AsteriskChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5)
)
_AstNumChannels_Type = Gauge32
_AstNumChannels_Object = MibScalar
astNumChannels = _AstNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 1),
    _AstNumChannels_Type()
)
astNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astNumChannels.setStatus("current")
_AstChanTable_Object = MibTable
astChanTable = _AstChanTable_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2)
)
if mibBuilder.loadTexts:
    astChanTable.setStatus("current")
_AstChanEntry_Object = MibTableRow
astChanEntry = _AstChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1)
)
astChanEntry.setIndexNames(
    (0, "ASTERISK-MIB", "astChanIndex"),
)
if mibBuilder.loadTexts:
    astChanEntry.setStatus("current")


class _AstChanIndex_Type(Integer32):
    """Custom type astChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AstChanIndex_Type.__name__ = "Integer32"
_AstChanIndex_Object = MibTableColumn
astChanIndex = _AstChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 1),
    _AstChanIndex_Type()
)
astChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanIndex.setStatus("current")
_AstChanName_Type = DisplayString
_AstChanName_Object = MibTableColumn
astChanName = _AstChanName_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 2),
    _AstChanName_Type()
)
astChanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanName.setStatus("current")
_AstChanLanguage_Type = DisplayString
_AstChanLanguage_Object = MibTableColumn
astChanLanguage = _AstChanLanguage_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 3),
    _AstChanLanguage_Type()
)
astChanLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanLanguage.setStatus("current")
_AstChanType_Type = DisplayString
_AstChanType_Object = MibTableColumn
astChanType = _AstChanType_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 4),
    _AstChanType_Type()
)
astChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanType.setStatus("current")
_AstChanMusicClass_Type = DisplayString
_AstChanMusicClass_Object = MibTableColumn
astChanMusicClass = _AstChanMusicClass_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 5),
    _AstChanMusicClass_Type()
)
astChanMusicClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMusicClass.setStatus("current")
_AstChanBridge_Type = DisplayString
_AstChanBridge_Object = MibTableColumn
astChanBridge = _AstChanBridge_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 6),
    _AstChanBridge_Type()
)
astChanBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanBridge.setStatus("current")
_AstChanMasq_Type = DisplayString
_AstChanMasq_Object = MibTableColumn
astChanMasq = _AstChanMasq_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 7),
    _AstChanMasq_Type()
)
astChanMasq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMasq.setStatus("current")
_AstChanMasqr_Type = DisplayString
_AstChanMasqr_Object = MibTableColumn
astChanMasqr = _AstChanMasqr_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 8),
    _AstChanMasqr_Type()
)
astChanMasqr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMasqr.setStatus("current")
_AstChanWhenHangup_Type = TimeTicks
_AstChanWhenHangup_Object = MibTableColumn
astChanWhenHangup = _AstChanWhenHangup_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 9),
    _AstChanWhenHangup_Type()
)
astChanWhenHangup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanWhenHangup.setStatus("current")
_AstChanApp_Type = DisplayString
_AstChanApp_Object = MibTableColumn
astChanApp = _AstChanApp_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 10),
    _AstChanApp_Type()
)
astChanApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanApp.setStatus("current")
_AstChanData_Type = DisplayString
_AstChanData_Object = MibTableColumn
astChanData = _AstChanData_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 11),
    _AstChanData_Type()
)
astChanData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanData.setStatus("current")
_AstChanContext_Type = DisplayString
_AstChanContext_Object = MibTableColumn
astChanContext = _AstChanContext_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 12),
    _AstChanContext_Type()
)
astChanContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanContext.setStatus("current")
_AstChanMacroContext_Type = DisplayString
_AstChanMacroContext_Object = MibTableColumn
astChanMacroContext = _AstChanMacroContext_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 13),
    _AstChanMacroContext_Type()
)
astChanMacroContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMacroContext.setStatus("current")
_AstChanMacroExten_Type = DisplayString
_AstChanMacroExten_Object = MibTableColumn
astChanMacroExten = _AstChanMacroExten_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 14),
    _AstChanMacroExten_Type()
)
astChanMacroExten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMacroExten.setStatus("current")
_AstChanMacroPri_Type = Integer32
_AstChanMacroPri_Object = MibTableColumn
astChanMacroPri = _AstChanMacroPri_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 15),
    _AstChanMacroPri_Type()
)
astChanMacroPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMacroPri.setStatus("current")
_AstChanExten_Type = DisplayString
_AstChanExten_Object = MibTableColumn
astChanExten = _AstChanExten_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 16),
    _AstChanExten_Type()
)
astChanExten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanExten.setStatus("current")
_AstChanPri_Type = Integer32
_AstChanPri_Object = MibTableColumn
astChanPri = _AstChanPri_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 17),
    _AstChanPri_Type()
)
astChanPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanPri.setStatus("current")
_AstChanAccountCode_Type = DisplayString
_AstChanAccountCode_Object = MibTableColumn
astChanAccountCode = _AstChanAccountCode_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 18),
    _AstChanAccountCode_Type()
)
astChanAccountCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanAccountCode.setStatus("current")
_AstChanForwardTo_Type = DisplayString
_AstChanForwardTo_Object = MibTableColumn
astChanForwardTo = _AstChanForwardTo_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 19),
    _AstChanForwardTo_Type()
)
astChanForwardTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanForwardTo.setStatus("current")
_AstChanUniqueId_Type = DisplayString
_AstChanUniqueId_Object = MibTableColumn
astChanUniqueId = _AstChanUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 20),
    _AstChanUniqueId_Type()
)
astChanUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanUniqueId.setStatus("current")
_AstChanCallGroup_Type = Unsigned32
_AstChanCallGroup_Object = MibTableColumn
astChanCallGroup = _AstChanCallGroup_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 21),
    _AstChanCallGroup_Type()
)
astChanCallGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCallGroup.setStatus("current")
_AstChanPickupGroup_Type = Unsigned32
_AstChanPickupGroup_Object = MibTableColumn
astChanPickupGroup = _AstChanPickupGroup_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 22),
    _AstChanPickupGroup_Type()
)
astChanPickupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanPickupGroup.setStatus("current")


class _AstChanState_Type(Integer32):
    """Custom type astChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("stateBusy", 7),
          ("stateDialing", 3),
          ("stateDialingOffHook", 8),
          ("stateDown", 0),
          ("stateOffHook", 2),
          ("statePreRing", 9),
          ("stateReserved", 1),
          ("stateRing", 4),
          ("stateRinging", 5),
          ("stateUp", 6))
    )


_AstChanState_Type.__name__ = "Integer32"
_AstChanState_Object = MibTableColumn
astChanState = _AstChanState_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 23),
    _AstChanState_Type()
)
astChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanState.setStatus("current")
_AstChanMuted_Type = TruthValue
_AstChanMuted_Object = MibTableColumn
astChanMuted = _AstChanMuted_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 24),
    _AstChanMuted_Type()
)
astChanMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanMuted.setStatus("current")
_AstChanRings_Type = Integer32
_AstChanRings_Object = MibTableColumn
astChanRings = _AstChanRings_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 25),
    _AstChanRings_Type()
)
astChanRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanRings.setStatus("current")
_AstChanCidDNID_Type = DisplayString
_AstChanCidDNID_Object = MibTableColumn
astChanCidDNID = _AstChanCidDNID_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 26),
    _AstChanCidDNID_Type()
)
astChanCidDNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidDNID.setStatus("current")
_AstChanCidNum_Type = DisplayString
_AstChanCidNum_Object = MibTableColumn
astChanCidNum = _AstChanCidNum_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 27),
    _AstChanCidNum_Type()
)
astChanCidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidNum.setStatus("current")
_AstChanCidName_Type = DisplayString
_AstChanCidName_Object = MibTableColumn
astChanCidName = _AstChanCidName_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 28),
    _AstChanCidName_Type()
)
astChanCidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidName.setStatus("current")
_AstChanCidANI_Type = DisplayString
_AstChanCidANI_Object = MibTableColumn
astChanCidANI = _AstChanCidANI_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 29),
    _AstChanCidANI_Type()
)
astChanCidANI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidANI.setStatus("current")
_AstChanCidRDNIS_Type = DisplayString
_AstChanCidRDNIS_Object = MibTableColumn
astChanCidRDNIS = _AstChanCidRDNIS_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 30),
    _AstChanCidRDNIS_Type()
)
astChanCidRDNIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidRDNIS.setStatus("current")
_AstChanCidPresentation_Type = DisplayString
_AstChanCidPresentation_Object = MibTableColumn
astChanCidPresentation = _AstChanCidPresentation_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 31),
    _AstChanCidPresentation_Type()
)
astChanCidPresentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidPresentation.setStatus("current")
_AstChanCidANI2_Type = Integer32
_AstChanCidANI2_Object = MibTableColumn
astChanCidANI2 = _AstChanCidANI2_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 32),
    _AstChanCidANI2_Type()
)
astChanCidANI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidANI2.setStatus("current")
_AstChanCidTON_Type = Integer32
_AstChanCidTON_Object = MibTableColumn
astChanCidTON = _AstChanCidTON_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 33),
    _AstChanCidTON_Type()
)
astChanCidTON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidTON.setStatus("current")
_AstChanCidTNS_Type = Integer32
_AstChanCidTNS_Object = MibTableColumn
astChanCidTNS = _AstChanCidTNS_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 34),
    _AstChanCidTNS_Type()
)
astChanCidTNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanCidTNS.setStatus("current")


class _AstChanAMAFlags_Type(Integer32):
    """Custom type astChanAMAFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("billing", 2),
          ("default", 0),
          ("documentation", 3),
          ("omit", 1))
    )


_AstChanAMAFlags_Type.__name__ = "Integer32"
_AstChanAMAFlags_Object = MibTableColumn
astChanAMAFlags = _AstChanAMAFlags_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 35),
    _AstChanAMAFlags_Type()
)
astChanAMAFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanAMAFlags.setStatus("current")


class _AstChanADSI_Type(Integer32):
    """Custom type astChanADSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("offHookOnly", 3),
          ("unavailable", 2),
          ("unknown", 0))
    )


_AstChanADSI_Type.__name__ = "Integer32"
_AstChanADSI_Object = MibTableColumn
astChanADSI = _AstChanADSI_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 36),
    _AstChanADSI_Type()
)
astChanADSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanADSI.setStatus("current")
_AstChanToneZone_Type = DisplayString
_AstChanToneZone_Object = MibTableColumn
astChanToneZone = _AstChanToneZone_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 37),
    _AstChanToneZone_Type()
)
astChanToneZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanToneZone.setStatus("current")


class _AstChanHangupCause_Type(Integer32):
    """Custom type astChanHangupCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              16,
              17,
              19,
              34,
              38,
              66)
        )
    )
    namedValues = NamedValues(
        *(("busy", 17),
          ("congestion", 34),
          ("failure", 38),
          ("noAnswer", 19),
          ("noSuchDriver", 66),
          ("normal", 16),
          ("notDefined", 0),
          ("unregistered", 3))
    )


_AstChanHangupCause_Type.__name__ = "Integer32"
_AstChanHangupCause_Object = MibTableColumn
astChanHangupCause = _AstChanHangupCause_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 38),
    _AstChanHangupCause_Type()
)
astChanHangupCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanHangupCause.setStatus("current")
_AstChanVariables_Type = DisplayString
_AstChanVariables_Object = MibTableColumn
astChanVariables = _AstChanVariables_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 39),
    _AstChanVariables_Type()
)
astChanVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanVariables.setStatus("current")


class _AstChanFlags_Type(Bits):
    """Custom type astChanFlags based on Bits"""
    namedValues = NamedValues(
        *(("autoIncrementingLoop", 9),
          ("blocking", 3),
          ("deferDTMF", 1),
          ("exception", 5),
          ("musicOnHold", 6),
          ("nativeBridge", 8),
          ("spying", 7),
          ("wantsJitter", 0),
          ("writeInterrupt", 2),
          ("zombie", 4))
    )

_AstChanFlags_Type.__name__ = "Bits"
_AstChanFlags_Object = MibTableColumn
astChanFlags = _AstChanFlags_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 40),
    _AstChanFlags_Type()
)
astChanFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanFlags.setStatus("current")


class _AstChanTransferCap_Type(Integer32):
    """Custom type astChanTransferCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              9,
              16,
              17,
              24)
        )
    )
    namedValues = NamedValues(
        *(("audio3k", 16),
          ("digital", 8),
          ("digitalWithTones", 17),
          ("restrictedDigital", 9),
          ("speech", 0),
          ("video", 24))
    )


_AstChanTransferCap_Type.__name__ = "Integer32"
_AstChanTransferCap_Object = MibTableColumn
astChanTransferCap = _AstChanTransferCap_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 41),
    _AstChanTransferCap_Type()
)
astChanTransferCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTransferCap.setStatus("current")
_AstNumChanTypes_Type = Integer32
_AstNumChanTypes_Object = MibScalar
astNumChanTypes = _AstNumChanTypes_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 3),
    _AstNumChanTypes_Type()
)
astNumChanTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astNumChanTypes.setStatus("current")
_AstChanTypeTable_Object = MibTable
astChanTypeTable = _AstChanTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4)
)
if mibBuilder.loadTexts:
    astChanTypeTable.setStatus("current")
_AstChanTypeEntry_Object = MibTableRow
astChanTypeEntry = _AstChanTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1)
)
astChanTypeEntry.setIndexNames(
    (0, "ASTERISK-MIB", "astChanTypeIndex"),
)
if mibBuilder.loadTexts:
    astChanTypeEntry.setStatus("current")


class _AstChanTypeIndex_Type(Integer32):
    """Custom type astChanTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AstChanTypeIndex_Type.__name__ = "Integer32"
_AstChanTypeIndex_Object = MibTableColumn
astChanTypeIndex = _AstChanTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 1),
    _AstChanTypeIndex_Type()
)
astChanTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeIndex.setStatus("current")
_AstChanTypeName_Type = DisplayString
_AstChanTypeName_Object = MibTableColumn
astChanTypeName = _AstChanTypeName_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 2),
    _AstChanTypeName_Type()
)
astChanTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeName.setStatus("current")
_AstChanTypeDesc_Type = DisplayString
_AstChanTypeDesc_Object = MibTableColumn
astChanTypeDesc = _AstChanTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 3),
    _AstChanTypeDesc_Type()
)
astChanTypeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeDesc.setStatus("current")
_AstChanTypeDeviceState_Type = TruthValue
_AstChanTypeDeviceState_Object = MibTableColumn
astChanTypeDeviceState = _AstChanTypeDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 4),
    _AstChanTypeDeviceState_Type()
)
astChanTypeDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeDeviceState.setStatus("current")
_AstChanTypeIndications_Type = TruthValue
_AstChanTypeIndications_Object = MibTableColumn
astChanTypeIndications = _AstChanTypeIndications_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 5),
    _AstChanTypeIndications_Type()
)
astChanTypeIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeIndications.setStatus("current")
_AstChanTypeTransfer_Type = TruthValue
_AstChanTypeTransfer_Object = MibTableColumn
astChanTypeTransfer = _AstChanTypeTransfer_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 6),
    _AstChanTypeTransfer_Type()
)
astChanTypeTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeTransfer.setStatus("current")
_AstChanTypeChannels_Type = Gauge32
_AstChanTypeChannels_Object = MibTableColumn
astChanTypeChannels = _AstChanTypeChannels_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 7),
    _AstChanTypeChannels_Type()
)
astChanTypeChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astChanTypeChannels.setStatus("current")
_AstChanScalars_ObjectIdentity = ObjectIdentity
astChanScalars = _AstChanScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 5)
)
_AstNumChanBridge_Type = Gauge32
_AstNumChanBridge_Object = MibScalar
astNumChanBridge = _AstNumChanBridge_Object(
    (1, 3, 6, 1, 4, 1, 22736, 1, 5, 5, 1),
    _AstNumChanBridge_Type()
)
astNumChanBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    astNumChanBridge.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASTERISK-MIB",
    **{"asterisk": asterisk,
       "asteriskVersion": asteriskVersion,
       "astVersionString": astVersionString,
       "astVersionTag": astVersionTag,
       "asteriskConfiguration": asteriskConfiguration,
       "astConfigUpTime": astConfigUpTime,
       "astConfigReloadTime": astConfigReloadTime,
       "astConfigPid": astConfigPid,
       "astConfigSocket": astConfigSocket,
       "astConfigCallsActive": astConfigCallsActive,
       "astConfigCallsProcessed": astConfigCallsProcessed,
       "asteriskModules": asteriskModules,
       "astNumModules": astNumModules,
       "asteriskIndications": asteriskIndications,
       "astNumIndications": astNumIndications,
       "astCurrentIndication": astCurrentIndication,
       "astIndicationsTable": astIndicationsTable,
       "astIndicationsEntry": astIndicationsEntry,
       "astIndIndex": astIndIndex,
       "astIndCountry": astIndCountry,
       "astIndAlias": astIndAlias,
       "astIndDescription": astIndDescription,
       "asteriskChannels": asteriskChannels,
       "astNumChannels": astNumChannels,
       "astChanTable": astChanTable,
       "astChanEntry": astChanEntry,
       "astChanIndex": astChanIndex,
       "astChanName": astChanName,
       "astChanLanguage": astChanLanguage,
       "astChanType": astChanType,
       "astChanMusicClass": astChanMusicClass,
       "astChanBridge": astChanBridge,
       "astChanMasq": astChanMasq,
       "astChanMasqr": astChanMasqr,
       "astChanWhenHangup": astChanWhenHangup,
       "astChanApp": astChanApp,
       "astChanData": astChanData,
       "astChanContext": astChanContext,
       "astChanMacroContext": astChanMacroContext,
       "astChanMacroExten": astChanMacroExten,
       "astChanMacroPri": astChanMacroPri,
       "astChanExten": astChanExten,
       "astChanPri": astChanPri,
       "astChanAccountCode": astChanAccountCode,
       "astChanForwardTo": astChanForwardTo,
       "astChanUniqueId": astChanUniqueId,
       "astChanCallGroup": astChanCallGroup,
       "astChanPickupGroup": astChanPickupGroup,
       "astChanState": astChanState,
       "astChanMuted": astChanMuted,
       "astChanRings": astChanRings,
       "astChanCidDNID": astChanCidDNID,
       "astChanCidNum": astChanCidNum,
       "astChanCidName": astChanCidName,
       "astChanCidANI": astChanCidANI,
       "astChanCidRDNIS": astChanCidRDNIS,
       "astChanCidPresentation": astChanCidPresentation,
       "astChanCidANI2": astChanCidANI2,
       "astChanCidTON": astChanCidTON,
       "astChanCidTNS": astChanCidTNS,
       "astChanAMAFlags": astChanAMAFlags,
       "astChanADSI": astChanADSI,
       "astChanToneZone": astChanToneZone,
       "astChanHangupCause": astChanHangupCause,
       "astChanVariables": astChanVariables,
       "astChanFlags": astChanFlags,
       "astChanTransferCap": astChanTransferCap,
       "astNumChanTypes": astNumChanTypes,
       "astChanTypeTable": astChanTypeTable,
       "astChanTypeEntry": astChanTypeEntry,
       "astChanTypeIndex": astChanTypeIndex,
       "astChanTypeName": astChanTypeName,
       "astChanTypeDesc": astChanTypeDesc,
       "astChanTypeDeviceState": astChanTypeDeviceState,
       "astChanTypeIndications": astChanTypeIndications,
       "astChanTypeTransfer": astChanTypeTransfer,
       "astChanTypeChannels": astChanTypeChannels,
       "astChanScalars": astChanScalars,
       "astNumChanBridge": astNumChanBridge}
)
