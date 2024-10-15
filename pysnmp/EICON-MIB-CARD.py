# SNMP MIB module (EICON-MIB-CARD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-CARD
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:44 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
    "NotificationType",
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



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("other", 1),
          ("ready", 3))
    )





class CardAdminState(Integer32):
    """Custom type CardAdminState based on Integer32"""
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
        *(("dump", 3),
          ("invalid", 5),
          ("reset", 6),
          ("start", 1),
          ("stop", 2),
          ("test", 4))
    )





class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class EiconCardType(Integer32):
    """Custom type EiconCardType based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("ect-MC-EC", 11),
          ("ect-MC-EC1M", 21),
          ("ect-MC-HSI", 12),
          ("ect-MC-HSI1M", 18),
          ("ect-MC-IMC", 14),
          ("ect-MC-ISDN", 33),
          ("ect-MC-MPNA", 16),
          ("ect-MC-MPNA2M", 30),
          ("ect-MC-SPCC", 5),
          ("ect-MC-SPCC2", 31),
          ("ect-NB-EC", 25),
          ("ect-NB-EC1M", 22),
          ("ect-NB-HSI1M", 19),
          ("ect-NB-IMC", 23),
          ("ect-NB-SPCC", 24),
          ("ect-NONE", 1),
          ("ect-PC-ACC8", 26),
          ("ect-PC-DNA", 3),
          ("ect-PC-DPNA", 6),
          ("ect-PC-DPNA2M", 28),
          ("ect-PC-EC", 7),
          ("ect-PC-EC1M", 20),
          ("ect-PC-ECHSI", 8),
          ("ect-PC-HSI1M", 17),
          ("ect-PC-HSI2", 35),
          ("ect-PC-IMC", 15),
          ("ect-PC-ISDN", 27),
          ("ect-PC-MPNA", 10),
          ("ect-PC-MPNA2M", 29),
          ("ect-PC-NA", 2),
          ("ect-PC-QPNA", 9),
          ("ect-PC-S51", 36),
          ("ect-PC-S52", 37),
          ("ect-PC-SPNA", 4),
          ("ect-PP-EC", 34),
          ("ect-PP-IMC", 32),
          ("ect-XX-DIGI", 13))
    )





class CardRef(Integer32):
    """Custom type CardRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2)
)
_CardNumberOfCards_Type = PositiveInteger
_CardNumberOfCards_Object = MibScalar
cardNumberOfCards = _CardNumberOfCards_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 1),
    _CardNumberOfCards_Type()
)
cardNumberOfCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNumberOfCards.setStatus("mandatory")
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1)
)
cardEntry.setIndexNames(
    (0, "EICON-MIB-CARD", "cardIndex"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("mandatory")
_CardIndex_Type = CardRef
_CardIndex_Object = MibTableColumn
cardIndex = _CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 1),
    _CardIndex_Type()
)
cardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndex.setStatus("mandatory")


class _CardName_Type(DisplayString):
    """Custom type cardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardName_Type.__name__ = "DisplayString"
_CardName_Object = MibTableColumn
cardName = _CardName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 2),
    _CardName_Type()
)
cardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardName.setStatus("mandatory")
_CardType_Type = EiconCardType
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 3),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("mandatory")
_CardOperState_Type = OperState
_CardOperState_Object = MibTableColumn
cardOperState = _CardOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 4),
    _CardOperState_Type()
)
cardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperState.setStatus("mandatory")
_CardAdminStateCtr_Type = CardAdminState
_CardAdminStateCtr_Object = MibTableColumn
cardAdminStateCtr = _CardAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 5),
    _CardAdminStateCtr_Type()
)
cardAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminStateCtr.setStatus("mandatory")


class _CardDomainConfigDirName_Type(DisplayString):
    """Custom type cardDomainConfigDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CardDomainConfigDirName_Type.__name__ = "DisplayString"
_CardDomainConfigDirName_Object = MibTableColumn
cardDomainConfigDirName = _CardDomainConfigDirName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 6),
    _CardDomainConfigDirName_Type()
)
cardDomainConfigDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDomainConfigDirName.setStatus("mandatory")
_CardLoadTime_Type = TimeTicks
_CardLoadTime_Object = MibTableColumn
cardLoadTime = _CardLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 7),
    _CardLoadTime_Type()
)
cardLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLoadTime.setStatus("mandatory")
_CardActionState_Type = ActionState
_CardActionState_Object = MibTableColumn
cardActionState = _CardActionState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 8),
    _CardActionState_Type()
)
cardActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardActionState.setStatus("mandatory")
_CardActionError_Type = Integer32
_CardActionError_Object = MibTableColumn
cardActionError = _CardActionError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 9),
    _CardActionError_Type()
)
cardActionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardActionError.setStatus("mandatory")


class _CardActionOutputFile_Type(DisplayString):
    """Custom type cardActionOutputFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CardActionOutputFile_Type.__name__ = "DisplayString"
_CardActionOutputFile_Object = MibTableColumn
cardActionOutputFile = _CardActionOutputFile_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 10),
    _CardActionOutputFile_Type()
)
cardActionOutputFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardActionOutputFile.setStatus("mandatory")
_CardProtocols_Type = Integer32
_CardProtocols_Object = MibTableColumn
cardProtocols = _CardProtocols_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 11),
    _CardProtocols_Type()
)
cardProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProtocols.setStatus("mandatory")
_CardHardwareTable_Object = MibTable
cardHardwareTable = _CardHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cardHardwareTable.setStatus("mandatory")
_CardHardwareEntry_Object = MibTableRow
cardHardwareEntry = _CardHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1)
)
cardHardwareEntry.setIndexNames(
    (0, "EICON-MIB-CARD", "cardHardCardRef"),
)
if mibBuilder.loadTexts:
    cardHardwareEntry.setStatus("mandatory")
_CardHardCardRef_Type = CardRef
_CardHardCardRef_Object = MibTableColumn
cardHardCardRef = _CardHardCardRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 1),
    _CardHardCardRef_Type()
)
cardHardCardRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardCardRef.setStatus("mandatory")
_CardHardMemAddr_Type = Integer32
_CardHardMemAddr_Object = MibTableColumn
cardHardMemAddr = _CardHardMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 2),
    _CardHardMemAddr_Type()
)
cardHardMemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardMemAddr.setStatus("mandatory")


class _CardHardIoAddr_Type(Integer32):
    """Custom type cardHardIoAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CardHardIoAddr_Type.__name__ = "Integer32"
_CardHardIoAddr_Object = MibTableColumn
cardHardIoAddr = _CardHardIoAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 3),
    _CardHardIoAddr_Type()
)
cardHardIoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardIoAddr.setStatus("mandatory")


class _CardHardIntrLevel_Type(Integer32):
    """Custom type cardHardIntrLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CardHardIntrLevel_Type.__name__ = "Integer32"
_CardHardIntrLevel_Object = MibTableColumn
cardHardIntrLevel = _CardHardIntrLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 4),
    _CardHardIntrLevel_Type()
)
cardHardIntrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardIntrLevel.setStatus("mandatory")
_CardHardNbOfPorts_Type = PortRef
_CardHardNbOfPorts_Object = MibTableColumn
cardHardNbOfPorts = _CardHardNbOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 5),
    _CardHardNbOfPorts_Type()
)
cardHardNbOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardNbOfPorts.setStatus("mandatory")


class _CardHardSlotNumber_Type(Integer32):
    """Custom type cardHardSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CardHardSlotNumber_Type.__name__ = "Integer32"
_CardHardSlotNumber_Object = MibTableColumn
cardHardSlotNumber = _CardHardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 6),
    _CardHardSlotNumber_Type()
)
cardHardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardSlotNumber.setStatus("mandatory")


class _CardHardVersion_Type(DisplayString):
    """Custom type cardHardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardHardVersion_Type.__name__ = "DisplayString"
_CardHardVersion_Object = MibTableColumn
cardHardVersion = _CardHardVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 7),
    _CardHardVersion_Type()
)
cardHardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardVersion.setStatus("mandatory")
_CardHardSerialNb_Type = PositiveInteger
_CardHardSerialNb_Object = MibTableColumn
cardHardSerialNb = _CardHardSerialNb_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 8),
    _CardHardSerialNb_Type()
)
cardHardSerialNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardSerialNb.setStatus("mandatory")


class _CardHardComponents_Type(DisplayString):
    """Custom type cardHardComponents based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardHardComponents_Type.__name__ = "DisplayString"
_CardHardComponents_Object = MibTableColumn
cardHardComponents = _CardHardComponents_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 9),
    _CardHardComponents_Type()
)
cardHardComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHardComponents.setStatus("mandatory")
_CardSoftwareTable_Object = MibTable
cardSoftwareTable = _CardSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cardSoftwareTable.setStatus("mandatory")
_CardSoftwareEntry_Object = MibTableRow
cardSoftwareEntry = _CardSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1)
)
cardSoftwareEntry.setIndexNames(
    (0, "EICON-MIB-CARD", "cardSoftCardRef"),
    (0, "EICON-MIB-CARD", "cardSoftModuleIndex"),
)
if mibBuilder.loadTexts:
    cardSoftwareEntry.setStatus("mandatory")
_CardSoftCardRef_Type = CardRef
_CardSoftCardRef_Object = MibTableColumn
cardSoftCardRef = _CardSoftCardRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 1),
    _CardSoftCardRef_Type()
)
cardSoftCardRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftCardRef.setStatus("mandatory")
_CardSoftModuleIndex_Type = PositiveInteger
_CardSoftModuleIndex_Object = MibTableColumn
cardSoftModuleIndex = _CardSoftModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 2),
    _CardSoftModuleIndex_Type()
)
cardSoftModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftModuleIndex.setStatus("mandatory")


class _CardSoftModuleName_Type(DisplayString):
    """Custom type cardSoftModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardSoftModuleName_Type.__name__ = "DisplayString"
_CardSoftModuleName_Object = MibTableColumn
cardSoftModuleName = _CardSoftModuleName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 3),
    _CardSoftModuleName_Type()
)
cardSoftModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftModuleName.setStatus("mandatory")


class _CardSoftVersion_Type(DisplayString):
    """Custom type cardSoftVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardSoftVersion_Type.__name__ = "DisplayString"
_CardSoftVersion_Object = MibTableColumn
cardSoftVersion = _CardSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 4),
    _CardSoftVersion_Type()
)
cardSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftVersion.setStatus("mandatory")


class _CardSoftDateProd_Type(DisplayString):
    """Custom type cardSoftDateProd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardSoftDateProd_Type.__name__ = "DisplayString"
_CardSoftDateProd_Object = MibTableColumn
cardSoftDateProd = _CardSoftDateProd_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 5),
    _CardSoftDateProd_Type()
)
cardSoftDateProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftDateProd.setStatus("mandatory")
_CardSoftRealSize_Type = PositiveInteger
_CardSoftRealSize_Object = MibTableColumn
cardSoftRealSize = _CardSoftRealSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 6),
    _CardSoftRealSize_Type()
)
cardSoftRealSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSoftRealSize.setStatus("mandatory")
_CardBiosSessionTable_Object = MibTable
cardBiosSessionTable = _CardBiosSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cardBiosSessionTable.setStatus("mandatory")
_CardBiosSessionEntry_Object = MibTableRow
cardBiosSessionEntry = _CardBiosSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1)
)
cardBiosSessionEntry.setIndexNames(
    (0, "EICON-MIB-CARD", "cardBiosSsnCardRef"),
    (0, "EICON-MIB-CARD", "cardBiosSsnIndex"),
)
if mibBuilder.loadTexts:
    cardBiosSessionEntry.setStatus("mandatory")
_CardBiosSsnCardRef_Type = CardRef
_CardBiosSsnCardRef_Object = MibTableColumn
cardBiosSsnCardRef = _CardBiosSsnCardRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 1),
    _CardBiosSsnCardRef_Type()
)
cardBiosSsnCardRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnCardRef.setStatus("mandatory")
_CardBiosSsnIndex_Type = PositiveInteger
_CardBiosSsnIndex_Object = MibTableColumn
cardBiosSsnIndex = _CardBiosSsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 2),
    _CardBiosSsnIndex_Type()
)
cardBiosSsnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnIndex.setStatus("mandatory")
_CardBiosSsnLsn_Type = PositiveInteger
_CardBiosSsnLsn_Object = MibTableColumn
cardBiosSsnLsn = _CardBiosSsnLsn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 3),
    _CardBiosSsnLsn_Type()
)
cardBiosSsnLsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnLsn.setStatus("mandatory")
_CardBiosSsnPortRef_Type = PortRef
_CardBiosSsnPortRef_Object = MibTableColumn
cardBiosSsnPortRef = _CardBiosSsnPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 4),
    _CardBiosSsnPortRef_Type()
)
cardBiosSsnPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnPortRef.setStatus("mandatory")


class _CardBiosSsnOperState_Type(Integer32):
    """Custom type cardBiosSsnOperState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 7),
          ("calling", 3),
          ("connected", 4),
          ("hangingup", 5),
          ("hungup", 6),
          ("listening", 2),
          ("other", 1),
          ("wait-for-user", 8))
    )


_CardBiosSsnOperState_Type.__name__ = "Integer32"
_CardBiosSsnOperState_Object = MibTableColumn
cardBiosSsnOperState = _CardBiosSsnOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 5),
    _CardBiosSsnOperState_Type()
)
cardBiosSsnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnOperState.setStatus("mandatory")


class _CardBiosSsnProtocol_Type(Integer32):
    """Custom type cardBiosSsnProtocol based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("appc", 5),
          ("conmgr", 14),
          ("dialer", 7),
          ("dlc", 6),
          ("frbs", 13),
          ("hdlc", 12),
          ("other", 1),
          ("remoteec", 15),
          ("sdlc", 2),
          ("snafm", 4),
          ("snapc", 3),
          ("sndcf", 10),
          ("x25", 11),
          ("xportiso", 8),
          ("xporttgx", 9))
    )


_CardBiosSsnProtocol_Type.__name__ = "Integer32"
_CardBiosSsnProtocol_Object = MibTableColumn
cardBiosSsnProtocol = _CardBiosSsnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 6),
    _CardBiosSsnProtocol_Type()
)
cardBiosSsnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnProtocol.setStatus("mandatory")


class _CardBiosSsnApplName_Type(DisplayString):
    """Custom type cardBiosSsnApplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardBiosSsnApplName_Type.__name__ = "DisplayString"
_CardBiosSsnApplName_Object = MibTableColumn
cardBiosSsnApplName = _CardBiosSsnApplName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 7),
    _CardBiosSsnApplName_Type()
)
cardBiosSsnApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnApplName.setStatus("mandatory")
_CardBiosSsnStartTime_Type = TimeTicks
_CardBiosSsnStartTime_Object = MibTableColumn
cardBiosSsnStartTime = _CardBiosSsnStartTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 8),
    _CardBiosSsnStartTime_Type()
)
cardBiosSsnStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBiosSsnStartTime.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)

# Managed Objects groups


# Notification objects

cardTrapHeartbeatLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 21)
)
cardTrapHeartbeatLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("EICON-MIB-CARD", "cardIndex"))
)
if mibBuilder.loadTexts:
    cardTrapHeartbeatLost.setStatus(
        ""
    )

cardTrapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 22)
)
cardTrapStateChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("EICON-MIB-CARD", "cardIndex"),
        ("EICON-MIB-CARD", "cardOperState"))
)
if mibBuilder.loadTexts:
    cardTrapStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-CARD",
    **{"OperState": OperState,
       "CardAdminState": CardAdminState,
       "ActionState": ActionState,
       "EiconCardType": EiconCardType,
       "CardRef": CardRef,
       "PortRef": PortRef,
       "PositiveInteger": PositiveInteger,
       "eicon": eicon,
       "cardTrapHeartbeatLost": cardTrapHeartbeatLost,
       "cardTrapStateChange": cardTrapStateChange,
       "management": management,
       "mibv2": mibv2,
       "card": card,
       "cardNumberOfCards": cardNumberOfCards,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardIndex": cardIndex,
       "cardName": cardName,
       "cardType": cardType,
       "cardOperState": cardOperState,
       "cardAdminStateCtr": cardAdminStateCtr,
       "cardDomainConfigDirName": cardDomainConfigDirName,
       "cardLoadTime": cardLoadTime,
       "cardActionState": cardActionState,
       "cardActionError": cardActionError,
       "cardActionOutputFile": cardActionOutputFile,
       "cardProtocols": cardProtocols,
       "cardHardwareTable": cardHardwareTable,
       "cardHardwareEntry": cardHardwareEntry,
       "cardHardCardRef": cardHardCardRef,
       "cardHardMemAddr": cardHardMemAddr,
       "cardHardIoAddr": cardHardIoAddr,
       "cardHardIntrLevel": cardHardIntrLevel,
       "cardHardNbOfPorts": cardHardNbOfPorts,
       "cardHardSlotNumber": cardHardSlotNumber,
       "cardHardVersion": cardHardVersion,
       "cardHardSerialNb": cardHardSerialNb,
       "cardHardComponents": cardHardComponents,
       "cardSoftwareTable": cardSoftwareTable,
       "cardSoftwareEntry": cardSoftwareEntry,
       "cardSoftCardRef": cardSoftCardRef,
       "cardSoftModuleIndex": cardSoftModuleIndex,
       "cardSoftModuleName": cardSoftModuleName,
       "cardSoftVersion": cardSoftVersion,
       "cardSoftDateProd": cardSoftDateProd,
       "cardSoftRealSize": cardSoftRealSize,
       "cardBiosSessionTable": cardBiosSessionTable,
       "cardBiosSessionEntry": cardBiosSessionEntry,
       "cardBiosSsnCardRef": cardBiosSsnCardRef,
       "cardBiosSsnIndex": cardBiosSsnIndex,
       "cardBiosSsnLsn": cardBiosSsnLsn,
       "cardBiosSsnPortRef": cardBiosSsnPortRef,
       "cardBiosSsnOperState": cardBiosSsnOperState,
       "cardBiosSsnProtocol": cardBiosSsnProtocol,
       "cardBiosSsnApplName": cardBiosSsnApplName,
       "cardBiosSsnStartTime": cardBiosSsnStartTime,
       "module": module}
)
