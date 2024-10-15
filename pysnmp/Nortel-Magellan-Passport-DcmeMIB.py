# SNMP MIB module (Nortel-Magellan-Passport-DcmeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DcmeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:33 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 EnterpriseDateAndTime,
 FixedPoint1,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "FixedPoint1",
    "Hex",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dcme_ObjectIdentity = ObjectIdentity
dcme = _Dcme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129)
)
_DcmeRowStatusTable_Object = MibTable
dcmeRowStatusTable = _DcmeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1)
)
if mibBuilder.loadTexts:
    dcmeRowStatusTable.setStatus("mandatory")
_DcmeRowStatusEntry_Object = MibTableRow
dcmeRowStatusEntry = _DcmeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1, 1)
)
dcmeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
)
if mibBuilder.loadTexts:
    dcmeRowStatusEntry.setStatus("mandatory")
_DcmeRowStatus_Type = RowStatus
_DcmeRowStatus_Object = MibTableColumn
dcmeRowStatus = _DcmeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1, 1, 1),
    _DcmeRowStatus_Type()
)
dcmeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeRowStatus.setStatus("mandatory")
_DcmeComponentName_Type = DisplayString
_DcmeComponentName_Object = MibTableColumn
dcmeComponentName = _DcmeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1, 1, 2),
    _DcmeComponentName_Type()
)
dcmeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeComponentName.setStatus("mandatory")
_DcmeStorageType_Type = StorageType
_DcmeStorageType_Object = MibTableColumn
dcmeStorageType = _DcmeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1, 1, 4),
    _DcmeStorageType_Type()
)
dcmeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeStorageType.setStatus("mandatory")


class _DcmeIndex_Type(Integer32):
    """Custom type dcmeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcmeIndex_Type.__name__ = "Integer32"
_DcmeIndex_Object = MibTableColumn
dcmeIndex = _DcmeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 1, 1, 10),
    _DcmeIndex_Type()
)
dcmeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcmeIndex.setStatus("mandatory")
_DcmeProfile_ObjectIdentity = ObjectIdentity
dcmeProfile = _DcmeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2)
)
_DcmeProfileRowStatusTable_Object = MibTable
dcmeProfileRowStatusTable = _DcmeProfileRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1)
)
if mibBuilder.loadTexts:
    dcmeProfileRowStatusTable.setStatus("mandatory")
_DcmeProfileRowStatusEntry_Object = MibTableRow
dcmeProfileRowStatusEntry = _DcmeProfileRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1, 1)
)
dcmeProfileRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    dcmeProfileRowStatusEntry.setStatus("mandatory")
_DcmeProfileRowStatus_Type = RowStatus
_DcmeProfileRowStatus_Object = MibTableColumn
dcmeProfileRowStatus = _DcmeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1, 1, 1),
    _DcmeProfileRowStatus_Type()
)
dcmeProfileRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeProfileRowStatus.setStatus("mandatory")
_DcmeProfileComponentName_Type = DisplayString
_DcmeProfileComponentName_Object = MibTableColumn
dcmeProfileComponentName = _DcmeProfileComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1, 1, 2),
    _DcmeProfileComponentName_Type()
)
dcmeProfileComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeProfileComponentName.setStatus("mandatory")
_DcmeProfileStorageType_Type = StorageType
_DcmeProfileStorageType_Object = MibTableColumn
dcmeProfileStorageType = _DcmeProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1, 1, 4),
    _DcmeProfileStorageType_Type()
)
dcmeProfileStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeProfileStorageType.setStatus("mandatory")
_DcmeProfileIndex_Type = NonReplicated
_DcmeProfileIndex_Object = MibTableColumn
dcmeProfileIndex = _DcmeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 1, 1, 10),
    _DcmeProfileIndex_Type()
)
dcmeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcmeProfileIndex.setStatus("mandatory")
_DcmeProfileLCOpsTable_Object = MibTable
dcmeProfileLCOpsTable = _DcmeProfileLCOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10)
)
if mibBuilder.loadTexts:
    dcmeProfileLCOpsTable.setStatus("mandatory")
_DcmeProfileLCOpsEntry_Object = MibTableRow
dcmeProfileLCOpsEntry = _DcmeProfileLCOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1)
)
dcmeProfileLCOpsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    dcmeProfileLCOpsEntry.setStatus("mandatory")


class _DcmeProfileSetupPriority_Type(Unsigned32):
    """Custom type dcmeProfileSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DcmeProfileSetupPriority_Type.__name__ = "Unsigned32"
_DcmeProfileSetupPriority_Object = MibTableColumn
dcmeProfileSetupPriority = _DcmeProfileSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 1),
    _DcmeProfileSetupPriority_Type()
)
dcmeProfileSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileSetupPriority.setStatus("mandatory")


class _DcmeProfileHoldingPriority_Type(Unsigned32):
    """Custom type dcmeProfileHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DcmeProfileHoldingPriority_Type.__name__ = "Unsigned32"
_DcmeProfileHoldingPriority_Object = MibTableColumn
dcmeProfileHoldingPriority = _DcmeProfileHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 2),
    _DcmeProfileHoldingPriority_Type()
)
dcmeProfileHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileHoldingPriority.setStatus("mandatory")


class _DcmeProfileBumpPreference_Type(Integer32):
    """Custom type dcmeProfileBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_DcmeProfileBumpPreference_Type.__name__ = "Integer32"
_DcmeProfileBumpPreference_Object = MibTableColumn
dcmeProfileBumpPreference = _DcmeProfileBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 3),
    _DcmeProfileBumpPreference_Type()
)
dcmeProfileBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileBumpPreference.setStatus("mandatory")


class _DcmeProfileRequiredTrafficType_Type(Integer32):
    """Custom type dcmeProfileRequiredTrafficType based on Integer32"""
    defaultValue = 0

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_DcmeProfileRequiredTrafficType_Type.__name__ = "Integer32"
_DcmeProfileRequiredTrafficType_Object = MibTableColumn
dcmeProfileRequiredTrafficType = _DcmeProfileRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 4),
    _DcmeProfileRequiredTrafficType_Type()
)
dcmeProfileRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileRequiredTrafficType.setStatus("mandatory")


class _DcmeProfilePermittedTrunkTypes_Type(OctetString):
    """Custom type dcmeProfilePermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DcmeProfilePermittedTrunkTypes_Type.__name__ = "OctetString"
_DcmeProfilePermittedTrunkTypes_Object = MibTableColumn
dcmeProfilePermittedTrunkTypes = _DcmeProfilePermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 5),
    _DcmeProfilePermittedTrunkTypes_Type()
)
dcmeProfilePermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfilePermittedTrunkTypes.setStatus("mandatory")


class _DcmeProfileRequiredSecurity_Type(Unsigned32):
    """Custom type dcmeProfileRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DcmeProfileRequiredSecurity_Type.__name__ = "Unsigned32"
_DcmeProfileRequiredSecurity_Object = MibTableColumn
dcmeProfileRequiredSecurity = _DcmeProfileRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 6),
    _DcmeProfileRequiredSecurity_Type()
)
dcmeProfileRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileRequiredSecurity.setStatus("mandatory")


class _DcmeProfileRequiredCustomerParm_Type(Unsigned32):
    """Custom type dcmeProfileRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DcmeProfileRequiredCustomerParm_Type.__name__ = "Unsigned32"
_DcmeProfileRequiredCustomerParm_Object = MibTableColumn
dcmeProfileRequiredCustomerParm = _DcmeProfileRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 7),
    _DcmeProfileRequiredCustomerParm_Type()
)
dcmeProfileRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileRequiredCustomerParm.setStatus("mandatory")


class _DcmeProfilePathAttributeToMinimize_Type(Integer32):
    """Custom type dcmeProfilePathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_DcmeProfilePathAttributeToMinimize_Type.__name__ = "Integer32"
_DcmeProfilePathAttributeToMinimize_Object = MibTableColumn
dcmeProfilePathAttributeToMinimize = _DcmeProfilePathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 8),
    _DcmeProfilePathAttributeToMinimize_Type()
)
dcmeProfilePathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfilePathAttributeToMinimize.setStatus("mandatory")


class _DcmeProfileMaximumAcceptableCost_Type(Unsigned32):
    """Custom type dcmeProfileMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcmeProfileMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_DcmeProfileMaximumAcceptableCost_Object = MibTableColumn
dcmeProfileMaximumAcceptableCost = _DcmeProfileMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 9),
    _DcmeProfileMaximumAcceptableCost_Type()
)
dcmeProfileMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMaximumAcceptableCost.setStatus("mandatory")


class _DcmeProfileMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type dcmeProfileMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_DcmeProfileMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_DcmeProfileMaximumAcceptableDelay_Object = MibTableColumn
dcmeProfileMaximumAcceptableDelay = _DcmeProfileMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 10),
    _DcmeProfileMaximumAcceptableDelay_Type()
)
dcmeProfileMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMaximumAcceptableDelay.setStatus("mandatory")


class _DcmeProfileEmissionPriority_Type(Unsigned32):
    """Custom type dcmeProfileEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DcmeProfileEmissionPriority_Type.__name__ = "Unsigned32"
_DcmeProfileEmissionPriority_Object = MibTableColumn
dcmeProfileEmissionPriority = _DcmeProfileEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 11),
    _DcmeProfileEmissionPriority_Type()
)
dcmeProfileEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileEmissionPriority.setStatus("mandatory")


class _DcmeProfileDiscardPriority_Type(Unsigned32):
    """Custom type dcmeProfileDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DcmeProfileDiscardPriority_Type.__name__ = "Unsigned32"
_DcmeProfileDiscardPriority_Object = MibTableColumn
dcmeProfileDiscardPriority = _DcmeProfileDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 12),
    _DcmeProfileDiscardPriority_Type()
)
dcmeProfileDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileDiscardPriority.setStatus("mandatory")


class _DcmeProfilePathFailureAction_Type(Integer32):
    """Custom type dcmeProfilePathFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_DcmeProfilePathFailureAction_Type.__name__ = "Integer32"
_DcmeProfilePathFailureAction_Object = MibTableColumn
dcmeProfilePathFailureAction = _DcmeProfilePathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 13),
    _DcmeProfilePathFailureAction_Type()
)
dcmeProfilePathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfilePathFailureAction.setStatus("mandatory")


class _DcmeProfileOptimization_Type(Integer32):
    """Custom type dcmeProfileOptimization based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DcmeProfileOptimization_Type.__name__ = "Integer32"
_DcmeProfileOptimization_Object = MibTableColumn
dcmeProfileOptimization = _DcmeProfileOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 10, 1, 14),
    _DcmeProfileOptimization_Type()
)
dcmeProfileOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileOptimization.setStatus("mandatory")
_DcmeProfileFrOpsTable_Object = MibTable
dcmeProfileFrOpsTable = _DcmeProfileFrOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11)
)
if mibBuilder.loadTexts:
    dcmeProfileFrOpsTable.setStatus("mandatory")
_DcmeProfileFrOpsEntry_Object = MibTableRow
dcmeProfileFrOpsEntry = _DcmeProfileFrOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1)
)
dcmeProfileFrOpsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    dcmeProfileFrOpsEntry.setStatus("mandatory")


class _DcmeProfileVoiceEncoding_Type(Integer32):
    """Custom type dcmeProfileVoiceEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711G726", 0),
          ("g728at16", 1),
          ("g729at8", 2))
    )


_DcmeProfileVoiceEncoding_Type.__name__ = "Integer32"
_DcmeProfileVoiceEncoding_Object = MibTableColumn
dcmeProfileVoiceEncoding = _DcmeProfileVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 1),
    _DcmeProfileVoiceEncoding_Type()
)
dcmeProfileVoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileVoiceEncoding.setStatus("mandatory")


class _DcmeProfileMaxVoiceBitRate_Type(Integer32):
    """Custom type dcmeProfileMaxVoiceBitRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_DcmeProfileMaxVoiceBitRate_Type.__name__ = "Integer32"
_DcmeProfileMaxVoiceBitRate_Object = MibTableColumn
dcmeProfileMaxVoiceBitRate = _DcmeProfileMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 2),
    _DcmeProfileMaxVoiceBitRate_Type()
)
dcmeProfileMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMaxVoiceBitRate.setStatus("mandatory")


class _DcmeProfileMinVoiceBitRate_Type(Integer32):
    """Custom type dcmeProfileMinVoiceBitRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_DcmeProfileMinVoiceBitRate_Type.__name__ = "Integer32"
_DcmeProfileMinVoiceBitRate_Object = MibTableColumn
dcmeProfileMinVoiceBitRate = _DcmeProfileMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 3),
    _DcmeProfileMinVoiceBitRate_Type()
)
dcmeProfileMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMinVoiceBitRate.setStatus("mandatory")


class _DcmeProfileVoiceTrafficOptimization_Type(Integer32):
    """Custom type dcmeProfileVoiceTrafficOptimization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 0),
          ("delay", 1))
    )


_DcmeProfileVoiceTrafficOptimization_Type.__name__ = "Integer32"
_DcmeProfileVoiceTrafficOptimization_Object = MibTableColumn
dcmeProfileVoiceTrafficOptimization = _DcmeProfileVoiceTrafficOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 4),
    _DcmeProfileVoiceTrafficOptimization_Type()
)
dcmeProfileVoiceTrafficOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileVoiceTrafficOptimization.setStatus("mandatory")


class _DcmeProfileSilenceSuppression_Type(Integer32):
    """Custom type dcmeProfileSilenceSuppression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_DcmeProfileSilenceSuppression_Type.__name__ = "Integer32"
_DcmeProfileSilenceSuppression_Object = MibTableColumn
dcmeProfileSilenceSuppression = _DcmeProfileSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 5),
    _DcmeProfileSilenceSuppression_Type()
)
dcmeProfileSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileSilenceSuppression.setStatus("mandatory")


class _DcmeProfileSilenceSuppressionFactor_Type(Unsigned32):
    """Custom type dcmeProfileSilenceSuppressionFactor based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_DcmeProfileSilenceSuppressionFactor_Type.__name__ = "Unsigned32"
_DcmeProfileSilenceSuppressionFactor_Object = MibTableColumn
dcmeProfileSilenceSuppressionFactor = _DcmeProfileSilenceSuppressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 6),
    _DcmeProfileSilenceSuppressionFactor_Type()
)
dcmeProfileSilenceSuppressionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileSilenceSuppressionFactor.setStatus("mandatory")


class _DcmeProfileEchoCancellation_Type(Integer32):
    """Custom type dcmeProfileEchoCancellation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DcmeProfileEchoCancellation_Type.__name__ = "Integer32"
_DcmeProfileEchoCancellation_Object = MibTableColumn
dcmeProfileEchoCancellation = _DcmeProfileEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 7),
    _DcmeProfileEchoCancellation_Type()
)
dcmeProfileEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileEchoCancellation.setStatus("mandatory")


class _DcmeProfileModemFaxEncoding_Type(Integer32):
    """Custom type dcmeProfileModemFaxEncoding based on Integer32"""
    defaultValue = 1

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
        *(("faxRelayG711G726", 2),
          ("faxRelayOnly", 1),
          ("g711G726", 0),
          ("useVoiceEncoding", 3))
    )


_DcmeProfileModemFaxEncoding_Type.__name__ = "Integer32"
_DcmeProfileModemFaxEncoding_Object = MibTableColumn
dcmeProfileModemFaxEncoding = _DcmeProfileModemFaxEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 9),
    _DcmeProfileModemFaxEncoding_Type()
)
dcmeProfileModemFaxEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileModemFaxEncoding.setStatus("mandatory")


class _DcmeProfileMaxModemFaxG711G726Rate_Type(Integer32):
    """Custom type dcmeProfileMaxModemFaxG711G726Rate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n32", 1),
          ("n64", 0))
    )


_DcmeProfileMaxModemFaxG711G726Rate_Type.__name__ = "Integer32"
_DcmeProfileMaxModemFaxG711G726Rate_Object = MibTableColumn
dcmeProfileMaxModemFaxG711G726Rate = _DcmeProfileMaxModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 10),
    _DcmeProfileMaxModemFaxG711G726Rate_Type()
)
dcmeProfileMaxModemFaxG711G726Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMaxModemFaxG711G726Rate.setStatus("mandatory")


class _DcmeProfileMinModemFaxG711G726Rate_Type(Integer32):
    """Custom type dcmeProfileMinModemFaxG711G726Rate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n32", 1),
          ("n64", 0))
    )


_DcmeProfileMinModemFaxG711G726Rate_Type.__name__ = "Integer32"
_DcmeProfileMinModemFaxG711G726Rate_Object = MibTableColumn
dcmeProfileMinModemFaxG711G726Rate = _DcmeProfileMinModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 11),
    _DcmeProfileMinModemFaxG711G726Rate_Type()
)
dcmeProfileMinModemFaxG711G726Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMinModemFaxG711G726Rate.setStatus("mandatory")


class _DcmeProfileFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type dcmeProfileFaxIdleSuppressionG711G726 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DcmeProfileFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_DcmeProfileFaxIdleSuppressionG711G726_Object = MibTableColumn
dcmeProfileFaxIdleSuppressionG711G726 = _DcmeProfileFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 12),
    _DcmeProfileFaxIdleSuppressionG711G726_Type()
)
dcmeProfileFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileFaxIdleSuppressionG711G726.setStatus("mandatory")


class _DcmeProfileInsertedOutputDelay_Type(Integer32):
    """Custom type dcmeProfileInsertedOutputDelay based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              15,
              22,
              30,
              35,
              40,
              45,
              50,
              75,
              100,
              125,
              150)
        )
    )
    namedValues = NamedValues(
        *(("n100", 100),
          ("n125", 125),
          ("n15", 15),
          ("n150", 150),
          ("n22", 22),
          ("n30", 30),
          ("n35", 35),
          ("n40", 40),
          ("n45", 45),
          ("n5", 5),
          ("n50", 50),
          ("n75", 75))
    )


_DcmeProfileInsertedOutputDelay_Type.__name__ = "Integer32"
_DcmeProfileInsertedOutputDelay_Object = MibTableColumn
dcmeProfileInsertedOutputDelay = _DcmeProfileInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 13),
    _DcmeProfileInsertedOutputDelay_Type()
)
dcmeProfileInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileInsertedOutputDelay.setStatus("mandatory")


class _DcmeProfileIngressAudioGain_Type(Integer32):
    """Custom type dcmeProfileIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_DcmeProfileIngressAudioGain_Type.__name__ = "Integer32"
_DcmeProfileIngressAudioGain_Object = MibTableColumn
dcmeProfileIngressAudioGain = _DcmeProfileIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 14),
    _DcmeProfileIngressAudioGain_Type()
)
dcmeProfileIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileIngressAudioGain.setStatus("mandatory")


class _DcmeProfileEgressAudioGain_Type(Integer32):
    """Custom type dcmeProfileEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_DcmeProfileEgressAudioGain_Type.__name__ = "Integer32"
_DcmeProfileEgressAudioGain_Object = MibTableColumn
dcmeProfileEgressAudioGain = _DcmeProfileEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 15),
    _DcmeProfileEgressAudioGain_Type()
)
dcmeProfileEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileEgressAudioGain.setStatus("mandatory")


class _DcmeProfileSpeechHangoverTime_Type(Unsigned32):
    """Custom type dcmeProfileSpeechHangoverTime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DcmeProfileSpeechHangoverTime_Type.__name__ = "Unsigned32"
_DcmeProfileSpeechHangoverTime_Object = MibTableColumn
dcmeProfileSpeechHangoverTime = _DcmeProfileSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 16),
    _DcmeProfileSpeechHangoverTime_Type()
)
dcmeProfileSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileSpeechHangoverTime.setStatus("mandatory")


class _DcmeProfileComfortNoiseCap_Type(Integer32):
    """Custom type dcmeProfileComfortNoiseCap based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-78, -78),
        ValueRangeConstraint(-65, -65),
        ValueRangeConstraint(-60, -60),
        ValueRangeConstraint(-54, -54),
        ValueRangeConstraint(-52, -52),
        ValueRangeConstraint(-50, -50),
        ValueRangeConstraint(-48, -48),
        ValueRangeConstraint(-46, -46),
        ValueRangeConstraint(-44, -44),
        ValueRangeConstraint(-42, -42),
        ValueRangeConstraint(-40, -40),
    )


_DcmeProfileComfortNoiseCap_Type.__name__ = "Integer32"
_DcmeProfileComfortNoiseCap_Object = MibTableColumn
dcmeProfileComfortNoiseCap = _DcmeProfileComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 17),
    _DcmeProfileComfortNoiseCap_Type()
)
dcmeProfileComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileComfortNoiseCap.setStatus("mandatory")


class _DcmeProfileModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type dcmeProfileModemFaxSpeechDiscrim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DcmeProfileModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_DcmeProfileModemFaxSpeechDiscrim_Object = MibTableColumn
dcmeProfileModemFaxSpeechDiscrim = _DcmeProfileModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 18),
    _DcmeProfileModemFaxSpeechDiscrim_Type()
)
dcmeProfileModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileModemFaxSpeechDiscrim.setStatus("mandatory")


class _DcmeProfileV17EncodedAsG711G726_Type(Integer32):
    """Custom type dcmeProfileV17EncodedAsG711G726 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DcmeProfileV17EncodedAsG711G726_Type.__name__ = "Integer32"
_DcmeProfileV17EncodedAsG711G726_Object = MibTableColumn
dcmeProfileV17EncodedAsG711G726 = _DcmeProfileV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 19),
    _DcmeProfileV17EncodedAsG711G726_Type()
)
dcmeProfileV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileV17EncodedAsG711G726.setStatus("mandatory")


class _DcmeProfileDtmfRegeneration_Type(Integer32):
    """Custom type dcmeProfileDtmfRegeneration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DcmeProfileDtmfRegeneration_Type.__name__ = "Integer32"
_DcmeProfileDtmfRegeneration_Object = MibTableColumn
dcmeProfileDtmfRegeneration = _DcmeProfileDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 20),
    _DcmeProfileDtmfRegeneration_Type()
)
dcmeProfileDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileDtmfRegeneration.setStatus("mandatory")


class _DcmeProfileMaxFaxRelayRate_Type(FixedPoint1):
    """Custom type dcmeProfileMaxFaxRelayRate based on FixedPoint1"""
    defaultValue = 144

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(144, 144),
    )


_DcmeProfileMaxFaxRelayRate_Type.__name__ = "FixedPoint1"
_DcmeProfileMaxFaxRelayRate_Object = MibTableColumn
dcmeProfileMaxFaxRelayRate = _DcmeProfileMaxFaxRelayRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 2, 11, 1, 21),
    _DcmeProfileMaxFaxRelayRate_Type()
)
dcmeProfileMaxFaxRelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeProfileMaxFaxRelayRate.setStatus("mandatory")
_DcmeProvTable_Object = MibTable
dcmeProvTable = _DcmeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10)
)
if mibBuilder.loadTexts:
    dcmeProvTable.setStatus("mandatory")
_DcmeProvEntry_Object = MibTableRow
dcmeProvEntry = _DcmeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1)
)
dcmeProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
)
if mibBuilder.loadTexts:
    dcmeProvEntry.setStatus("mandatory")


class _DcmeCommentText_Type(AsciiString):
    """Custom type dcmeCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DcmeCommentText_Type.__name__ = "AsciiString"
_DcmeCommentText_Object = MibTableColumn
dcmeCommentText = _DcmeCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 1),
    _DcmeCommentText_Type()
)
dcmeCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeCommentText.setStatus("mandatory")


class _DcmePreestablishedConnections_Type(Unsigned32):
    """Custom type dcmePreestablishedConnections based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DcmePreestablishedConnections_Type.__name__ = "Unsigned32"
_DcmePreestablishedConnections_Object = MibTableColumn
dcmePreestablishedConnections = _DcmePreestablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 2),
    _DcmePreestablishedConnections_Type()
)
dcmePreestablishedConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmePreestablishedConnections.setStatus("mandatory")


class _DcmeTrmThreshold_Type(Unsigned32):
    """Custom type dcmeTrmThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_DcmeTrmThreshold_Type.__name__ = "Unsigned32"
_DcmeTrmThreshold_Object = MibTableColumn
dcmeTrmThreshold = _DcmeTrmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 3),
    _DcmeTrmThreshold_Type()
)
dcmeTrmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeTrmThreshold.setStatus("mandatory")


class _DcmeTrmSignalChangeInterval_Type(Unsigned32):
    """Custom type dcmeTrmSignalChangeInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_DcmeTrmSignalChangeInterval_Type.__name__ = "Unsigned32"
_DcmeTrmSignalChangeInterval_Object = MibTableColumn
dcmeTrmSignalChangeInterval = _DcmeTrmSignalChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 4),
    _DcmeTrmSignalChangeInterval_Type()
)
dcmeTrmSignalChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeTrmSignalChangeInterval.setStatus("mandatory")


class _DcmeSpeechAlarmThreshold_Type(Unsigned32):
    """Custom type dcmeSpeechAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcmeSpeechAlarmThreshold_Type.__name__ = "Unsigned32"
_DcmeSpeechAlarmThreshold_Object = MibTableColumn
dcmeSpeechAlarmThreshold = _DcmeSpeechAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 5),
    _DcmeSpeechAlarmThreshold_Type()
)
dcmeSpeechAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeSpeechAlarmThreshold.setStatus("mandatory")


class _DcmeAudio3kHzAlarmThreshold_Type(Unsigned32):
    """Custom type dcmeAudio3kHzAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcmeAudio3kHzAlarmThreshold_Type.__name__ = "Unsigned32"
_DcmeAudio3kHzAlarmThreshold_Object = MibTableColumn
dcmeAudio3kHzAlarmThreshold = _DcmeAudio3kHzAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 6),
    _DcmeAudio3kHzAlarmThreshold_Type()
)
dcmeAudio3kHzAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeAudio3kHzAlarmThreshold.setStatus("mandatory")


class _DcmeUnrestricted64kAlarmThreshold_Type(Unsigned32):
    """Custom type dcmeUnrestricted64kAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcmeUnrestricted64kAlarmThreshold_Type.__name__ = "Unsigned32"
_DcmeUnrestricted64kAlarmThreshold_Object = MibTableColumn
dcmeUnrestricted64kAlarmThreshold = _DcmeUnrestricted64kAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 7),
    _DcmeUnrestricted64kAlarmThreshold_Type()
)
dcmeUnrestricted64kAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeUnrestricted64kAlarmThreshold.setStatus("mandatory")


class _DcmeAlarmTimeInterval_Type(Unsigned32):
    """Custom type dcmeAlarmTimeInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_DcmeAlarmTimeInterval_Type.__name__ = "Unsigned32"
_DcmeAlarmTimeInterval_Object = MibTableColumn
dcmeAlarmTimeInterval = _DcmeAlarmTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 8),
    _DcmeAlarmTimeInterval_Type()
)
dcmeAlarmTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeAlarmTimeInterval.setStatus("mandatory")


class _DcmeMaxUnrestricted64kCalls_Type(Unsigned32):
    """Custom type dcmeMaxUnrestricted64kCalls based on Unsigned32"""
    defaultValue = 420

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_DcmeMaxUnrestricted64kCalls_Type.__name__ = "Unsigned32"
_DcmeMaxUnrestricted64kCalls_Object = MibTableColumn
dcmeMaxUnrestricted64kCalls = _DcmeMaxUnrestricted64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 10, 1, 9),
    _DcmeMaxUnrestricted64kCalls_Type()
)
dcmeMaxUnrestricted64kCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeMaxUnrestricted64kCalls.setStatus("mandatory")
_DcmeStateTable_Object = MibTable
dcmeStateTable = _DcmeStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 11)
)
if mibBuilder.loadTexts:
    dcmeStateTable.setStatus("mandatory")
_DcmeStateEntry_Object = MibTableRow
dcmeStateEntry = _DcmeStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 11, 1)
)
dcmeStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
)
if mibBuilder.loadTexts:
    dcmeStateEntry.setStatus("mandatory")


class _DcmeAdminState_Type(Integer32):
    """Custom type dcmeAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DcmeAdminState_Type.__name__ = "Integer32"
_DcmeAdminState_Object = MibTableColumn
dcmeAdminState = _DcmeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 11, 1, 1),
    _DcmeAdminState_Type()
)
dcmeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeAdminState.setStatus("mandatory")


class _DcmeOperationalState_Type(Integer32):
    """Custom type dcmeOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DcmeOperationalState_Type.__name__ = "Integer32"
_DcmeOperationalState_Object = MibTableColumn
dcmeOperationalState = _DcmeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 11, 1, 2),
    _DcmeOperationalState_Type()
)
dcmeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeOperationalState.setStatus("mandatory")


class _DcmeUsageState_Type(Integer32):
    """Custom type dcmeUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DcmeUsageState_Type.__name__ = "Integer32"
_DcmeUsageState_Object = MibTableColumn
dcmeUsageState = _DcmeUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 11, 1, 3),
    _DcmeUsageState_Type()
)
dcmeUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeUsageState.setStatus("mandatory")
_DcmeStatsTable_Object = MibTable
dcmeStatsTable = _DcmeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 13)
)
if mibBuilder.loadTexts:
    dcmeStatsTable.setStatus("mandatory")
_DcmeStatsEntry_Object = MibTableRow
dcmeStatsEntry = _DcmeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 13, 1)
)
dcmeStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
)
if mibBuilder.loadTexts:
    dcmeStatsEntry.setStatus("mandatory")
_DcmeTrm64kNotAvailable_Type = Counter32
_DcmeTrm64kNotAvailable_Object = MibTableColumn
dcmeTrm64kNotAvailable = _DcmeTrm64kNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 13, 1, 1),
    _DcmeTrm64kNotAvailable_Type()
)
dcmeTrm64kNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeTrm64kNotAvailable.setStatus("mandatory")
_DcmeTrmSpeechNotAvailable_Type = Counter32
_DcmeTrmSpeechNotAvailable_Object = MibTableColumn
dcmeTrmSpeechNotAvailable = _DcmeTrmSpeechNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 13, 1, 2),
    _DcmeTrmSpeechNotAvailable_Type()
)
dcmeTrmSpeechNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeTrmSpeechNotAvailable.setStatus("mandatory")
_DcmeDLinksTable_Object = MibTable
dcmeDLinksTable = _DcmeDLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 419)
)
if mibBuilder.loadTexts:
    dcmeDLinksTable.setStatus("mandatory")
_DcmeDLinksEntry_Object = MibTableRow
dcmeDLinksEntry = _DcmeDLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 419, 1)
)
dcmeDLinksEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeDLinksValue"),
)
if mibBuilder.loadTexts:
    dcmeDLinksEntry.setStatus("mandatory")
_DcmeDLinksValue_Type = Link
_DcmeDLinksValue_Object = MibTableColumn
dcmeDLinksValue = _DcmeDLinksValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 419, 1, 1),
    _DcmeDLinksValue_Type()
)
dcmeDLinksValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmeDLinksValue.setStatus("mandatory")
_DcmeDLinksRowStatus_Type = RowStatus
_DcmeDLinksRowStatus_Object = MibTableColumn
dcmeDLinksRowStatus = _DcmeDLinksRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 419, 1, 2),
    _DcmeDLinksRowStatus_Type()
)
dcmeDLinksRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dcmeDLinksRowStatus.setStatus("mandatory")
_DcmeActiveDcmeLinksTable_Object = MibTable
dcmeActiveDcmeLinksTable = _DcmeActiveDcmeLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 420)
)
if mibBuilder.loadTexts:
    dcmeActiveDcmeLinksTable.setStatus("mandatory")
_DcmeActiveDcmeLinksEntry_Object = MibTableRow
dcmeActiveDcmeLinksEntry = _DcmeActiveDcmeLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 420, 1)
)
dcmeActiveDcmeLinksEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dcmeActiveDcmeLinksValue"),
)
if mibBuilder.loadTexts:
    dcmeActiveDcmeLinksEntry.setStatus("mandatory")
_DcmeActiveDcmeLinksValue_Type = RowPointer
_DcmeActiveDcmeLinksValue_Object = MibTableColumn
dcmeActiveDcmeLinksValue = _DcmeActiveDcmeLinksValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 129, 420, 1, 1),
    _DcmeActiveDcmeLinksValue_Type()
)
dcmeActiveDcmeLinksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmeActiveDcmeLinksValue.setStatus("mandatory")
_Dcl_ObjectIdentity = ObjectIdentity
dcl = _Dcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130)
)
_DclRowStatusTable_Object = MibTable
dclRowStatusTable = _DclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1)
)
if mibBuilder.loadTexts:
    dclRowStatusTable.setStatus("mandatory")
_DclRowStatusEntry_Object = MibTableRow
dclRowStatusEntry = _DclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1, 1)
)
dclRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
)
if mibBuilder.loadTexts:
    dclRowStatusEntry.setStatus("mandatory")
_DclRowStatus_Type = RowStatus
_DclRowStatus_Object = MibTableColumn
dclRowStatus = _DclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1, 1, 1),
    _DclRowStatus_Type()
)
dclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclRowStatus.setStatus("mandatory")
_DclComponentName_Type = DisplayString
_DclComponentName_Object = MibTableColumn
dclComponentName = _DclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1, 1, 2),
    _DclComponentName_Type()
)
dclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclComponentName.setStatus("mandatory")
_DclStorageType_Type = StorageType
_DclStorageType_Object = MibTableColumn
dclStorageType = _DclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1, 1, 4),
    _DclStorageType_Type()
)
dclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclStorageType.setStatus("mandatory")


class _DclIndex_Type(Integer32):
    """Custom type dclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_DclIndex_Type.__name__ = "Integer32"
_DclIndex_Object = MibTableColumn
dclIndex = _DclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 1, 1, 10),
    _DclIndex_Type()
)
dclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclIndex.setStatus("mandatory")
_DclDna_ObjectIdentity = ObjectIdentity
dclDna = _DclDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2)
)
_DclDnaRowStatusTable_Object = MibTable
dclDnaRowStatusTable = _DclDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1)
)
if mibBuilder.loadTexts:
    dclDnaRowStatusTable.setStatus("mandatory")
_DclDnaRowStatusEntry_Object = MibTableRow
dclDnaRowStatusEntry = _DclDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1, 1)
)
dclDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclDnaIndex"),
)
if mibBuilder.loadTexts:
    dclDnaRowStatusEntry.setStatus("mandatory")
_DclDnaRowStatus_Type = RowStatus
_DclDnaRowStatus_Object = MibTableColumn
dclDnaRowStatus = _DclDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1, 1, 1),
    _DclDnaRowStatus_Type()
)
dclDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclDnaRowStatus.setStatus("mandatory")
_DclDnaComponentName_Type = DisplayString
_DclDnaComponentName_Object = MibTableColumn
dclDnaComponentName = _DclDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1, 1, 2),
    _DclDnaComponentName_Type()
)
dclDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclDnaComponentName.setStatus("mandatory")
_DclDnaStorageType_Type = StorageType
_DclDnaStorageType_Object = MibTableColumn
dclDnaStorageType = _DclDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1, 1, 4),
    _DclDnaStorageType_Type()
)
dclDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclDnaStorageType.setStatus("mandatory")
_DclDnaIndex_Type = NonReplicated
_DclDnaIndex_Object = MibTableColumn
dclDnaIndex = _DclDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 1, 1, 10),
    _DclDnaIndex_Type()
)
dclDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclDnaIndex.setStatus("mandatory")
_DclDnaAddressTable_Object = MibTable
dclDnaAddressTable = _DclDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 10)
)
if mibBuilder.loadTexts:
    dclDnaAddressTable.setStatus("mandatory")
_DclDnaAddressEntry_Object = MibTableRow
dclDnaAddressEntry = _DclDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 10, 1)
)
dclDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclDnaIndex"),
)
if mibBuilder.loadTexts:
    dclDnaAddressEntry.setStatus("mandatory")


class _DclDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type dclDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_DclDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_DclDnaNumberingPlanIndicator_Object = MibTableColumn
dclDnaNumberingPlanIndicator = _DclDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 10, 1, 1),
    _DclDnaNumberingPlanIndicator_Type()
)
dclDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclDnaNumberingPlanIndicator.setStatus("mandatory")


class _DclDnaDataNetworkAddress_Type(DigitString):
    """Custom type dclDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DclDnaDataNetworkAddress_Type.__name__ = "DigitString"
_DclDnaDataNetworkAddress_Object = MibTableColumn
dclDnaDataNetworkAddress = _DclDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 2, 10, 1, 2),
    _DclDnaDataNetworkAddress_Type()
)
dclDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclDnaDataNetworkAddress.setStatus("mandatory")
_DclFramer_ObjectIdentity = ObjectIdentity
dclFramer = _DclFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3)
)
_DclFramerRowStatusTable_Object = MibTable
dclFramerRowStatusTable = _DclFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1)
)
if mibBuilder.loadTexts:
    dclFramerRowStatusTable.setStatus("mandatory")
_DclFramerRowStatusEntry_Object = MibTableRow
dclFramerRowStatusEntry = _DclFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1, 1)
)
dclFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclFramerIndex"),
)
if mibBuilder.loadTexts:
    dclFramerRowStatusEntry.setStatus("mandatory")
_DclFramerRowStatus_Type = RowStatus
_DclFramerRowStatus_Object = MibTableColumn
dclFramerRowStatus = _DclFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1, 1, 1),
    _DclFramerRowStatus_Type()
)
dclFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerRowStatus.setStatus("mandatory")
_DclFramerComponentName_Type = DisplayString
_DclFramerComponentName_Object = MibTableColumn
dclFramerComponentName = _DclFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1, 1, 2),
    _DclFramerComponentName_Type()
)
dclFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerComponentName.setStatus("mandatory")
_DclFramerStorageType_Type = StorageType
_DclFramerStorageType_Object = MibTableColumn
dclFramerStorageType = _DclFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1, 1, 4),
    _DclFramerStorageType_Type()
)
dclFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerStorageType.setStatus("mandatory")
_DclFramerIndex_Type = NonReplicated
_DclFramerIndex_Object = MibTableColumn
dclFramerIndex = _DclFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 1, 1, 10),
    _DclFramerIndex_Type()
)
dclFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclFramerIndex.setStatus("mandatory")
_DclFramerProvTable_Object = MibTable
dclFramerProvTable = _DclFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 10)
)
if mibBuilder.loadTexts:
    dclFramerProvTable.setStatus("mandatory")
_DclFramerProvEntry_Object = MibTableRow
dclFramerProvEntry = _DclFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 10, 1)
)
dclFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclFramerIndex"),
)
if mibBuilder.loadTexts:
    dclFramerProvEntry.setStatus("mandatory")
_DclFramerInterfaceName_Type = Link
_DclFramerInterfaceName_Object = MibTableColumn
dclFramerInterfaceName = _DclFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 10, 1, 1),
    _DclFramerInterfaceName_Type()
)
dclFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclFramerInterfaceName.setStatus("mandatory")
_DclFramerStateTable_Object = MibTable
dclFramerStateTable = _DclFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 12)
)
if mibBuilder.loadTexts:
    dclFramerStateTable.setStatus("mandatory")
_DclFramerStateEntry_Object = MibTableRow
dclFramerStateEntry = _DclFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 12, 1)
)
dclFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclFramerIndex"),
)
if mibBuilder.loadTexts:
    dclFramerStateEntry.setStatus("mandatory")


class _DclFramerAdminState_Type(Integer32):
    """Custom type dclFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DclFramerAdminState_Type.__name__ = "Integer32"
_DclFramerAdminState_Object = MibTableColumn
dclFramerAdminState = _DclFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 12, 1, 1),
    _DclFramerAdminState_Type()
)
dclFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerAdminState.setStatus("mandatory")


class _DclFramerOperationalState_Type(Integer32):
    """Custom type dclFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclFramerOperationalState_Type.__name__ = "Integer32"
_DclFramerOperationalState_Object = MibTableColumn
dclFramerOperationalState = _DclFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 12, 1, 2),
    _DclFramerOperationalState_Type()
)
dclFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerOperationalState.setStatus("mandatory")


class _DclFramerUsageState_Type(Integer32):
    """Custom type dclFramerUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DclFramerUsageState_Type.__name__ = "Integer32"
_DclFramerUsageState_Object = MibTableColumn
dclFramerUsageState = _DclFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 3, 12, 1, 3),
    _DclFramerUsageState_Type()
)
dclFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclFramerUsageState.setStatus("mandatory")
_DclVs_ObjectIdentity = ObjectIdentity
dclVs = _DclVs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4)
)
_DclVsRowStatusTable_Object = MibTable
dclVsRowStatusTable = _DclVsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1)
)
if mibBuilder.loadTexts:
    dclVsRowStatusTable.setStatus("mandatory")
_DclVsRowStatusEntry_Object = MibTableRow
dclVsRowStatusEntry = _DclVsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1, 1)
)
dclVsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
)
if mibBuilder.loadTexts:
    dclVsRowStatusEntry.setStatus("mandatory")
_DclVsRowStatus_Type = RowStatus
_DclVsRowStatus_Object = MibTableColumn
dclVsRowStatus = _DclVsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1, 1, 1),
    _DclVsRowStatus_Type()
)
dclVsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsRowStatus.setStatus("mandatory")
_DclVsComponentName_Type = DisplayString
_DclVsComponentName_Object = MibTableColumn
dclVsComponentName = _DclVsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1, 1, 2),
    _DclVsComponentName_Type()
)
dclVsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsComponentName.setStatus("mandatory")
_DclVsStorageType_Type = StorageType
_DclVsStorageType_Object = MibTableColumn
dclVsStorageType = _DclVsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1, 1, 4),
    _DclVsStorageType_Type()
)
dclVsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsStorageType.setStatus("mandatory")


class _DclVsIndex_Type(Integer32):
    """Custom type dclVsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DclVsIndex_Type.__name__ = "Integer32"
_DclVsIndex_Object = MibTableColumn
dclVsIndex = _DclVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 1, 1, 10),
    _DclVsIndex_Type()
)
dclVsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsIndex.setStatus("mandatory")
_DclVsFramer_ObjectIdentity = ObjectIdentity
dclVsFramer = _DclVsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2)
)
_DclVsFramerRowStatusTable_Object = MibTable
dclVsFramerRowStatusTable = _DclVsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dclVsFramerRowStatusTable.setStatus("mandatory")
_DclVsFramerRowStatusEntry_Object = MibTableRow
dclVsFramerRowStatusEntry = _DclVsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1, 1)
)
dclVsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerRowStatusEntry.setStatus("mandatory")
_DclVsFramerRowStatus_Type = RowStatus
_DclVsFramerRowStatus_Object = MibTableColumn
dclVsFramerRowStatus = _DclVsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1, 1, 1),
    _DclVsFramerRowStatus_Type()
)
dclVsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerRowStatus.setStatus("mandatory")
_DclVsFramerComponentName_Type = DisplayString
_DclVsFramerComponentName_Object = MibTableColumn
dclVsFramerComponentName = _DclVsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1, 1, 2),
    _DclVsFramerComponentName_Type()
)
dclVsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerComponentName.setStatus("mandatory")
_DclVsFramerStorageType_Type = StorageType
_DclVsFramerStorageType_Object = MibTableColumn
dclVsFramerStorageType = _DclVsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1, 1, 4),
    _DclVsFramerStorageType_Type()
)
dclVsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerStorageType.setStatus("mandatory")
_DclVsFramerIndex_Type = NonReplicated
_DclVsFramerIndex_Object = MibTableColumn
dclVsFramerIndex = _DclVsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 1, 1, 10),
    _DclVsFramerIndex_Type()
)
dclVsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerIndex.setStatus("mandatory")
_DclVsFramerVfpDebug_ObjectIdentity = ObjectIdentity
dclVsFramerVfpDebug = _DclVsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5)
)
_DclVsFramerVfpDebugRowStatusTable_Object = MibTable
dclVsFramerVfpDebugRowStatusTable = _DclVsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_DclVsFramerVfpDebugRowStatusEntry_Object = MibTableRow
dclVsFramerVfpDebugRowStatusEntry = _DclVsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1, 1)
)
dclVsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_DclVsFramerVfpDebugRowStatus_Type = RowStatus
_DclVsFramerVfpDebugRowStatus_Object = MibTableColumn
dclVsFramerVfpDebugRowStatus = _DclVsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1, 1, 1),
    _DclVsFramerVfpDebugRowStatus_Type()
)
dclVsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugRowStatus.setStatus("mandatory")
_DclVsFramerVfpDebugComponentName_Type = DisplayString
_DclVsFramerVfpDebugComponentName_Object = MibTableColumn
dclVsFramerVfpDebugComponentName = _DclVsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1, 1, 2),
    _DclVsFramerVfpDebugComponentName_Type()
)
dclVsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugComponentName.setStatus("mandatory")
_DclVsFramerVfpDebugStorageType_Type = StorageType
_DclVsFramerVfpDebugStorageType_Object = MibTableColumn
dclVsFramerVfpDebugStorageType = _DclVsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1, 1, 4),
    _DclVsFramerVfpDebugStorageType_Type()
)
dclVsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugStorageType.setStatus("mandatory")
_DclVsFramerVfpDebugIndex_Type = NonReplicated
_DclVsFramerVfpDebugIndex_Object = MibTableColumn
dclVsFramerVfpDebugIndex = _DclVsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 5, 1, 1, 10),
    _DclVsFramerVfpDebugIndex_Type()
)
dclVsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerVfpDebugIndex.setStatus("mandatory")
_DclVsFramerMvpDebug_ObjectIdentity = ObjectIdentity
dclVsFramerMvpDebug = _DclVsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6)
)
_DclVsFramerMvpDebugRowStatusTable_Object = MibTable
dclVsFramerMvpDebugRowStatusTable = _DclVsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_DclVsFramerMvpDebugRowStatusEntry_Object = MibTableRow
dclVsFramerMvpDebugRowStatusEntry = _DclVsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1, 1)
)
dclVsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_DclVsFramerMvpDebugRowStatus_Type = RowStatus
_DclVsFramerMvpDebugRowStatus_Object = MibTableColumn
dclVsFramerMvpDebugRowStatus = _DclVsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1, 1, 1),
    _DclVsFramerMvpDebugRowStatus_Type()
)
dclVsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugRowStatus.setStatus("mandatory")
_DclVsFramerMvpDebugComponentName_Type = DisplayString
_DclVsFramerMvpDebugComponentName_Object = MibTableColumn
dclVsFramerMvpDebugComponentName = _DclVsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1, 1, 2),
    _DclVsFramerMvpDebugComponentName_Type()
)
dclVsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugComponentName.setStatus("mandatory")
_DclVsFramerMvpDebugStorageType_Type = StorageType
_DclVsFramerMvpDebugStorageType_Object = MibTableColumn
dclVsFramerMvpDebugStorageType = _DclVsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1, 1, 4),
    _DclVsFramerMvpDebugStorageType_Type()
)
dclVsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugStorageType.setStatus("mandatory")
_DclVsFramerMvpDebugIndex_Type = NonReplicated
_DclVsFramerMvpDebugIndex_Object = MibTableColumn
dclVsFramerMvpDebugIndex = _DclVsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 6, 1, 1, 10),
    _DclVsFramerMvpDebugIndex_Type()
)
dclVsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerMvpDebugIndex.setStatus("mandatory")
_DclVsFramerPcmCapture_ObjectIdentity = ObjectIdentity
dclVsFramerPcmCapture = _DclVsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7)
)
_DclVsFramerPcmCaptureRowStatusTable_Object = MibTable
dclVsFramerPcmCaptureRowStatusTable = _DclVsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_DclVsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
dclVsFramerPcmCaptureRowStatusEntry = _DclVsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1, 1)
)
dclVsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_DclVsFramerPcmCaptureRowStatus_Type = RowStatus
_DclVsFramerPcmCaptureRowStatus_Object = MibTableColumn
dclVsFramerPcmCaptureRowStatus = _DclVsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1, 1, 1),
    _DclVsFramerPcmCaptureRowStatus_Type()
)
dclVsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureRowStatus.setStatus("mandatory")
_DclVsFramerPcmCaptureComponentName_Type = DisplayString
_DclVsFramerPcmCaptureComponentName_Object = MibTableColumn
dclVsFramerPcmCaptureComponentName = _DclVsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1, 1, 2),
    _DclVsFramerPcmCaptureComponentName_Type()
)
dclVsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureComponentName.setStatus("mandatory")
_DclVsFramerPcmCaptureStorageType_Type = StorageType
_DclVsFramerPcmCaptureStorageType_Object = MibTableColumn
dclVsFramerPcmCaptureStorageType = _DclVsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1, 1, 4),
    _DclVsFramerPcmCaptureStorageType_Type()
)
dclVsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureStorageType.setStatus("mandatory")
_DclVsFramerPcmCaptureIndex_Type = NonReplicated
_DclVsFramerPcmCaptureIndex_Object = MibTableColumn
dclVsFramerPcmCaptureIndex = _DclVsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 7, 1, 1, 10),
    _DclVsFramerPcmCaptureIndex_Type()
)
dclVsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerPcmCaptureIndex.setStatus("mandatory")
_DclVsFramerProvTable_Object = MibTable
dclVsFramerProvTable = _DclVsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 10)
)
if mibBuilder.loadTexts:
    dclVsFramerProvTable.setStatus("mandatory")
_DclVsFramerProvEntry_Object = MibTableRow
dclVsFramerProvEntry = _DclVsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 10, 1)
)
dclVsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerProvEntry.setStatus("mandatory")
_DclVsFramerInterfaceName_Type = Link
_DclVsFramerInterfaceName_Object = MibTableColumn
dclVsFramerInterfaceName = _DclVsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 10, 1, 1),
    _DclVsFramerInterfaceName_Type()
)
dclVsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerInterfaceName.setStatus("mandatory")
_DclVsFramerStateTable_Object = MibTable
dclVsFramerStateTable = _DclVsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 14)
)
if mibBuilder.loadTexts:
    dclVsFramerStateTable.setStatus("mandatory")
_DclVsFramerStateEntry_Object = MibTableRow
dclVsFramerStateEntry = _DclVsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 14, 1)
)
dclVsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerStateEntry.setStatus("mandatory")


class _DclVsFramerAdminState_Type(Integer32):
    """Custom type dclVsFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DclVsFramerAdminState_Type.__name__ = "Integer32"
_DclVsFramerAdminState_Object = MibTableColumn
dclVsFramerAdminState = _DclVsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 14, 1, 1),
    _DclVsFramerAdminState_Type()
)
dclVsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerAdminState.setStatus("mandatory")


class _DclVsFramerOperationalState_Type(Integer32):
    """Custom type dclVsFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclVsFramerOperationalState_Type.__name__ = "Integer32"
_DclVsFramerOperationalState_Object = MibTableColumn
dclVsFramerOperationalState = _DclVsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 14, 1, 2),
    _DclVsFramerOperationalState_Type()
)
dclVsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerOperationalState.setStatus("mandatory")


class _DclVsFramerUsageState_Type(Integer32):
    """Custom type dclVsFramerUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DclVsFramerUsageState_Type.__name__ = "Integer32"
_DclVsFramerUsageState_Object = MibTableColumn
dclVsFramerUsageState = _DclVsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 14, 1, 3),
    _DclVsFramerUsageState_Type()
)
dclVsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerUsageState.setStatus("mandatory")
_DclVsFramerStatsTable_Object = MibTable
dclVsFramerStatsTable = _DclVsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15)
)
if mibBuilder.loadTexts:
    dclVsFramerStatsTable.setStatus("mandatory")
_DclVsFramerStatsEntry_Object = MibTableRow
dclVsFramerStatsEntry = _DclVsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1)
)
dclVsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerStatsEntry.setStatus("mandatory")


class _DclVsFramerTotalCells_Type(Unsigned32):
    """Custom type dclVsFramerTotalCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerTotalCells_Type.__name__ = "Unsigned32"
_DclVsFramerTotalCells_Object = MibTableColumn
dclVsFramerTotalCells = _DclVsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 1),
    _DclVsFramerTotalCells_Type()
)
dclVsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerTotalCells.setStatus("mandatory")


class _DclVsFramerAudioCells_Type(Unsigned32):
    """Custom type dclVsFramerAudioCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerAudioCells_Type.__name__ = "Unsigned32"
_DclVsFramerAudioCells_Object = MibTableColumn
dclVsFramerAudioCells = _DclVsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 2),
    _DclVsFramerAudioCells_Type()
)
dclVsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerAudioCells.setStatus("mandatory")


class _DclVsFramerSilenceCells_Type(Unsigned32):
    """Custom type dclVsFramerSilenceCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerSilenceCells_Type.__name__ = "Unsigned32"
_DclVsFramerSilenceCells_Object = MibTableColumn
dclVsFramerSilenceCells = _DclVsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 4),
    _DclVsFramerSilenceCells_Type()
)
dclVsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerSilenceCells.setStatus("mandatory")


class _DclVsFramerModemCells_Type(Unsigned32):
    """Custom type dclVsFramerModemCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerModemCells_Type.__name__ = "Unsigned32"
_DclVsFramerModemCells_Object = MibTableColumn
dclVsFramerModemCells = _DclVsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 5),
    _DclVsFramerModemCells_Type()
)
dclVsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerModemCells.setStatus("obsolete")


class _DclVsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type dclVsFramerCurrentEncodingRate based on Integer32"""
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
        *(("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_DclVsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_DclVsFramerCurrentEncodingRate_Object = MibTableColumn
dclVsFramerCurrentEncodingRate = _DclVsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 6),
    _DclVsFramerCurrentEncodingRate_Type()
)
dclVsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerCurrentEncodingRate.setStatus("obsolete")


class _DclVsFramerLrcErrors_Type(Unsigned32):
    """Custom type dclVsFramerLrcErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerLrcErrors_Type.__name__ = "Unsigned32"
_DclVsFramerLrcErrors_Object = MibTableColumn
dclVsFramerLrcErrors = _DclVsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 7),
    _DclVsFramerLrcErrors_Type()
)
dclVsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerLrcErrors.setStatus("mandatory")


class _DclVsFramerFrmLostInNetwork_Type(Unsigned32):
    """Custom type dclVsFramerFrmLostInNetwork based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerFrmLostInNetwork_Type.__name__ = "Unsigned32"
_DclVsFramerFrmLostInNetwork_Object = MibTableColumn
dclVsFramerFrmLostInNetwork = _DclVsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 8),
    _DclVsFramerFrmLostInNetwork_Type()
)
dclVsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFrmLostInNetwork.setStatus("mandatory")


class _DclVsFramerFrmUnderRuns_Type(Unsigned32):
    """Custom type dclVsFramerFrmUnderRuns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerFrmUnderRuns_Type.__name__ = "Unsigned32"
_DclVsFramerFrmUnderRuns_Object = MibTableColumn
dclVsFramerFrmUnderRuns = _DclVsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 9),
    _DclVsFramerFrmUnderRuns_Type()
)
dclVsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFrmUnderRuns.setStatus("mandatory")


class _DclVsFramerFrmDumped_Type(Unsigned32):
    """Custom type dclVsFramerFrmDumped based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerFrmDumped_Type.__name__ = "Unsigned32"
_DclVsFramerFrmDumped_Object = MibTableColumn
dclVsFramerFrmDumped = _DclVsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 10),
    _DclVsFramerFrmDumped_Type()
)
dclVsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFrmDumped.setStatus("mandatory")
_DclVsFramerModemSilenceCells_Type = Counter32
_DclVsFramerModemSilenceCells_Object = MibTableColumn
dclVsFramerModemSilenceCells = _DclVsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 26),
    _DclVsFramerModemSilenceCells_Type()
)
dclVsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerModemSilenceCells.setStatus("obsolete")


class _DclVsFramerCurrentEncoding_Type(Integer32):
    """Custom type dclVsFramerCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_DclVsFramerCurrentEncoding_Type.__name__ = "Integer32"
_DclVsFramerCurrentEncoding_Object = MibTableColumn
dclVsFramerCurrentEncoding = _DclVsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 27),
    _DclVsFramerCurrentEncoding_Type()
)
dclVsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerCurrentEncoding.setStatus("obsolete")


class _DclVsFramerTptStatus_Type(Integer32):
    """Custom type dclVsFramerTptStatus based on Integer32"""
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
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0),
          ("rejected", 1))
    )


_DclVsFramerTptStatus_Type.__name__ = "Integer32"
_DclVsFramerTptStatus_Object = MibTableColumn
dclVsFramerTptStatus = _DclVsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 28),
    _DclVsFramerTptStatus_Type()
)
dclVsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerTptStatus.setStatus("obsolete")
_DclVsFramerFaxRelayCells_Type = Counter32
_DclVsFramerFaxRelayCells_Object = MibTableColumn
dclVsFramerFaxRelayCells = _DclVsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 35),
    _DclVsFramerFaxRelayCells_Type()
)
dclVsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFaxRelayCells.setStatus("mandatory")


class _DclVsFramerModemFaxCells_Type(Unsigned32):
    """Custom type dclVsFramerModemFaxCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerModemFaxCells_Type.__name__ = "Unsigned32"
_DclVsFramerModemFaxCells_Object = MibTableColumn
dclVsFramerModemFaxCells = _DclVsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 36),
    _DclVsFramerModemFaxCells_Type()
)
dclVsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerModemFaxCells.setStatus("mandatory")
_DclVsFramerFaxIdleCells_Type = Counter32
_DclVsFramerFaxIdleCells_Object = MibTableColumn
dclVsFramerFaxIdleCells = _DclVsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 15, 1, 37),
    _DclVsFramerFaxIdleCells_Type()
)
dclVsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFaxIdleCells.setStatus("mandatory")
_DclVsFramerOperTable_Object = MibTable
dclVsFramerOperTable = _DclVsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 16)
)
if mibBuilder.loadTexts:
    dclVsFramerOperTable.setStatus("mandatory")
_DclVsFramerOperEntry_Object = MibTableRow
dclVsFramerOperEntry = _DclVsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 16, 1)
)
dclVsFramerOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerOperEntry.setStatus("mandatory")


class _DclVsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type dclVsFramerOpCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_DclVsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_DclVsFramerOpCurrentEncoding_Object = MibTableColumn
dclVsFramerOpCurrentEncoding = _DclVsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 16, 1, 1),
    _DclVsFramerOpCurrentEncoding_Type()
)
dclVsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerOpCurrentEncoding.setStatus("mandatory")


class _DclVsFramerCurrentRate_Type(Integer32):
    """Custom type dclVsFramerCurrentRate based on Integer32"""
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
        *(("n0", 0),
          ("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_DclVsFramerCurrentRate_Type.__name__ = "Integer32"
_DclVsFramerCurrentRate_Object = MibTableColumn
dclVsFramerCurrentRate = _DclVsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 16, 1, 2),
    _DclVsFramerCurrentRate_Type()
)
dclVsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerCurrentRate.setStatus("mandatory")


class _DclVsFramerOpTptStatus_Type(Integer32):
    """Custom type dclVsFramerOpTptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0))
    )


_DclVsFramerOpTptStatus_Type.__name__ = "Integer32"
_DclVsFramerOpTptStatus_Object = MibTableColumn
dclVsFramerOpTptStatus = _DclVsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 16, 1, 3),
    _DclVsFramerOpTptStatus_Type()
)
dclVsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerOpTptStatus.setStatus("mandatory")
_DclVsFramerNegTable_Object = MibTable
dclVsFramerNegTable = _DclVsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17)
)
if mibBuilder.loadTexts:
    dclVsFramerNegTable.setStatus("mandatory")
_DclVsFramerNegEntry_Object = MibTableRow
dclVsFramerNegEntry = _DclVsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1)
)
dclVsFramerNegEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerNegEntry.setStatus("mandatory")


class _DclVsFramerNegotiatedSilenceSuppression_Type(Integer32):
    """Custom type dclVsFramerNegotiatedSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_DclVsFramerNegotiatedSilenceSuppression_Type.__name__ = "Integer32"
_DclVsFramerNegotiatedSilenceSuppression_Object = MibTableColumn
dclVsFramerNegotiatedSilenceSuppression = _DclVsFramerNegotiatedSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1, 1),
    _DclVsFramerNegotiatedSilenceSuppression_Type()
)
dclVsFramerNegotiatedSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerNegotiatedSilenceSuppression.setStatus("mandatory")


class _DclVsFramerNegotiatedFisG711G726_Type(Integer32):
    """Custom type dclVsFramerNegotiatedFisG711G726 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DclVsFramerNegotiatedFisG711G726_Type.__name__ = "Integer32"
_DclVsFramerNegotiatedFisG711G726_Object = MibTableColumn
dclVsFramerNegotiatedFisG711G726 = _DclVsFramerNegotiatedFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1, 2),
    _DclVsFramerNegotiatedFisG711G726_Type()
)
dclVsFramerNegotiatedFisG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerNegotiatedFisG711G726.setStatus("mandatory")


class _DclVsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type dclVsFramerNegotiatedDtmfRegeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DclVsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_DclVsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
dclVsFramerNegotiatedDtmfRegeneration = _DclVsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1, 3),
    _DclVsFramerNegotiatedDtmfRegeneration_Type()
)
dclVsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _DclVsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type dclVsFramerNegotiatedV17AsG711G726 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DclVsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_DclVsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
dclVsFramerNegotiatedV17AsG711G726 = _DclVsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1, 4),
    _DclVsFramerNegotiatedV17AsG711G726_Type()
)
dclVsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _DclVsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type dclVsFramerNegotiatedTandemPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclVsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_DclVsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
dclVsFramerNegotiatedTandemPassThrough = _DclVsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 17, 1, 5),
    _DclVsFramerNegotiatedTandemPassThrough_Type()
)
dclVsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_DclVsFramerFrmToNetworkTable_Object = MibTable
dclVsFramerFrmToNetworkTable = _DclVsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 315)
)
if mibBuilder.loadTexts:
    dclVsFramerFrmToNetworkTable.setStatus("mandatory")
_DclVsFramerFrmToNetworkEntry_Object = MibTableRow
dclVsFramerFrmToNetworkEntry = _DclVsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 315, 1)
)
dclVsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerFrmToNetworkEntry.setStatus("mandatory")


class _DclVsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type dclVsFramerFrmToNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n16KbitS", 3),
          ("n24KbitS", 2),
          ("n32KbitS", 1),
          ("n64KbitS", 0),
          ("n8KbitS", 4))
    )


_DclVsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_DclVsFramerFrmToNetworkIndex_Object = MibTableColumn
dclVsFramerFrmToNetworkIndex = _DclVsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 315, 1, 1),
    _DclVsFramerFrmToNetworkIndex_Type()
)
dclVsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerFrmToNetworkIndex.setStatus("mandatory")


class _DclVsFramerFrmToNetworkValue_Type(Unsigned32):
    """Custom type dclVsFramerFrmToNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerFrmToNetworkValue_Type.__name__ = "Unsigned32"
_DclVsFramerFrmToNetworkValue_Object = MibTableColumn
dclVsFramerFrmToNetworkValue = _DclVsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 315, 1, 2),
    _DclVsFramerFrmToNetworkValue_Type()
)
dclVsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFrmToNetworkValue.setStatus("mandatory")
_DclVsFramerFrmFromNetworkTable_Object = MibTable
dclVsFramerFrmFromNetworkTable = _DclVsFramerFrmFromNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 316)
)
if mibBuilder.loadTexts:
    dclVsFramerFrmFromNetworkTable.setStatus("mandatory")
_DclVsFramerFrmFromNetworkEntry_Object = MibTableRow
dclVsFramerFrmFromNetworkEntry = _DclVsFramerFrmFromNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 316, 1)
)
dclVsFramerFrmFromNetworkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerFrmFromNetworkIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerFrmFromNetworkEntry.setStatus("mandatory")


class _DclVsFramerFrmFromNetworkIndex_Type(Integer32):
    """Custom type dclVsFramerFrmFromNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n16KbitS", 3),
          ("n24KbitS", 2),
          ("n32KbitS", 1),
          ("n64KbitS", 0),
          ("n8KbitS", 4))
    )


_DclVsFramerFrmFromNetworkIndex_Type.__name__ = "Integer32"
_DclVsFramerFrmFromNetworkIndex_Object = MibTableColumn
dclVsFramerFrmFromNetworkIndex = _DclVsFramerFrmFromNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 316, 1, 1),
    _DclVsFramerFrmFromNetworkIndex_Type()
)
dclVsFramerFrmFromNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerFrmFromNetworkIndex.setStatus("mandatory")


class _DclVsFramerFrmFromNetworkValue_Type(Unsigned32):
    """Custom type dclVsFramerFrmFromNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsFramerFrmFromNetworkValue_Type.__name__ = "Unsigned32"
_DclVsFramerFrmFromNetworkValue_Object = MibTableColumn
dclVsFramerFrmFromNetworkValue = _DclVsFramerFrmFromNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 316, 1, 2),
    _DclVsFramerFrmFromNetworkValue_Type()
)
dclVsFramerFrmFromNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsFramerFrmFromNetworkValue.setStatus("mandatory")
_DclVsFramerNEncodingTable_Object = MibTable
dclVsFramerNEncodingTable = _DclVsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 467)
)
if mibBuilder.loadTexts:
    dclVsFramerNEncodingTable.setStatus("mandatory")
_DclVsFramerNEncodingEntry_Object = MibTableRow
dclVsFramerNEncodingEntry = _DclVsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 467, 1)
)
dclVsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerNEncodingEntry.setStatus("mandatory")


class _DclVsFramerNEncodingIndex_Type(Integer32):
    """Custom type dclVsFramerNEncodingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_DclVsFramerNEncodingIndex_Type.__name__ = "Integer32"
_DclVsFramerNEncodingIndex_Object = MibTableColumn
dclVsFramerNEncodingIndex = _DclVsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 467, 1, 1),
    _DclVsFramerNEncodingIndex_Type()
)
dclVsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerNEncodingIndex.setStatus("mandatory")


class _DclVsFramerNEncodingValue_Type(Integer32):
    """Custom type dclVsFramerNEncodingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              31,
              64,
              68,
              255)
        )
    )
    namedValues = NamedValues(
        *(("g711", 5),
          ("g711G726", 31),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17V29V27Relay", 68),
          ("v29V27Relay", 64))
    )


_DclVsFramerNEncodingValue_Type.__name__ = "Integer32"
_DclVsFramerNEncodingValue_Object = MibTableColumn
dclVsFramerNEncodingValue = _DclVsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 467, 1, 2),
    _DclVsFramerNEncodingValue_Type()
)
dclVsFramerNEncodingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerNEncodingValue.setStatus("mandatory")
_DclVsFramerNRatesTable_Object = MibTable
dclVsFramerNRatesTable = _DclVsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 479)
)
if mibBuilder.loadTexts:
    dclVsFramerNRatesTable.setStatus("mandatory")
_DclVsFramerNRatesEntry_Object = MibTableRow
dclVsFramerNRatesEntry = _DclVsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 479, 1)
)
dclVsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerNRatesTrafficIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    dclVsFramerNRatesEntry.setStatus("mandatory")


class _DclVsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type dclVsFramerNRatesTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_DclVsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_DclVsFramerNRatesTrafficIndex_Object = MibTableColumn
dclVsFramerNRatesTrafficIndex = _DclVsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 479, 1, 1),
    _DclVsFramerNRatesTrafficIndex_Type()
)
dclVsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerNRatesTrafficIndex.setStatus("mandatory")


class _DclVsFramerNRatesRateIndex_Type(Integer32):
    """Custom type dclVsFramerNRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_DclVsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_DclVsFramerNRatesRateIndex_Object = MibTableColumn
dclVsFramerNRatesRateIndex = _DclVsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 479, 1, 2),
    _DclVsFramerNRatesRateIndex_Type()
)
dclVsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsFramerNRatesRateIndex.setStatus("mandatory")


class _DclVsFramerNRatesValue_Type(Integer32):
    """Custom type dclVsFramerNRatesValue based on Integer32"""
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
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("n00", 0),
          ("n03", 1),
          ("n12", 2),
          ("n120", 7),
          ("n144", 8),
          ("n160", 67),
          ("n24", 3),
          ("n240", 68),
          ("n320", 69),
          ("n48", 4),
          ("n640", 70),
          ("n72", 5),
          ("n80", 66),
          ("n96", 6))
    )


_DclVsFramerNRatesValue_Type.__name__ = "Integer32"
_DclVsFramerNRatesValue_Object = MibTableColumn
dclVsFramerNRatesValue = _DclVsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 2, 479, 1, 3),
    _DclVsFramerNRatesValue_Type()
)
dclVsFramerNRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsFramerNRatesValue.setStatus("mandatory")
_DclVsLCo_ObjectIdentity = ObjectIdentity
dclVsLCo = _DclVsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3)
)
_DclVsLCoRowStatusTable_Object = MibTable
dclVsLCoRowStatusTable = _DclVsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dclVsLCoRowStatusTable.setStatus("mandatory")
_DclVsLCoRowStatusEntry_Object = MibTableRow
dclVsLCoRowStatusEntry = _DclVsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1, 1)
)
dclVsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    dclVsLCoRowStatusEntry.setStatus("mandatory")
_DclVsLCoRowStatus_Type = RowStatus
_DclVsLCoRowStatus_Object = MibTableColumn
dclVsLCoRowStatus = _DclVsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1, 1, 1),
    _DclVsLCoRowStatus_Type()
)
dclVsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRowStatus.setStatus("mandatory")
_DclVsLCoComponentName_Type = DisplayString
_DclVsLCoComponentName_Object = MibTableColumn
dclVsLCoComponentName = _DclVsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1, 1, 2),
    _DclVsLCoComponentName_Type()
)
dclVsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoComponentName.setStatus("mandatory")
_DclVsLCoStorageType_Type = StorageType
_DclVsLCoStorageType_Object = MibTableColumn
dclVsLCoStorageType = _DclVsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1, 1, 4),
    _DclVsLCoStorageType_Type()
)
dclVsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoStorageType.setStatus("mandatory")
_DclVsLCoIndex_Type = NonReplicated
_DclVsLCoIndex_Object = MibTableColumn
dclVsLCoIndex = _DclVsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 1, 1, 10),
    _DclVsLCoIndex_Type()
)
dclVsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dclVsLCoIndex.setStatus("mandatory")
_DclVsLCoPathDataTable_Object = MibTable
dclVsLCoPathDataTable = _DclVsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10)
)
if mibBuilder.loadTexts:
    dclVsLCoPathDataTable.setStatus("mandatory")
_DclVsLCoPathDataEntry_Object = MibTableRow
dclVsLCoPathDataEntry = _DclVsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1)
)
dclVsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    dclVsLCoPathDataEntry.setStatus("mandatory")


class _DclVsLCoState_Type(Integer32):
    """Custom type dclVsLCoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_DclVsLCoState_Type.__name__ = "Integer32"
_DclVsLCoState_Object = MibTableColumn
dclVsLCoState = _DclVsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 1),
    _DclVsLCoState_Type()
)
dclVsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoState.setStatus("mandatory")


class _DclVsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type dclVsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DclVsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_DclVsLCoOverrideRemoteName_Object = MibTableColumn
dclVsLCoOverrideRemoteName = _DclVsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 2),
    _DclVsLCoOverrideRemoteName_Type()
)
dclVsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsLCoOverrideRemoteName.setStatus("mandatory")


class _DclVsLCoEnd_Type(Integer32):
    """Custom type dclVsLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_DclVsLCoEnd_Type.__name__ = "Integer32"
_DclVsLCoEnd_Object = MibTableColumn
dclVsLCoEnd = _DclVsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 3),
    _DclVsLCoEnd_Type()
)
dclVsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoEnd.setStatus("mandatory")


class _DclVsLCoCostMetric_Type(Unsigned32):
    """Custom type dclVsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DclVsLCoCostMetric_Type.__name__ = "Unsigned32"
_DclVsLCoCostMetric_Object = MibTableColumn
dclVsLCoCostMetric = _DclVsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 4),
    _DclVsLCoCostMetric_Type()
)
dclVsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoCostMetric.setStatus("mandatory")


class _DclVsLCoDelayMetric_Type(Unsigned32):
    """Custom type dclVsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_DclVsLCoDelayMetric_Type.__name__ = "Unsigned32"
_DclVsLCoDelayMetric_Object = MibTableColumn
dclVsLCoDelayMetric = _DclVsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 5),
    _DclVsLCoDelayMetric_Type()
)
dclVsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoDelayMetric.setStatus("mandatory")


class _DclVsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type dclVsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_DclVsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_DclVsLCoRoundTripDelay_Object = MibTableColumn
dclVsLCoRoundTripDelay = _DclVsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 6),
    _DclVsLCoRoundTripDelay_Type()
)
dclVsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRoundTripDelay.setStatus("mandatory")


class _DclVsLCoSetupPriority_Type(Unsigned32):
    """Custom type dclVsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DclVsLCoSetupPriority_Type.__name__ = "Unsigned32"
_DclVsLCoSetupPriority_Object = MibTableColumn
dclVsLCoSetupPriority = _DclVsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 7),
    _DclVsLCoSetupPriority_Type()
)
dclVsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoSetupPriority.setStatus("mandatory")


class _DclVsLCoHoldingPriority_Type(Unsigned32):
    """Custom type dclVsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DclVsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_DclVsLCoHoldingPriority_Object = MibTableColumn
dclVsLCoHoldingPriority = _DclVsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 8),
    _DclVsLCoHoldingPriority_Type()
)
dclVsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoHoldingPriority.setStatus("mandatory")


class _DclVsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type dclVsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_DclVsLCoRequiredTxBandwidth_Object = MibTableColumn
dclVsLCoRequiredTxBandwidth = _DclVsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 9),
    _DclVsLCoRequiredTxBandwidth_Type()
)
dclVsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRequiredTxBandwidth.setStatus("mandatory")


class _DclVsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type dclVsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DclVsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_DclVsLCoRequiredRxBandwidth_Object = MibTableColumn
dclVsLCoRequiredRxBandwidth = _DclVsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 10),
    _DclVsLCoRequiredRxBandwidth_Type()
)
dclVsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRequiredRxBandwidth.setStatus("mandatory")


class _DclVsLCoRequiredTrafficType_Type(Integer32):
    """Custom type dclVsLCoRequiredTrafficType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_DclVsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_DclVsLCoRequiredTrafficType_Object = MibTableColumn
dclVsLCoRequiredTrafficType = _DclVsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 11),
    _DclVsLCoRequiredTrafficType_Type()
)
dclVsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRequiredTrafficType.setStatus("mandatory")


class _DclVsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type dclVsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DclVsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_DclVsLCoPermittedTrunkTypes_Object = MibTableColumn
dclVsLCoPermittedTrunkTypes = _DclVsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 12),
    _DclVsLCoPermittedTrunkTypes_Type()
)
dclVsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPermittedTrunkTypes.setStatus("mandatory")


class _DclVsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type dclVsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DclVsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_DclVsLCoRequiredSecurity_Object = MibTableColumn
dclVsLCoRequiredSecurity = _DclVsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 13),
    _DclVsLCoRequiredSecurity_Type()
)
dclVsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRequiredSecurity.setStatus("mandatory")


class _DclVsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type dclVsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DclVsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_DclVsLCoRequiredCustomerParameter_Object = MibTableColumn
dclVsLCoRequiredCustomerParameter = _DclVsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 14),
    _DclVsLCoRequiredCustomerParameter_Type()
)
dclVsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRequiredCustomerParameter.setStatus("mandatory")


class _DclVsLCoEmissionPriority_Type(Unsigned32):
    """Custom type dclVsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DclVsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_DclVsLCoEmissionPriority_Object = MibTableColumn
dclVsLCoEmissionPriority = _DclVsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 15),
    _DclVsLCoEmissionPriority_Type()
)
dclVsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoEmissionPriority.setStatus("mandatory")


class _DclVsLCoDiscardPriority_Type(Unsigned32):
    """Custom type dclVsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DclVsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_DclVsLCoDiscardPriority_Object = MibTableColumn
dclVsLCoDiscardPriority = _DclVsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 16),
    _DclVsLCoDiscardPriority_Type()
)
dclVsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoDiscardPriority.setStatus("mandatory")


class _DclVsLCoPathType_Type(Integer32):
    """Custom type dclVsLCoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_DclVsLCoPathType_Type.__name__ = "Integer32"
_DclVsLCoPathType_Object = MibTableColumn
dclVsLCoPathType = _DclVsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 17),
    _DclVsLCoPathType_Type()
)
dclVsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPathType.setStatus("mandatory")


class _DclVsLCoRetryCount_Type(Unsigned32):
    """Custom type dclVsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DclVsLCoRetryCount_Type.__name__ = "Unsigned32"
_DclVsLCoRetryCount_Object = MibTableColumn
dclVsLCoRetryCount = _DclVsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 18),
    _DclVsLCoRetryCount_Type()
)
dclVsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoRetryCount.setStatus("mandatory")


class _DclVsLCoPathFailureCount_Type(Unsigned32):
    """Custom type dclVsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DclVsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_DclVsLCoPathFailureCount_Object = MibTableColumn
dclVsLCoPathFailureCount = _DclVsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 19),
    _DclVsLCoPathFailureCount_Type()
)
dclVsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPathFailureCount.setStatus("mandatory")


class _DclVsLCoReasonForNoRoute_Type(Integer32):
    """Custom type dclVsLCoReasonForNoRoute based on Integer32"""
    defaultValue = 0

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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_DclVsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_DclVsLCoReasonForNoRoute_Object = MibTableColumn
dclVsLCoReasonForNoRoute = _DclVsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 20),
    _DclVsLCoReasonForNoRoute_Type()
)
dclVsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoReasonForNoRoute.setStatus("mandatory")


class _DclVsLCoLastTearDownReason_Type(Integer32):
    """Custom type dclVsLCoLastTearDownReason based on Integer32"""
    defaultValue = 0

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_DclVsLCoLastTearDownReason_Type.__name__ = "Integer32"
_DclVsLCoLastTearDownReason_Object = MibTableColumn
dclVsLCoLastTearDownReason = _DclVsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 21),
    _DclVsLCoLastTearDownReason_Type()
)
dclVsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoLastTearDownReason.setStatus("mandatory")


class _DclVsLCoPathFailureAction_Type(Integer32):
    """Custom type dclVsLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_DclVsLCoPathFailureAction_Type.__name__ = "Integer32"
_DclVsLCoPathFailureAction_Object = MibTableColumn
dclVsLCoPathFailureAction = _DclVsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 22),
    _DclVsLCoPathFailureAction_Type()
)
dclVsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPathFailureAction.setStatus("mandatory")


class _DclVsLCoBumpPreference_Type(Integer32):
    """Custom type dclVsLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_DclVsLCoBumpPreference_Type.__name__ = "Integer32"
_DclVsLCoBumpPreference_Object = MibTableColumn
dclVsLCoBumpPreference = _DclVsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 23),
    _DclVsLCoBumpPreference_Type()
)
dclVsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoBumpPreference.setStatus("mandatory")


class _DclVsLCoOptimization_Type(Integer32):
    """Custom type dclVsLCoOptimization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclVsLCoOptimization_Type.__name__ = "Integer32"
_DclVsLCoOptimization_Object = MibTableColumn
dclVsLCoOptimization = _DclVsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 24),
    _DclVsLCoOptimization_Type()
)
dclVsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoOptimization.setStatus("mandatory")


class _DclVsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type dclVsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_DclVsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_DclVsLCoPathUpDateTime_Object = MibTableColumn
dclVsLCoPathUpDateTime = _DclVsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 10, 1, 25),
    _DclVsLCoPathUpDateTime_Type()
)
dclVsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPathUpDateTime.setStatus("mandatory")
_DclVsLCoStatsTable_Object = MibTable
dclVsLCoStatsTable = _DclVsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11)
)
if mibBuilder.loadTexts:
    dclVsLCoStatsTable.setStatus("mandatory")
_DclVsLCoStatsEntry_Object = MibTableRow
dclVsLCoStatsEntry = _DclVsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11, 1)
)
dclVsLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    dclVsLCoStatsEntry.setStatus("mandatory")
_DclVsLCoPktsToNetwork_Type = PassportCounter64
_DclVsLCoPktsToNetwork_Object = MibTableColumn
dclVsLCoPktsToNetwork = _DclVsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11, 1, 1),
    _DclVsLCoPktsToNetwork_Type()
)
dclVsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPktsToNetwork.setStatus("mandatory")
_DclVsLCoBytesToNetwork_Type = PassportCounter64
_DclVsLCoBytesToNetwork_Object = MibTableColumn
dclVsLCoBytesToNetwork = _DclVsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11, 1, 2),
    _DclVsLCoBytesToNetwork_Type()
)
dclVsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoBytesToNetwork.setStatus("mandatory")
_DclVsLCoPktsFromNetwork_Type = PassportCounter64
_DclVsLCoPktsFromNetwork_Object = MibTableColumn
dclVsLCoPktsFromNetwork = _DclVsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11, 1, 3),
    _DclVsLCoPktsFromNetwork_Type()
)
dclVsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPktsFromNetwork.setStatus("mandatory")
_DclVsLCoBytesFromNetwork_Type = PassportCounter64
_DclVsLCoBytesFromNetwork_Object = MibTableColumn
dclVsLCoBytesFromNetwork = _DclVsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 11, 1, 4),
    _DclVsLCoBytesFromNetwork_Type()
)
dclVsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoBytesFromNetwork.setStatus("mandatory")
_DclVsLCoPathTable_Object = MibTable
dclVsLCoPathTable = _DclVsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 264)
)
if mibBuilder.loadTexts:
    dclVsLCoPathTable.setStatus("mandatory")
_DclVsLCoPathEntry_Object = MibTableRow
dclVsLCoPathEntry = _DclVsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 264, 1)
)
dclVsLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsLCoIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsLCoPathValue"),
)
if mibBuilder.loadTexts:
    dclVsLCoPathEntry.setStatus("mandatory")


class _DclVsLCoPathValue_Type(AsciiString):
    """Custom type dclVsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DclVsLCoPathValue_Type.__name__ = "AsciiString"
_DclVsLCoPathValue_Object = MibTableColumn
dclVsLCoPathValue = _DclVsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 3, 264, 1, 1),
    _DclVsLCoPathValue_Type()
)
dclVsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsLCoPathValue.setStatus("mandatory")
_DclVsProvTable_Object = MibTable
dclVsProvTable = _DclVsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 10)
)
if mibBuilder.loadTexts:
    dclVsProvTable.setStatus("mandatory")
_DclVsProvEntry_Object = MibTableRow
dclVsProvEntry = _DclVsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 10, 1)
)
dclVsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
)
if mibBuilder.loadTexts:
    dclVsProvEntry.setStatus("mandatory")


class _DclVsVsType_Type(Integer32):
    """Custom type dclVsVsType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamicVs", 0),
          ("permanent64kVs", 1))
    )


_DclVsVsType_Type.__name__ = "Integer32"
_DclVsVsType_Object = MibTableColumn
dclVsVsType = _DclVsVsType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 10, 1, 1),
    _DclVsVsType_Type()
)
dclVsVsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclVsVsType.setStatus("mandatory")
_DclVsOperTable_Object = MibTable
dclVsOperTable = _DclVsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11)
)
if mibBuilder.loadTexts:
    dclVsOperTable.setStatus("mandatory")
_DclVsOperEntry_Object = MibTableRow
dclVsOperEntry = _DclVsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11, 1)
)
dclVsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
)
if mibBuilder.loadTexts:
    dclVsOperEntry.setStatus("mandatory")


class _DclVsStatus_Type(Integer32):
    """Custom type dclVsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("seized", 1))
    )


_DclVsStatus_Type.__name__ = "Integer32"
_DclVsStatus_Object = MibTableColumn
dclVsStatus = _DclVsStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11, 1, 1),
    _DclVsStatus_Type()
)
dclVsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsStatus.setStatus("mandatory")


class _DclVsCallType_Type(Integer32):
    """Custom type dclVsCallType based on Integer32"""
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
        *(("n31KHz", 2),
          ("n64KbitS", 3),
          ("none", 0),
          ("speech", 1))
    )


_DclVsCallType_Type.__name__ = "Integer32"
_DclVsCallType_Object = MibTableColumn
dclVsCallType = _DclVsCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11, 1, 3),
    _DclVsCallType_Type()
)
dclVsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsCallType.setStatus("mandatory")


class _DclVsReceivedAbBits_Type(Integer32):
    """Custom type dclVsReceivedAbBits based on Integer32"""
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
        *(("n31KHzRequest10", 2),
          ("n64KbitSRequest11", 3),
          ("none00", 0),
          ("normalServiceAvailable01", 1))
    )


_DclVsReceivedAbBits_Type.__name__ = "Integer32"
_DclVsReceivedAbBits_Object = MibTableColumn
dclVsReceivedAbBits = _DclVsReceivedAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11, 1, 4),
    _DclVsReceivedAbBits_Type()
)
dclVsReceivedAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsReceivedAbBits.setStatus("mandatory")


class _DclVsTransmittedAbBits_Type(Integer32):
    """Custom type dclVsTransmittedAbBits based on Integer32"""
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
        *(("channelOutOfService11", 3),
          ("none00", 0),
          ("normalServiceAvailable01", 1),
          ("specialServiceAck10", 2))
    )


_DclVsTransmittedAbBits_Type.__name__ = "Integer32"
_DclVsTransmittedAbBits_Object = MibTableColumn
dclVsTransmittedAbBits = _DclVsTransmittedAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 11, 1, 5),
    _DclVsTransmittedAbBits_Type()
)
dclVsTransmittedAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsTransmittedAbBits.setStatus("mandatory")
_DclVsStatsTable_Object = MibTable
dclVsStatsTable = _DclVsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 12)
)
if mibBuilder.loadTexts:
    dclVsStatsTable.setStatus("mandatory")
_DclVsStatsEntry_Object = MibTableRow
dclVsStatsEntry = _DclVsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 12, 1)
)
dclVsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
)
if mibBuilder.loadTexts:
    dclVsStatsEntry.setStatus("mandatory")
_DclVsTotalCalls_Type = Counter32
_DclVsTotalCalls_Object = MibTableColumn
dclVsTotalCalls = _DclVsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 12, 1, 1),
    _DclVsTotalCalls_Type()
)
dclVsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsTotalCalls.setStatus("mandatory")
_DclVsTotalCallSeconds_Type = Counter32
_DclVsTotalCallSeconds_Object = MibTableColumn
dclVsTotalCallSeconds = _DclVsTotalCallSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 12, 1, 2),
    _DclVsTotalCallSeconds_Type()
)
dclVsTotalCallSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsTotalCallSeconds.setStatus("mandatory")
_DclVsInvalidAbBits_Type = Counter32
_DclVsInvalidAbBits_Object = MibTableColumn
dclVsInvalidAbBits = _DclVsInvalidAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 12, 1, 3),
    _DclVsInvalidAbBits_Type()
)
dclVsInvalidAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsInvalidAbBits.setStatus("mandatory")
_DclVsStateTable_Object = MibTable
dclVsStateTable = _DclVsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 13)
)
if mibBuilder.loadTexts:
    dclVsStateTable.setStatus("mandatory")
_DclVsStateEntry_Object = MibTableRow
dclVsStateEntry = _DclVsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 13, 1)
)
dclVsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclVsIndex"),
)
if mibBuilder.loadTexts:
    dclVsStateEntry.setStatus("mandatory")


class _DclVsAdminState_Type(Integer32):
    """Custom type dclVsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DclVsAdminState_Type.__name__ = "Integer32"
_DclVsAdminState_Object = MibTableColumn
dclVsAdminState = _DclVsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 13, 1, 1),
    _DclVsAdminState_Type()
)
dclVsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsAdminState.setStatus("mandatory")


class _DclVsOperationalState_Type(Integer32):
    """Custom type dclVsOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclVsOperationalState_Type.__name__ = "Integer32"
_DclVsOperationalState_Object = MibTableColumn
dclVsOperationalState = _DclVsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 13, 1, 2),
    _DclVsOperationalState_Type()
)
dclVsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsOperationalState.setStatus("mandatory")


class _DclVsUsageState_Type(Integer32):
    """Custom type dclVsUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DclVsUsageState_Type.__name__ = "Integer32"
_DclVsUsageState_Object = MibTableColumn
dclVsUsageState = _DclVsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 4, 13, 1, 3),
    _DclVsUsageState_Type()
)
dclVsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclVsUsageState.setStatus("mandatory")
_DclProvTable_Object = MibTable
dclProvTable = _DclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10)
)
if mibBuilder.loadTexts:
    dclProvTable.setStatus("mandatory")
_DclProvEntry_Object = MibTableRow
dclProvEntry = _DclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1)
)
dclProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
)
if mibBuilder.loadTexts:
    dclProvEntry.setStatus("mandatory")


class _DclCommentText_Type(AsciiString):
    """Custom type dclCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DclCommentText_Type.__name__ = "AsciiString"
_DclCommentText_Object = MibTableColumn
dclCommentText = _DclCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 1),
    _DclCommentText_Type()
)
dclCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclCommentText.setStatus("mandatory")


class _DclRemoteNpi_Type(Integer32):
    """Custom type dclRemoteNpi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_DclRemoteNpi_Type.__name__ = "Integer32"
_DclRemoteNpi_Object = MibTableColumn
dclRemoteNpi = _DclRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 2),
    _DclRemoteNpi_Type()
)
dclRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclRemoteNpi.setStatus("mandatory")


class _DclRemoteDna_Type(DigitString):
    """Custom type dclRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DclRemoteDna_Type.__name__ = "DigitString"
_DclRemoteDna_Object = MibTableColumn
dclRemoteDna = _DclRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 3),
    _DclRemoteDna_Type()
)
dclRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclRemoteDna.setStatus("mandatory")
_DclDcme_Type = Link
_DclDcme_Object = MibTableColumn
dclDcme = _DclDcme_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 4),
    _DclDcme_Type()
)
dclDcme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclDcme.setStatus("mandatory")


class _DclIdlePattern_Type(Hex):
    """Custom type dclIdlePattern based on Hex"""
    defaultValue = 213

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DclIdlePattern_Type.__name__ = "Hex"
_DclIdlePattern_Object = MibTableColumn
dclIdlePattern = _DclIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 5),
    _DclIdlePattern_Type()
)
dclIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclIdlePattern.setStatus("mandatory")


class _DclAlternateIdlePattern_Type(Hex):
    """Custom type dclAlternateIdlePattern based on Hex"""
    defaultValue = 213

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DclAlternateIdlePattern_Type.__name__ = "Hex"
_DclAlternateIdlePattern_Object = MibTableColumn
dclAlternateIdlePattern = _DclAlternateIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 10, 1, 6),
    _DclAlternateIdlePattern_Type()
)
dclAlternateIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dclAlternateIdlePattern.setStatus("mandatory")
_DclStateTable_Object = MibTable
dclStateTable = _DclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 11)
)
if mibBuilder.loadTexts:
    dclStateTable.setStatus("mandatory")
_DclStateEntry_Object = MibTableRow
dclStateEntry = _DclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 11, 1)
)
dclStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
)
if mibBuilder.loadTexts:
    dclStateEntry.setStatus("mandatory")


class _DclAdminState_Type(Integer32):
    """Custom type dclAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DclAdminState_Type.__name__ = "Integer32"
_DclAdminState_Object = MibTableColumn
dclAdminState = _DclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 11, 1, 1),
    _DclAdminState_Type()
)
dclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclAdminState.setStatus("mandatory")


class _DclOperationalState_Type(Integer32):
    """Custom type dclOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DclOperationalState_Type.__name__ = "Integer32"
_DclOperationalState_Object = MibTableColumn
dclOperationalState = _DclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 11, 1, 2),
    _DclOperationalState_Type()
)
dclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclOperationalState.setStatus("mandatory")


class _DclUsageState_Type(Integer32):
    """Custom type dclUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DclUsageState_Type.__name__ = "Integer32"
_DclUsageState_Object = MibTableColumn
dclUsageState = _DclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 11, 1, 3),
    _DclUsageState_Type()
)
dclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclUsageState.setStatus("mandatory")
_DclOperTable_Object = MibTable
dclOperTable = _DclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12)
)
if mibBuilder.loadTexts:
    dclOperTable.setStatus("mandatory")
_DclOperEntry_Object = MibTableRow
dclOperEntry = _DclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1)
)
dclOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
)
if mibBuilder.loadTexts:
    dclOperEntry.setStatus("mandatory")


class _DclActiveSpeechCalls_Type(Gauge32):
    """Custom type dclActiveSpeechCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_DclActiveSpeechCalls_Type.__name__ = "Gauge32"
_DclActiveSpeechCalls_Object = MibTableColumn
dclActiveSpeechCalls = _DclActiveSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1, 1),
    _DclActiveSpeechCalls_Type()
)
dclActiveSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclActiveSpeechCalls.setStatus("mandatory")


class _DclActive3kHzCalls_Type(Gauge32):
    """Custom type dclActive3kHzCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_DclActive3kHzCalls_Type.__name__ = "Gauge32"
_DclActive3kHzCalls_Object = MibTableColumn
dclActive3kHzCalls = _DclActive3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1, 2),
    _DclActive3kHzCalls_Type()
)
dclActive3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclActive3kHzCalls.setStatus("mandatory")


class _DclActive64kCalls_Type(Gauge32):
    """Custom type dclActive64kCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_DclActive64kCalls_Type.__name__ = "Gauge32"
_DclActive64kCalls_Object = MibTableColumn
dclActive64kCalls = _DclActive64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1, 3),
    _DclActive64kCalls_Type()
)
dclActive64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclActive64kCalls.setStatus("mandatory")


class _DclReceivedTrmSignal_Type(Integer32):
    """Custom type dclReceivedTrmSignal based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dcmeClearOfTraffic111", 7),
          ("invalid001", 1),
          ("invalid010", 2),
          ("invalid011", 3),
          ("invalid100", 4),
          ("maintenanceReleaseAck110", 6),
          ("none000", 0),
          ("switchingCentreNormal101", 5))
    )


_DclReceivedTrmSignal_Type.__name__ = "Integer32"
_DclReceivedTrmSignal_Object = MibTableColumn
dclReceivedTrmSignal = _DclReceivedTrmSignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1, 4),
    _DclReceivedTrmSignal_Type()
)
dclReceivedTrmSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclReceivedTrmSignal.setStatus("mandatory")


class _DclTransmittedTrmSignal_Type(Integer32):
    """Custom type dclTransmittedTrmSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dcmeNormal100", 4),
          ("maintenanceReleaseRequest110", 6),
          ("no64KbitSCapacity101", 5),
          ("noCapacityAvailable111", 7),
          ("none000", 0))
    )


_DclTransmittedTrmSignal_Type.__name__ = "Integer32"
_DclTransmittedTrmSignal_Object = MibTableColumn
dclTransmittedTrmSignal = _DclTransmittedTrmSignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 12, 1, 5),
    _DclTransmittedTrmSignal_Type()
)
dclTransmittedTrmSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclTransmittedTrmSignal.setStatus("mandatory")
_DclStatsTable_Object = MibTable
dclStatsTable = _DclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13)
)
if mibBuilder.loadTexts:
    dclStatsTable.setStatus("mandatory")
_DclStatsEntry_Object = MibTableRow
dclStatsEntry = _DclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1)
)
dclStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DcmeMIB", "dclIndex"),
)
if mibBuilder.loadTexts:
    dclStatsEntry.setStatus("mandatory")
_DclTotalSpeechCalls_Type = Counter32
_DclTotalSpeechCalls_Object = MibTableColumn
dclTotalSpeechCalls = _DclTotalSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 1),
    _DclTotalSpeechCalls_Type()
)
dclTotalSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclTotalSpeechCalls.setStatus("mandatory")
_DclTotal3kHzCalls_Type = Counter32
_DclTotal3kHzCalls_Object = MibTableColumn
dclTotal3kHzCalls = _DclTotal3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 2),
    _DclTotal3kHzCalls_Type()
)
dclTotal3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclTotal3kHzCalls.setStatus("mandatory")
_DclTotal64kCalls_Type = Counter32
_DclTotal64kCalls_Object = MibTableColumn
dclTotal64kCalls = _DclTotal64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 3),
    _DclTotal64kCalls_Type()
)
dclTotal64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclTotal64kCalls.setStatus("mandatory")
_DclRejectedSpeechCalls_Type = Counter32
_DclRejectedSpeechCalls_Object = MibTableColumn
dclRejectedSpeechCalls = _DclRejectedSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 4),
    _DclRejectedSpeechCalls_Type()
)
dclRejectedSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclRejectedSpeechCalls.setStatus("mandatory")
_DclRejected3kHzCalls_Type = Counter32
_DclRejected3kHzCalls_Object = MibTableColumn
dclRejected3kHzCalls = _DclRejected3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 5),
    _DclRejected3kHzCalls_Type()
)
dclRejected3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclRejected3kHzCalls.setStatus("mandatory")
_DclRejected64kCalls_Type = Counter32
_DclRejected64kCalls_Object = MibTableColumn
dclRejected64kCalls = _DclRejected64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 6),
    _DclRejected64kCalls_Type()
)
dclRejected64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclRejected64kCalls.setStatus("mandatory")
_DclInvalidTrmSignals_Type = Counter32
_DclInvalidTrmSignals_Object = MibTableColumn
dclInvalidTrmSignals = _DclInvalidTrmSignals_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 130, 13, 1, 7),
    _DclInvalidTrmSignals_Type()
)
dclInvalidTrmSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dclInvalidTrmSignals.setStatus("mandatory")
_DcmeMIB_ObjectIdentity = ObjectIdentity
dcmeMIB = _DcmeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134)
)
_DcmeGroup_ObjectIdentity = ObjectIdentity
dcmeGroup = _DcmeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 1)
)
_DcmeGroupBE_ObjectIdentity = ObjectIdentity
dcmeGroupBE = _DcmeGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 1, 5)
)
_DcmeGroupBE01_ObjectIdentity = ObjectIdentity
dcmeGroupBE01 = _DcmeGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 1, 5, 2)
)
_DcmeGroupBE01A_ObjectIdentity = ObjectIdentity
dcmeGroupBE01A = _DcmeGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 1, 5, 2, 2)
)
_DcmeCapabilities_ObjectIdentity = ObjectIdentity
dcmeCapabilities = _DcmeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 3)
)
_DcmeCapabilitiesBE_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesBE = _DcmeCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 3, 5)
)
_DcmeCapabilitiesBE01_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesBE01 = _DcmeCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 3, 5, 2)
)
_DcmeCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesBE01A = _DcmeCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 134, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DcmeMIB",
    **{"dcme": dcme,
       "dcmeRowStatusTable": dcmeRowStatusTable,
       "dcmeRowStatusEntry": dcmeRowStatusEntry,
       "dcmeRowStatus": dcmeRowStatus,
       "dcmeComponentName": dcmeComponentName,
       "dcmeStorageType": dcmeStorageType,
       "dcmeIndex": dcmeIndex,
       "dcmeProfile": dcmeProfile,
       "dcmeProfileRowStatusTable": dcmeProfileRowStatusTable,
       "dcmeProfileRowStatusEntry": dcmeProfileRowStatusEntry,
       "dcmeProfileRowStatus": dcmeProfileRowStatus,
       "dcmeProfileComponentName": dcmeProfileComponentName,
       "dcmeProfileStorageType": dcmeProfileStorageType,
       "dcmeProfileIndex": dcmeProfileIndex,
       "dcmeProfileLCOpsTable": dcmeProfileLCOpsTable,
       "dcmeProfileLCOpsEntry": dcmeProfileLCOpsEntry,
       "dcmeProfileSetupPriority": dcmeProfileSetupPriority,
       "dcmeProfileHoldingPriority": dcmeProfileHoldingPriority,
       "dcmeProfileBumpPreference": dcmeProfileBumpPreference,
       "dcmeProfileRequiredTrafficType": dcmeProfileRequiredTrafficType,
       "dcmeProfilePermittedTrunkTypes": dcmeProfilePermittedTrunkTypes,
       "dcmeProfileRequiredSecurity": dcmeProfileRequiredSecurity,
       "dcmeProfileRequiredCustomerParm": dcmeProfileRequiredCustomerParm,
       "dcmeProfilePathAttributeToMinimize": dcmeProfilePathAttributeToMinimize,
       "dcmeProfileMaximumAcceptableCost": dcmeProfileMaximumAcceptableCost,
       "dcmeProfileMaximumAcceptableDelay": dcmeProfileMaximumAcceptableDelay,
       "dcmeProfileEmissionPriority": dcmeProfileEmissionPriority,
       "dcmeProfileDiscardPriority": dcmeProfileDiscardPriority,
       "dcmeProfilePathFailureAction": dcmeProfilePathFailureAction,
       "dcmeProfileOptimization": dcmeProfileOptimization,
       "dcmeProfileFrOpsTable": dcmeProfileFrOpsTable,
       "dcmeProfileFrOpsEntry": dcmeProfileFrOpsEntry,
       "dcmeProfileVoiceEncoding": dcmeProfileVoiceEncoding,
       "dcmeProfileMaxVoiceBitRate": dcmeProfileMaxVoiceBitRate,
       "dcmeProfileMinVoiceBitRate": dcmeProfileMinVoiceBitRate,
       "dcmeProfileVoiceTrafficOptimization": dcmeProfileVoiceTrafficOptimization,
       "dcmeProfileSilenceSuppression": dcmeProfileSilenceSuppression,
       "dcmeProfileSilenceSuppressionFactor": dcmeProfileSilenceSuppressionFactor,
       "dcmeProfileEchoCancellation": dcmeProfileEchoCancellation,
       "dcmeProfileModemFaxEncoding": dcmeProfileModemFaxEncoding,
       "dcmeProfileMaxModemFaxG711G726Rate": dcmeProfileMaxModemFaxG711G726Rate,
       "dcmeProfileMinModemFaxG711G726Rate": dcmeProfileMinModemFaxG711G726Rate,
       "dcmeProfileFaxIdleSuppressionG711G726": dcmeProfileFaxIdleSuppressionG711G726,
       "dcmeProfileInsertedOutputDelay": dcmeProfileInsertedOutputDelay,
       "dcmeProfileIngressAudioGain": dcmeProfileIngressAudioGain,
       "dcmeProfileEgressAudioGain": dcmeProfileEgressAudioGain,
       "dcmeProfileSpeechHangoverTime": dcmeProfileSpeechHangoverTime,
       "dcmeProfileComfortNoiseCap": dcmeProfileComfortNoiseCap,
       "dcmeProfileModemFaxSpeechDiscrim": dcmeProfileModemFaxSpeechDiscrim,
       "dcmeProfileV17EncodedAsG711G726": dcmeProfileV17EncodedAsG711G726,
       "dcmeProfileDtmfRegeneration": dcmeProfileDtmfRegeneration,
       "dcmeProfileMaxFaxRelayRate": dcmeProfileMaxFaxRelayRate,
       "dcmeProvTable": dcmeProvTable,
       "dcmeProvEntry": dcmeProvEntry,
       "dcmeCommentText": dcmeCommentText,
       "dcmePreestablishedConnections": dcmePreestablishedConnections,
       "dcmeTrmThreshold": dcmeTrmThreshold,
       "dcmeTrmSignalChangeInterval": dcmeTrmSignalChangeInterval,
       "dcmeSpeechAlarmThreshold": dcmeSpeechAlarmThreshold,
       "dcmeAudio3kHzAlarmThreshold": dcmeAudio3kHzAlarmThreshold,
       "dcmeUnrestricted64kAlarmThreshold": dcmeUnrestricted64kAlarmThreshold,
       "dcmeAlarmTimeInterval": dcmeAlarmTimeInterval,
       "dcmeMaxUnrestricted64kCalls": dcmeMaxUnrestricted64kCalls,
       "dcmeStateTable": dcmeStateTable,
       "dcmeStateEntry": dcmeStateEntry,
       "dcmeAdminState": dcmeAdminState,
       "dcmeOperationalState": dcmeOperationalState,
       "dcmeUsageState": dcmeUsageState,
       "dcmeStatsTable": dcmeStatsTable,
       "dcmeStatsEntry": dcmeStatsEntry,
       "dcmeTrm64kNotAvailable": dcmeTrm64kNotAvailable,
       "dcmeTrmSpeechNotAvailable": dcmeTrmSpeechNotAvailable,
       "dcmeDLinksTable": dcmeDLinksTable,
       "dcmeDLinksEntry": dcmeDLinksEntry,
       "dcmeDLinksValue": dcmeDLinksValue,
       "dcmeDLinksRowStatus": dcmeDLinksRowStatus,
       "dcmeActiveDcmeLinksTable": dcmeActiveDcmeLinksTable,
       "dcmeActiveDcmeLinksEntry": dcmeActiveDcmeLinksEntry,
       "dcmeActiveDcmeLinksValue": dcmeActiveDcmeLinksValue,
       "dcl": dcl,
       "dclRowStatusTable": dclRowStatusTable,
       "dclRowStatusEntry": dclRowStatusEntry,
       "dclRowStatus": dclRowStatus,
       "dclComponentName": dclComponentName,
       "dclStorageType": dclStorageType,
       "dclIndex": dclIndex,
       "dclDna": dclDna,
       "dclDnaRowStatusTable": dclDnaRowStatusTable,
       "dclDnaRowStatusEntry": dclDnaRowStatusEntry,
       "dclDnaRowStatus": dclDnaRowStatus,
       "dclDnaComponentName": dclDnaComponentName,
       "dclDnaStorageType": dclDnaStorageType,
       "dclDnaIndex": dclDnaIndex,
       "dclDnaAddressTable": dclDnaAddressTable,
       "dclDnaAddressEntry": dclDnaAddressEntry,
       "dclDnaNumberingPlanIndicator": dclDnaNumberingPlanIndicator,
       "dclDnaDataNetworkAddress": dclDnaDataNetworkAddress,
       "dclFramer": dclFramer,
       "dclFramerRowStatusTable": dclFramerRowStatusTable,
       "dclFramerRowStatusEntry": dclFramerRowStatusEntry,
       "dclFramerRowStatus": dclFramerRowStatus,
       "dclFramerComponentName": dclFramerComponentName,
       "dclFramerStorageType": dclFramerStorageType,
       "dclFramerIndex": dclFramerIndex,
       "dclFramerProvTable": dclFramerProvTable,
       "dclFramerProvEntry": dclFramerProvEntry,
       "dclFramerInterfaceName": dclFramerInterfaceName,
       "dclFramerStateTable": dclFramerStateTable,
       "dclFramerStateEntry": dclFramerStateEntry,
       "dclFramerAdminState": dclFramerAdminState,
       "dclFramerOperationalState": dclFramerOperationalState,
       "dclFramerUsageState": dclFramerUsageState,
       "dclVs": dclVs,
       "dclVsRowStatusTable": dclVsRowStatusTable,
       "dclVsRowStatusEntry": dclVsRowStatusEntry,
       "dclVsRowStatus": dclVsRowStatus,
       "dclVsComponentName": dclVsComponentName,
       "dclVsStorageType": dclVsStorageType,
       "dclVsIndex": dclVsIndex,
       "dclVsFramer": dclVsFramer,
       "dclVsFramerRowStatusTable": dclVsFramerRowStatusTable,
       "dclVsFramerRowStatusEntry": dclVsFramerRowStatusEntry,
       "dclVsFramerRowStatus": dclVsFramerRowStatus,
       "dclVsFramerComponentName": dclVsFramerComponentName,
       "dclVsFramerStorageType": dclVsFramerStorageType,
       "dclVsFramerIndex": dclVsFramerIndex,
       "dclVsFramerVfpDebug": dclVsFramerVfpDebug,
       "dclVsFramerVfpDebugRowStatusTable": dclVsFramerVfpDebugRowStatusTable,
       "dclVsFramerVfpDebugRowStatusEntry": dclVsFramerVfpDebugRowStatusEntry,
       "dclVsFramerVfpDebugRowStatus": dclVsFramerVfpDebugRowStatus,
       "dclVsFramerVfpDebugComponentName": dclVsFramerVfpDebugComponentName,
       "dclVsFramerVfpDebugStorageType": dclVsFramerVfpDebugStorageType,
       "dclVsFramerVfpDebugIndex": dclVsFramerVfpDebugIndex,
       "dclVsFramerMvpDebug": dclVsFramerMvpDebug,
       "dclVsFramerMvpDebugRowStatusTable": dclVsFramerMvpDebugRowStatusTable,
       "dclVsFramerMvpDebugRowStatusEntry": dclVsFramerMvpDebugRowStatusEntry,
       "dclVsFramerMvpDebugRowStatus": dclVsFramerMvpDebugRowStatus,
       "dclVsFramerMvpDebugComponentName": dclVsFramerMvpDebugComponentName,
       "dclVsFramerMvpDebugStorageType": dclVsFramerMvpDebugStorageType,
       "dclVsFramerMvpDebugIndex": dclVsFramerMvpDebugIndex,
       "dclVsFramerPcmCapture": dclVsFramerPcmCapture,
       "dclVsFramerPcmCaptureRowStatusTable": dclVsFramerPcmCaptureRowStatusTable,
       "dclVsFramerPcmCaptureRowStatusEntry": dclVsFramerPcmCaptureRowStatusEntry,
       "dclVsFramerPcmCaptureRowStatus": dclVsFramerPcmCaptureRowStatus,
       "dclVsFramerPcmCaptureComponentName": dclVsFramerPcmCaptureComponentName,
       "dclVsFramerPcmCaptureStorageType": dclVsFramerPcmCaptureStorageType,
       "dclVsFramerPcmCaptureIndex": dclVsFramerPcmCaptureIndex,
       "dclVsFramerProvTable": dclVsFramerProvTable,
       "dclVsFramerProvEntry": dclVsFramerProvEntry,
       "dclVsFramerInterfaceName": dclVsFramerInterfaceName,
       "dclVsFramerStateTable": dclVsFramerStateTable,
       "dclVsFramerStateEntry": dclVsFramerStateEntry,
       "dclVsFramerAdminState": dclVsFramerAdminState,
       "dclVsFramerOperationalState": dclVsFramerOperationalState,
       "dclVsFramerUsageState": dclVsFramerUsageState,
       "dclVsFramerStatsTable": dclVsFramerStatsTable,
       "dclVsFramerStatsEntry": dclVsFramerStatsEntry,
       "dclVsFramerTotalCells": dclVsFramerTotalCells,
       "dclVsFramerAudioCells": dclVsFramerAudioCells,
       "dclVsFramerSilenceCells": dclVsFramerSilenceCells,
       "dclVsFramerModemCells": dclVsFramerModemCells,
       "dclVsFramerCurrentEncodingRate": dclVsFramerCurrentEncodingRate,
       "dclVsFramerLrcErrors": dclVsFramerLrcErrors,
       "dclVsFramerFrmLostInNetwork": dclVsFramerFrmLostInNetwork,
       "dclVsFramerFrmUnderRuns": dclVsFramerFrmUnderRuns,
       "dclVsFramerFrmDumped": dclVsFramerFrmDumped,
       "dclVsFramerModemSilenceCells": dclVsFramerModemSilenceCells,
       "dclVsFramerCurrentEncoding": dclVsFramerCurrentEncoding,
       "dclVsFramerTptStatus": dclVsFramerTptStatus,
       "dclVsFramerFaxRelayCells": dclVsFramerFaxRelayCells,
       "dclVsFramerModemFaxCells": dclVsFramerModemFaxCells,
       "dclVsFramerFaxIdleCells": dclVsFramerFaxIdleCells,
       "dclVsFramerOperTable": dclVsFramerOperTable,
       "dclVsFramerOperEntry": dclVsFramerOperEntry,
       "dclVsFramerOpCurrentEncoding": dclVsFramerOpCurrentEncoding,
       "dclVsFramerCurrentRate": dclVsFramerCurrentRate,
       "dclVsFramerOpTptStatus": dclVsFramerOpTptStatus,
       "dclVsFramerNegTable": dclVsFramerNegTable,
       "dclVsFramerNegEntry": dclVsFramerNegEntry,
       "dclVsFramerNegotiatedSilenceSuppression": dclVsFramerNegotiatedSilenceSuppression,
       "dclVsFramerNegotiatedFisG711G726": dclVsFramerNegotiatedFisG711G726,
       "dclVsFramerNegotiatedDtmfRegeneration": dclVsFramerNegotiatedDtmfRegeneration,
       "dclVsFramerNegotiatedV17AsG711G726": dclVsFramerNegotiatedV17AsG711G726,
       "dclVsFramerNegotiatedTandemPassThrough": dclVsFramerNegotiatedTandemPassThrough,
       "dclVsFramerFrmToNetworkTable": dclVsFramerFrmToNetworkTable,
       "dclVsFramerFrmToNetworkEntry": dclVsFramerFrmToNetworkEntry,
       "dclVsFramerFrmToNetworkIndex": dclVsFramerFrmToNetworkIndex,
       "dclVsFramerFrmToNetworkValue": dclVsFramerFrmToNetworkValue,
       "dclVsFramerFrmFromNetworkTable": dclVsFramerFrmFromNetworkTable,
       "dclVsFramerFrmFromNetworkEntry": dclVsFramerFrmFromNetworkEntry,
       "dclVsFramerFrmFromNetworkIndex": dclVsFramerFrmFromNetworkIndex,
       "dclVsFramerFrmFromNetworkValue": dclVsFramerFrmFromNetworkValue,
       "dclVsFramerNEncodingTable": dclVsFramerNEncodingTable,
       "dclVsFramerNEncodingEntry": dclVsFramerNEncodingEntry,
       "dclVsFramerNEncodingIndex": dclVsFramerNEncodingIndex,
       "dclVsFramerNEncodingValue": dclVsFramerNEncodingValue,
       "dclVsFramerNRatesTable": dclVsFramerNRatesTable,
       "dclVsFramerNRatesEntry": dclVsFramerNRatesEntry,
       "dclVsFramerNRatesTrafficIndex": dclVsFramerNRatesTrafficIndex,
       "dclVsFramerNRatesRateIndex": dclVsFramerNRatesRateIndex,
       "dclVsFramerNRatesValue": dclVsFramerNRatesValue,
       "dclVsLCo": dclVsLCo,
       "dclVsLCoRowStatusTable": dclVsLCoRowStatusTable,
       "dclVsLCoRowStatusEntry": dclVsLCoRowStatusEntry,
       "dclVsLCoRowStatus": dclVsLCoRowStatus,
       "dclVsLCoComponentName": dclVsLCoComponentName,
       "dclVsLCoStorageType": dclVsLCoStorageType,
       "dclVsLCoIndex": dclVsLCoIndex,
       "dclVsLCoPathDataTable": dclVsLCoPathDataTable,
       "dclVsLCoPathDataEntry": dclVsLCoPathDataEntry,
       "dclVsLCoState": dclVsLCoState,
       "dclVsLCoOverrideRemoteName": dclVsLCoOverrideRemoteName,
       "dclVsLCoEnd": dclVsLCoEnd,
       "dclVsLCoCostMetric": dclVsLCoCostMetric,
       "dclVsLCoDelayMetric": dclVsLCoDelayMetric,
       "dclVsLCoRoundTripDelay": dclVsLCoRoundTripDelay,
       "dclVsLCoSetupPriority": dclVsLCoSetupPriority,
       "dclVsLCoHoldingPriority": dclVsLCoHoldingPriority,
       "dclVsLCoRequiredTxBandwidth": dclVsLCoRequiredTxBandwidth,
       "dclVsLCoRequiredRxBandwidth": dclVsLCoRequiredRxBandwidth,
       "dclVsLCoRequiredTrafficType": dclVsLCoRequiredTrafficType,
       "dclVsLCoPermittedTrunkTypes": dclVsLCoPermittedTrunkTypes,
       "dclVsLCoRequiredSecurity": dclVsLCoRequiredSecurity,
       "dclVsLCoRequiredCustomerParameter": dclVsLCoRequiredCustomerParameter,
       "dclVsLCoEmissionPriority": dclVsLCoEmissionPriority,
       "dclVsLCoDiscardPriority": dclVsLCoDiscardPriority,
       "dclVsLCoPathType": dclVsLCoPathType,
       "dclVsLCoRetryCount": dclVsLCoRetryCount,
       "dclVsLCoPathFailureCount": dclVsLCoPathFailureCount,
       "dclVsLCoReasonForNoRoute": dclVsLCoReasonForNoRoute,
       "dclVsLCoLastTearDownReason": dclVsLCoLastTearDownReason,
       "dclVsLCoPathFailureAction": dclVsLCoPathFailureAction,
       "dclVsLCoBumpPreference": dclVsLCoBumpPreference,
       "dclVsLCoOptimization": dclVsLCoOptimization,
       "dclVsLCoPathUpDateTime": dclVsLCoPathUpDateTime,
       "dclVsLCoStatsTable": dclVsLCoStatsTable,
       "dclVsLCoStatsEntry": dclVsLCoStatsEntry,
       "dclVsLCoPktsToNetwork": dclVsLCoPktsToNetwork,
       "dclVsLCoBytesToNetwork": dclVsLCoBytesToNetwork,
       "dclVsLCoPktsFromNetwork": dclVsLCoPktsFromNetwork,
       "dclVsLCoBytesFromNetwork": dclVsLCoBytesFromNetwork,
       "dclVsLCoPathTable": dclVsLCoPathTable,
       "dclVsLCoPathEntry": dclVsLCoPathEntry,
       "dclVsLCoPathValue": dclVsLCoPathValue,
       "dclVsProvTable": dclVsProvTable,
       "dclVsProvEntry": dclVsProvEntry,
       "dclVsVsType": dclVsVsType,
       "dclVsOperTable": dclVsOperTable,
       "dclVsOperEntry": dclVsOperEntry,
       "dclVsStatus": dclVsStatus,
       "dclVsCallType": dclVsCallType,
       "dclVsReceivedAbBits": dclVsReceivedAbBits,
       "dclVsTransmittedAbBits": dclVsTransmittedAbBits,
       "dclVsStatsTable": dclVsStatsTable,
       "dclVsStatsEntry": dclVsStatsEntry,
       "dclVsTotalCalls": dclVsTotalCalls,
       "dclVsTotalCallSeconds": dclVsTotalCallSeconds,
       "dclVsInvalidAbBits": dclVsInvalidAbBits,
       "dclVsStateTable": dclVsStateTable,
       "dclVsStateEntry": dclVsStateEntry,
       "dclVsAdminState": dclVsAdminState,
       "dclVsOperationalState": dclVsOperationalState,
       "dclVsUsageState": dclVsUsageState,
       "dclProvTable": dclProvTable,
       "dclProvEntry": dclProvEntry,
       "dclCommentText": dclCommentText,
       "dclRemoteNpi": dclRemoteNpi,
       "dclRemoteDna": dclRemoteDna,
       "dclDcme": dclDcme,
       "dclIdlePattern": dclIdlePattern,
       "dclAlternateIdlePattern": dclAlternateIdlePattern,
       "dclStateTable": dclStateTable,
       "dclStateEntry": dclStateEntry,
       "dclAdminState": dclAdminState,
       "dclOperationalState": dclOperationalState,
       "dclUsageState": dclUsageState,
       "dclOperTable": dclOperTable,
       "dclOperEntry": dclOperEntry,
       "dclActiveSpeechCalls": dclActiveSpeechCalls,
       "dclActive3kHzCalls": dclActive3kHzCalls,
       "dclActive64kCalls": dclActive64kCalls,
       "dclReceivedTrmSignal": dclReceivedTrmSignal,
       "dclTransmittedTrmSignal": dclTransmittedTrmSignal,
       "dclStatsTable": dclStatsTable,
       "dclStatsEntry": dclStatsEntry,
       "dclTotalSpeechCalls": dclTotalSpeechCalls,
       "dclTotal3kHzCalls": dclTotal3kHzCalls,
       "dclTotal64kCalls": dclTotal64kCalls,
       "dclRejectedSpeechCalls": dclRejectedSpeechCalls,
       "dclRejected3kHzCalls": dclRejected3kHzCalls,
       "dclRejected64kCalls": dclRejected64kCalls,
       "dclInvalidTrmSignals": dclInvalidTrmSignals,
       "dcmeMIB": dcmeMIB,
       "dcmeGroup": dcmeGroup,
       "dcmeGroupBE": dcmeGroupBE,
       "dcmeGroupBE01": dcmeGroupBE01,
       "dcmeGroupBE01A": dcmeGroupBE01A,
       "dcmeCapabilities": dcmeCapabilities,
       "dcmeCapabilitiesBE": dcmeCapabilitiesBE,
       "dcmeCapabilitiesBE01": dcmeCapabilitiesBE01,
       "dcmeCapabilitiesBE01A": dcmeCapabilitiesBE01A}
)
