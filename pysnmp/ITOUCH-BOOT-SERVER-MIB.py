# SNMP MIB module (ITOUCH-BOOT-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-BOOT-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:05 2024
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

(AddressType,
 DateTime,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "AddressType",
    "DateTime",
    "iTouch")

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



class DialogStatus(Integer32):
    """Custom type DialogStatus based on Integer32"""
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
        *(("badFileData", 5),
          ("deviceWriteProtected", 6),
          ("fileSystemError", 11),
          ("fileTooLarge", 2),
          ("none", 1),
          ("notExecutableFile", 4),
          ("notImageFile", 3),
          ("operationTimeout", 7),
          ("protocolError", 10),
          ("remoteFileAccessViolation", 9),
          ("remoteFileNotFound", 8),
          ("success", 13),
          ("temporaryResourceConflict", 12))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XBootServer_ObjectIdentity = ObjectIdentity
xBootServer = _XBootServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6)
)
_XBsBasic_ObjectIdentity = ObjectIdentity
xBsBasic = _XBsBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 1)
)


class _BasicLogLimit_Type(Integer32):
    """Custom type basicLogLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BasicLogLimit_Type.__name__ = "Integer32"
_BasicLogLimit_Object = MibScalar
basicLogLimit = _BasicLogLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 1),
    _BasicLogLimit_Type()
)
basicLogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLogLimit.setStatus("mandatory")


class _BasicActiveLimit_Type(Integer32):
    """Custom type basicActiveLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_BasicActiveLimit_Type.__name__ = "Integer32"
_BasicActiveLimit_Object = MibScalar
basicActiveLimit = _BasicActiveLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 2),
    _BasicActiveLimit_Type()
)
basicActiveLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicActiveLimit.setStatus("mandatory")
_BasicActiveNumber_Type = Gauge32
_BasicActiveNumber_Object = MibScalar
basicActiveNumber = _BasicActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 3),
    _BasicActiveNumber_Type()
)
basicActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveNumber.setStatus("mandatory")
_BasicClientNumber_Type = Gauge32
_BasicClientNumber_Object = MibScalar
basicClientNumber = _BasicClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 4),
    _BasicClientNumber_Type()
)
basicClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicClientNumber.setStatus("mandatory")
_BasicOffersSent_Type = Counter32
_BasicOffersSent_Object = MibScalar
basicOffersSent = _BasicOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 5),
    _BasicOffersSent_Type()
)
basicOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicOffersSent.setStatus("mandatory")
_BasicEventTotal_Type = Gauge32
_BasicEventTotal_Object = MibScalar
basicEventTotal = _BasicEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 6),
    _BasicEventTotal_Type()
)
basicEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicEventTotal.setStatus("mandatory")


class _BasicEventPurge_Type(Integer32):
    """Custom type basicEventPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicEventPurge_Type.__name__ = "Integer32"
_BasicEventPurge_Object = MibScalar
basicEventPurge = _BasicEventPurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 7),
    _BasicEventPurge_Type()
)
basicEventPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicEventPurge.setStatus("mandatory")
_ActiveTable_Object = MibTable
activeTable = _ActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8)
)
if mibBuilder.loadTexts:
    activeTable.setStatus("mandatory")
_ActiveEntry_Object = MibTableRow
activeEntry = _ActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1)
)
activeEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "activeIdentificationType"),
    (0, "ITOUCH-BOOT-SERVER-MIB", "activeIdentification"),
)
if mibBuilder.loadTexts:
    activeEntry.setStatus("mandatory")
_ActiveIdentificationType_Type = AddressType
_ActiveIdentificationType_Object = MibTableColumn
activeIdentificationType = _ActiveIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 1),
    _ActiveIdentificationType_Type()
)
activeIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeIdentificationType.setStatus("mandatory")


class _ActiveIdentification_Type(OctetString):
    """Custom type activeIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ActiveIdentification_Type.__name__ = "OctetString"
_ActiveIdentification_Object = MibTableColumn
activeIdentification = _ActiveIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 2),
    _ActiveIdentification_Type()
)
activeIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeIdentification.setStatus("mandatory")


class _ActiveFunction_Type(Integer32):
    """Custom type activeFunction based on Integer32"""
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
        *(("dump", 3),
          ("imageUpdate", 4),
          ("load", 2),
          ("parameterStore", 1))
    )


_ActiveFunction_Type.__name__ = "Integer32"
_ActiveFunction_Object = MibTableColumn
activeFunction = _ActiveFunction_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 3),
    _ActiveFunction_Type()
)
activeFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFunction.setStatus("mandatory")


class _ActiveSoftwareVersionType_Type(Integer32):
    """Custom type activeSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("diagnostic", 5),
          ("notApplicable", 6),
          ("production", 3),
          ("special", 4))
    )


_ActiveSoftwareVersionType_Type.__name__ = "Integer32"
_ActiveSoftwareVersionType_Object = MibTableColumn
activeSoftwareVersionType = _ActiveSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 4),
    _ActiveSoftwareVersionType_Type()
)
activeSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeSoftwareVersionType.setStatus("mandatory")


class _ActiveSoftwareVersion_Type(OctetString):
    """Custom type activeSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ActiveSoftwareVersion_Type.__name__ = "OctetString"
_ActiveSoftwareVersion_Object = MibTableColumn
activeSoftwareVersion = _ActiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 5),
    _ActiveSoftwareVersion_Type()
)
activeSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeSoftwareVersion.setStatus("mandatory")
_ActiveParameterVersion_Type = Integer32
_ActiveParameterVersion_Object = MibTableColumn
activeParameterVersion = _ActiveParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 6),
    _ActiveParameterVersion_Type()
)
activeParameterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeParameterVersion.setStatus("mandatory")
_ActiveCurrentSequence_Type = Integer32
_ActiveCurrentSequence_Object = MibTableColumn
activeCurrentSequence = _ActiveCurrentSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 7),
    _ActiveCurrentSequence_Type()
)
activeCurrentSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCurrentSequence.setStatus("mandatory")
_ActiveBytesRemaining_Type = Integer32
_ActiveBytesRemaining_Object = MibTableColumn
activeBytesRemaining = _ActiveBytesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 8),
    _ActiveBytesRemaining_Type()
)
activeBytesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeBytesRemaining.setStatus("mandatory")


class _ActiveFile_Type(DisplayString):
    """Custom type activeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ActiveFile_Type.__name__ = "DisplayString"
_ActiveFile_Object = MibTableColumn
activeFile = _ActiveFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 9),
    _ActiveFile_Type()
)
activeFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFile.setStatus("mandatory")
_ActiveStatus_Type = DialogStatus
_ActiveStatus_Object = MibTableColumn
activeStatus = _ActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 10),
    _ActiveStatus_Type()
)
activeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeStatus.setStatus("mandatory")


class _ActiveState_Type(Integer32):
    """Custom type activeState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cleanup", 10),
          ("closeFile", 9),
          ("closePartner", 8),
          ("done", 11),
          ("error", 12),
          ("idle", 1),
          ("internal1", 2),
          ("internal2", 3),
          ("openFile", 5),
          ("openPartner", 4),
          ("receivePartner", 6),
          ("writeFile", 7))
    )


_ActiveState_Type.__name__ = "Integer32"
_ActiveState_Object = MibTableColumn
activeState = _ActiveState_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 11),
    _ActiveState_Type()
)
activeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeState.setStatus("mandatory")
_ClientTable_Object = MibTable
clientTable = _ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9)
)
if mibBuilder.loadTexts:
    clientTable.setStatus("mandatory")
_ClientEntry_Object = MibTableRow
clientEntry = _ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1)
)
clientEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "clientIdentificationType"),
    (0, "ITOUCH-BOOT-SERVER-MIB", "clientIdentification"),
)
if mibBuilder.loadTexts:
    clientEntry.setStatus("mandatory")
_ClientIdentificationType_Type = AddressType
_ClientIdentificationType_Object = MibTableColumn
clientIdentificationType = _ClientIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 1),
    _ClientIdentificationType_Type()
)
clientIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIdentificationType.setStatus("mandatory")


class _ClientIdentification_Type(OctetString):
    """Custom type clientIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ClientIdentification_Type.__name__ = "OctetString"
_ClientIdentification_Object = MibTableColumn
clientIdentification = _ClientIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 2),
    _ClientIdentification_Type()
)
clientIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIdentification.setStatus("mandatory")


class _ClientEntryStatus_Type(Integer32):
    """Custom type clientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ClientEntryStatus_Type.__name__ = "Integer32"
_ClientEntryStatus_Object = MibTableColumn
clientEntryStatus = _ClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 3),
    _ClientEntryStatus_Type()
)
clientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientEntryStatus.setStatus("mandatory")


class _ClientName_Type(DisplayString):
    """Custom type clientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientName_Type.__name__ = "DisplayString"
_ClientName_Object = MibTableColumn
clientName = _ClientName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 4),
    _ClientName_Type()
)
clientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientName.setStatus("mandatory")


class _ClientLoadFile_Type(DisplayString):
    """Custom type clientLoadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientLoadFile_Type.__name__ = "DisplayString"
_ClientLoadFile_Object = MibTableColumn
clientLoadFile = _ClientLoadFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 5),
    _ClientLoadFile_Type()
)
clientLoadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLoadFile.setStatus("mandatory")


class _ClientDiagnosticFile_Type(DisplayString):
    """Custom type clientDiagnosticFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientDiagnosticFile_Type.__name__ = "DisplayString"
_ClientDiagnosticFile_Object = MibTableColumn
clientDiagnosticFile = _ClientDiagnosticFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 6),
    _ClientDiagnosticFile_Type()
)
clientDiagnosticFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDiagnosticFile.setStatus("mandatory")


class _ClientLoadService_Type(Integer32):
    """Custom type clientLoadService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientLoadService_Type.__name__ = "Integer32"
_ClientLoadService_Object = MibTableColumn
clientLoadService = _ClientLoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 7),
    _ClientLoadService_Type()
)
clientLoadService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLoadService.setStatus("mandatory")


class _ClientDumpService_Type(Integer32):
    """Custom type clientDumpService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientDumpService_Type.__name__ = "Integer32"
_ClientDumpService_Object = MibTableColumn
clientDumpService = _ClientDumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 8),
    _ClientDumpService_Type()
)
clientDumpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDumpService.setStatus("mandatory")
_NamedTable_Object = MibTable
namedTable = _NamedTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10)
)
if mibBuilder.loadTexts:
    namedTable.setStatus("mandatory")
_NamedEntry_Object = MibTableRow
namedEntry = _NamedEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1)
)
namedEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "namedName"),
)
if mibBuilder.loadTexts:
    namedEntry.setStatus("mandatory")
_NamedIdentificationType_Type = AddressType
_NamedIdentificationType_Object = MibTableColumn
namedIdentificationType = _NamedIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 1),
    _NamedIdentificationType_Type()
)
namedIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedIdentificationType.setStatus("mandatory")


class _NamedIdentification_Type(OctetString):
    """Custom type namedIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_NamedIdentification_Type.__name__ = "OctetString"
_NamedIdentification_Object = MibTableColumn
namedIdentification = _NamedIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 2),
    _NamedIdentification_Type()
)
namedIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedIdentification.setStatus("mandatory")


class _NamedEntryStatus_Type(Integer32):
    """Custom type namedEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NamedEntryStatus_Type.__name__ = "Integer32"
_NamedEntryStatus_Object = MibTableColumn
namedEntryStatus = _NamedEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 3),
    _NamedEntryStatus_Type()
)
namedEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedEntryStatus.setStatus("mandatory")


class _NamedName_Type(DisplayString):
    """Custom type namedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedName_Type.__name__ = "DisplayString"
_NamedName_Object = MibTableColumn
namedName = _NamedName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 4),
    _NamedName_Type()
)
namedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedName.setStatus("mandatory")


class _NamedLoadFile_Type(DisplayString):
    """Custom type namedLoadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedLoadFile_Type.__name__ = "DisplayString"
_NamedLoadFile_Object = MibTableColumn
namedLoadFile = _NamedLoadFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 5),
    _NamedLoadFile_Type()
)
namedLoadFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedLoadFile.setStatus("mandatory")


class _NamedDiagnosticFile_Type(DisplayString):
    """Custom type namedDiagnosticFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedDiagnosticFile_Type.__name__ = "DisplayString"
_NamedDiagnosticFile_Object = MibTableColumn
namedDiagnosticFile = _NamedDiagnosticFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 6),
    _NamedDiagnosticFile_Type()
)
namedDiagnosticFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedDiagnosticFile.setStatus("mandatory")


class _NamedLoadService_Type(Integer32):
    """Custom type namedLoadService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NamedLoadService_Type.__name__ = "Integer32"
_NamedLoadService_Object = MibTableColumn
namedLoadService = _NamedLoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 7),
    _NamedLoadService_Type()
)
namedLoadService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedLoadService.setStatus("mandatory")


class _NamedDumpService_Type(Integer32):
    """Custom type namedDumpService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NamedDumpService_Type.__name__ = "Integer32"
_NamedDumpService_Object = MibTableColumn
namedDumpService = _NamedDumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 8),
    _NamedDumpService_Type()
)
namedDumpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namedDumpService.setStatus("mandatory")
_XEventTable_Object = MibTable
xEventTable = _XEventTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11)
)
if mibBuilder.loadTexts:
    xEventTable.setStatus("mandatory")
_XEventEntry_Object = MibTableRow
xEventEntry = _XEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1)
)
xEventEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "xEventIndex"),
)
if mibBuilder.loadTexts:
    xEventEntry.setStatus("mandatory")
_XEventIndex_Type = Integer32
_XEventIndex_Object = MibTableColumn
xEventIndex = _XEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1, 1),
    _XEventIndex_Type()
)
xEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xEventIndex.setStatus("mandatory")


class _XEventText_Type(DisplayString):
    """Custom type xEventText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_XEventText_Type.__name__ = "DisplayString"
_XEventText_Object = MibTableColumn
xEventText = _XEventText_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1, 2),
    _XEventText_Type()
)
xEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xEventText.setStatus("mandatory")
_BasicDeviceNumber_Type = Integer32
_BasicDeviceNumber_Object = MibScalar
basicDeviceNumber = _BasicDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 12),
    _BasicDeviceNumber_Type()
)
basicDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDeviceNumber.setStatus("mandatory")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1)
)
deviceEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")
_DeviceIndex_Type = Integer32
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("mandatory")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")


class _DeviceDescr_Type(DisplayString):
    """Custom type deviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DeviceDescr_Type.__name__ = "DisplayString"
_DeviceDescr_Object = MibTableColumn
deviceDescr = _DeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 3),
    _DeviceDescr_Type()
)
deviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDescr.setStatus("mandatory")


class _DeviceOperation_Type(Integer32):
    """Custom type deviceOperation based on Integer32"""
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
        *(("erase", 5),
          ("format", 3),
          ("idle", 4),
          ("loadingClient", 8),
          ("paramStore", 6),
          ("read", 1),
          ("unpack", 7),
          ("write", 2))
    )


_DeviceOperation_Type.__name__ = "Integer32"
_DeviceOperation_Object = MibTableColumn
deviceOperation = _DeviceOperation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 4),
    _DeviceOperation_Type()
)
deviceOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOperation.setStatus("mandatory")


class _DeviceFormat_Type(Integer32):
    """Custom type deviceFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("formatted", 2),
          ("unformatted", 1),
          ("unknown", 3))
    )


_DeviceFormat_Type.__name__ = "Integer32"
_DeviceFormat_Object = MibTableColumn
deviceFormat = _DeviceFormat_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 5),
    _DeviceFormat_Type()
)
deviceFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFormat.setStatus("mandatory")


class _DeviceProtection_Type(Integer32):
    """Custom type deviceProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 3),
          ("write-enabled", 1),
          ("write-protected", 2))
    )


_DeviceProtection_Type.__name__ = "Integer32"
_DeviceProtection_Object = MibTableColumn
deviceProtection = _DeviceProtection_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 6),
    _DeviceProtection_Type()
)
deviceProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceProtection.setStatus("mandatory")


class _DeviceFormatMedium_Type(Integer32):
    """Custom type deviceFormatMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_DeviceFormatMedium_Type.__name__ = "Integer32"
_DeviceFormatMedium_Object = MibTableColumn
deviceFormatMedium = _DeviceFormatMedium_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 7),
    _DeviceFormatMedium_Type()
)
deviceFormatMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFormatMedium.setStatus("mandatory")


class _DeviceGetFile_Type(Integer32):
    """Custom type deviceGetFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("execute", 2),
          ("ready", 1))
    )


_DeviceGetFile_Type.__name__ = "Integer32"
_DeviceGetFile_Object = MibTableColumn
deviceGetFile = _DeviceGetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 8),
    _DeviceGetFile_Type()
)
deviceGetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFile.setStatus("mandatory")
_DeviceGetFileHostIdentificationType_Type = AddressType
_DeviceGetFileHostIdentificationType_Object = MibTableColumn
deviceGetFileHostIdentificationType = _DeviceGetFileHostIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 9),
    _DeviceGetFileHostIdentificationType_Type()
)
deviceGetFileHostIdentificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileHostIdentificationType.setStatus("mandatory")


class _DeviceGetFileHostIdentification_Type(OctetString):
    """Custom type deviceGetFileHostIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_DeviceGetFileHostIdentification_Type.__name__ = "OctetString"
_DeviceGetFileHostIdentification_Object = MibTableColumn
deviceGetFileHostIdentification = _DeviceGetFileHostIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 10),
    _DeviceGetFileHostIdentification_Type()
)
deviceGetFileHostIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileHostIdentification.setStatus("mandatory")


class _DeviceGetFileName_Type(DisplayString):
    """Custom type deviceGetFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DeviceGetFileName_Type.__name__ = "DisplayString"
_DeviceGetFileName_Object = MibTableColumn
deviceGetFileName = _DeviceGetFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 11),
    _DeviceGetFileName_Type()
)
deviceGetFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileName.setStatus("mandatory")


class _DeviceGetFileArea_Type(Integer32):
    """Custom type deviceGetFileArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DeviceGetFileArea_Type.__name__ = "Integer32"
_DeviceGetFileArea_Object = MibTableColumn
deviceGetFileArea = _DeviceGetFileArea_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 12),
    _DeviceGetFileArea_Type()
)
deviceGetFileArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileArea.setStatus("mandatory")


class _DeviceFormatOption_Type(Integer32):
    """Custom type deviceFormatOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DeviceFormatOption_Type.__name__ = "Integer32"
_DeviceFormatOption_Object = MibTableColumn
deviceFormatOption = _DeviceFormatOption_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 13),
    _DeviceFormatOption_Type()
)
deviceFormatOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFormatOption.setStatus("mandatory")


class _DeviceFormatRedundantParams_Type(Integer32):
    """Custom type deviceFormatRedundantParams based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonredundant", 1),
          ("redundant", 2))
    )


_DeviceFormatRedundantParams_Type.__name__ = "Integer32"
_DeviceFormatRedundantParams_Object = MibTableColumn
deviceFormatRedundantParams = _DeviceFormatRedundantParams_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 14),
    _DeviceFormatRedundantParams_Type()
)
deviceFormatRedundantParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFormatRedundantParams.setStatus("mandatory")
_DevicePreviousStatus_Type = DialogStatus
_DevicePreviousStatus_Object = MibTableColumn
devicePreviousStatus = _DevicePreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 15),
    _DevicePreviousStatus_Type()
)
devicePreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePreviousStatus.setStatus("mandatory")
_XDump_ObjectIdentity = ObjectIdentity
xDump = _XDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 2)
)


class _DumpService_Type(Integer32):
    """Custom type dumpService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DumpService_Type.__name__ = "Integer32"
_DumpService_Object = MibScalar
dumpService = _DumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 1),
    _DumpService_Type()
)
dumpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpService.setStatus("mandatory")


class _DumpDrive_Type(Integer32):
    """Custom type dumpDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DumpDrive_Type.__name__ = "Integer32"
_DumpDrive_Object = MibScalar
dumpDrive = _DumpDrive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 2),
    _DumpDrive_Type()
)
dumpDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpDrive.setStatus("mandatory")


class _DumpMerit_Type(Integer32):
    """Custom type dumpMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DumpMerit_Type.__name__ = "Integer32"
_DumpMerit_Object = MibScalar
dumpMerit = _DumpMerit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 3),
    _DumpMerit_Type()
)
dumpMerit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpMerit.setStatus("mandatory")


class _DumpSize_Type(Integer32):
    """Custom type dumpSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("small", 1))
    )


_DumpSize_Type.__name__ = "Integer32"
_DumpSize_Object = MibScalar
dumpSize = _DumpSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 4),
    _DumpSize_Type()
)
dumpSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpSize.setStatus("mandatory")
_DumpCompleted_Type = Counter32
_DumpCompleted_Object = MibScalar
dumpCompleted = _DumpCompleted_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 5),
    _DumpCompleted_Type()
)
dumpCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpCompleted.setStatus("mandatory")
_DumpActive_Type = Gauge32
_DumpActive_Object = MibScalar
dumpActive = _DumpActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 6),
    _DumpActive_Type()
)
dumpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpActive.setStatus("mandatory")
_DumpFileNumber_Type = Gauge32
_DumpFileNumber_Object = MibScalar
dumpFileNumber = _DumpFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 7),
    _DumpFileNumber_Type()
)
dumpFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileNumber.setStatus("mandatory")
_DumpFileTable_Object = MibTable
dumpFileTable = _DumpFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8)
)
if mibBuilder.loadTexts:
    dumpFileTable.setStatus("mandatory")
_DumpFileEntry_Object = MibTableRow
dumpFileEntry = _DumpFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1)
)
dumpFileEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "dumpFileIdentificationType"),
    (0, "ITOUCH-BOOT-SERVER-MIB", "dumpFileIdentification"),
)
if mibBuilder.loadTexts:
    dumpFileEntry.setStatus("mandatory")
_DumpFileIdentificationType_Type = AddressType
_DumpFileIdentificationType_Object = MibTableColumn
dumpFileIdentificationType = _DumpFileIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 1),
    _DumpFileIdentificationType_Type()
)
dumpFileIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileIdentificationType.setStatus("mandatory")


class _DumpFileIdentification_Type(OctetString):
    """Custom type dumpFileIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_DumpFileIdentification_Type.__name__ = "OctetString"
_DumpFileIdentification_Object = MibTableColumn
dumpFileIdentification = _DumpFileIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 2),
    _DumpFileIdentification_Type()
)
dumpFileIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileIdentification.setStatus("mandatory")


class _DumpFileEntryStatus_Type(Integer32):
    """Custom type dumpFileEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_DumpFileEntryStatus_Type.__name__ = "Integer32"
_DumpFileEntryStatus_Object = MibTableColumn
dumpFileEntryStatus = _DumpFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 3),
    _DumpFileEntryStatus_Type()
)
dumpFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpFileEntryStatus.setStatus("mandatory")
_DumpFileCreation_Type = DateTime
_DumpFileCreation_Object = MibTableColumn
dumpFileCreation = _DumpFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 4),
    _DumpFileCreation_Type()
)
dumpFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileCreation.setStatus("mandatory")
_DumpFileSize_Type = Integer32
_DumpFileSize_Object = MibTableColumn
dumpFileSize = _DumpFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 5),
    _DumpFileSize_Type()
)
dumpFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileSize.setStatus("mandatory")
_XLoad_ObjectIdentity = ObjectIdentity
xLoad = _XLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 3)
)


class _LoadService_Type(Integer32):
    """Custom type loadService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LoadService_Type.__name__ = "Integer32"
_LoadService_Object = MibScalar
loadService = _LoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 1),
    _LoadService_Type()
)
loadService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadService.setStatus("mandatory")


class _LoadMerit_Type(Integer32):
    """Custom type loadMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LoadMerit_Type.__name__ = "Integer32"
_LoadMerit_Object = MibScalar
loadMerit = _LoadMerit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 2),
    _LoadMerit_Type()
)
loadMerit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMerit.setStatus("mandatory")
_LoadCompleted_Type = Counter32
_LoadCompleted_Object = MibScalar
loadCompleted = _LoadCompleted_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 3),
    _LoadCompleted_Type()
)
loadCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCompleted.setStatus("mandatory")
_LoadActive_Type = Gauge32
_LoadActive_Object = MibScalar
loadActive = _LoadActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 4),
    _LoadActive_Type()
)
loadActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadActive.setStatus("mandatory")
_LoadFileNumber_Type = Gauge32
_LoadFileNumber_Object = MibScalar
loadFileNumber = _LoadFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 5),
    _LoadFileNumber_Type()
)
loadFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileNumber.setStatus("mandatory")
_LoadFileTable_Object = MibTable
loadFileTable = _LoadFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6)
)
if mibBuilder.loadTexts:
    loadFileTable.setStatus("mandatory")
_LoadFileEntry_Object = MibTableRow
loadFileEntry = _LoadFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1)
)
loadFileEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "loadFileName"),
)
if mibBuilder.loadTexts:
    loadFileEntry.setStatus("mandatory")


class _LoadFileName_Type(DisplayString):
    """Custom type loadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LoadFileName_Type.__name__ = "DisplayString"
_LoadFileName_Object = MibTableColumn
loadFileName = _LoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 1),
    _LoadFileName_Type()
)
loadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileName.setStatus("mandatory")
_LoadFileCreation_Type = DateTime
_LoadFileCreation_Object = MibTableColumn
loadFileCreation = _LoadFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 2),
    _LoadFileCreation_Type()
)
loadFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileCreation.setStatus("mandatory")
_LoadFileSize_Type = Integer32
_LoadFileSize_Object = MibTableColumn
loadFileSize = _LoadFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 3),
    _LoadFileSize_Type()
)
loadFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSize.setStatus("mandatory")


class _LoadFileSoftwareVersionType_Type(Integer32):
    """Custom type loadFileSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("production", 3),
          ("special", 4))
    )


_LoadFileSoftwareVersionType_Type.__name__ = "Integer32"
_LoadFileSoftwareVersionType_Object = MibTableColumn
loadFileSoftwareVersionType = _LoadFileSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 4),
    _LoadFileSoftwareVersionType_Type()
)
loadFileSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSoftwareVersionType.setStatus("mandatory")


class _LoadFileSoftwareVersion_Type(OctetString):
    """Custom type loadFileSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LoadFileSoftwareVersion_Type.__name__ = "OctetString"
_LoadFileSoftwareVersion_Object = MibTableColumn
loadFileSoftwareVersion = _LoadFileSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 5),
    _LoadFileSoftwareVersion_Type()
)
loadFileSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSoftwareVersion.setStatus("mandatory")
_XParam_ObjectIdentity = ObjectIdentity
xParam = _XParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 4)
)


class _ParamService_Type(Integer32):
    """Custom type paramService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamService_Type.__name__ = "Integer32"
_ParamService_Object = MibScalar
paramService = _ParamService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 1),
    _ParamService_Type()
)
paramService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramService.setStatus("mandatory")


class _ParamDefaultService_Type(Integer32):
    """Custom type paramDefaultService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamDefaultService_Type.__name__ = "Integer32"
_ParamDefaultService_Object = MibScalar
paramDefaultService = _ParamDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 2),
    _ParamDefaultService_Type()
)
paramDefaultService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDefaultService.setStatus("mandatory")


class _ParamDrive_Type(Integer32):
    """Custom type paramDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ParamDrive_Type.__name__ = "Integer32"
_ParamDrive_Object = MibScalar
paramDrive = _ParamDrive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 3),
    _ParamDrive_Type()
)
paramDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDrive.setStatus("mandatory")
_ParamActive_Type = Gauge32
_ParamActive_Object = MibScalar
paramActive = _ParamActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 4),
    _ParamActive_Type()
)
paramActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramActive.setStatus("mandatory")
_ParamStorageActive_Type = Gauge32
_ParamStorageActive_Object = MibScalar
paramStorageActive = _ParamStorageActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 5),
    _ParamStorageActive_Type()
)
paramStorageActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramStorageActive.setStatus("mandatory")
_ParamFileNumber_Type = Gauge32
_ParamFileNumber_Object = MibScalar
paramFileNumber = _ParamFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 6),
    _ParamFileNumber_Type()
)
paramFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileNumber.setStatus("mandatory")
_ParamFileTable_Object = MibTable
paramFileTable = _ParamFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7)
)
if mibBuilder.loadTexts:
    paramFileTable.setStatus("mandatory")
_ParamFileEntry_Object = MibTableRow
paramFileEntry = _ParamFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1)
)
paramFileEntry.setIndexNames(
    (0, "ITOUCH-BOOT-SERVER-MIB", "paramFileIdentificationType"),
    (0, "ITOUCH-BOOT-SERVER-MIB", "paramFileIdentification"),
)
if mibBuilder.loadTexts:
    paramFileEntry.setStatus("mandatory")
_ParamFileIdentificationType_Type = AddressType
_ParamFileIdentificationType_Object = MibTableColumn
paramFileIdentificationType = _ParamFileIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 1),
    _ParamFileIdentificationType_Type()
)
paramFileIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileIdentificationType.setStatus("mandatory")


class _ParamFileIdentification_Type(OctetString):
    """Custom type paramFileIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ParamFileIdentification_Type.__name__ = "OctetString"
_ParamFileIdentification_Object = MibTableColumn
paramFileIdentification = _ParamFileIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 2),
    _ParamFileIdentification_Type()
)
paramFileIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileIdentification.setStatus("mandatory")


class _ParamFileEntryStatus_Type(Integer32):
    """Custom type paramFileEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ParamFileEntryStatus_Type.__name__ = "Integer32"
_ParamFileEntryStatus_Object = MibTableColumn
paramFileEntryStatus = _ParamFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 3),
    _ParamFileEntryStatus_Type()
)
paramFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramFileEntryStatus.setStatus("mandatory")
_ParamFileWrite_Type = DateTime
_ParamFileWrite_Object = MibTableColumn
paramFileWrite = _ParamFileWrite_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 4),
    _ParamFileWrite_Type()
)
paramFileWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileWrite.setStatus("mandatory")
_ParamFileSize_Type = Integer32
_ParamFileSize_Object = MibTableColumn
paramFileSize = _ParamFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 5),
    _ParamFileSize_Type()
)
paramFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileSize.setStatus("mandatory")
_ParamFileParameterVersion_Type = Integer32
_ParamFileParameterVersion_Object = MibTableColumn
paramFileParameterVersion = _ParamFileParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 6),
    _ParamFileParameterVersion_Type()
)
paramFileParameterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileParameterVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-BOOT-SERVER-MIB",
    **{"DialogStatus": DialogStatus,
       "xBootServer": xBootServer,
       "xBsBasic": xBsBasic,
       "basicLogLimit": basicLogLimit,
       "basicActiveLimit": basicActiveLimit,
       "basicActiveNumber": basicActiveNumber,
       "basicClientNumber": basicClientNumber,
       "basicOffersSent": basicOffersSent,
       "basicEventTotal": basicEventTotal,
       "basicEventPurge": basicEventPurge,
       "activeTable": activeTable,
       "activeEntry": activeEntry,
       "activeIdentificationType": activeIdentificationType,
       "activeIdentification": activeIdentification,
       "activeFunction": activeFunction,
       "activeSoftwareVersionType": activeSoftwareVersionType,
       "activeSoftwareVersion": activeSoftwareVersion,
       "activeParameterVersion": activeParameterVersion,
       "activeCurrentSequence": activeCurrentSequence,
       "activeBytesRemaining": activeBytesRemaining,
       "activeFile": activeFile,
       "activeStatus": activeStatus,
       "activeState": activeState,
       "clientTable": clientTable,
       "clientEntry": clientEntry,
       "clientIdentificationType": clientIdentificationType,
       "clientIdentification": clientIdentification,
       "clientEntryStatus": clientEntryStatus,
       "clientName": clientName,
       "clientLoadFile": clientLoadFile,
       "clientDiagnosticFile": clientDiagnosticFile,
       "clientLoadService": clientLoadService,
       "clientDumpService": clientDumpService,
       "namedTable": namedTable,
       "namedEntry": namedEntry,
       "namedIdentificationType": namedIdentificationType,
       "namedIdentification": namedIdentification,
       "namedEntryStatus": namedEntryStatus,
       "namedName": namedName,
       "namedLoadFile": namedLoadFile,
       "namedDiagnosticFile": namedDiagnosticFile,
       "namedLoadService": namedLoadService,
       "namedDumpService": namedDumpService,
       "xEventTable": xEventTable,
       "xEventEntry": xEventEntry,
       "xEventIndex": xEventIndex,
       "xEventText": xEventText,
       "basicDeviceNumber": basicDeviceNumber,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "deviceName": deviceName,
       "deviceDescr": deviceDescr,
       "deviceOperation": deviceOperation,
       "deviceFormat": deviceFormat,
       "deviceProtection": deviceProtection,
       "deviceFormatMedium": deviceFormatMedium,
       "deviceGetFile": deviceGetFile,
       "deviceGetFileHostIdentificationType": deviceGetFileHostIdentificationType,
       "deviceGetFileHostIdentification": deviceGetFileHostIdentification,
       "deviceGetFileName": deviceGetFileName,
       "deviceGetFileArea": deviceGetFileArea,
       "deviceFormatOption": deviceFormatOption,
       "deviceFormatRedundantParams": deviceFormatRedundantParams,
       "devicePreviousStatus": devicePreviousStatus,
       "xDump": xDump,
       "dumpService": dumpService,
       "dumpDrive": dumpDrive,
       "dumpMerit": dumpMerit,
       "dumpSize": dumpSize,
       "dumpCompleted": dumpCompleted,
       "dumpActive": dumpActive,
       "dumpFileNumber": dumpFileNumber,
       "dumpFileTable": dumpFileTable,
       "dumpFileEntry": dumpFileEntry,
       "dumpFileIdentificationType": dumpFileIdentificationType,
       "dumpFileIdentification": dumpFileIdentification,
       "dumpFileEntryStatus": dumpFileEntryStatus,
       "dumpFileCreation": dumpFileCreation,
       "dumpFileSize": dumpFileSize,
       "xLoad": xLoad,
       "loadService": loadService,
       "loadMerit": loadMerit,
       "loadCompleted": loadCompleted,
       "loadActive": loadActive,
       "loadFileNumber": loadFileNumber,
       "loadFileTable": loadFileTable,
       "loadFileEntry": loadFileEntry,
       "loadFileName": loadFileName,
       "loadFileCreation": loadFileCreation,
       "loadFileSize": loadFileSize,
       "loadFileSoftwareVersionType": loadFileSoftwareVersionType,
       "loadFileSoftwareVersion": loadFileSoftwareVersion,
       "xParam": xParam,
       "paramService": paramService,
       "paramDefaultService": paramDefaultService,
       "paramDrive": paramDrive,
       "paramActive": paramActive,
       "paramStorageActive": paramStorageActive,
       "paramFileNumber": paramFileNumber,
       "paramFileTable": paramFileTable,
       "paramFileEntry": paramFileEntry,
       "paramFileIdentificationType": paramFileIdentificationType,
       "paramFileIdentification": paramFileIdentification,
       "paramFileEntryStatus": paramFileEntryStatus,
       "paramFileWrite": paramFileWrite,
       "paramFileSize": paramFileSize,
       "paramFileParameterVersion": paramFileParameterVersion}
)
