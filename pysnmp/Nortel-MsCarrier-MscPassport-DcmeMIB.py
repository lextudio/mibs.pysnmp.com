# SNMP MIB module (Nortel-MsCarrier-MscPassport-DcmeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DcmeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:09 2024
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
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
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
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "FixedPoint1",
    "Hex",
    "Link",
    "NonReplicated",
    "PassportCounter64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscDcme_ObjectIdentity = ObjectIdentity
mscDcme = _MscDcme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129)
)
_MscDcmeRowStatusTable_Object = MibTable
mscDcmeRowStatusTable = _MscDcmeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1)
)
if mibBuilder.loadTexts:
    mscDcmeRowStatusTable.setStatus("mandatory")
_MscDcmeRowStatusEntry_Object = MibTableRow
mscDcmeRowStatusEntry = _MscDcmeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1, 1)
)
mscDcmeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeRowStatusEntry.setStatus("mandatory")
_MscDcmeRowStatus_Type = RowStatus
_MscDcmeRowStatus_Object = MibTableColumn
mscDcmeRowStatus = _MscDcmeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1, 1, 1),
    _MscDcmeRowStatus_Type()
)
mscDcmeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeRowStatus.setStatus("mandatory")
_MscDcmeComponentName_Type = DisplayString
_MscDcmeComponentName_Object = MibTableColumn
mscDcmeComponentName = _MscDcmeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1, 1, 2),
    _MscDcmeComponentName_Type()
)
mscDcmeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeComponentName.setStatus("mandatory")
_MscDcmeStorageType_Type = StorageType
_MscDcmeStorageType_Object = MibTableColumn
mscDcmeStorageType = _MscDcmeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1, 1, 4),
    _MscDcmeStorageType_Type()
)
mscDcmeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeStorageType.setStatus("mandatory")


class _MscDcmeIndex_Type(Integer32):
    """Custom type mscDcmeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscDcmeIndex_Type.__name__ = "Integer32"
_MscDcmeIndex_Object = MibTableColumn
mscDcmeIndex = _MscDcmeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 1, 1, 10),
    _MscDcmeIndex_Type()
)
mscDcmeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDcmeIndex.setStatus("mandatory")
_MscDcmeProfile_ObjectIdentity = ObjectIdentity
mscDcmeProfile = _MscDcmeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2)
)
_MscDcmeProfileRowStatusTable_Object = MibTable
mscDcmeProfileRowStatusTable = _MscDcmeProfileRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1)
)
if mibBuilder.loadTexts:
    mscDcmeProfileRowStatusTable.setStatus("mandatory")
_MscDcmeProfileRowStatusEntry_Object = MibTableRow
mscDcmeProfileRowStatusEntry = _MscDcmeProfileRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1, 1)
)
mscDcmeProfileRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeProfileRowStatusEntry.setStatus("mandatory")
_MscDcmeProfileRowStatus_Type = RowStatus
_MscDcmeProfileRowStatus_Object = MibTableColumn
mscDcmeProfileRowStatus = _MscDcmeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1, 1, 1),
    _MscDcmeProfileRowStatus_Type()
)
mscDcmeProfileRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeProfileRowStatus.setStatus("mandatory")
_MscDcmeProfileComponentName_Type = DisplayString
_MscDcmeProfileComponentName_Object = MibTableColumn
mscDcmeProfileComponentName = _MscDcmeProfileComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1, 1, 2),
    _MscDcmeProfileComponentName_Type()
)
mscDcmeProfileComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeProfileComponentName.setStatus("mandatory")
_MscDcmeProfileStorageType_Type = StorageType
_MscDcmeProfileStorageType_Object = MibTableColumn
mscDcmeProfileStorageType = _MscDcmeProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1, 1, 4),
    _MscDcmeProfileStorageType_Type()
)
mscDcmeProfileStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeProfileStorageType.setStatus("mandatory")
_MscDcmeProfileIndex_Type = NonReplicated
_MscDcmeProfileIndex_Object = MibTableColumn
mscDcmeProfileIndex = _MscDcmeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 1, 1, 10),
    _MscDcmeProfileIndex_Type()
)
mscDcmeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDcmeProfileIndex.setStatus("mandatory")
_MscDcmeProfileLCOpsTable_Object = MibTable
mscDcmeProfileLCOpsTable = _MscDcmeProfileLCOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10)
)
if mibBuilder.loadTexts:
    mscDcmeProfileLCOpsTable.setStatus("mandatory")
_MscDcmeProfileLCOpsEntry_Object = MibTableRow
mscDcmeProfileLCOpsEntry = _MscDcmeProfileLCOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1)
)
mscDcmeProfileLCOpsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeProfileLCOpsEntry.setStatus("mandatory")


class _MscDcmeProfileSetupPriority_Type(Unsigned32):
    """Custom type mscDcmeProfileSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscDcmeProfileSetupPriority_Type.__name__ = "Unsigned32"
_MscDcmeProfileSetupPriority_Object = MibTableColumn
mscDcmeProfileSetupPriority = _MscDcmeProfileSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 1),
    _MscDcmeProfileSetupPriority_Type()
)
mscDcmeProfileSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileSetupPriority.setStatus("mandatory")


class _MscDcmeProfileHoldingPriority_Type(Unsigned32):
    """Custom type mscDcmeProfileHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscDcmeProfileHoldingPriority_Type.__name__ = "Unsigned32"
_MscDcmeProfileHoldingPriority_Object = MibTableColumn
mscDcmeProfileHoldingPriority = _MscDcmeProfileHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 2),
    _MscDcmeProfileHoldingPriority_Type()
)
mscDcmeProfileHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileHoldingPriority.setStatus("mandatory")


class _MscDcmeProfileBumpPreference_Type(Integer32):
    """Custom type mscDcmeProfileBumpPreference based on Integer32"""
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


_MscDcmeProfileBumpPreference_Type.__name__ = "Integer32"
_MscDcmeProfileBumpPreference_Object = MibTableColumn
mscDcmeProfileBumpPreference = _MscDcmeProfileBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 3),
    _MscDcmeProfileBumpPreference_Type()
)
mscDcmeProfileBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileBumpPreference.setStatus("mandatory")


class _MscDcmeProfileRequiredTrafficType_Type(Integer32):
    """Custom type mscDcmeProfileRequiredTrafficType based on Integer32"""
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


_MscDcmeProfileRequiredTrafficType_Type.__name__ = "Integer32"
_MscDcmeProfileRequiredTrafficType_Object = MibTableColumn
mscDcmeProfileRequiredTrafficType = _MscDcmeProfileRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 4),
    _MscDcmeProfileRequiredTrafficType_Type()
)
mscDcmeProfileRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileRequiredTrafficType.setStatus("mandatory")


class _MscDcmeProfilePermittedTrunkTypes_Type(OctetString):
    """Custom type mscDcmeProfilePermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDcmeProfilePermittedTrunkTypes_Type.__name__ = "OctetString"
_MscDcmeProfilePermittedTrunkTypes_Object = MibTableColumn
mscDcmeProfilePermittedTrunkTypes = _MscDcmeProfilePermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 5),
    _MscDcmeProfilePermittedTrunkTypes_Type()
)
mscDcmeProfilePermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfilePermittedTrunkTypes.setStatus("mandatory")


class _MscDcmeProfileRequiredSecurity_Type(Unsigned32):
    """Custom type mscDcmeProfileRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscDcmeProfileRequiredSecurity_Type.__name__ = "Unsigned32"
_MscDcmeProfileRequiredSecurity_Object = MibTableColumn
mscDcmeProfileRequiredSecurity = _MscDcmeProfileRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 6),
    _MscDcmeProfileRequiredSecurity_Type()
)
mscDcmeProfileRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileRequiredSecurity.setStatus("mandatory")


class _MscDcmeProfileRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscDcmeProfileRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscDcmeProfileRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscDcmeProfileRequiredCustomerParm_Object = MibTableColumn
mscDcmeProfileRequiredCustomerParm = _MscDcmeProfileRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 7),
    _MscDcmeProfileRequiredCustomerParm_Type()
)
mscDcmeProfileRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileRequiredCustomerParm.setStatus("mandatory")


class _MscDcmeProfilePathAttributeToMinimize_Type(Integer32):
    """Custom type mscDcmeProfilePathAttributeToMinimize based on Integer32"""
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


_MscDcmeProfilePathAttributeToMinimize_Type.__name__ = "Integer32"
_MscDcmeProfilePathAttributeToMinimize_Object = MibTableColumn
mscDcmeProfilePathAttributeToMinimize = _MscDcmeProfilePathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 8),
    _MscDcmeProfilePathAttributeToMinimize_Type()
)
mscDcmeProfilePathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfilePathAttributeToMinimize.setStatus("mandatory")


class _MscDcmeProfileMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscDcmeProfileMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDcmeProfileMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscDcmeProfileMaximumAcceptableCost_Object = MibTableColumn
mscDcmeProfileMaximumAcceptableCost = _MscDcmeProfileMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 9),
    _MscDcmeProfileMaximumAcceptableCost_Type()
)
mscDcmeProfileMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMaximumAcceptableCost.setStatus("mandatory")


class _MscDcmeProfileMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscDcmeProfileMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscDcmeProfileMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscDcmeProfileMaximumAcceptableDelay_Object = MibTableColumn
mscDcmeProfileMaximumAcceptableDelay = _MscDcmeProfileMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 10),
    _MscDcmeProfileMaximumAcceptableDelay_Type()
)
mscDcmeProfileMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMaximumAcceptableDelay.setStatus("mandatory")


class _MscDcmeProfileEmissionPriority_Type(Unsigned32):
    """Custom type mscDcmeProfileEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscDcmeProfileEmissionPriority_Type.__name__ = "Unsigned32"
_MscDcmeProfileEmissionPriority_Object = MibTableColumn
mscDcmeProfileEmissionPriority = _MscDcmeProfileEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 11),
    _MscDcmeProfileEmissionPriority_Type()
)
mscDcmeProfileEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileEmissionPriority.setStatus("mandatory")


class _MscDcmeProfileDiscardPriority_Type(Unsigned32):
    """Custom type mscDcmeProfileDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscDcmeProfileDiscardPriority_Type.__name__ = "Unsigned32"
_MscDcmeProfileDiscardPriority_Object = MibTableColumn
mscDcmeProfileDiscardPriority = _MscDcmeProfileDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 12),
    _MscDcmeProfileDiscardPriority_Type()
)
mscDcmeProfileDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileDiscardPriority.setStatus("mandatory")


class _MscDcmeProfilePathFailureAction_Type(Integer32):
    """Custom type mscDcmeProfilePathFailureAction based on Integer32"""
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


_MscDcmeProfilePathFailureAction_Type.__name__ = "Integer32"
_MscDcmeProfilePathFailureAction_Object = MibTableColumn
mscDcmeProfilePathFailureAction = _MscDcmeProfilePathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 13),
    _MscDcmeProfilePathFailureAction_Type()
)
mscDcmeProfilePathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfilePathFailureAction.setStatus("mandatory")


class _MscDcmeProfileOptimization_Type(Integer32):
    """Custom type mscDcmeProfileOptimization based on Integer32"""
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


_MscDcmeProfileOptimization_Type.__name__ = "Integer32"
_MscDcmeProfileOptimization_Object = MibTableColumn
mscDcmeProfileOptimization = _MscDcmeProfileOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 10, 1, 14),
    _MscDcmeProfileOptimization_Type()
)
mscDcmeProfileOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileOptimization.setStatus("mandatory")
_MscDcmeProfileFrOpsTable_Object = MibTable
mscDcmeProfileFrOpsTable = _MscDcmeProfileFrOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11)
)
if mibBuilder.loadTexts:
    mscDcmeProfileFrOpsTable.setStatus("mandatory")
_MscDcmeProfileFrOpsEntry_Object = MibTableRow
mscDcmeProfileFrOpsEntry = _MscDcmeProfileFrOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1)
)
mscDcmeProfileFrOpsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeProfileIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeProfileFrOpsEntry.setStatus("mandatory")


class _MscDcmeProfileVoiceEncoding_Type(Integer32):
    """Custom type mscDcmeProfileVoiceEncoding based on Integer32"""
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


_MscDcmeProfileVoiceEncoding_Type.__name__ = "Integer32"
_MscDcmeProfileVoiceEncoding_Object = MibTableColumn
mscDcmeProfileVoiceEncoding = _MscDcmeProfileVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 1),
    _MscDcmeProfileVoiceEncoding_Type()
)
mscDcmeProfileVoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileVoiceEncoding.setStatus("mandatory")


class _MscDcmeProfileMaxVoiceBitRate_Type(Integer32):
    """Custom type mscDcmeProfileMaxVoiceBitRate based on Integer32"""
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


_MscDcmeProfileMaxVoiceBitRate_Type.__name__ = "Integer32"
_MscDcmeProfileMaxVoiceBitRate_Object = MibTableColumn
mscDcmeProfileMaxVoiceBitRate = _MscDcmeProfileMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 2),
    _MscDcmeProfileMaxVoiceBitRate_Type()
)
mscDcmeProfileMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMaxVoiceBitRate.setStatus("mandatory")


class _MscDcmeProfileMinVoiceBitRate_Type(Integer32):
    """Custom type mscDcmeProfileMinVoiceBitRate based on Integer32"""
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


_MscDcmeProfileMinVoiceBitRate_Type.__name__ = "Integer32"
_MscDcmeProfileMinVoiceBitRate_Object = MibTableColumn
mscDcmeProfileMinVoiceBitRate = _MscDcmeProfileMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 3),
    _MscDcmeProfileMinVoiceBitRate_Type()
)
mscDcmeProfileMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMinVoiceBitRate.setStatus("mandatory")


class _MscDcmeProfileVoiceTrafficOptimization_Type(Integer32):
    """Custom type mscDcmeProfileVoiceTrafficOptimization based on Integer32"""
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


_MscDcmeProfileVoiceTrafficOptimization_Type.__name__ = "Integer32"
_MscDcmeProfileVoiceTrafficOptimization_Object = MibTableColumn
mscDcmeProfileVoiceTrafficOptimization = _MscDcmeProfileVoiceTrafficOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 4),
    _MscDcmeProfileVoiceTrafficOptimization_Type()
)
mscDcmeProfileVoiceTrafficOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileVoiceTrafficOptimization.setStatus("mandatory")


class _MscDcmeProfileSilenceSuppression_Type(Integer32):
    """Custom type mscDcmeProfileSilenceSuppression based on Integer32"""
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


_MscDcmeProfileSilenceSuppression_Type.__name__ = "Integer32"
_MscDcmeProfileSilenceSuppression_Object = MibTableColumn
mscDcmeProfileSilenceSuppression = _MscDcmeProfileSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 5),
    _MscDcmeProfileSilenceSuppression_Type()
)
mscDcmeProfileSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileSilenceSuppression.setStatus("mandatory")


class _MscDcmeProfileSilenceSuppressionFactor_Type(Unsigned32):
    """Custom type mscDcmeProfileSilenceSuppressionFactor based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MscDcmeProfileSilenceSuppressionFactor_Type.__name__ = "Unsigned32"
_MscDcmeProfileSilenceSuppressionFactor_Object = MibTableColumn
mscDcmeProfileSilenceSuppressionFactor = _MscDcmeProfileSilenceSuppressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 6),
    _MscDcmeProfileSilenceSuppressionFactor_Type()
)
mscDcmeProfileSilenceSuppressionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileSilenceSuppressionFactor.setStatus("mandatory")


class _MscDcmeProfileEchoCancellation_Type(Integer32):
    """Custom type mscDcmeProfileEchoCancellation based on Integer32"""
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


_MscDcmeProfileEchoCancellation_Type.__name__ = "Integer32"
_MscDcmeProfileEchoCancellation_Object = MibTableColumn
mscDcmeProfileEchoCancellation = _MscDcmeProfileEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 7),
    _MscDcmeProfileEchoCancellation_Type()
)
mscDcmeProfileEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileEchoCancellation.setStatus("mandatory")


class _MscDcmeProfileModemFaxEncoding_Type(Integer32):
    """Custom type mscDcmeProfileModemFaxEncoding based on Integer32"""
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


_MscDcmeProfileModemFaxEncoding_Type.__name__ = "Integer32"
_MscDcmeProfileModemFaxEncoding_Object = MibTableColumn
mscDcmeProfileModemFaxEncoding = _MscDcmeProfileModemFaxEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 9),
    _MscDcmeProfileModemFaxEncoding_Type()
)
mscDcmeProfileModemFaxEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileModemFaxEncoding.setStatus("mandatory")


class _MscDcmeProfileMaxModemFaxG711G726Rate_Type(Integer32):
    """Custom type mscDcmeProfileMaxModemFaxG711G726Rate based on Integer32"""
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


_MscDcmeProfileMaxModemFaxG711G726Rate_Type.__name__ = "Integer32"
_MscDcmeProfileMaxModemFaxG711G726Rate_Object = MibTableColumn
mscDcmeProfileMaxModemFaxG711G726Rate = _MscDcmeProfileMaxModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 10),
    _MscDcmeProfileMaxModemFaxG711G726Rate_Type()
)
mscDcmeProfileMaxModemFaxG711G726Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMaxModemFaxG711G726Rate.setStatus("mandatory")


class _MscDcmeProfileMinModemFaxG711G726Rate_Type(Integer32):
    """Custom type mscDcmeProfileMinModemFaxG711G726Rate based on Integer32"""
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


_MscDcmeProfileMinModemFaxG711G726Rate_Type.__name__ = "Integer32"
_MscDcmeProfileMinModemFaxG711G726Rate_Object = MibTableColumn
mscDcmeProfileMinModemFaxG711G726Rate = _MscDcmeProfileMinModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 11),
    _MscDcmeProfileMinModemFaxG711G726Rate_Type()
)
mscDcmeProfileMinModemFaxG711G726Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMinModemFaxG711G726Rate.setStatus("mandatory")


class _MscDcmeProfileFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type mscDcmeProfileFaxIdleSuppressionG711G726 based on Integer32"""
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


_MscDcmeProfileFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_MscDcmeProfileFaxIdleSuppressionG711G726_Object = MibTableColumn
mscDcmeProfileFaxIdleSuppressionG711G726 = _MscDcmeProfileFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 12),
    _MscDcmeProfileFaxIdleSuppressionG711G726_Type()
)
mscDcmeProfileFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileFaxIdleSuppressionG711G726.setStatus("mandatory")


class _MscDcmeProfileInsertedOutputDelay_Type(Integer32):
    """Custom type mscDcmeProfileInsertedOutputDelay based on Integer32"""
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


_MscDcmeProfileInsertedOutputDelay_Type.__name__ = "Integer32"
_MscDcmeProfileInsertedOutputDelay_Object = MibTableColumn
mscDcmeProfileInsertedOutputDelay = _MscDcmeProfileInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 13),
    _MscDcmeProfileInsertedOutputDelay_Type()
)
mscDcmeProfileInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileInsertedOutputDelay.setStatus("mandatory")


class _MscDcmeProfileIngressAudioGain_Type(Integer32):
    """Custom type mscDcmeProfileIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscDcmeProfileIngressAudioGain_Type.__name__ = "Integer32"
_MscDcmeProfileIngressAudioGain_Object = MibTableColumn
mscDcmeProfileIngressAudioGain = _MscDcmeProfileIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 14),
    _MscDcmeProfileIngressAudioGain_Type()
)
mscDcmeProfileIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileIngressAudioGain.setStatus("mandatory")


class _MscDcmeProfileEgressAudioGain_Type(Integer32):
    """Custom type mscDcmeProfileEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscDcmeProfileEgressAudioGain_Type.__name__ = "Integer32"
_MscDcmeProfileEgressAudioGain_Object = MibTableColumn
mscDcmeProfileEgressAudioGain = _MscDcmeProfileEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 15),
    _MscDcmeProfileEgressAudioGain_Type()
)
mscDcmeProfileEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileEgressAudioGain.setStatus("mandatory")


class _MscDcmeProfileSpeechHangoverTime_Type(Unsigned32):
    """Custom type mscDcmeProfileSpeechHangoverTime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_MscDcmeProfileSpeechHangoverTime_Type.__name__ = "Unsigned32"
_MscDcmeProfileSpeechHangoverTime_Object = MibTableColumn
mscDcmeProfileSpeechHangoverTime = _MscDcmeProfileSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 16),
    _MscDcmeProfileSpeechHangoverTime_Type()
)
mscDcmeProfileSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileSpeechHangoverTime.setStatus("mandatory")


class _MscDcmeProfileComfortNoiseCap_Type(Integer32):
    """Custom type mscDcmeProfileComfortNoiseCap based on Integer32"""
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


_MscDcmeProfileComfortNoiseCap_Type.__name__ = "Integer32"
_MscDcmeProfileComfortNoiseCap_Object = MibTableColumn
mscDcmeProfileComfortNoiseCap = _MscDcmeProfileComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 17),
    _MscDcmeProfileComfortNoiseCap_Type()
)
mscDcmeProfileComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileComfortNoiseCap.setStatus("mandatory")


class _MscDcmeProfileModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type mscDcmeProfileModemFaxSpeechDiscrim based on Integer32"""
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


_MscDcmeProfileModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_MscDcmeProfileModemFaxSpeechDiscrim_Object = MibTableColumn
mscDcmeProfileModemFaxSpeechDiscrim = _MscDcmeProfileModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 18),
    _MscDcmeProfileModemFaxSpeechDiscrim_Type()
)
mscDcmeProfileModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileModemFaxSpeechDiscrim.setStatus("mandatory")


class _MscDcmeProfileV17EncodedAsG711G726_Type(Integer32):
    """Custom type mscDcmeProfileV17EncodedAsG711G726 based on Integer32"""
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


_MscDcmeProfileV17EncodedAsG711G726_Type.__name__ = "Integer32"
_MscDcmeProfileV17EncodedAsG711G726_Object = MibTableColumn
mscDcmeProfileV17EncodedAsG711G726 = _MscDcmeProfileV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 19),
    _MscDcmeProfileV17EncodedAsG711G726_Type()
)
mscDcmeProfileV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileV17EncodedAsG711G726.setStatus("mandatory")


class _MscDcmeProfileDtmfRegeneration_Type(Integer32):
    """Custom type mscDcmeProfileDtmfRegeneration based on Integer32"""
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


_MscDcmeProfileDtmfRegeneration_Type.__name__ = "Integer32"
_MscDcmeProfileDtmfRegeneration_Object = MibTableColumn
mscDcmeProfileDtmfRegeneration = _MscDcmeProfileDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 20),
    _MscDcmeProfileDtmfRegeneration_Type()
)
mscDcmeProfileDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileDtmfRegeneration.setStatus("mandatory")


class _MscDcmeProfileMaxFaxRelayRate_Type(FixedPoint1):
    """Custom type mscDcmeProfileMaxFaxRelayRate based on FixedPoint1"""
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


_MscDcmeProfileMaxFaxRelayRate_Type.__name__ = "FixedPoint1"
_MscDcmeProfileMaxFaxRelayRate_Object = MibTableColumn
mscDcmeProfileMaxFaxRelayRate = _MscDcmeProfileMaxFaxRelayRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 2, 11, 1, 21),
    _MscDcmeProfileMaxFaxRelayRate_Type()
)
mscDcmeProfileMaxFaxRelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeProfileMaxFaxRelayRate.setStatus("mandatory")
_MscDcmeProvTable_Object = MibTable
mscDcmeProvTable = _MscDcmeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10)
)
if mibBuilder.loadTexts:
    mscDcmeProvTable.setStatus("mandatory")
_MscDcmeProvEntry_Object = MibTableRow
mscDcmeProvEntry = _MscDcmeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1)
)
mscDcmeProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeProvEntry.setStatus("mandatory")


class _MscDcmeCommentText_Type(AsciiString):
    """Custom type mscDcmeCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDcmeCommentText_Type.__name__ = "AsciiString"
_MscDcmeCommentText_Object = MibTableColumn
mscDcmeCommentText = _MscDcmeCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 1),
    _MscDcmeCommentText_Type()
)
mscDcmeCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeCommentText.setStatus("mandatory")


class _MscDcmePreestablishedConnections_Type(Unsigned32):
    """Custom type mscDcmePreestablishedConnections based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscDcmePreestablishedConnections_Type.__name__ = "Unsigned32"
_MscDcmePreestablishedConnections_Object = MibTableColumn
mscDcmePreestablishedConnections = _MscDcmePreestablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 2),
    _MscDcmePreestablishedConnections_Type()
)
mscDcmePreestablishedConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmePreestablishedConnections.setStatus("mandatory")


class _MscDcmeTrmThreshold_Type(Unsigned32):
    """Custom type mscDcmeTrmThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscDcmeTrmThreshold_Type.__name__ = "Unsigned32"
_MscDcmeTrmThreshold_Object = MibTableColumn
mscDcmeTrmThreshold = _MscDcmeTrmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 3),
    _MscDcmeTrmThreshold_Type()
)
mscDcmeTrmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeTrmThreshold.setStatus("mandatory")


class _MscDcmeTrmSignalChangeInterval_Type(Unsigned32):
    """Custom type mscDcmeTrmSignalChangeInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_MscDcmeTrmSignalChangeInterval_Type.__name__ = "Unsigned32"
_MscDcmeTrmSignalChangeInterval_Object = MibTableColumn
mscDcmeTrmSignalChangeInterval = _MscDcmeTrmSignalChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 4),
    _MscDcmeTrmSignalChangeInterval_Type()
)
mscDcmeTrmSignalChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeTrmSignalChangeInterval.setStatus("mandatory")


class _MscDcmeSpeechAlarmThreshold_Type(Unsigned32):
    """Custom type mscDcmeSpeechAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscDcmeSpeechAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDcmeSpeechAlarmThreshold_Object = MibTableColumn
mscDcmeSpeechAlarmThreshold = _MscDcmeSpeechAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 5),
    _MscDcmeSpeechAlarmThreshold_Type()
)
mscDcmeSpeechAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeSpeechAlarmThreshold.setStatus("mandatory")


class _MscDcmeAudio3kHzAlarmThreshold_Type(Unsigned32):
    """Custom type mscDcmeAudio3kHzAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscDcmeAudio3kHzAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDcmeAudio3kHzAlarmThreshold_Object = MibTableColumn
mscDcmeAudio3kHzAlarmThreshold = _MscDcmeAudio3kHzAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 6),
    _MscDcmeAudio3kHzAlarmThreshold_Type()
)
mscDcmeAudio3kHzAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeAudio3kHzAlarmThreshold.setStatus("mandatory")


class _MscDcmeUnrestricted64kAlarmThreshold_Type(Unsigned32):
    """Custom type mscDcmeUnrestricted64kAlarmThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscDcmeUnrestricted64kAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDcmeUnrestricted64kAlarmThreshold_Object = MibTableColumn
mscDcmeUnrestricted64kAlarmThreshold = _MscDcmeUnrestricted64kAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 7),
    _MscDcmeUnrestricted64kAlarmThreshold_Type()
)
mscDcmeUnrestricted64kAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeUnrestricted64kAlarmThreshold.setStatus("mandatory")


class _MscDcmeAlarmTimeInterval_Type(Unsigned32):
    """Custom type mscDcmeAlarmTimeInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_MscDcmeAlarmTimeInterval_Type.__name__ = "Unsigned32"
_MscDcmeAlarmTimeInterval_Object = MibTableColumn
mscDcmeAlarmTimeInterval = _MscDcmeAlarmTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 8),
    _MscDcmeAlarmTimeInterval_Type()
)
mscDcmeAlarmTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeAlarmTimeInterval.setStatus("mandatory")


class _MscDcmeMaxUnrestricted64kCalls_Type(Unsigned32):
    """Custom type mscDcmeMaxUnrestricted64kCalls based on Unsigned32"""
    defaultValue = 420

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_MscDcmeMaxUnrestricted64kCalls_Type.__name__ = "Unsigned32"
_MscDcmeMaxUnrestricted64kCalls_Object = MibTableColumn
mscDcmeMaxUnrestricted64kCalls = _MscDcmeMaxUnrestricted64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 10, 1, 9),
    _MscDcmeMaxUnrestricted64kCalls_Type()
)
mscDcmeMaxUnrestricted64kCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeMaxUnrestricted64kCalls.setStatus("mandatory")
_MscDcmeStateTable_Object = MibTable
mscDcmeStateTable = _MscDcmeStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 11)
)
if mibBuilder.loadTexts:
    mscDcmeStateTable.setStatus("mandatory")
_MscDcmeStateEntry_Object = MibTableRow
mscDcmeStateEntry = _MscDcmeStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 11, 1)
)
mscDcmeStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeStateEntry.setStatus("mandatory")


class _MscDcmeAdminState_Type(Integer32):
    """Custom type mscDcmeAdminState based on Integer32"""
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


_MscDcmeAdminState_Type.__name__ = "Integer32"
_MscDcmeAdminState_Object = MibTableColumn
mscDcmeAdminState = _MscDcmeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 11, 1, 1),
    _MscDcmeAdminState_Type()
)
mscDcmeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeAdminState.setStatus("mandatory")


class _MscDcmeOperationalState_Type(Integer32):
    """Custom type mscDcmeOperationalState based on Integer32"""
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


_MscDcmeOperationalState_Type.__name__ = "Integer32"
_MscDcmeOperationalState_Object = MibTableColumn
mscDcmeOperationalState = _MscDcmeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 11, 1, 2),
    _MscDcmeOperationalState_Type()
)
mscDcmeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeOperationalState.setStatus("mandatory")


class _MscDcmeUsageState_Type(Integer32):
    """Custom type mscDcmeUsageState based on Integer32"""
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


_MscDcmeUsageState_Type.__name__ = "Integer32"
_MscDcmeUsageState_Object = MibTableColumn
mscDcmeUsageState = _MscDcmeUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 11, 1, 3),
    _MscDcmeUsageState_Type()
)
mscDcmeUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeUsageState.setStatus("mandatory")
_MscDcmeStatsTable_Object = MibTable
mscDcmeStatsTable = _MscDcmeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 13)
)
if mibBuilder.loadTexts:
    mscDcmeStatsTable.setStatus("mandatory")
_MscDcmeStatsEntry_Object = MibTableRow
mscDcmeStatsEntry = _MscDcmeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 13, 1)
)
mscDcmeStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
)
if mibBuilder.loadTexts:
    mscDcmeStatsEntry.setStatus("mandatory")
_MscDcmeTrm64kNotAvailable_Type = Counter32
_MscDcmeTrm64kNotAvailable_Object = MibTableColumn
mscDcmeTrm64kNotAvailable = _MscDcmeTrm64kNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 13, 1, 1),
    _MscDcmeTrm64kNotAvailable_Type()
)
mscDcmeTrm64kNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeTrm64kNotAvailable.setStatus("mandatory")
_MscDcmeTrmSpeechNotAvailable_Type = Counter32
_MscDcmeTrmSpeechNotAvailable_Object = MibTableColumn
mscDcmeTrmSpeechNotAvailable = _MscDcmeTrmSpeechNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 13, 1, 2),
    _MscDcmeTrmSpeechNotAvailable_Type()
)
mscDcmeTrmSpeechNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeTrmSpeechNotAvailable.setStatus("mandatory")
_MscDcmeDLinksTable_Object = MibTable
mscDcmeDLinksTable = _MscDcmeDLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 419)
)
if mibBuilder.loadTexts:
    mscDcmeDLinksTable.setStatus("mandatory")
_MscDcmeDLinksEntry_Object = MibTableRow
mscDcmeDLinksEntry = _MscDcmeDLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 419, 1)
)
mscDcmeDLinksEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeDLinksValue"),
)
if mibBuilder.loadTexts:
    mscDcmeDLinksEntry.setStatus("mandatory")
_MscDcmeDLinksValue_Type = Link
_MscDcmeDLinksValue_Object = MibTableColumn
mscDcmeDLinksValue = _MscDcmeDLinksValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 419, 1, 1),
    _MscDcmeDLinksValue_Type()
)
mscDcmeDLinksValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDcmeDLinksValue.setStatus("mandatory")
_MscDcmeDLinksRowStatus_Type = RowStatus
_MscDcmeDLinksRowStatus_Object = MibTableColumn
mscDcmeDLinksRowStatus = _MscDcmeDLinksRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 419, 1, 2),
    _MscDcmeDLinksRowStatus_Type()
)
mscDcmeDLinksRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscDcmeDLinksRowStatus.setStatus("mandatory")
_MscDcmeActiveDcmeLinksTable_Object = MibTable
mscDcmeActiveDcmeLinksTable = _MscDcmeActiveDcmeLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 420)
)
if mibBuilder.loadTexts:
    mscDcmeActiveDcmeLinksTable.setStatus("mandatory")
_MscDcmeActiveDcmeLinksEntry_Object = MibTableRow
mscDcmeActiveDcmeLinksEntry = _MscDcmeActiveDcmeLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 420, 1)
)
mscDcmeActiveDcmeLinksEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDcmeActiveDcmeLinksValue"),
)
if mibBuilder.loadTexts:
    mscDcmeActiveDcmeLinksEntry.setStatus("mandatory")
_MscDcmeActiveDcmeLinksValue_Type = RowPointer
_MscDcmeActiveDcmeLinksValue_Object = MibTableColumn
mscDcmeActiveDcmeLinksValue = _MscDcmeActiveDcmeLinksValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 129, 420, 1, 1),
    _MscDcmeActiveDcmeLinksValue_Type()
)
mscDcmeActiveDcmeLinksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDcmeActiveDcmeLinksValue.setStatus("mandatory")
_MscDcl_ObjectIdentity = ObjectIdentity
mscDcl = _MscDcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130)
)
_MscDclRowStatusTable_Object = MibTable
mscDclRowStatusTable = _MscDclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1)
)
if mibBuilder.loadTexts:
    mscDclRowStatusTable.setStatus("mandatory")
_MscDclRowStatusEntry_Object = MibTableRow
mscDclRowStatusEntry = _MscDclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1, 1)
)
mscDclRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
)
if mibBuilder.loadTexts:
    mscDclRowStatusEntry.setStatus("mandatory")
_MscDclRowStatus_Type = RowStatus
_MscDclRowStatus_Object = MibTableColumn
mscDclRowStatus = _MscDclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1, 1, 1),
    _MscDclRowStatus_Type()
)
mscDclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclRowStatus.setStatus("mandatory")
_MscDclComponentName_Type = DisplayString
_MscDclComponentName_Object = MibTableColumn
mscDclComponentName = _MscDclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1, 1, 2),
    _MscDclComponentName_Type()
)
mscDclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclComponentName.setStatus("mandatory")
_MscDclStorageType_Type = StorageType
_MscDclStorageType_Object = MibTableColumn
mscDclStorageType = _MscDclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1, 1, 4),
    _MscDclStorageType_Type()
)
mscDclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclStorageType.setStatus("mandatory")


class _MscDclIndex_Type(Integer32):
    """Custom type mscDclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MscDclIndex_Type.__name__ = "Integer32"
_MscDclIndex_Object = MibTableColumn
mscDclIndex = _MscDclIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 1, 1, 10),
    _MscDclIndex_Type()
)
mscDclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclIndex.setStatus("mandatory")
_MscDclDna_ObjectIdentity = ObjectIdentity
mscDclDna = _MscDclDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2)
)
_MscDclDnaRowStatusTable_Object = MibTable
mscDclDnaRowStatusTable = _MscDclDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1)
)
if mibBuilder.loadTexts:
    mscDclDnaRowStatusTable.setStatus("mandatory")
_MscDclDnaRowStatusEntry_Object = MibTableRow
mscDclDnaRowStatusEntry = _MscDclDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1, 1)
)
mscDclDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclDnaIndex"),
)
if mibBuilder.loadTexts:
    mscDclDnaRowStatusEntry.setStatus("mandatory")
_MscDclDnaRowStatus_Type = RowStatus
_MscDclDnaRowStatus_Object = MibTableColumn
mscDclDnaRowStatus = _MscDclDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1, 1, 1),
    _MscDclDnaRowStatus_Type()
)
mscDclDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclDnaRowStatus.setStatus("mandatory")
_MscDclDnaComponentName_Type = DisplayString
_MscDclDnaComponentName_Object = MibTableColumn
mscDclDnaComponentName = _MscDclDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1, 1, 2),
    _MscDclDnaComponentName_Type()
)
mscDclDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclDnaComponentName.setStatus("mandatory")
_MscDclDnaStorageType_Type = StorageType
_MscDclDnaStorageType_Object = MibTableColumn
mscDclDnaStorageType = _MscDclDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1, 1, 4),
    _MscDclDnaStorageType_Type()
)
mscDclDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclDnaStorageType.setStatus("mandatory")
_MscDclDnaIndex_Type = NonReplicated
_MscDclDnaIndex_Object = MibTableColumn
mscDclDnaIndex = _MscDclDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 1, 1, 10),
    _MscDclDnaIndex_Type()
)
mscDclDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclDnaIndex.setStatus("mandatory")
_MscDclDnaAddressTable_Object = MibTable
mscDclDnaAddressTable = _MscDclDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 10)
)
if mibBuilder.loadTexts:
    mscDclDnaAddressTable.setStatus("mandatory")
_MscDclDnaAddressEntry_Object = MibTableRow
mscDclDnaAddressEntry = _MscDclDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 10, 1)
)
mscDclDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclDnaIndex"),
)
if mibBuilder.loadTexts:
    mscDclDnaAddressEntry.setStatus("mandatory")


class _MscDclDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscDclDnaNumberingPlanIndicator based on Integer32"""
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


_MscDclDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscDclDnaNumberingPlanIndicator_Object = MibTableColumn
mscDclDnaNumberingPlanIndicator = _MscDclDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 10, 1, 1),
    _MscDclDnaNumberingPlanIndicator_Type()
)
mscDclDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscDclDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscDclDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscDclDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscDclDnaDataNetworkAddress_Object = MibTableColumn
mscDclDnaDataNetworkAddress = _MscDclDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 2, 10, 1, 2),
    _MscDclDnaDataNetworkAddress_Type()
)
mscDclDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclDnaDataNetworkAddress.setStatus("mandatory")
_MscDclFramer_ObjectIdentity = ObjectIdentity
mscDclFramer = _MscDclFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3)
)
_MscDclFramerRowStatusTable_Object = MibTable
mscDclFramerRowStatusTable = _MscDclFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1)
)
if mibBuilder.loadTexts:
    mscDclFramerRowStatusTable.setStatus("mandatory")
_MscDclFramerRowStatusEntry_Object = MibTableRow
mscDclFramerRowStatusEntry = _MscDclFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1, 1)
)
mscDclFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclFramerRowStatusEntry.setStatus("mandatory")
_MscDclFramerRowStatus_Type = RowStatus
_MscDclFramerRowStatus_Object = MibTableColumn
mscDclFramerRowStatus = _MscDclFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1, 1, 1),
    _MscDclFramerRowStatus_Type()
)
mscDclFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerRowStatus.setStatus("mandatory")
_MscDclFramerComponentName_Type = DisplayString
_MscDclFramerComponentName_Object = MibTableColumn
mscDclFramerComponentName = _MscDclFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1, 1, 2),
    _MscDclFramerComponentName_Type()
)
mscDclFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerComponentName.setStatus("mandatory")
_MscDclFramerStorageType_Type = StorageType
_MscDclFramerStorageType_Object = MibTableColumn
mscDclFramerStorageType = _MscDclFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1, 1, 4),
    _MscDclFramerStorageType_Type()
)
mscDclFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerStorageType.setStatus("mandatory")
_MscDclFramerIndex_Type = NonReplicated
_MscDclFramerIndex_Object = MibTableColumn
mscDclFramerIndex = _MscDclFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 1, 1, 10),
    _MscDclFramerIndex_Type()
)
mscDclFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclFramerIndex.setStatus("mandatory")
_MscDclFramerProvTable_Object = MibTable
mscDclFramerProvTable = _MscDclFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 10)
)
if mibBuilder.loadTexts:
    mscDclFramerProvTable.setStatus("mandatory")
_MscDclFramerProvEntry_Object = MibTableRow
mscDclFramerProvEntry = _MscDclFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 10, 1)
)
mscDclFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclFramerProvEntry.setStatus("mandatory")
_MscDclFramerInterfaceName_Type = Link
_MscDclFramerInterfaceName_Object = MibTableColumn
mscDclFramerInterfaceName = _MscDclFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 10, 1, 1),
    _MscDclFramerInterfaceName_Type()
)
mscDclFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclFramerInterfaceName.setStatus("mandatory")
_MscDclFramerStateTable_Object = MibTable
mscDclFramerStateTable = _MscDclFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 12)
)
if mibBuilder.loadTexts:
    mscDclFramerStateTable.setStatus("mandatory")
_MscDclFramerStateEntry_Object = MibTableRow
mscDclFramerStateEntry = _MscDclFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 12, 1)
)
mscDclFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclFramerStateEntry.setStatus("mandatory")


class _MscDclFramerAdminState_Type(Integer32):
    """Custom type mscDclFramerAdminState based on Integer32"""
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


_MscDclFramerAdminState_Type.__name__ = "Integer32"
_MscDclFramerAdminState_Object = MibTableColumn
mscDclFramerAdminState = _MscDclFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 12, 1, 1),
    _MscDclFramerAdminState_Type()
)
mscDclFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerAdminState.setStatus("mandatory")


class _MscDclFramerOperationalState_Type(Integer32):
    """Custom type mscDclFramerOperationalState based on Integer32"""
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


_MscDclFramerOperationalState_Type.__name__ = "Integer32"
_MscDclFramerOperationalState_Object = MibTableColumn
mscDclFramerOperationalState = _MscDclFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 12, 1, 2),
    _MscDclFramerOperationalState_Type()
)
mscDclFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerOperationalState.setStatus("mandatory")


class _MscDclFramerUsageState_Type(Integer32):
    """Custom type mscDclFramerUsageState based on Integer32"""
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


_MscDclFramerUsageState_Type.__name__ = "Integer32"
_MscDclFramerUsageState_Object = MibTableColumn
mscDclFramerUsageState = _MscDclFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 3, 12, 1, 3),
    _MscDclFramerUsageState_Type()
)
mscDclFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclFramerUsageState.setStatus("mandatory")
_MscDclVs_ObjectIdentity = ObjectIdentity
mscDclVs = _MscDclVs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4)
)
_MscDclVsRowStatusTable_Object = MibTable
mscDclVsRowStatusTable = _MscDclVsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1)
)
if mibBuilder.loadTexts:
    mscDclVsRowStatusTable.setStatus("mandatory")
_MscDclVsRowStatusEntry_Object = MibTableRow
mscDclVsRowStatusEntry = _MscDclVsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1, 1)
)
mscDclVsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsRowStatusEntry.setStatus("mandatory")
_MscDclVsRowStatus_Type = RowStatus
_MscDclVsRowStatus_Object = MibTableColumn
mscDclVsRowStatus = _MscDclVsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1, 1, 1),
    _MscDclVsRowStatus_Type()
)
mscDclVsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsRowStatus.setStatus("mandatory")
_MscDclVsComponentName_Type = DisplayString
_MscDclVsComponentName_Object = MibTableColumn
mscDclVsComponentName = _MscDclVsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1, 1, 2),
    _MscDclVsComponentName_Type()
)
mscDclVsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsComponentName.setStatus("mandatory")
_MscDclVsStorageType_Type = StorageType
_MscDclVsStorageType_Object = MibTableColumn
mscDclVsStorageType = _MscDclVsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1, 1, 4),
    _MscDclVsStorageType_Type()
)
mscDclVsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsStorageType.setStatus("mandatory")


class _MscDclVsIndex_Type(Integer32):
    """Custom type mscDclVsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscDclVsIndex_Type.__name__ = "Integer32"
_MscDclVsIndex_Object = MibTableColumn
mscDclVsIndex = _MscDclVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 1, 1, 10),
    _MscDclVsIndex_Type()
)
mscDclVsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsIndex.setStatus("mandatory")
_MscDclVsFramer_ObjectIdentity = ObjectIdentity
mscDclVsFramer = _MscDclVsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2)
)
_MscDclVsFramerRowStatusTable_Object = MibTable
mscDclVsFramerRowStatusTable = _MscDclVsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscDclVsFramerRowStatusTable.setStatus("mandatory")
_MscDclVsFramerRowStatusEntry_Object = MibTableRow
mscDclVsFramerRowStatusEntry = _MscDclVsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1, 1)
)
mscDclVsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerRowStatusEntry.setStatus("mandatory")
_MscDclVsFramerRowStatus_Type = RowStatus
_MscDclVsFramerRowStatus_Object = MibTableColumn
mscDclVsFramerRowStatus = _MscDclVsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1, 1, 1),
    _MscDclVsFramerRowStatus_Type()
)
mscDclVsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerRowStatus.setStatus("mandatory")
_MscDclVsFramerComponentName_Type = DisplayString
_MscDclVsFramerComponentName_Object = MibTableColumn
mscDclVsFramerComponentName = _MscDclVsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1, 1, 2),
    _MscDclVsFramerComponentName_Type()
)
mscDclVsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerComponentName.setStatus("mandatory")
_MscDclVsFramerStorageType_Type = StorageType
_MscDclVsFramerStorageType_Object = MibTableColumn
mscDclVsFramerStorageType = _MscDclVsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1, 1, 4),
    _MscDclVsFramerStorageType_Type()
)
mscDclVsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerStorageType.setStatus("mandatory")
_MscDclVsFramerIndex_Type = NonReplicated
_MscDclVsFramerIndex_Object = MibTableColumn
mscDclVsFramerIndex = _MscDclVsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 1, 1, 10),
    _MscDclVsFramerIndex_Type()
)
mscDclVsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerIndex.setStatus("mandatory")
_MscDclVsFramerVfpDebug_ObjectIdentity = ObjectIdentity
mscDclVsFramerVfpDebug = _MscDclVsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5)
)
_MscDclVsFramerVfpDebugRowStatusTable_Object = MibTable
mscDclVsFramerVfpDebugRowStatusTable = _MscDclVsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_MscDclVsFramerVfpDebugRowStatusEntry_Object = MibTableRow
mscDclVsFramerVfpDebugRowStatusEntry = _MscDclVsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1, 1)
)
mscDclVsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_MscDclVsFramerVfpDebugRowStatus_Type = RowStatus
_MscDclVsFramerVfpDebugRowStatus_Object = MibTableColumn
mscDclVsFramerVfpDebugRowStatus = _MscDclVsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1, 1, 1),
    _MscDclVsFramerVfpDebugRowStatus_Type()
)
mscDclVsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugRowStatus.setStatus("mandatory")
_MscDclVsFramerVfpDebugComponentName_Type = DisplayString
_MscDclVsFramerVfpDebugComponentName_Object = MibTableColumn
mscDclVsFramerVfpDebugComponentName = _MscDclVsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1, 1, 2),
    _MscDclVsFramerVfpDebugComponentName_Type()
)
mscDclVsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugComponentName.setStatus("mandatory")
_MscDclVsFramerVfpDebugStorageType_Type = StorageType
_MscDclVsFramerVfpDebugStorageType_Object = MibTableColumn
mscDclVsFramerVfpDebugStorageType = _MscDclVsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1, 1, 4),
    _MscDclVsFramerVfpDebugStorageType_Type()
)
mscDclVsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugStorageType.setStatus("mandatory")
_MscDclVsFramerVfpDebugIndex_Type = NonReplicated
_MscDclVsFramerVfpDebugIndex_Object = MibTableColumn
mscDclVsFramerVfpDebugIndex = _MscDclVsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 5, 1, 1, 10),
    _MscDclVsFramerVfpDebugIndex_Type()
)
mscDclVsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerVfpDebugIndex.setStatus("mandatory")
_MscDclVsFramerMvpDebug_ObjectIdentity = ObjectIdentity
mscDclVsFramerMvpDebug = _MscDclVsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6)
)
_MscDclVsFramerMvpDebugRowStatusTable_Object = MibTable
mscDclVsFramerMvpDebugRowStatusTable = _MscDclVsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_MscDclVsFramerMvpDebugRowStatusEntry_Object = MibTableRow
mscDclVsFramerMvpDebugRowStatusEntry = _MscDclVsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1, 1)
)
mscDclVsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_MscDclVsFramerMvpDebugRowStatus_Type = RowStatus
_MscDclVsFramerMvpDebugRowStatus_Object = MibTableColumn
mscDclVsFramerMvpDebugRowStatus = _MscDclVsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1, 1, 1),
    _MscDclVsFramerMvpDebugRowStatus_Type()
)
mscDclVsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugRowStatus.setStatus("mandatory")
_MscDclVsFramerMvpDebugComponentName_Type = DisplayString
_MscDclVsFramerMvpDebugComponentName_Object = MibTableColumn
mscDclVsFramerMvpDebugComponentName = _MscDclVsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1, 1, 2),
    _MscDclVsFramerMvpDebugComponentName_Type()
)
mscDclVsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugComponentName.setStatus("mandatory")
_MscDclVsFramerMvpDebugStorageType_Type = StorageType
_MscDclVsFramerMvpDebugStorageType_Object = MibTableColumn
mscDclVsFramerMvpDebugStorageType = _MscDclVsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1, 1, 4),
    _MscDclVsFramerMvpDebugStorageType_Type()
)
mscDclVsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugStorageType.setStatus("mandatory")
_MscDclVsFramerMvpDebugIndex_Type = NonReplicated
_MscDclVsFramerMvpDebugIndex_Object = MibTableColumn
mscDclVsFramerMvpDebugIndex = _MscDclVsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 6, 1, 1, 10),
    _MscDclVsFramerMvpDebugIndex_Type()
)
mscDclVsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerMvpDebugIndex.setStatus("mandatory")
_MscDclVsFramerPcmCapture_ObjectIdentity = ObjectIdentity
mscDclVsFramerPcmCapture = _MscDclVsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7)
)
_MscDclVsFramerPcmCaptureRowStatusTable_Object = MibTable
mscDclVsFramerPcmCaptureRowStatusTable = _MscDclVsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_MscDclVsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
mscDclVsFramerPcmCaptureRowStatusEntry = _MscDclVsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1, 1)
)
mscDclVsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_MscDclVsFramerPcmCaptureRowStatus_Type = RowStatus
_MscDclVsFramerPcmCaptureRowStatus_Object = MibTableColumn
mscDclVsFramerPcmCaptureRowStatus = _MscDclVsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1, 1, 1),
    _MscDclVsFramerPcmCaptureRowStatus_Type()
)
mscDclVsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureRowStatus.setStatus("mandatory")
_MscDclVsFramerPcmCaptureComponentName_Type = DisplayString
_MscDclVsFramerPcmCaptureComponentName_Object = MibTableColumn
mscDclVsFramerPcmCaptureComponentName = _MscDclVsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1, 1, 2),
    _MscDclVsFramerPcmCaptureComponentName_Type()
)
mscDclVsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureComponentName.setStatus("mandatory")
_MscDclVsFramerPcmCaptureStorageType_Type = StorageType
_MscDclVsFramerPcmCaptureStorageType_Object = MibTableColumn
mscDclVsFramerPcmCaptureStorageType = _MscDclVsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1, 1, 4),
    _MscDclVsFramerPcmCaptureStorageType_Type()
)
mscDclVsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureStorageType.setStatus("mandatory")
_MscDclVsFramerPcmCaptureIndex_Type = NonReplicated
_MscDclVsFramerPcmCaptureIndex_Object = MibTableColumn
mscDclVsFramerPcmCaptureIndex = _MscDclVsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 7, 1, 1, 10),
    _MscDclVsFramerPcmCaptureIndex_Type()
)
mscDclVsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerPcmCaptureIndex.setStatus("mandatory")
_MscDclVsFramerProvTable_Object = MibTable
mscDclVsFramerProvTable = _MscDclVsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscDclVsFramerProvTable.setStatus("mandatory")
_MscDclVsFramerProvEntry_Object = MibTableRow
mscDclVsFramerProvEntry = _MscDclVsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 10, 1)
)
mscDclVsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerProvEntry.setStatus("mandatory")
_MscDclVsFramerInterfaceName_Type = Link
_MscDclVsFramerInterfaceName_Object = MibTableColumn
mscDclVsFramerInterfaceName = _MscDclVsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 10, 1, 1),
    _MscDclVsFramerInterfaceName_Type()
)
mscDclVsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerInterfaceName.setStatus("mandatory")
_MscDclVsFramerStateTable_Object = MibTable
mscDclVsFramerStateTable = _MscDclVsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 14)
)
if mibBuilder.loadTexts:
    mscDclVsFramerStateTable.setStatus("mandatory")
_MscDclVsFramerStateEntry_Object = MibTableRow
mscDclVsFramerStateEntry = _MscDclVsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 14, 1)
)
mscDclVsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerStateEntry.setStatus("mandatory")


class _MscDclVsFramerAdminState_Type(Integer32):
    """Custom type mscDclVsFramerAdminState based on Integer32"""
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


_MscDclVsFramerAdminState_Type.__name__ = "Integer32"
_MscDclVsFramerAdminState_Object = MibTableColumn
mscDclVsFramerAdminState = _MscDclVsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 14, 1, 1),
    _MscDclVsFramerAdminState_Type()
)
mscDclVsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerAdminState.setStatus("mandatory")


class _MscDclVsFramerOperationalState_Type(Integer32):
    """Custom type mscDclVsFramerOperationalState based on Integer32"""
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


_MscDclVsFramerOperationalState_Type.__name__ = "Integer32"
_MscDclVsFramerOperationalState_Object = MibTableColumn
mscDclVsFramerOperationalState = _MscDclVsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 14, 1, 2),
    _MscDclVsFramerOperationalState_Type()
)
mscDclVsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerOperationalState.setStatus("mandatory")


class _MscDclVsFramerUsageState_Type(Integer32):
    """Custom type mscDclVsFramerUsageState based on Integer32"""
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


_MscDclVsFramerUsageState_Type.__name__ = "Integer32"
_MscDclVsFramerUsageState_Object = MibTableColumn
mscDclVsFramerUsageState = _MscDclVsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 14, 1, 3),
    _MscDclVsFramerUsageState_Type()
)
mscDclVsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerUsageState.setStatus("mandatory")
_MscDclVsFramerStatsTable_Object = MibTable
mscDclVsFramerStatsTable = _MscDclVsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15)
)
if mibBuilder.loadTexts:
    mscDclVsFramerStatsTable.setStatus("mandatory")
_MscDclVsFramerStatsEntry_Object = MibTableRow
mscDclVsFramerStatsEntry = _MscDclVsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1)
)
mscDclVsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerStatsEntry.setStatus("mandatory")


class _MscDclVsFramerTotalCells_Type(Unsigned32):
    """Custom type mscDclVsFramerTotalCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerTotalCells_Type.__name__ = "Unsigned32"
_MscDclVsFramerTotalCells_Object = MibTableColumn
mscDclVsFramerTotalCells = _MscDclVsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 1),
    _MscDclVsFramerTotalCells_Type()
)
mscDclVsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerTotalCells.setStatus("mandatory")


class _MscDclVsFramerAudioCells_Type(Unsigned32):
    """Custom type mscDclVsFramerAudioCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerAudioCells_Type.__name__ = "Unsigned32"
_MscDclVsFramerAudioCells_Object = MibTableColumn
mscDclVsFramerAudioCells = _MscDclVsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 2),
    _MscDclVsFramerAudioCells_Type()
)
mscDclVsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerAudioCells.setStatus("mandatory")


class _MscDclVsFramerSilenceCells_Type(Unsigned32):
    """Custom type mscDclVsFramerSilenceCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerSilenceCells_Type.__name__ = "Unsigned32"
_MscDclVsFramerSilenceCells_Object = MibTableColumn
mscDclVsFramerSilenceCells = _MscDclVsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 4),
    _MscDclVsFramerSilenceCells_Type()
)
mscDclVsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerSilenceCells.setStatus("mandatory")


class _MscDclVsFramerModemCells_Type(Unsigned32):
    """Custom type mscDclVsFramerModemCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerModemCells_Type.__name__ = "Unsigned32"
_MscDclVsFramerModemCells_Object = MibTableColumn
mscDclVsFramerModemCells = _MscDclVsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 5),
    _MscDclVsFramerModemCells_Type()
)
mscDclVsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerModemCells.setStatus("obsolete")


class _MscDclVsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type mscDclVsFramerCurrentEncodingRate based on Integer32"""
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


_MscDclVsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_MscDclVsFramerCurrentEncodingRate_Object = MibTableColumn
mscDclVsFramerCurrentEncodingRate = _MscDclVsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 6),
    _MscDclVsFramerCurrentEncodingRate_Type()
)
mscDclVsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerCurrentEncodingRate.setStatus("obsolete")


class _MscDclVsFramerLrcErrors_Type(Unsigned32):
    """Custom type mscDclVsFramerLrcErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDclVsFramerLrcErrors_Object = MibTableColumn
mscDclVsFramerLrcErrors = _MscDclVsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 7),
    _MscDclVsFramerLrcErrors_Type()
)
mscDclVsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerLrcErrors.setStatus("mandatory")


class _MscDclVsFramerFrmLostInNetwork_Type(Unsigned32):
    """Custom type mscDclVsFramerFrmLostInNetwork based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerFrmLostInNetwork_Type.__name__ = "Unsigned32"
_MscDclVsFramerFrmLostInNetwork_Object = MibTableColumn
mscDclVsFramerFrmLostInNetwork = _MscDclVsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 8),
    _MscDclVsFramerFrmLostInNetwork_Type()
)
mscDclVsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmLostInNetwork.setStatus("mandatory")


class _MscDclVsFramerFrmUnderRuns_Type(Unsigned32):
    """Custom type mscDclVsFramerFrmUnderRuns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerFrmUnderRuns_Type.__name__ = "Unsigned32"
_MscDclVsFramerFrmUnderRuns_Object = MibTableColumn
mscDclVsFramerFrmUnderRuns = _MscDclVsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 9),
    _MscDclVsFramerFrmUnderRuns_Type()
)
mscDclVsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmUnderRuns.setStatus("mandatory")


class _MscDclVsFramerFrmDumped_Type(Unsigned32):
    """Custom type mscDclVsFramerFrmDumped based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerFrmDumped_Type.__name__ = "Unsigned32"
_MscDclVsFramerFrmDumped_Object = MibTableColumn
mscDclVsFramerFrmDumped = _MscDclVsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 10),
    _MscDclVsFramerFrmDumped_Type()
)
mscDclVsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmDumped.setStatus("mandatory")
_MscDclVsFramerModemSilenceCells_Type = Counter32
_MscDclVsFramerModemSilenceCells_Object = MibTableColumn
mscDclVsFramerModemSilenceCells = _MscDclVsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 26),
    _MscDclVsFramerModemSilenceCells_Type()
)
mscDclVsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerModemSilenceCells.setStatus("obsolete")


class _MscDclVsFramerCurrentEncoding_Type(Integer32):
    """Custom type mscDclVsFramerCurrentEncoding based on Integer32"""
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


_MscDclVsFramerCurrentEncoding_Type.__name__ = "Integer32"
_MscDclVsFramerCurrentEncoding_Object = MibTableColumn
mscDclVsFramerCurrentEncoding = _MscDclVsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 27),
    _MscDclVsFramerCurrentEncoding_Type()
)
mscDclVsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerCurrentEncoding.setStatus("obsolete")


class _MscDclVsFramerTptStatus_Type(Integer32):
    """Custom type mscDclVsFramerTptStatus based on Integer32"""
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


_MscDclVsFramerTptStatus_Type.__name__ = "Integer32"
_MscDclVsFramerTptStatus_Object = MibTableColumn
mscDclVsFramerTptStatus = _MscDclVsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 28),
    _MscDclVsFramerTptStatus_Type()
)
mscDclVsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerTptStatus.setStatus("obsolete")
_MscDclVsFramerFaxRelayCells_Type = Counter32
_MscDclVsFramerFaxRelayCells_Object = MibTableColumn
mscDclVsFramerFaxRelayCells = _MscDclVsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 35),
    _MscDclVsFramerFaxRelayCells_Type()
)
mscDclVsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFaxRelayCells.setStatus("mandatory")


class _MscDclVsFramerModemFaxCells_Type(Unsigned32):
    """Custom type mscDclVsFramerModemFaxCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerModemFaxCells_Type.__name__ = "Unsigned32"
_MscDclVsFramerModemFaxCells_Object = MibTableColumn
mscDclVsFramerModemFaxCells = _MscDclVsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 36),
    _MscDclVsFramerModemFaxCells_Type()
)
mscDclVsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerModemFaxCells.setStatus("mandatory")
_MscDclVsFramerFaxIdleCells_Type = Counter32
_MscDclVsFramerFaxIdleCells_Object = MibTableColumn
mscDclVsFramerFaxIdleCells = _MscDclVsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 15, 1, 37),
    _MscDclVsFramerFaxIdleCells_Type()
)
mscDclVsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFaxIdleCells.setStatus("mandatory")
_MscDclVsFramerOperTable_Object = MibTable
mscDclVsFramerOperTable = _MscDclVsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 16)
)
if mibBuilder.loadTexts:
    mscDclVsFramerOperTable.setStatus("mandatory")
_MscDclVsFramerOperEntry_Object = MibTableRow
mscDclVsFramerOperEntry = _MscDclVsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 16, 1)
)
mscDclVsFramerOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerOperEntry.setStatus("mandatory")


class _MscDclVsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type mscDclVsFramerOpCurrentEncoding based on Integer32"""
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


_MscDclVsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_MscDclVsFramerOpCurrentEncoding_Object = MibTableColumn
mscDclVsFramerOpCurrentEncoding = _MscDclVsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 16, 1, 1),
    _MscDclVsFramerOpCurrentEncoding_Type()
)
mscDclVsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerOpCurrentEncoding.setStatus("mandatory")


class _MscDclVsFramerCurrentRate_Type(Integer32):
    """Custom type mscDclVsFramerCurrentRate based on Integer32"""
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


_MscDclVsFramerCurrentRate_Type.__name__ = "Integer32"
_MscDclVsFramerCurrentRate_Object = MibTableColumn
mscDclVsFramerCurrentRate = _MscDclVsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 16, 1, 2),
    _MscDclVsFramerCurrentRate_Type()
)
mscDclVsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerCurrentRate.setStatus("mandatory")


class _MscDclVsFramerOpTptStatus_Type(Integer32):
    """Custom type mscDclVsFramerOpTptStatus based on Integer32"""
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


_MscDclVsFramerOpTptStatus_Type.__name__ = "Integer32"
_MscDclVsFramerOpTptStatus_Object = MibTableColumn
mscDclVsFramerOpTptStatus = _MscDclVsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 16, 1, 3),
    _MscDclVsFramerOpTptStatus_Type()
)
mscDclVsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerOpTptStatus.setStatus("mandatory")
_MscDclVsFramerNegTable_Object = MibTable
mscDclVsFramerNegTable = _MscDclVsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17)
)
if mibBuilder.loadTexts:
    mscDclVsFramerNegTable.setStatus("mandatory")
_MscDclVsFramerNegEntry_Object = MibTableRow
mscDclVsFramerNegEntry = _MscDclVsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1)
)
mscDclVsFramerNegEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerNegEntry.setStatus("mandatory")


class _MscDclVsFramerNegotiatedSilenceSuppression_Type(Integer32):
    """Custom type mscDclVsFramerNegotiatedSilenceSuppression based on Integer32"""
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


_MscDclVsFramerNegotiatedSilenceSuppression_Type.__name__ = "Integer32"
_MscDclVsFramerNegotiatedSilenceSuppression_Object = MibTableColumn
mscDclVsFramerNegotiatedSilenceSuppression = _MscDclVsFramerNegotiatedSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1, 1),
    _MscDclVsFramerNegotiatedSilenceSuppression_Type()
)
mscDclVsFramerNegotiatedSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerNegotiatedSilenceSuppression.setStatus("mandatory")


class _MscDclVsFramerNegotiatedFisG711G726_Type(Integer32):
    """Custom type mscDclVsFramerNegotiatedFisG711G726 based on Integer32"""
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


_MscDclVsFramerNegotiatedFisG711G726_Type.__name__ = "Integer32"
_MscDclVsFramerNegotiatedFisG711G726_Object = MibTableColumn
mscDclVsFramerNegotiatedFisG711G726 = _MscDclVsFramerNegotiatedFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1, 2),
    _MscDclVsFramerNegotiatedFisG711G726_Type()
)
mscDclVsFramerNegotiatedFisG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerNegotiatedFisG711G726.setStatus("mandatory")


class _MscDclVsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type mscDclVsFramerNegotiatedDtmfRegeneration based on Integer32"""
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


_MscDclVsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_MscDclVsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
mscDclVsFramerNegotiatedDtmfRegeneration = _MscDclVsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1, 3),
    _MscDclVsFramerNegotiatedDtmfRegeneration_Type()
)
mscDclVsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _MscDclVsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type mscDclVsFramerNegotiatedV17AsG711G726 based on Integer32"""
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


_MscDclVsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_MscDclVsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
mscDclVsFramerNegotiatedV17AsG711G726 = _MscDclVsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1, 4),
    _MscDclVsFramerNegotiatedV17AsG711G726_Type()
)
mscDclVsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _MscDclVsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type mscDclVsFramerNegotiatedTandemPassThrough based on Integer32"""
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


_MscDclVsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_MscDclVsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
mscDclVsFramerNegotiatedTandemPassThrough = _MscDclVsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 17, 1, 5),
    _MscDclVsFramerNegotiatedTandemPassThrough_Type()
)
mscDclVsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_MscDclVsFramerFrmToNetworkTable_Object = MibTable
mscDclVsFramerFrmToNetworkTable = _MscDclVsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 315)
)
if mibBuilder.loadTexts:
    mscDclVsFramerFrmToNetworkTable.setStatus("mandatory")
_MscDclVsFramerFrmToNetworkEntry_Object = MibTableRow
mscDclVsFramerFrmToNetworkEntry = _MscDclVsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 315, 1)
)
mscDclVsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerFrmToNetworkEntry.setStatus("mandatory")


class _MscDclVsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type mscDclVsFramerFrmToNetworkIndex based on Integer32"""
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


_MscDclVsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_MscDclVsFramerFrmToNetworkIndex_Object = MibTableColumn
mscDclVsFramerFrmToNetworkIndex = _MscDclVsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 315, 1, 1),
    _MscDclVsFramerFrmToNetworkIndex_Type()
)
mscDclVsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmToNetworkIndex.setStatus("mandatory")


class _MscDclVsFramerFrmToNetworkValue_Type(Unsigned32):
    """Custom type mscDclVsFramerFrmToNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerFrmToNetworkValue_Type.__name__ = "Unsigned32"
_MscDclVsFramerFrmToNetworkValue_Object = MibTableColumn
mscDclVsFramerFrmToNetworkValue = _MscDclVsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 315, 1, 2),
    _MscDclVsFramerFrmToNetworkValue_Type()
)
mscDclVsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmToNetworkValue.setStatus("mandatory")
_MscDclVsFramerFrmFromNetworkTable_Object = MibTable
mscDclVsFramerFrmFromNetworkTable = _MscDclVsFramerFrmFromNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 316)
)
if mibBuilder.loadTexts:
    mscDclVsFramerFrmFromNetworkTable.setStatus("mandatory")
_MscDclVsFramerFrmFromNetworkEntry_Object = MibTableRow
mscDclVsFramerFrmFromNetworkEntry = _MscDclVsFramerFrmFromNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 316, 1)
)
mscDclVsFramerFrmFromNetworkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerFrmFromNetworkIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerFrmFromNetworkEntry.setStatus("mandatory")


class _MscDclVsFramerFrmFromNetworkIndex_Type(Integer32):
    """Custom type mscDclVsFramerFrmFromNetworkIndex based on Integer32"""
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


_MscDclVsFramerFrmFromNetworkIndex_Type.__name__ = "Integer32"
_MscDclVsFramerFrmFromNetworkIndex_Object = MibTableColumn
mscDclVsFramerFrmFromNetworkIndex = _MscDclVsFramerFrmFromNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 316, 1, 1),
    _MscDclVsFramerFrmFromNetworkIndex_Type()
)
mscDclVsFramerFrmFromNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmFromNetworkIndex.setStatus("mandatory")


class _MscDclVsFramerFrmFromNetworkValue_Type(Unsigned32):
    """Custom type mscDclVsFramerFrmFromNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsFramerFrmFromNetworkValue_Type.__name__ = "Unsigned32"
_MscDclVsFramerFrmFromNetworkValue_Object = MibTableColumn
mscDclVsFramerFrmFromNetworkValue = _MscDclVsFramerFrmFromNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 316, 1, 2),
    _MscDclVsFramerFrmFromNetworkValue_Type()
)
mscDclVsFramerFrmFromNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsFramerFrmFromNetworkValue.setStatus("mandatory")
_MscDclVsFramerNEncodingTable_Object = MibTable
mscDclVsFramerNEncodingTable = _MscDclVsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 467)
)
if mibBuilder.loadTexts:
    mscDclVsFramerNEncodingTable.setStatus("mandatory")
_MscDclVsFramerNEncodingEntry_Object = MibTableRow
mscDclVsFramerNEncodingEntry = _MscDclVsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 467, 1)
)
mscDclVsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerNEncodingEntry.setStatus("mandatory")


class _MscDclVsFramerNEncodingIndex_Type(Integer32):
    """Custom type mscDclVsFramerNEncodingIndex based on Integer32"""
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


_MscDclVsFramerNEncodingIndex_Type.__name__ = "Integer32"
_MscDclVsFramerNEncodingIndex_Object = MibTableColumn
mscDclVsFramerNEncodingIndex = _MscDclVsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 467, 1, 1),
    _MscDclVsFramerNEncodingIndex_Type()
)
mscDclVsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerNEncodingIndex.setStatus("mandatory")


class _MscDclVsFramerNEncodingValue_Type(Integer32):
    """Custom type mscDclVsFramerNEncodingValue based on Integer32"""
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


_MscDclVsFramerNEncodingValue_Type.__name__ = "Integer32"
_MscDclVsFramerNEncodingValue_Object = MibTableColumn
mscDclVsFramerNEncodingValue = _MscDclVsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 467, 1, 2),
    _MscDclVsFramerNEncodingValue_Type()
)
mscDclVsFramerNEncodingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerNEncodingValue.setStatus("mandatory")
_MscDclVsFramerNRatesTable_Object = MibTable
mscDclVsFramerNRatesTable = _MscDclVsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 479)
)
if mibBuilder.loadTexts:
    mscDclVsFramerNRatesTable.setStatus("mandatory")
_MscDclVsFramerNRatesEntry_Object = MibTableRow
mscDclVsFramerNRatesEntry = _MscDclVsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 479, 1)
)
mscDclVsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerNRatesTrafficIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsFramerNRatesEntry.setStatus("mandatory")


class _MscDclVsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type mscDclVsFramerNRatesTrafficIndex based on Integer32"""
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


_MscDclVsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_MscDclVsFramerNRatesTrafficIndex_Object = MibTableColumn
mscDclVsFramerNRatesTrafficIndex = _MscDclVsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 479, 1, 1),
    _MscDclVsFramerNRatesTrafficIndex_Type()
)
mscDclVsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerNRatesTrafficIndex.setStatus("mandatory")


class _MscDclVsFramerNRatesRateIndex_Type(Integer32):
    """Custom type mscDclVsFramerNRatesRateIndex based on Integer32"""
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


_MscDclVsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_MscDclVsFramerNRatesRateIndex_Object = MibTableColumn
mscDclVsFramerNRatesRateIndex = _MscDclVsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 479, 1, 2),
    _MscDclVsFramerNRatesRateIndex_Type()
)
mscDclVsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsFramerNRatesRateIndex.setStatus("mandatory")


class _MscDclVsFramerNRatesValue_Type(Integer32):
    """Custom type mscDclVsFramerNRatesValue based on Integer32"""
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


_MscDclVsFramerNRatesValue_Type.__name__ = "Integer32"
_MscDclVsFramerNRatesValue_Object = MibTableColumn
mscDclVsFramerNRatesValue = _MscDclVsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 2, 479, 1, 3),
    _MscDclVsFramerNRatesValue_Type()
)
mscDclVsFramerNRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsFramerNRatesValue.setStatus("mandatory")
_MscDclVsLCo_ObjectIdentity = ObjectIdentity
mscDclVsLCo = _MscDclVsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3)
)
_MscDclVsLCoRowStatusTable_Object = MibTable
mscDclVsLCoRowStatusTable = _MscDclVsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscDclVsLCoRowStatusTable.setStatus("mandatory")
_MscDclVsLCoRowStatusEntry_Object = MibTableRow
mscDclVsLCoRowStatusEntry = _MscDclVsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1, 1)
)
mscDclVsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsLCoRowStatusEntry.setStatus("mandatory")
_MscDclVsLCoRowStatus_Type = RowStatus
_MscDclVsLCoRowStatus_Object = MibTableColumn
mscDclVsLCoRowStatus = _MscDclVsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1, 1, 1),
    _MscDclVsLCoRowStatus_Type()
)
mscDclVsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRowStatus.setStatus("mandatory")
_MscDclVsLCoComponentName_Type = DisplayString
_MscDclVsLCoComponentName_Object = MibTableColumn
mscDclVsLCoComponentName = _MscDclVsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1, 1, 2),
    _MscDclVsLCoComponentName_Type()
)
mscDclVsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoComponentName.setStatus("mandatory")
_MscDclVsLCoStorageType_Type = StorageType
_MscDclVsLCoStorageType_Object = MibTableColumn
mscDclVsLCoStorageType = _MscDclVsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1, 1, 4),
    _MscDclVsLCoStorageType_Type()
)
mscDclVsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoStorageType.setStatus("mandatory")
_MscDclVsLCoIndex_Type = NonReplicated
_MscDclVsLCoIndex_Object = MibTableColumn
mscDclVsLCoIndex = _MscDclVsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 1, 1, 10),
    _MscDclVsLCoIndex_Type()
)
mscDclVsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDclVsLCoIndex.setStatus("mandatory")
_MscDclVsLCoPathDataTable_Object = MibTable
mscDclVsLCoPathDataTable = _MscDclVsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscDclVsLCoPathDataTable.setStatus("mandatory")
_MscDclVsLCoPathDataEntry_Object = MibTableRow
mscDclVsLCoPathDataEntry = _MscDclVsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1)
)
mscDclVsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsLCoPathDataEntry.setStatus("mandatory")


class _MscDclVsLCoState_Type(Integer32):
    """Custom type mscDclVsLCoState based on Integer32"""
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


_MscDclVsLCoState_Type.__name__ = "Integer32"
_MscDclVsLCoState_Object = MibTableColumn
mscDclVsLCoState = _MscDclVsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 1),
    _MscDclVsLCoState_Type()
)
mscDclVsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoState.setStatus("mandatory")


class _MscDclVsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscDclVsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDclVsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscDclVsLCoOverrideRemoteName_Object = MibTableColumn
mscDclVsLCoOverrideRemoteName = _MscDclVsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 2),
    _MscDclVsLCoOverrideRemoteName_Type()
)
mscDclVsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsLCoOverrideRemoteName.setStatus("mandatory")


class _MscDclVsLCoEnd_Type(Integer32):
    """Custom type mscDclVsLCoEnd based on Integer32"""
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


_MscDclVsLCoEnd_Type.__name__ = "Integer32"
_MscDclVsLCoEnd_Object = MibTableColumn
mscDclVsLCoEnd = _MscDclVsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 3),
    _MscDclVsLCoEnd_Type()
)
mscDclVsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoEnd.setStatus("mandatory")


class _MscDclVsLCoCostMetric_Type(Unsigned32):
    """Custom type mscDclVsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDclVsLCoCostMetric_Type.__name__ = "Unsigned32"
_MscDclVsLCoCostMetric_Object = MibTableColumn
mscDclVsLCoCostMetric = _MscDclVsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 4),
    _MscDclVsLCoCostMetric_Type()
)
mscDclVsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoCostMetric.setStatus("mandatory")


class _MscDclVsLCoDelayMetric_Type(Unsigned32):
    """Custom type mscDclVsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscDclVsLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscDclVsLCoDelayMetric_Object = MibTableColumn
mscDclVsLCoDelayMetric = _MscDclVsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 5),
    _MscDclVsLCoDelayMetric_Type()
)
mscDclVsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoDelayMetric.setStatus("mandatory")


class _MscDclVsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscDclVsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscDclVsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscDclVsLCoRoundTripDelay_Object = MibTableColumn
mscDclVsLCoRoundTripDelay = _MscDclVsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 6),
    _MscDclVsLCoRoundTripDelay_Type()
)
mscDclVsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRoundTripDelay.setStatus("mandatory")


class _MscDclVsLCoSetupPriority_Type(Unsigned32):
    """Custom type mscDclVsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscDclVsLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscDclVsLCoSetupPriority_Object = MibTableColumn
mscDclVsLCoSetupPriority = _MscDclVsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 7),
    _MscDclVsLCoSetupPriority_Type()
)
mscDclVsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoSetupPriority.setStatus("mandatory")


class _MscDclVsLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscDclVsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscDclVsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscDclVsLCoHoldingPriority_Object = MibTableColumn
mscDclVsLCoHoldingPriority = _MscDclVsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 8),
    _MscDclVsLCoHoldingPriority_Type()
)
mscDclVsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoHoldingPriority.setStatus("mandatory")


class _MscDclVsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscDclVsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscDclVsLCoRequiredTxBandwidth_Object = MibTableColumn
mscDclVsLCoRequiredTxBandwidth = _MscDclVsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 9),
    _MscDclVsLCoRequiredTxBandwidth_Type()
)
mscDclVsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscDclVsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscDclVsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDclVsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscDclVsLCoRequiredRxBandwidth_Object = MibTableColumn
mscDclVsLCoRequiredRxBandwidth = _MscDclVsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 10),
    _MscDclVsLCoRequiredRxBandwidth_Type()
)
mscDclVsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscDclVsLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscDclVsLCoRequiredTrafficType based on Integer32"""
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


_MscDclVsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscDclVsLCoRequiredTrafficType_Object = MibTableColumn
mscDclVsLCoRequiredTrafficType = _MscDclVsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 11),
    _MscDclVsLCoRequiredTrafficType_Type()
)
mscDclVsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRequiredTrafficType.setStatus("mandatory")


class _MscDclVsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscDclVsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDclVsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscDclVsLCoPermittedTrunkTypes_Object = MibTableColumn
mscDclVsLCoPermittedTrunkTypes = _MscDclVsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 12),
    _MscDclVsLCoPermittedTrunkTypes_Type()
)
mscDclVsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscDclVsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscDclVsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscDclVsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscDclVsLCoRequiredSecurity_Object = MibTableColumn
mscDclVsLCoRequiredSecurity = _MscDclVsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 13),
    _MscDclVsLCoRequiredSecurity_Type()
)
mscDclVsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRequiredSecurity.setStatus("mandatory")


class _MscDclVsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscDclVsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscDclVsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscDclVsLCoRequiredCustomerParameter_Object = MibTableColumn
mscDclVsLCoRequiredCustomerParameter = _MscDclVsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 14),
    _MscDclVsLCoRequiredCustomerParameter_Type()
)
mscDclVsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscDclVsLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscDclVsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscDclVsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscDclVsLCoEmissionPriority_Object = MibTableColumn
mscDclVsLCoEmissionPriority = _MscDclVsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 15),
    _MscDclVsLCoEmissionPriority_Type()
)
mscDclVsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoEmissionPriority.setStatus("mandatory")


class _MscDclVsLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscDclVsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscDclVsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscDclVsLCoDiscardPriority_Object = MibTableColumn
mscDclVsLCoDiscardPriority = _MscDclVsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 16),
    _MscDclVsLCoDiscardPriority_Type()
)
mscDclVsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoDiscardPriority.setStatus("mandatory")


class _MscDclVsLCoPathType_Type(Integer32):
    """Custom type mscDclVsLCoPathType based on Integer32"""
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


_MscDclVsLCoPathType_Type.__name__ = "Integer32"
_MscDclVsLCoPathType_Object = MibTableColumn
mscDclVsLCoPathType = _MscDclVsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 17),
    _MscDclVsLCoPathType_Type()
)
mscDclVsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPathType.setStatus("mandatory")


class _MscDclVsLCoRetryCount_Type(Unsigned32):
    """Custom type mscDclVsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDclVsLCoRetryCount_Type.__name__ = "Unsigned32"
_MscDclVsLCoRetryCount_Object = MibTableColumn
mscDclVsLCoRetryCount = _MscDclVsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 18),
    _MscDclVsLCoRetryCount_Type()
)
mscDclVsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoRetryCount.setStatus("mandatory")


class _MscDclVsLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscDclVsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscDclVsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscDclVsLCoPathFailureCount_Object = MibTableColumn
mscDclVsLCoPathFailureCount = _MscDclVsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 19),
    _MscDclVsLCoPathFailureCount_Type()
)
mscDclVsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPathFailureCount.setStatus("mandatory")


class _MscDclVsLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscDclVsLCoReasonForNoRoute based on Integer32"""
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


_MscDclVsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscDclVsLCoReasonForNoRoute_Object = MibTableColumn
mscDclVsLCoReasonForNoRoute = _MscDclVsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 20),
    _MscDclVsLCoReasonForNoRoute_Type()
)
mscDclVsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoReasonForNoRoute.setStatus("mandatory")


class _MscDclVsLCoLastTearDownReason_Type(Integer32):
    """Custom type mscDclVsLCoLastTearDownReason based on Integer32"""
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


_MscDclVsLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscDclVsLCoLastTearDownReason_Object = MibTableColumn
mscDclVsLCoLastTearDownReason = _MscDclVsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 21),
    _MscDclVsLCoLastTearDownReason_Type()
)
mscDclVsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoLastTearDownReason.setStatus("mandatory")


class _MscDclVsLCoPathFailureAction_Type(Integer32):
    """Custom type mscDclVsLCoPathFailureAction based on Integer32"""
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


_MscDclVsLCoPathFailureAction_Type.__name__ = "Integer32"
_MscDclVsLCoPathFailureAction_Object = MibTableColumn
mscDclVsLCoPathFailureAction = _MscDclVsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 22),
    _MscDclVsLCoPathFailureAction_Type()
)
mscDclVsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPathFailureAction.setStatus("mandatory")


class _MscDclVsLCoBumpPreference_Type(Integer32):
    """Custom type mscDclVsLCoBumpPreference based on Integer32"""
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


_MscDclVsLCoBumpPreference_Type.__name__ = "Integer32"
_MscDclVsLCoBumpPreference_Object = MibTableColumn
mscDclVsLCoBumpPreference = _MscDclVsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 23),
    _MscDclVsLCoBumpPreference_Type()
)
mscDclVsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoBumpPreference.setStatus("mandatory")


class _MscDclVsLCoOptimization_Type(Integer32):
    """Custom type mscDclVsLCoOptimization based on Integer32"""
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


_MscDclVsLCoOptimization_Type.__name__ = "Integer32"
_MscDclVsLCoOptimization_Object = MibTableColumn
mscDclVsLCoOptimization = _MscDclVsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 24),
    _MscDclVsLCoOptimization_Type()
)
mscDclVsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoOptimization.setStatus("mandatory")


class _MscDclVsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscDclVsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscDclVsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscDclVsLCoPathUpDateTime_Object = MibTableColumn
mscDclVsLCoPathUpDateTime = _MscDclVsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 10, 1, 25),
    _MscDclVsLCoPathUpDateTime_Type()
)
mscDclVsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPathUpDateTime.setStatus("mandatory")
_MscDclVsLCoStatsTable_Object = MibTable
mscDclVsLCoStatsTable = _MscDclVsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mscDclVsLCoStatsTable.setStatus("mandatory")
_MscDclVsLCoStatsEntry_Object = MibTableRow
mscDclVsLCoStatsEntry = _MscDclVsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11, 1)
)
mscDclVsLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsLCoStatsEntry.setStatus("mandatory")
_MscDclVsLCoPktsToNetwork_Type = PassportCounter64
_MscDclVsLCoPktsToNetwork_Object = MibTableColumn
mscDclVsLCoPktsToNetwork = _MscDclVsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11, 1, 1),
    _MscDclVsLCoPktsToNetwork_Type()
)
mscDclVsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPktsToNetwork.setStatus("mandatory")
_MscDclVsLCoBytesToNetwork_Type = PassportCounter64
_MscDclVsLCoBytesToNetwork_Object = MibTableColumn
mscDclVsLCoBytesToNetwork = _MscDclVsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11, 1, 2),
    _MscDclVsLCoBytesToNetwork_Type()
)
mscDclVsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoBytesToNetwork.setStatus("mandatory")
_MscDclVsLCoPktsFromNetwork_Type = PassportCounter64
_MscDclVsLCoPktsFromNetwork_Object = MibTableColumn
mscDclVsLCoPktsFromNetwork = _MscDclVsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11, 1, 3),
    _MscDclVsLCoPktsFromNetwork_Type()
)
mscDclVsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPktsFromNetwork.setStatus("mandatory")
_MscDclVsLCoBytesFromNetwork_Type = PassportCounter64
_MscDclVsLCoBytesFromNetwork_Object = MibTableColumn
mscDclVsLCoBytesFromNetwork = _MscDclVsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 11, 1, 4),
    _MscDclVsLCoBytesFromNetwork_Type()
)
mscDclVsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoBytesFromNetwork.setStatus("mandatory")
_MscDclVsLCoPathTable_Object = MibTable
mscDclVsLCoPathTable = _MscDclVsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 264)
)
if mibBuilder.loadTexts:
    mscDclVsLCoPathTable.setStatus("mandatory")
_MscDclVsLCoPathEntry_Object = MibTableRow
mscDclVsLCoPathEntry = _MscDclVsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 264, 1)
)
mscDclVsLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscDclVsLCoPathEntry.setStatus("mandatory")


class _MscDclVsLCoPathValue_Type(AsciiString):
    """Custom type mscDclVsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDclVsLCoPathValue_Type.__name__ = "AsciiString"
_MscDclVsLCoPathValue_Object = MibTableColumn
mscDclVsLCoPathValue = _MscDclVsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 3, 264, 1, 1),
    _MscDclVsLCoPathValue_Type()
)
mscDclVsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsLCoPathValue.setStatus("mandatory")
_MscDclVsProvTable_Object = MibTable
mscDclVsProvTable = _MscDclVsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 10)
)
if mibBuilder.loadTexts:
    mscDclVsProvTable.setStatus("mandatory")
_MscDclVsProvEntry_Object = MibTableRow
mscDclVsProvEntry = _MscDclVsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 10, 1)
)
mscDclVsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsProvEntry.setStatus("mandatory")


class _MscDclVsVsType_Type(Integer32):
    """Custom type mscDclVsVsType based on Integer32"""
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


_MscDclVsVsType_Type.__name__ = "Integer32"
_MscDclVsVsType_Object = MibTableColumn
mscDclVsVsType = _MscDclVsVsType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 10, 1, 1),
    _MscDclVsVsType_Type()
)
mscDclVsVsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclVsVsType.setStatus("mandatory")
_MscDclVsOperTable_Object = MibTable
mscDclVsOperTable = _MscDclVsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11)
)
if mibBuilder.loadTexts:
    mscDclVsOperTable.setStatus("mandatory")
_MscDclVsOperEntry_Object = MibTableRow
mscDclVsOperEntry = _MscDclVsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11, 1)
)
mscDclVsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsOperEntry.setStatus("mandatory")


class _MscDclVsStatus_Type(Integer32):
    """Custom type mscDclVsStatus based on Integer32"""
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


_MscDclVsStatus_Type.__name__ = "Integer32"
_MscDclVsStatus_Object = MibTableColumn
mscDclVsStatus = _MscDclVsStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11, 1, 1),
    _MscDclVsStatus_Type()
)
mscDclVsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsStatus.setStatus("mandatory")


class _MscDclVsCallType_Type(Integer32):
    """Custom type mscDclVsCallType based on Integer32"""
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


_MscDclVsCallType_Type.__name__ = "Integer32"
_MscDclVsCallType_Object = MibTableColumn
mscDclVsCallType = _MscDclVsCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11, 1, 3),
    _MscDclVsCallType_Type()
)
mscDclVsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsCallType.setStatus("mandatory")


class _MscDclVsReceivedAbBits_Type(Integer32):
    """Custom type mscDclVsReceivedAbBits based on Integer32"""
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


_MscDclVsReceivedAbBits_Type.__name__ = "Integer32"
_MscDclVsReceivedAbBits_Object = MibTableColumn
mscDclVsReceivedAbBits = _MscDclVsReceivedAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11, 1, 4),
    _MscDclVsReceivedAbBits_Type()
)
mscDclVsReceivedAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsReceivedAbBits.setStatus("mandatory")


class _MscDclVsTransmittedAbBits_Type(Integer32):
    """Custom type mscDclVsTransmittedAbBits based on Integer32"""
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


_MscDclVsTransmittedAbBits_Type.__name__ = "Integer32"
_MscDclVsTransmittedAbBits_Object = MibTableColumn
mscDclVsTransmittedAbBits = _MscDclVsTransmittedAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 11, 1, 5),
    _MscDclVsTransmittedAbBits_Type()
)
mscDclVsTransmittedAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsTransmittedAbBits.setStatus("mandatory")
_MscDclVsStatsTable_Object = MibTable
mscDclVsStatsTable = _MscDclVsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 12)
)
if mibBuilder.loadTexts:
    mscDclVsStatsTable.setStatus("mandatory")
_MscDclVsStatsEntry_Object = MibTableRow
mscDclVsStatsEntry = _MscDclVsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 12, 1)
)
mscDclVsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsStatsEntry.setStatus("mandatory")
_MscDclVsTotalCalls_Type = Counter32
_MscDclVsTotalCalls_Object = MibTableColumn
mscDclVsTotalCalls = _MscDclVsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 12, 1, 1),
    _MscDclVsTotalCalls_Type()
)
mscDclVsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsTotalCalls.setStatus("mandatory")
_MscDclVsTotalCallSeconds_Type = Counter32
_MscDclVsTotalCallSeconds_Object = MibTableColumn
mscDclVsTotalCallSeconds = _MscDclVsTotalCallSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 12, 1, 2),
    _MscDclVsTotalCallSeconds_Type()
)
mscDclVsTotalCallSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsTotalCallSeconds.setStatus("mandatory")
_MscDclVsInvalidAbBits_Type = Counter32
_MscDclVsInvalidAbBits_Object = MibTableColumn
mscDclVsInvalidAbBits = _MscDclVsInvalidAbBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 12, 1, 3),
    _MscDclVsInvalidAbBits_Type()
)
mscDclVsInvalidAbBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsInvalidAbBits.setStatus("mandatory")
_MscDclVsStateTable_Object = MibTable
mscDclVsStateTable = _MscDclVsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 13)
)
if mibBuilder.loadTexts:
    mscDclVsStateTable.setStatus("mandatory")
_MscDclVsStateEntry_Object = MibTableRow
mscDclVsStateEntry = _MscDclVsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 13, 1)
)
mscDclVsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclVsIndex"),
)
if mibBuilder.loadTexts:
    mscDclVsStateEntry.setStatus("mandatory")


class _MscDclVsAdminState_Type(Integer32):
    """Custom type mscDclVsAdminState based on Integer32"""
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


_MscDclVsAdminState_Type.__name__ = "Integer32"
_MscDclVsAdminState_Object = MibTableColumn
mscDclVsAdminState = _MscDclVsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 13, 1, 1),
    _MscDclVsAdminState_Type()
)
mscDclVsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsAdminState.setStatus("mandatory")


class _MscDclVsOperationalState_Type(Integer32):
    """Custom type mscDclVsOperationalState based on Integer32"""
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


_MscDclVsOperationalState_Type.__name__ = "Integer32"
_MscDclVsOperationalState_Object = MibTableColumn
mscDclVsOperationalState = _MscDclVsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 13, 1, 2),
    _MscDclVsOperationalState_Type()
)
mscDclVsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsOperationalState.setStatus("mandatory")


class _MscDclVsUsageState_Type(Integer32):
    """Custom type mscDclVsUsageState based on Integer32"""
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


_MscDclVsUsageState_Type.__name__ = "Integer32"
_MscDclVsUsageState_Object = MibTableColumn
mscDclVsUsageState = _MscDclVsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 4, 13, 1, 3),
    _MscDclVsUsageState_Type()
)
mscDclVsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclVsUsageState.setStatus("mandatory")
_MscDclProvTable_Object = MibTable
mscDclProvTable = _MscDclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10)
)
if mibBuilder.loadTexts:
    mscDclProvTable.setStatus("mandatory")
_MscDclProvEntry_Object = MibTableRow
mscDclProvEntry = _MscDclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1)
)
mscDclProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
)
if mibBuilder.loadTexts:
    mscDclProvEntry.setStatus("mandatory")


class _MscDclCommentText_Type(AsciiString):
    """Custom type mscDclCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDclCommentText_Type.__name__ = "AsciiString"
_MscDclCommentText_Object = MibTableColumn
mscDclCommentText = _MscDclCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 1),
    _MscDclCommentText_Type()
)
mscDclCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclCommentText.setStatus("mandatory")


class _MscDclRemoteNpi_Type(Integer32):
    """Custom type mscDclRemoteNpi based on Integer32"""
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


_MscDclRemoteNpi_Type.__name__ = "Integer32"
_MscDclRemoteNpi_Object = MibTableColumn
mscDclRemoteNpi = _MscDclRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 2),
    _MscDclRemoteNpi_Type()
)
mscDclRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclRemoteNpi.setStatus("mandatory")


class _MscDclRemoteDna_Type(DigitString):
    """Custom type mscDclRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscDclRemoteDna_Type.__name__ = "DigitString"
_MscDclRemoteDna_Object = MibTableColumn
mscDclRemoteDna = _MscDclRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 3),
    _MscDclRemoteDna_Type()
)
mscDclRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclRemoteDna.setStatus("mandatory")
_MscDclDcme_Type = Link
_MscDclDcme_Object = MibTableColumn
mscDclDcme = _MscDclDcme_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 4),
    _MscDclDcme_Type()
)
mscDclDcme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclDcme.setStatus("mandatory")


class _MscDclIdlePattern_Type(Hex):
    """Custom type mscDclIdlePattern based on Hex"""
    defaultValue = 213

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDclIdlePattern_Type.__name__ = "Hex"
_MscDclIdlePattern_Object = MibTableColumn
mscDclIdlePattern = _MscDclIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 5),
    _MscDclIdlePattern_Type()
)
mscDclIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclIdlePattern.setStatus("mandatory")


class _MscDclAlternateIdlePattern_Type(Hex):
    """Custom type mscDclAlternateIdlePattern based on Hex"""
    defaultValue = 213

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDclAlternateIdlePattern_Type.__name__ = "Hex"
_MscDclAlternateIdlePattern_Object = MibTableColumn
mscDclAlternateIdlePattern = _MscDclAlternateIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 10, 1, 6),
    _MscDclAlternateIdlePattern_Type()
)
mscDclAlternateIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDclAlternateIdlePattern.setStatus("mandatory")
_MscDclStateTable_Object = MibTable
mscDclStateTable = _MscDclStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 11)
)
if mibBuilder.loadTexts:
    mscDclStateTable.setStatus("mandatory")
_MscDclStateEntry_Object = MibTableRow
mscDclStateEntry = _MscDclStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 11, 1)
)
mscDclStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
)
if mibBuilder.loadTexts:
    mscDclStateEntry.setStatus("mandatory")


class _MscDclAdminState_Type(Integer32):
    """Custom type mscDclAdminState based on Integer32"""
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


_MscDclAdminState_Type.__name__ = "Integer32"
_MscDclAdminState_Object = MibTableColumn
mscDclAdminState = _MscDclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 11, 1, 1),
    _MscDclAdminState_Type()
)
mscDclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclAdminState.setStatus("mandatory")


class _MscDclOperationalState_Type(Integer32):
    """Custom type mscDclOperationalState based on Integer32"""
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


_MscDclOperationalState_Type.__name__ = "Integer32"
_MscDclOperationalState_Object = MibTableColumn
mscDclOperationalState = _MscDclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 11, 1, 2),
    _MscDclOperationalState_Type()
)
mscDclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclOperationalState.setStatus("mandatory")


class _MscDclUsageState_Type(Integer32):
    """Custom type mscDclUsageState based on Integer32"""
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


_MscDclUsageState_Type.__name__ = "Integer32"
_MscDclUsageState_Object = MibTableColumn
mscDclUsageState = _MscDclUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 11, 1, 3),
    _MscDclUsageState_Type()
)
mscDclUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclUsageState.setStatus("mandatory")
_MscDclOperTable_Object = MibTable
mscDclOperTable = _MscDclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12)
)
if mibBuilder.loadTexts:
    mscDclOperTable.setStatus("mandatory")
_MscDclOperEntry_Object = MibTableRow
mscDclOperEntry = _MscDclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1)
)
mscDclOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
)
if mibBuilder.loadTexts:
    mscDclOperEntry.setStatus("mandatory")


class _MscDclActiveSpeechCalls_Type(Gauge32):
    """Custom type mscDclActiveSpeechCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscDclActiveSpeechCalls_Type.__name__ = "Gauge32"
_MscDclActiveSpeechCalls_Object = MibTableColumn
mscDclActiveSpeechCalls = _MscDclActiveSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1, 1),
    _MscDclActiveSpeechCalls_Type()
)
mscDclActiveSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclActiveSpeechCalls.setStatus("mandatory")


class _MscDclActive3kHzCalls_Type(Gauge32):
    """Custom type mscDclActive3kHzCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscDclActive3kHzCalls_Type.__name__ = "Gauge32"
_MscDclActive3kHzCalls_Object = MibTableColumn
mscDclActive3kHzCalls = _MscDclActive3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1, 2),
    _MscDclActive3kHzCalls_Type()
)
mscDclActive3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclActive3kHzCalls.setStatus("mandatory")


class _MscDclActive64kCalls_Type(Gauge32):
    """Custom type mscDclActive64kCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscDclActive64kCalls_Type.__name__ = "Gauge32"
_MscDclActive64kCalls_Object = MibTableColumn
mscDclActive64kCalls = _MscDclActive64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1, 3),
    _MscDclActive64kCalls_Type()
)
mscDclActive64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclActive64kCalls.setStatus("mandatory")


class _MscDclReceivedTrmSignal_Type(Integer32):
    """Custom type mscDclReceivedTrmSignal based on Integer32"""
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


_MscDclReceivedTrmSignal_Type.__name__ = "Integer32"
_MscDclReceivedTrmSignal_Object = MibTableColumn
mscDclReceivedTrmSignal = _MscDclReceivedTrmSignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1, 4),
    _MscDclReceivedTrmSignal_Type()
)
mscDclReceivedTrmSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclReceivedTrmSignal.setStatus("mandatory")


class _MscDclTransmittedTrmSignal_Type(Integer32):
    """Custom type mscDclTransmittedTrmSignal based on Integer32"""
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


_MscDclTransmittedTrmSignal_Type.__name__ = "Integer32"
_MscDclTransmittedTrmSignal_Object = MibTableColumn
mscDclTransmittedTrmSignal = _MscDclTransmittedTrmSignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 12, 1, 5),
    _MscDclTransmittedTrmSignal_Type()
)
mscDclTransmittedTrmSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclTransmittedTrmSignal.setStatus("mandatory")
_MscDclStatsTable_Object = MibTable
mscDclStatsTable = _MscDclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13)
)
if mibBuilder.loadTexts:
    mscDclStatsTable.setStatus("mandatory")
_MscDclStatsEntry_Object = MibTableRow
mscDclStatsEntry = _MscDclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1)
)
mscDclStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DcmeMIB", "mscDclIndex"),
)
if mibBuilder.loadTexts:
    mscDclStatsEntry.setStatus("mandatory")
_MscDclTotalSpeechCalls_Type = Counter32
_MscDclTotalSpeechCalls_Object = MibTableColumn
mscDclTotalSpeechCalls = _MscDclTotalSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 1),
    _MscDclTotalSpeechCalls_Type()
)
mscDclTotalSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclTotalSpeechCalls.setStatus("mandatory")
_MscDclTotal3kHzCalls_Type = Counter32
_MscDclTotal3kHzCalls_Object = MibTableColumn
mscDclTotal3kHzCalls = _MscDclTotal3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 2),
    _MscDclTotal3kHzCalls_Type()
)
mscDclTotal3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclTotal3kHzCalls.setStatus("mandatory")
_MscDclTotal64kCalls_Type = Counter32
_MscDclTotal64kCalls_Object = MibTableColumn
mscDclTotal64kCalls = _MscDclTotal64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 3),
    _MscDclTotal64kCalls_Type()
)
mscDclTotal64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclTotal64kCalls.setStatus("mandatory")
_MscDclRejectedSpeechCalls_Type = Counter32
_MscDclRejectedSpeechCalls_Object = MibTableColumn
mscDclRejectedSpeechCalls = _MscDclRejectedSpeechCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 4),
    _MscDclRejectedSpeechCalls_Type()
)
mscDclRejectedSpeechCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclRejectedSpeechCalls.setStatus("mandatory")
_MscDclRejected3kHzCalls_Type = Counter32
_MscDclRejected3kHzCalls_Object = MibTableColumn
mscDclRejected3kHzCalls = _MscDclRejected3kHzCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 5),
    _MscDclRejected3kHzCalls_Type()
)
mscDclRejected3kHzCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclRejected3kHzCalls.setStatus("mandatory")
_MscDclRejected64kCalls_Type = Counter32
_MscDclRejected64kCalls_Object = MibTableColumn
mscDclRejected64kCalls = _MscDclRejected64kCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 6),
    _MscDclRejected64kCalls_Type()
)
mscDclRejected64kCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclRejected64kCalls.setStatus("mandatory")
_MscDclInvalidTrmSignals_Type = Counter32
_MscDclInvalidTrmSignals_Object = MibTableColumn
mscDclInvalidTrmSignals = _MscDclInvalidTrmSignals_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 130, 13, 1, 7),
    _MscDclInvalidTrmSignals_Type()
)
mscDclInvalidTrmSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDclInvalidTrmSignals.setStatus("mandatory")
_DcmeMIB_ObjectIdentity = ObjectIdentity
dcmeMIB = _DcmeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134)
)
_DcmeGroup_ObjectIdentity = ObjectIdentity
dcmeGroup = _DcmeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 1)
)
_DcmeGroupCA_ObjectIdentity = ObjectIdentity
dcmeGroupCA = _DcmeGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 1, 1)
)
_DcmeGroupCA02_ObjectIdentity = ObjectIdentity
dcmeGroupCA02 = _DcmeGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 1, 1, 3)
)
_DcmeGroupCA02A_ObjectIdentity = ObjectIdentity
dcmeGroupCA02A = _DcmeGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 1, 1, 3, 2)
)
_DcmeCapabilities_ObjectIdentity = ObjectIdentity
dcmeCapabilities = _DcmeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 3)
)
_DcmeCapabilitiesCA_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesCA = _DcmeCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 3, 1)
)
_DcmeCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesCA02 = _DcmeCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 3, 1, 3)
)
_DcmeCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dcmeCapabilitiesCA02A = _DcmeCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 134, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DcmeMIB",
    **{"mscDcme": mscDcme,
       "mscDcmeRowStatusTable": mscDcmeRowStatusTable,
       "mscDcmeRowStatusEntry": mscDcmeRowStatusEntry,
       "mscDcmeRowStatus": mscDcmeRowStatus,
       "mscDcmeComponentName": mscDcmeComponentName,
       "mscDcmeStorageType": mscDcmeStorageType,
       "mscDcmeIndex": mscDcmeIndex,
       "mscDcmeProfile": mscDcmeProfile,
       "mscDcmeProfileRowStatusTable": mscDcmeProfileRowStatusTable,
       "mscDcmeProfileRowStatusEntry": mscDcmeProfileRowStatusEntry,
       "mscDcmeProfileRowStatus": mscDcmeProfileRowStatus,
       "mscDcmeProfileComponentName": mscDcmeProfileComponentName,
       "mscDcmeProfileStorageType": mscDcmeProfileStorageType,
       "mscDcmeProfileIndex": mscDcmeProfileIndex,
       "mscDcmeProfileLCOpsTable": mscDcmeProfileLCOpsTable,
       "mscDcmeProfileLCOpsEntry": mscDcmeProfileLCOpsEntry,
       "mscDcmeProfileSetupPriority": mscDcmeProfileSetupPriority,
       "mscDcmeProfileHoldingPriority": mscDcmeProfileHoldingPriority,
       "mscDcmeProfileBumpPreference": mscDcmeProfileBumpPreference,
       "mscDcmeProfileRequiredTrafficType": mscDcmeProfileRequiredTrafficType,
       "mscDcmeProfilePermittedTrunkTypes": mscDcmeProfilePermittedTrunkTypes,
       "mscDcmeProfileRequiredSecurity": mscDcmeProfileRequiredSecurity,
       "mscDcmeProfileRequiredCustomerParm": mscDcmeProfileRequiredCustomerParm,
       "mscDcmeProfilePathAttributeToMinimize": mscDcmeProfilePathAttributeToMinimize,
       "mscDcmeProfileMaximumAcceptableCost": mscDcmeProfileMaximumAcceptableCost,
       "mscDcmeProfileMaximumAcceptableDelay": mscDcmeProfileMaximumAcceptableDelay,
       "mscDcmeProfileEmissionPriority": mscDcmeProfileEmissionPriority,
       "mscDcmeProfileDiscardPriority": mscDcmeProfileDiscardPriority,
       "mscDcmeProfilePathFailureAction": mscDcmeProfilePathFailureAction,
       "mscDcmeProfileOptimization": mscDcmeProfileOptimization,
       "mscDcmeProfileFrOpsTable": mscDcmeProfileFrOpsTable,
       "mscDcmeProfileFrOpsEntry": mscDcmeProfileFrOpsEntry,
       "mscDcmeProfileVoiceEncoding": mscDcmeProfileVoiceEncoding,
       "mscDcmeProfileMaxVoiceBitRate": mscDcmeProfileMaxVoiceBitRate,
       "mscDcmeProfileMinVoiceBitRate": mscDcmeProfileMinVoiceBitRate,
       "mscDcmeProfileVoiceTrafficOptimization": mscDcmeProfileVoiceTrafficOptimization,
       "mscDcmeProfileSilenceSuppression": mscDcmeProfileSilenceSuppression,
       "mscDcmeProfileSilenceSuppressionFactor": mscDcmeProfileSilenceSuppressionFactor,
       "mscDcmeProfileEchoCancellation": mscDcmeProfileEchoCancellation,
       "mscDcmeProfileModemFaxEncoding": mscDcmeProfileModemFaxEncoding,
       "mscDcmeProfileMaxModemFaxG711G726Rate": mscDcmeProfileMaxModemFaxG711G726Rate,
       "mscDcmeProfileMinModemFaxG711G726Rate": mscDcmeProfileMinModemFaxG711G726Rate,
       "mscDcmeProfileFaxIdleSuppressionG711G726": mscDcmeProfileFaxIdleSuppressionG711G726,
       "mscDcmeProfileInsertedOutputDelay": mscDcmeProfileInsertedOutputDelay,
       "mscDcmeProfileIngressAudioGain": mscDcmeProfileIngressAudioGain,
       "mscDcmeProfileEgressAudioGain": mscDcmeProfileEgressAudioGain,
       "mscDcmeProfileSpeechHangoverTime": mscDcmeProfileSpeechHangoverTime,
       "mscDcmeProfileComfortNoiseCap": mscDcmeProfileComfortNoiseCap,
       "mscDcmeProfileModemFaxSpeechDiscrim": mscDcmeProfileModemFaxSpeechDiscrim,
       "mscDcmeProfileV17EncodedAsG711G726": mscDcmeProfileV17EncodedAsG711G726,
       "mscDcmeProfileDtmfRegeneration": mscDcmeProfileDtmfRegeneration,
       "mscDcmeProfileMaxFaxRelayRate": mscDcmeProfileMaxFaxRelayRate,
       "mscDcmeProvTable": mscDcmeProvTable,
       "mscDcmeProvEntry": mscDcmeProvEntry,
       "mscDcmeCommentText": mscDcmeCommentText,
       "mscDcmePreestablishedConnections": mscDcmePreestablishedConnections,
       "mscDcmeTrmThreshold": mscDcmeTrmThreshold,
       "mscDcmeTrmSignalChangeInterval": mscDcmeTrmSignalChangeInterval,
       "mscDcmeSpeechAlarmThreshold": mscDcmeSpeechAlarmThreshold,
       "mscDcmeAudio3kHzAlarmThreshold": mscDcmeAudio3kHzAlarmThreshold,
       "mscDcmeUnrestricted64kAlarmThreshold": mscDcmeUnrestricted64kAlarmThreshold,
       "mscDcmeAlarmTimeInterval": mscDcmeAlarmTimeInterval,
       "mscDcmeMaxUnrestricted64kCalls": mscDcmeMaxUnrestricted64kCalls,
       "mscDcmeStateTable": mscDcmeStateTable,
       "mscDcmeStateEntry": mscDcmeStateEntry,
       "mscDcmeAdminState": mscDcmeAdminState,
       "mscDcmeOperationalState": mscDcmeOperationalState,
       "mscDcmeUsageState": mscDcmeUsageState,
       "mscDcmeStatsTable": mscDcmeStatsTable,
       "mscDcmeStatsEntry": mscDcmeStatsEntry,
       "mscDcmeTrm64kNotAvailable": mscDcmeTrm64kNotAvailable,
       "mscDcmeTrmSpeechNotAvailable": mscDcmeTrmSpeechNotAvailable,
       "mscDcmeDLinksTable": mscDcmeDLinksTable,
       "mscDcmeDLinksEntry": mscDcmeDLinksEntry,
       "mscDcmeDLinksValue": mscDcmeDLinksValue,
       "mscDcmeDLinksRowStatus": mscDcmeDLinksRowStatus,
       "mscDcmeActiveDcmeLinksTable": mscDcmeActiveDcmeLinksTable,
       "mscDcmeActiveDcmeLinksEntry": mscDcmeActiveDcmeLinksEntry,
       "mscDcmeActiveDcmeLinksValue": mscDcmeActiveDcmeLinksValue,
       "mscDcl": mscDcl,
       "mscDclRowStatusTable": mscDclRowStatusTable,
       "mscDclRowStatusEntry": mscDclRowStatusEntry,
       "mscDclRowStatus": mscDclRowStatus,
       "mscDclComponentName": mscDclComponentName,
       "mscDclStorageType": mscDclStorageType,
       "mscDclIndex": mscDclIndex,
       "mscDclDna": mscDclDna,
       "mscDclDnaRowStatusTable": mscDclDnaRowStatusTable,
       "mscDclDnaRowStatusEntry": mscDclDnaRowStatusEntry,
       "mscDclDnaRowStatus": mscDclDnaRowStatus,
       "mscDclDnaComponentName": mscDclDnaComponentName,
       "mscDclDnaStorageType": mscDclDnaStorageType,
       "mscDclDnaIndex": mscDclDnaIndex,
       "mscDclDnaAddressTable": mscDclDnaAddressTable,
       "mscDclDnaAddressEntry": mscDclDnaAddressEntry,
       "mscDclDnaNumberingPlanIndicator": mscDclDnaNumberingPlanIndicator,
       "mscDclDnaDataNetworkAddress": mscDclDnaDataNetworkAddress,
       "mscDclFramer": mscDclFramer,
       "mscDclFramerRowStatusTable": mscDclFramerRowStatusTable,
       "mscDclFramerRowStatusEntry": mscDclFramerRowStatusEntry,
       "mscDclFramerRowStatus": mscDclFramerRowStatus,
       "mscDclFramerComponentName": mscDclFramerComponentName,
       "mscDclFramerStorageType": mscDclFramerStorageType,
       "mscDclFramerIndex": mscDclFramerIndex,
       "mscDclFramerProvTable": mscDclFramerProvTable,
       "mscDclFramerProvEntry": mscDclFramerProvEntry,
       "mscDclFramerInterfaceName": mscDclFramerInterfaceName,
       "mscDclFramerStateTable": mscDclFramerStateTable,
       "mscDclFramerStateEntry": mscDclFramerStateEntry,
       "mscDclFramerAdminState": mscDclFramerAdminState,
       "mscDclFramerOperationalState": mscDclFramerOperationalState,
       "mscDclFramerUsageState": mscDclFramerUsageState,
       "mscDclVs": mscDclVs,
       "mscDclVsRowStatusTable": mscDclVsRowStatusTable,
       "mscDclVsRowStatusEntry": mscDclVsRowStatusEntry,
       "mscDclVsRowStatus": mscDclVsRowStatus,
       "mscDclVsComponentName": mscDclVsComponentName,
       "mscDclVsStorageType": mscDclVsStorageType,
       "mscDclVsIndex": mscDclVsIndex,
       "mscDclVsFramer": mscDclVsFramer,
       "mscDclVsFramerRowStatusTable": mscDclVsFramerRowStatusTable,
       "mscDclVsFramerRowStatusEntry": mscDclVsFramerRowStatusEntry,
       "mscDclVsFramerRowStatus": mscDclVsFramerRowStatus,
       "mscDclVsFramerComponentName": mscDclVsFramerComponentName,
       "mscDclVsFramerStorageType": mscDclVsFramerStorageType,
       "mscDclVsFramerIndex": mscDclVsFramerIndex,
       "mscDclVsFramerVfpDebug": mscDclVsFramerVfpDebug,
       "mscDclVsFramerVfpDebugRowStatusTable": mscDclVsFramerVfpDebugRowStatusTable,
       "mscDclVsFramerVfpDebugRowStatusEntry": mscDclVsFramerVfpDebugRowStatusEntry,
       "mscDclVsFramerVfpDebugRowStatus": mscDclVsFramerVfpDebugRowStatus,
       "mscDclVsFramerVfpDebugComponentName": mscDclVsFramerVfpDebugComponentName,
       "mscDclVsFramerVfpDebugStorageType": mscDclVsFramerVfpDebugStorageType,
       "mscDclVsFramerVfpDebugIndex": mscDclVsFramerVfpDebugIndex,
       "mscDclVsFramerMvpDebug": mscDclVsFramerMvpDebug,
       "mscDclVsFramerMvpDebugRowStatusTable": mscDclVsFramerMvpDebugRowStatusTable,
       "mscDclVsFramerMvpDebugRowStatusEntry": mscDclVsFramerMvpDebugRowStatusEntry,
       "mscDclVsFramerMvpDebugRowStatus": mscDclVsFramerMvpDebugRowStatus,
       "mscDclVsFramerMvpDebugComponentName": mscDclVsFramerMvpDebugComponentName,
       "mscDclVsFramerMvpDebugStorageType": mscDclVsFramerMvpDebugStorageType,
       "mscDclVsFramerMvpDebugIndex": mscDclVsFramerMvpDebugIndex,
       "mscDclVsFramerPcmCapture": mscDclVsFramerPcmCapture,
       "mscDclVsFramerPcmCaptureRowStatusTable": mscDclVsFramerPcmCaptureRowStatusTable,
       "mscDclVsFramerPcmCaptureRowStatusEntry": mscDclVsFramerPcmCaptureRowStatusEntry,
       "mscDclVsFramerPcmCaptureRowStatus": mscDclVsFramerPcmCaptureRowStatus,
       "mscDclVsFramerPcmCaptureComponentName": mscDclVsFramerPcmCaptureComponentName,
       "mscDclVsFramerPcmCaptureStorageType": mscDclVsFramerPcmCaptureStorageType,
       "mscDclVsFramerPcmCaptureIndex": mscDclVsFramerPcmCaptureIndex,
       "mscDclVsFramerProvTable": mscDclVsFramerProvTable,
       "mscDclVsFramerProvEntry": mscDclVsFramerProvEntry,
       "mscDclVsFramerInterfaceName": mscDclVsFramerInterfaceName,
       "mscDclVsFramerStateTable": mscDclVsFramerStateTable,
       "mscDclVsFramerStateEntry": mscDclVsFramerStateEntry,
       "mscDclVsFramerAdminState": mscDclVsFramerAdminState,
       "mscDclVsFramerOperationalState": mscDclVsFramerOperationalState,
       "mscDclVsFramerUsageState": mscDclVsFramerUsageState,
       "mscDclVsFramerStatsTable": mscDclVsFramerStatsTable,
       "mscDclVsFramerStatsEntry": mscDclVsFramerStatsEntry,
       "mscDclVsFramerTotalCells": mscDclVsFramerTotalCells,
       "mscDclVsFramerAudioCells": mscDclVsFramerAudioCells,
       "mscDclVsFramerSilenceCells": mscDclVsFramerSilenceCells,
       "mscDclVsFramerModemCells": mscDclVsFramerModemCells,
       "mscDclVsFramerCurrentEncodingRate": mscDclVsFramerCurrentEncodingRate,
       "mscDclVsFramerLrcErrors": mscDclVsFramerLrcErrors,
       "mscDclVsFramerFrmLostInNetwork": mscDclVsFramerFrmLostInNetwork,
       "mscDclVsFramerFrmUnderRuns": mscDclVsFramerFrmUnderRuns,
       "mscDclVsFramerFrmDumped": mscDclVsFramerFrmDumped,
       "mscDclVsFramerModemSilenceCells": mscDclVsFramerModemSilenceCells,
       "mscDclVsFramerCurrentEncoding": mscDclVsFramerCurrentEncoding,
       "mscDclVsFramerTptStatus": mscDclVsFramerTptStatus,
       "mscDclVsFramerFaxRelayCells": mscDclVsFramerFaxRelayCells,
       "mscDclVsFramerModemFaxCells": mscDclVsFramerModemFaxCells,
       "mscDclVsFramerFaxIdleCells": mscDclVsFramerFaxIdleCells,
       "mscDclVsFramerOperTable": mscDclVsFramerOperTable,
       "mscDclVsFramerOperEntry": mscDclVsFramerOperEntry,
       "mscDclVsFramerOpCurrentEncoding": mscDclVsFramerOpCurrentEncoding,
       "mscDclVsFramerCurrentRate": mscDclVsFramerCurrentRate,
       "mscDclVsFramerOpTptStatus": mscDclVsFramerOpTptStatus,
       "mscDclVsFramerNegTable": mscDclVsFramerNegTable,
       "mscDclVsFramerNegEntry": mscDclVsFramerNegEntry,
       "mscDclVsFramerNegotiatedSilenceSuppression": mscDclVsFramerNegotiatedSilenceSuppression,
       "mscDclVsFramerNegotiatedFisG711G726": mscDclVsFramerNegotiatedFisG711G726,
       "mscDclVsFramerNegotiatedDtmfRegeneration": mscDclVsFramerNegotiatedDtmfRegeneration,
       "mscDclVsFramerNegotiatedV17AsG711G726": mscDclVsFramerNegotiatedV17AsG711G726,
       "mscDclVsFramerNegotiatedTandemPassThrough": mscDclVsFramerNegotiatedTandemPassThrough,
       "mscDclVsFramerFrmToNetworkTable": mscDclVsFramerFrmToNetworkTable,
       "mscDclVsFramerFrmToNetworkEntry": mscDclVsFramerFrmToNetworkEntry,
       "mscDclVsFramerFrmToNetworkIndex": mscDclVsFramerFrmToNetworkIndex,
       "mscDclVsFramerFrmToNetworkValue": mscDclVsFramerFrmToNetworkValue,
       "mscDclVsFramerFrmFromNetworkTable": mscDclVsFramerFrmFromNetworkTable,
       "mscDclVsFramerFrmFromNetworkEntry": mscDclVsFramerFrmFromNetworkEntry,
       "mscDclVsFramerFrmFromNetworkIndex": mscDclVsFramerFrmFromNetworkIndex,
       "mscDclVsFramerFrmFromNetworkValue": mscDclVsFramerFrmFromNetworkValue,
       "mscDclVsFramerNEncodingTable": mscDclVsFramerNEncodingTable,
       "mscDclVsFramerNEncodingEntry": mscDclVsFramerNEncodingEntry,
       "mscDclVsFramerNEncodingIndex": mscDclVsFramerNEncodingIndex,
       "mscDclVsFramerNEncodingValue": mscDclVsFramerNEncodingValue,
       "mscDclVsFramerNRatesTable": mscDclVsFramerNRatesTable,
       "mscDclVsFramerNRatesEntry": mscDclVsFramerNRatesEntry,
       "mscDclVsFramerNRatesTrafficIndex": mscDclVsFramerNRatesTrafficIndex,
       "mscDclVsFramerNRatesRateIndex": mscDclVsFramerNRatesRateIndex,
       "mscDclVsFramerNRatesValue": mscDclVsFramerNRatesValue,
       "mscDclVsLCo": mscDclVsLCo,
       "mscDclVsLCoRowStatusTable": mscDclVsLCoRowStatusTable,
       "mscDclVsLCoRowStatusEntry": mscDclVsLCoRowStatusEntry,
       "mscDclVsLCoRowStatus": mscDclVsLCoRowStatus,
       "mscDclVsLCoComponentName": mscDclVsLCoComponentName,
       "mscDclVsLCoStorageType": mscDclVsLCoStorageType,
       "mscDclVsLCoIndex": mscDclVsLCoIndex,
       "mscDclVsLCoPathDataTable": mscDclVsLCoPathDataTable,
       "mscDclVsLCoPathDataEntry": mscDclVsLCoPathDataEntry,
       "mscDclVsLCoState": mscDclVsLCoState,
       "mscDclVsLCoOverrideRemoteName": mscDclVsLCoOverrideRemoteName,
       "mscDclVsLCoEnd": mscDclVsLCoEnd,
       "mscDclVsLCoCostMetric": mscDclVsLCoCostMetric,
       "mscDclVsLCoDelayMetric": mscDclVsLCoDelayMetric,
       "mscDclVsLCoRoundTripDelay": mscDclVsLCoRoundTripDelay,
       "mscDclVsLCoSetupPriority": mscDclVsLCoSetupPriority,
       "mscDclVsLCoHoldingPriority": mscDclVsLCoHoldingPriority,
       "mscDclVsLCoRequiredTxBandwidth": mscDclVsLCoRequiredTxBandwidth,
       "mscDclVsLCoRequiredRxBandwidth": mscDclVsLCoRequiredRxBandwidth,
       "mscDclVsLCoRequiredTrafficType": mscDclVsLCoRequiredTrafficType,
       "mscDclVsLCoPermittedTrunkTypes": mscDclVsLCoPermittedTrunkTypes,
       "mscDclVsLCoRequiredSecurity": mscDclVsLCoRequiredSecurity,
       "mscDclVsLCoRequiredCustomerParameter": mscDclVsLCoRequiredCustomerParameter,
       "mscDclVsLCoEmissionPriority": mscDclVsLCoEmissionPriority,
       "mscDclVsLCoDiscardPriority": mscDclVsLCoDiscardPriority,
       "mscDclVsLCoPathType": mscDclVsLCoPathType,
       "mscDclVsLCoRetryCount": mscDclVsLCoRetryCount,
       "mscDclVsLCoPathFailureCount": mscDclVsLCoPathFailureCount,
       "mscDclVsLCoReasonForNoRoute": mscDclVsLCoReasonForNoRoute,
       "mscDclVsLCoLastTearDownReason": mscDclVsLCoLastTearDownReason,
       "mscDclVsLCoPathFailureAction": mscDclVsLCoPathFailureAction,
       "mscDclVsLCoBumpPreference": mscDclVsLCoBumpPreference,
       "mscDclVsLCoOptimization": mscDclVsLCoOptimization,
       "mscDclVsLCoPathUpDateTime": mscDclVsLCoPathUpDateTime,
       "mscDclVsLCoStatsTable": mscDclVsLCoStatsTable,
       "mscDclVsLCoStatsEntry": mscDclVsLCoStatsEntry,
       "mscDclVsLCoPktsToNetwork": mscDclVsLCoPktsToNetwork,
       "mscDclVsLCoBytesToNetwork": mscDclVsLCoBytesToNetwork,
       "mscDclVsLCoPktsFromNetwork": mscDclVsLCoPktsFromNetwork,
       "mscDclVsLCoBytesFromNetwork": mscDclVsLCoBytesFromNetwork,
       "mscDclVsLCoPathTable": mscDclVsLCoPathTable,
       "mscDclVsLCoPathEntry": mscDclVsLCoPathEntry,
       "mscDclVsLCoPathValue": mscDclVsLCoPathValue,
       "mscDclVsProvTable": mscDclVsProvTable,
       "mscDclVsProvEntry": mscDclVsProvEntry,
       "mscDclVsVsType": mscDclVsVsType,
       "mscDclVsOperTable": mscDclVsOperTable,
       "mscDclVsOperEntry": mscDclVsOperEntry,
       "mscDclVsStatus": mscDclVsStatus,
       "mscDclVsCallType": mscDclVsCallType,
       "mscDclVsReceivedAbBits": mscDclVsReceivedAbBits,
       "mscDclVsTransmittedAbBits": mscDclVsTransmittedAbBits,
       "mscDclVsStatsTable": mscDclVsStatsTable,
       "mscDclVsStatsEntry": mscDclVsStatsEntry,
       "mscDclVsTotalCalls": mscDclVsTotalCalls,
       "mscDclVsTotalCallSeconds": mscDclVsTotalCallSeconds,
       "mscDclVsInvalidAbBits": mscDclVsInvalidAbBits,
       "mscDclVsStateTable": mscDclVsStateTable,
       "mscDclVsStateEntry": mscDclVsStateEntry,
       "mscDclVsAdminState": mscDclVsAdminState,
       "mscDclVsOperationalState": mscDclVsOperationalState,
       "mscDclVsUsageState": mscDclVsUsageState,
       "mscDclProvTable": mscDclProvTable,
       "mscDclProvEntry": mscDclProvEntry,
       "mscDclCommentText": mscDclCommentText,
       "mscDclRemoteNpi": mscDclRemoteNpi,
       "mscDclRemoteDna": mscDclRemoteDna,
       "mscDclDcme": mscDclDcme,
       "mscDclIdlePattern": mscDclIdlePattern,
       "mscDclAlternateIdlePattern": mscDclAlternateIdlePattern,
       "mscDclStateTable": mscDclStateTable,
       "mscDclStateEntry": mscDclStateEntry,
       "mscDclAdminState": mscDclAdminState,
       "mscDclOperationalState": mscDclOperationalState,
       "mscDclUsageState": mscDclUsageState,
       "mscDclOperTable": mscDclOperTable,
       "mscDclOperEntry": mscDclOperEntry,
       "mscDclActiveSpeechCalls": mscDclActiveSpeechCalls,
       "mscDclActive3kHzCalls": mscDclActive3kHzCalls,
       "mscDclActive64kCalls": mscDclActive64kCalls,
       "mscDclReceivedTrmSignal": mscDclReceivedTrmSignal,
       "mscDclTransmittedTrmSignal": mscDclTransmittedTrmSignal,
       "mscDclStatsTable": mscDclStatsTable,
       "mscDclStatsEntry": mscDclStatsEntry,
       "mscDclTotalSpeechCalls": mscDclTotalSpeechCalls,
       "mscDclTotal3kHzCalls": mscDclTotal3kHzCalls,
       "mscDclTotal64kCalls": mscDclTotal64kCalls,
       "mscDclRejectedSpeechCalls": mscDclRejectedSpeechCalls,
       "mscDclRejected3kHzCalls": mscDclRejected3kHzCalls,
       "mscDclRejected64kCalls": mscDclRejected64kCalls,
       "mscDclInvalidTrmSignals": mscDclInvalidTrmSignals,
       "dcmeMIB": dcmeMIB,
       "dcmeGroup": dcmeGroup,
       "dcmeGroupCA": dcmeGroupCA,
       "dcmeGroupCA02": dcmeGroupCA02,
       "dcmeGroupCA02A": dcmeGroupCA02A,
       "dcmeCapabilities": dcmeCapabilities,
       "dcmeCapabilitiesCA": dcmeCapabilitiesCA,
       "dcmeCapabilitiesCA02": dcmeCapabilitiesCA02,
       "dcmeCapabilitiesCA02A": dcmeCapabilitiesCA02A}
)
