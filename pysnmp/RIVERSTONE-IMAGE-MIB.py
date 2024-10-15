# SNMP MIB module (RIVERSTONE-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-IMAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:46 2024
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

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rsImageMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13)
)
rsImageMib.setRevisions(
        ("2001-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsImageMibErrorCode(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("commandCompleted", 7),
          ("internalError", 8),
          ("invalidImage", 6),
          ("networkError", 4),
          ("noInfo", 1),
          ("noSpace", 5),
          ("successfullyCompleted", 2),
          ("tftpServerError", 9),
          ("timeout", 3))
    )



class RsImageMibControlModuleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupCM", 2),
          ("primaryCM", 1))
    )



class RsImageMibSlotIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slot0", 1),
          ("slot1", 2))
    )



class RsImageMibImageIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firstImage", 1),
          ("secondImage", 2),
          ("thirdImage", 3))
    )



class RsImageMibChosen(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chosen", 2),
          ("noInfo", 1),
          ("notChosen", 3))
    )



# MIB Managed Objects in the order of their OIDs



class _RsImageMibAction_Type(Integer32):
    """Custom type rsImageMibAction based on Integer32"""
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
        *(("addImageToAgent", 2),
          ("chooseImageOnAgent", 4),
          ("deleteImageFromAgent", 3),
          ("noop", 1))
    )


_RsImageMibAction_Type.__name__ = "Integer32"
_RsImageMibAction_Object = MibScalar
rsImageMibAction = _RsImageMibAction_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 1),
    _RsImageMibAction_Type()
)
rsImageMibAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibAction.setStatus("current")
_RsImageMibTftpServerAddress_Type = IpAddress
_RsImageMibTftpServerAddress_Object = MibScalar
rsImageMibTftpServerAddress = _RsImageMibTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 2),
    _RsImageMibTftpServerAddress_Type()
)
rsImageMibTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibTftpServerAddress.setStatus("current")


class _RsImageMibHostName_Type(DisplayString):
    """Custom type rsImageMibHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibHostName_Type.__name__ = "DisplayString"
_RsImageMibHostName_Object = MibScalar
rsImageMibHostName = _RsImageMibHostName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 3),
    _RsImageMibHostName_Type()
)
rsImageMibHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibHostName.setStatus("current")


class _RsImageMibTftpUrl_Type(DisplayString):
    """Custom type rsImageMibTftpUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibTftpUrl_Type.__name__ = "DisplayString"
_RsImageMibTftpUrl_Object = MibScalar
rsImageMibTftpUrl = _RsImageMibTftpUrl_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 4),
    _RsImageMibTftpUrl_Type()
)
rsImageMibTftpUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibTftpUrl.setStatus("current")


class _RsImageMibImageName_Type(DisplayString):
    """Custom type rsImageMibImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibImageName_Type.__name__ = "DisplayString"
_RsImageMibImageName_Object = MibScalar
rsImageMibImageName = _RsImageMibImageName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 5),
    _RsImageMibImageName_Type()
)
rsImageMibImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibImageName.setStatus("current")


class _RsImageMibDestination_Type(Integer32):
    """Custom type rsImageMibDestination based on Integer32"""
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
        *(("bCM", 3),
          ("bCMslot0", 6),
          ("bCMslot1", 7),
          ("both", 1),
          ("pCM", 2),
          ("pCMslot0", 4),
          ("pCMslot1", 5))
    )


_RsImageMibDestination_Type.__name__ = "Integer32"
_RsImageMibDestination_Object = MibScalar
rsImageMibDestination = _RsImageMibDestination_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 6),
    _RsImageMibDestination_Type()
)
rsImageMibDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibDestination.setStatus("current")
_RsImageMibActivateTransfer_Type = TruthValue
_RsImageMibActivateTransfer_Object = MibScalar
rsImageMibActivateTransfer = _RsImageMibActivateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 7),
    _RsImageMibActivateTransfer_Type()
)
rsImageMibActivateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsImageMibActivateTransfer.setStatus("current")


class _RsImageMibPrimaryCMOperationStatus_Type(Integer32):
    """Custom type rsImageMibPrimaryCMOperationStatus based on Integer32"""
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
        *(("actionComplete", 5),
          ("adding", 2),
          ("choosing", 4),
          ("deleting", 3),
          ("error", 6),
          ("idle", 1))
    )


_RsImageMibPrimaryCMOperationStatus_Type.__name__ = "Integer32"
_RsImageMibPrimaryCMOperationStatus_Object = MibScalar
rsImageMibPrimaryCMOperationStatus = _RsImageMibPrimaryCMOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 8),
    _RsImageMibPrimaryCMOperationStatus_Type()
)
rsImageMibPrimaryCMOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibPrimaryCMOperationStatus.setStatus("current")


class _RsImageMibBackupCMOperationStatus_Type(Integer32):
    """Custom type rsImageMibBackupCMOperationStatus based on Integer32"""
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
        *(("actionComplete", 5),
          ("adding", 2),
          ("choosing", 4),
          ("deleting", 3),
          ("error", 6),
          ("idle", 1))
    )


_RsImageMibBackupCMOperationStatus_Type.__name__ = "Integer32"
_RsImageMibBackupCMOperationStatus_Object = MibScalar
rsImageMibBackupCMOperationStatus = _RsImageMibBackupCMOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 9),
    _RsImageMibBackupCMOperationStatus_Type()
)
rsImageMibBackupCMOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibBackupCMOperationStatus.setStatus("current")
_RsImageMibPrimaryCMLastError_Type = RsImageMibErrorCode
_RsImageMibPrimaryCMLastError_Object = MibScalar
rsImageMibPrimaryCMLastError = _RsImageMibPrimaryCMLastError_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 10),
    _RsImageMibPrimaryCMLastError_Type()
)
rsImageMibPrimaryCMLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibPrimaryCMLastError.setStatus("current")
_RsImageMibBackupCMLastError_Type = RsImageMibErrorCode
_RsImageMibBackupCMLastError_Object = MibScalar
rsImageMibBackupCMLastError = _RsImageMibBackupCMLastError_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 11),
    _RsImageMibBackupCMLastError_Type()
)
rsImageMibBackupCMLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibBackupCMLastError.setStatus("current")


class _RsImageMibPrimaryCMLastErrorString_Type(DisplayString):
    """Custom type rsImageMibPrimaryCMLastErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibPrimaryCMLastErrorString_Type.__name__ = "DisplayString"
_RsImageMibPrimaryCMLastErrorString_Object = MibScalar
rsImageMibPrimaryCMLastErrorString = _RsImageMibPrimaryCMLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 12),
    _RsImageMibPrimaryCMLastErrorString_Type()
)
rsImageMibPrimaryCMLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibPrimaryCMLastErrorString.setStatus("current")


class _RsImageMibBackupCMLastErrorString_Type(DisplayString):
    """Custom type rsImageMibBackupCMLastErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibBackupCMLastErrorString_Type.__name__ = "DisplayString"
_RsImageMibBackupCMLastErrorString_Object = MibScalar
rsImageMibBackupCMLastErrorString = _RsImageMibBackupCMLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 13),
    _RsImageMibBackupCMLastErrorString_Type()
)
rsImageMibBackupCMLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibBackupCMLastErrorString.setStatus("current")
_RsImageMibListTable_Object = MibTable
rsImageMibListTable = _RsImageMibListTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14)
)
if mibBuilder.loadTexts:
    rsImageMibListTable.setStatus("current")
_RsImageMibListEntry_Object = MibTableRow
rsImageMibListEntry = _RsImageMibListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1)
)
rsImageMibListEntry.setIndexNames(
    (0, "RIVERSTONE-IMAGE-MIB", "rsImageMibControlModuleIndex"),
    (0, "RIVERSTONE-IMAGE-MIB", "rsImageMibSlotIndex"),
    (0, "RIVERSTONE-IMAGE-MIB", "rsImageMibImageIndex"),
)
if mibBuilder.loadTexts:
    rsImageMibListEntry.setStatus("current")
_RsImageMibControlModuleIndex_Type = RsImageMibControlModuleIndex
_RsImageMibControlModuleIndex_Object = MibTableColumn
rsImageMibControlModuleIndex = _RsImageMibControlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 1),
    _RsImageMibControlModuleIndex_Type()
)
rsImageMibControlModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsImageMibControlModuleIndex.setStatus("current")
_RsImageMibSlotIndex_Type = RsImageMibSlotIndex
_RsImageMibSlotIndex_Object = MibTableColumn
rsImageMibSlotIndex = _RsImageMibSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 2),
    _RsImageMibSlotIndex_Type()
)
rsImageMibSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsImageMibSlotIndex.setStatus("current")
_RsImageMibImageIndex_Type = RsImageMibImageIndex
_RsImageMibImageIndex_Object = MibTableColumn
rsImageMibImageIndex = _RsImageMibImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 3),
    _RsImageMibImageIndex_Type()
)
rsImageMibImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsImageMibImageIndex.setStatus("current")


class _RsImageMibListImageName_Type(DisplayString):
    """Custom type rsImageMibListImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibListImageName_Type.__name__ = "DisplayString"
_RsImageMibListImageName_Object = MibTableColumn
rsImageMibListImageName = _RsImageMibListImageName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 4),
    _RsImageMibListImageName_Type()
)
rsImageMibListImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibListImageName.setStatus("current")


class _RsImageMibVersion_Type(DisplayString):
    """Custom type rsImageMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsImageMibVersion_Type.__name__ = "DisplayString"
_RsImageMibVersion_Object = MibTableColumn
rsImageMibVersion = _RsImageMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 5),
    _RsImageMibVersion_Type()
)
rsImageMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibVersion.setStatus("current")
_RsImageMibChosen_Type = RsImageMibChosen
_RsImageMibChosen_Object = MibTableColumn
rsImageMibChosen = _RsImageMibChosen_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 6),
    _RsImageMibChosen_Type()
)
rsImageMibChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsImageMibChosen.setStatus("current")
_RsImageMibConformance_ObjectIdentity = ObjectIdentity
rsImageMibConformance = _RsImageMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15)
)
_RsImageMibGroups_ObjectIdentity = ObjectIdentity
rsImageMibGroups = _RsImageMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1)
)
_RsImageMibCompliance_ObjectIdentity = ObjectIdentity
rsImageMibCompliance = _RsImageMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 2)
)

# Managed Objects groups

rsImageMibAddDeleteChooseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 1)
)
rsImageMibAddDeleteChooseGroup.setObjects(
      *(("RIVERSTONE-IMAGE-MIB", "rsImageMibAction"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibTftpServerAddress"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibHostName"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibTftpUrl"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibImageName"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibDestination"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibActivateTransfer"))
)
if mibBuilder.loadTexts:
    rsImageMibAddDeleteChooseGroup.setStatus("current")

rsImageMibListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 2)
)
rsImageMibListGroup.setObjects(
      *(("RIVERSTONE-IMAGE-MIB", "rsImageMibListImageName"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibVersion"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibChosen"))
)
if mibBuilder.loadTexts:
    rsImageMibListGroup.setStatus("current")

rsImageMibStatusAndErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 3)
)
rsImageMibStatusAndErrorGroup.setObjects(
      *(("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMOperationStatus"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMOperationStatus"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMLastError"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMLastError"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMLastErrorString"),
        ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMLastErrorString"))
)
if mibBuilder.loadTexts:
    rsImageMibStatusAndErrorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsImageMibBasicComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 2, 1)
)
if mibBuilder.loadTexts:
    rsImageMibBasicComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-IMAGE-MIB",
    **{"RsImageMibErrorCode": RsImageMibErrorCode,
       "RsImageMibControlModuleIndex": RsImageMibControlModuleIndex,
       "RsImageMibSlotIndex": RsImageMibSlotIndex,
       "RsImageMibImageIndex": RsImageMibImageIndex,
       "RsImageMibChosen": RsImageMibChosen,
       "rsImageMib": rsImageMib,
       "rsImageMibAction": rsImageMibAction,
       "rsImageMibTftpServerAddress": rsImageMibTftpServerAddress,
       "rsImageMibHostName": rsImageMibHostName,
       "rsImageMibTftpUrl": rsImageMibTftpUrl,
       "rsImageMibImageName": rsImageMibImageName,
       "rsImageMibDestination": rsImageMibDestination,
       "rsImageMibActivateTransfer": rsImageMibActivateTransfer,
       "rsImageMibPrimaryCMOperationStatus": rsImageMibPrimaryCMOperationStatus,
       "rsImageMibBackupCMOperationStatus": rsImageMibBackupCMOperationStatus,
       "rsImageMibPrimaryCMLastError": rsImageMibPrimaryCMLastError,
       "rsImageMibBackupCMLastError": rsImageMibBackupCMLastError,
       "rsImageMibPrimaryCMLastErrorString": rsImageMibPrimaryCMLastErrorString,
       "rsImageMibBackupCMLastErrorString": rsImageMibBackupCMLastErrorString,
       "rsImageMibListTable": rsImageMibListTable,
       "rsImageMibListEntry": rsImageMibListEntry,
       "rsImageMibControlModuleIndex": rsImageMibControlModuleIndex,
       "rsImageMibSlotIndex": rsImageMibSlotIndex,
       "rsImageMibImageIndex": rsImageMibImageIndex,
       "rsImageMibListImageName": rsImageMibListImageName,
       "rsImageMibVersion": rsImageMibVersion,
       "rsImageMibChosen": rsImageMibChosen,
       "rsImageMibConformance": rsImageMibConformance,
       "rsImageMibGroups": rsImageMibGroups,
       "rsImageMibAddDeleteChooseGroup": rsImageMibAddDeleteChooseGroup,
       "rsImageMibListGroup": rsImageMibListGroup,
       "rsImageMibStatusAndErrorGroup": rsImageMibStatusAndErrorGroup,
       "rsImageMibCompliance": rsImageMibCompliance,
       "rsImageMibBasicComplianceV1": rsImageMibBasicComplianceV1}
)
