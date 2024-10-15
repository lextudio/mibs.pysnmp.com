# SNMP MIB module (ACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:38 2024
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

(giproducts,) = mibBuilder.importSymbols(
    "BCS-IDENT-MIB",
    "giproducts")

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

acpStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11)
)
acpStatus.setRevisions(
        ("2003-06-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcpNumberofEncryptTypes_Type = Integer32
_AcpNumberofEncryptTypes_Object = MibScalar
acpNumberofEncryptTypes = _AcpNumberofEncryptTypes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 1),
    _AcpNumberofEncryptTypes_Type()
)
acpNumberofEncryptTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpNumberofEncryptTypes.setStatus("current")
_AcpNumberofDecryptTypes_Type = Integer32
_AcpNumberofDecryptTypes_Object = MibScalar
acpNumberofDecryptTypes = _AcpNumberofDecryptTypes_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 2),
    _AcpNumberofDecryptTypes_Type()
)
acpNumberofDecryptTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpNumberofDecryptTypes.setStatus("current")
_AcpStatusTable_Object = MibTable
acpStatusTable = _AcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3)
)
if mibBuilder.loadTexts:
    acpStatusTable.setStatus("current")
_AcpStatusEntry_Object = MibTableRow
acpStatusEntry = _AcpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1)
)
acpStatusEntry.setIndexNames(
    (0, "ACP-MIB", "acpEncryptType"),
    (0, "ACP-MIB", "acpUnitIndex"),
    (0, "ACP-MIB", "acpServiceIndex"),
)
if mibBuilder.loadTexts:
    acpStatusEntry.setStatus("current")


class _AcpEncryptType_Type(Integer32):
    """Custom type acpEncryptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decryptAcp", 2),
          ("encryptAcp", 1))
    )


_AcpEncryptType_Type.__name__ = "Integer32"
_AcpEncryptType_Object = MibTableColumn
acpEncryptType = _AcpEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 1),
    _AcpEncryptType_Type()
)
acpEncryptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpEncryptType.setStatus("current")
_AcpUnitIndex_Type = Integer32
_AcpUnitIndex_Object = MibTableColumn
acpUnitIndex = _AcpUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 2),
    _AcpUnitIndex_Type()
)
acpUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpUnitIndex.setStatus("current")
_AcpServiceIndex_Type = Integer32
_AcpServiceIndex_Object = MibTableColumn
acpServiceIndex = _AcpServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 3),
    _AcpServiceIndex_Type()
)
acpServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpServiceIndex.setStatus("current")


class _AcpScramblingMode_Type(Integer32):
    """Custom type acpScramblingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csa", 2),
          ("des", 1))
    )


_AcpScramblingMode_Type.__name__ = "Integer32"
_AcpScramblingMode_Object = MibTableColumn
acpScramblingMode = _AcpScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 4),
    _AcpScramblingMode_Type()
)
acpScramblingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpScramblingMode.setStatus("current")
_AcpUnitAddress_Type = OctetString
_AcpUnitAddress_Object = MibTableColumn
acpUnitAddress = _AcpUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 5),
    _AcpUnitAddress_Type()
)
acpUnitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpUnitAddress.setStatus("current")


class _AcpInputInterface_Type(Integer32):
    """Custom type acpInputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acpInterfaceParallel", 2),
          ("acpInterfaceSerial", 1))
    )


_AcpInputInterface_Type.__name__ = "Integer32"
_AcpInputInterface_Object = MibTableColumn
acpInputInterface = _AcpInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 6),
    _AcpInputInterface_Type()
)
acpInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpInputInterface.setStatus("current")


class _AcpOutputInterface_Type(Integer32):
    """Custom type acpOutputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acpInterfaceParallel", 2),
          ("acpInterfaceSerial", 1))
    )


_AcpOutputInterface_Type.__name__ = "Integer32"
_AcpOutputInterface_Object = MibTableColumn
acpOutputInterface = _AcpOutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 7),
    _AcpOutputInterface_Type()
)
acpOutputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpOutputInterface.setStatus("current")


class _AcpServNumber_Type(Integer32):
    """Custom type acpServNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcpServNumber_Type.__name__ = "Integer32"
_AcpServNumber_Object = MibTableColumn
acpServNumber = _AcpServNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 8),
    _AcpServNumber_Type()
)
acpServNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpServNumber.setStatus("current")


class _AcpServAuthorization_Type(Integer32):
    """Custom type acpServAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("unauthorized", 1),
          ("unknown", 255))
    )


_AcpServAuthorization_Type.__name__ = "Integer32"
_AcpServAuthorization_Object = MibTableColumn
acpServAuthorization = _AcpServAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 9),
    _AcpServAuthorization_Type()
)
acpServAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpServAuthorization.setStatus("current")
_AcpServAuthReaCode_Type = Integer32
_AcpServAuthReaCode_Object = MibTableColumn
acpServAuthReaCode = _AcpServAuthReaCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 10),
    _AcpServAuthReaCode_Type()
)
acpServAuthReaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpServAuthReaCode.setStatus("current")


class _AcpServEncryption_Type(Integer32):
    """Custom type acpServEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixedpk", 2),
          ("fixedwk", 1),
          ("fullencryption", 4),
          ("unencrypted", 3),
          ("unknown", 255))
    )


_AcpServEncryption_Type.__name__ = "Integer32"
_AcpServEncryption_Object = MibTableColumn
acpServEncryption = _AcpServEncryption_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 11),
    _AcpServEncryption_Type()
)
acpServEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpServEncryption.setStatus("current")
_AcpCatSeqNums_Type = Integer32
_AcpCatSeqNums_Object = MibTableColumn
acpCatSeqNums = _AcpCatSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 12),
    _AcpCatSeqNums_Type()
)
acpCatSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpCatSeqNums.setStatus("current")
_AcpEmmCount_Type = Integer32
_AcpEmmCount_Object = MibTableColumn
acpEmmCount = _AcpEmmCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 13),
    _AcpEmmCount_Type()
)
acpEmmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEmmCount.setStatus("current")
_AcpProgramEpochNumber_Type = Integer32
_AcpProgramEpochNumber_Object = MibTableColumn
acpProgramEpochNumber = _AcpProgramEpochNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 14),
    _AcpProgramEpochNumber_Type()
)
acpProgramEpochNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpProgramEpochNumber.setStatus("current")
_AcpNextProgramEpochNumber_Type = Integer32
_AcpNextProgramEpochNumber_Object = MibTableColumn
acpNextProgramEpochNumber = _AcpNextProgramEpochNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 15),
    _AcpNextProgramEpochNumber_Type()
)
acpNextProgramEpochNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpNextProgramEpochNumber.setStatus("current")


class _AcpNextServAuthorization_Type(Integer32):
    """Custom type acpNextServAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("unauthorized", 1),
          ("unknown", 255))
    )


_AcpNextServAuthorization_Type.__name__ = "Integer32"
_AcpNextServAuthorization_Object = MibTableColumn
acpNextServAuthorization = _AcpNextServAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 16),
    _AcpNextServAuthorization_Type()
)
acpNextServAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpNextServAuthorization.setStatus("current")
_AcpNextServAuthReasonCode_Type = Integer32
_AcpNextServAuthReasonCode_Object = MibTableColumn
acpNextServAuthReasonCode = _AcpNextServAuthReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 17),
    _AcpNextServAuthReasonCode_Type()
)
acpNextServAuthReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpNextServAuthReasonCode.setStatus("current")
_AcpInputSourceIdA_Type = Integer32
_AcpInputSourceIdA_Object = MibTableColumn
acpInputSourceIdA = _AcpInputSourceIdA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 18),
    _AcpInputSourceIdA_Type()
)
acpInputSourceIdA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpInputSourceIdA.setStatus("current")
_AcpInputSourceIdB_Type = Integer32
_AcpInputSourceIdB_Object = MibTableColumn
acpInputSourceIdB = _AcpInputSourceIdB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 19),
    _AcpInputSourceIdB_Type()
)
acpInputSourceIdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpInputSourceIdB.setStatus("current")
_AcpPidTable_Object = MibTable
acpPidTable = _AcpPidTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4)
)
if mibBuilder.loadTexts:
    acpPidTable.setStatus("current")
_AcpPidEntry_Object = MibTableRow
acpPidEntry = _AcpPidEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1)
)
acpPidEntry.setIndexNames(
    (0, "ACP-MIB", "acpPidTblEncryptType"),
    (0, "ACP-MIB", "acpPidTblUnitIndex"),
    (0, "ACP-MIB", "acpPidTblServiceIndex"),
    (0, "ACP-MIB", "acpPidTblPidIndex"),
)
if mibBuilder.loadTexts:
    acpPidEntry.setStatus("current")


class _AcpPidTblEncryptType_Type(Integer32):
    """Custom type acpPidTblEncryptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decryptAcp", 2),
          ("encryptAcp", 1))
    )


_AcpPidTblEncryptType_Type.__name__ = "Integer32"
_AcpPidTblEncryptType_Object = MibTableColumn
acpPidTblEncryptType = _AcpPidTblEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 1),
    _AcpPidTblEncryptType_Type()
)
acpPidTblEncryptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpPidTblEncryptType.setStatus("current")
_AcpPidTblUnitIndex_Type = Integer32
_AcpPidTblUnitIndex_Object = MibTableColumn
acpPidTblUnitIndex = _AcpPidTblUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 2),
    _AcpPidTblUnitIndex_Type()
)
acpPidTblUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpPidTblUnitIndex.setStatus("current")
_AcpPidTblServiceIndex_Type = Integer32
_AcpPidTblServiceIndex_Object = MibTableColumn
acpPidTblServiceIndex = _AcpPidTblServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 3),
    _AcpPidTblServiceIndex_Type()
)
acpPidTblServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpPidTblServiceIndex.setStatus("current")
_AcpPidTblPidIndex_Type = Integer32
_AcpPidTblPidIndex_Object = MibTableColumn
acpPidTblPidIndex = _AcpPidTblPidIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 4),
    _AcpPidTblPidIndex_Type()
)
acpPidTblPidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpPidTblPidIndex.setStatus("current")
_AcpPidTblAssignedPid_Type = Integer32
_AcpPidTblAssignedPid_Object = MibTableColumn
acpPidTblAssignedPid = _AcpPidTblAssignedPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 5),
    _AcpPidTblAssignedPid_Type()
)
acpPidTblAssignedPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpPidTblAssignedPid.setStatus("current")
_AcpPidTblEcmPid_Type = Integer32
_AcpPidTblEcmPid_Object = MibTableColumn
acpPidTblEcmPid = _AcpPidTblEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 6),
    _AcpPidTblEcmPid_Type()
)
acpPidTblEcmPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpPidTblEcmPid.setStatus("current")
_AcpPidTblPidMask_Type = Integer32
_AcpPidTblPidMask_Object = MibTableColumn
acpPidTblPidMask = _AcpPidTblPidMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 7),
    _AcpPidTblPidMask_Type()
)
acpPidTblPidMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpPidTblPidMask.setStatus("current")
_AcpMibRevision_Type = Integer32
_AcpMibRevision_Object = MibScalar
acpMibRevision = _AcpMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11, 99),
    _AcpMibRevision_Type()
)
acpMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMibRevision.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACP-MIB",
    **{"acpStatus": acpStatus,
       "acpNumberofEncryptTypes": acpNumberofEncryptTypes,
       "acpNumberofDecryptTypes": acpNumberofDecryptTypes,
       "acpStatusTable": acpStatusTable,
       "acpStatusEntry": acpStatusEntry,
       "acpEncryptType": acpEncryptType,
       "acpUnitIndex": acpUnitIndex,
       "acpServiceIndex": acpServiceIndex,
       "acpScramblingMode": acpScramblingMode,
       "acpUnitAddress": acpUnitAddress,
       "acpInputInterface": acpInputInterface,
       "acpOutputInterface": acpOutputInterface,
       "acpServNumber": acpServNumber,
       "acpServAuthorization": acpServAuthorization,
       "acpServAuthReaCode": acpServAuthReaCode,
       "acpServEncryption": acpServEncryption,
       "acpCatSeqNums": acpCatSeqNums,
       "acpEmmCount": acpEmmCount,
       "acpProgramEpochNumber": acpProgramEpochNumber,
       "acpNextProgramEpochNumber": acpNextProgramEpochNumber,
       "acpNextServAuthorization": acpNextServAuthorization,
       "acpNextServAuthReasonCode": acpNextServAuthReasonCode,
       "acpInputSourceIdA": acpInputSourceIdA,
       "acpInputSourceIdB": acpInputSourceIdB,
       "acpPidTable": acpPidTable,
       "acpPidEntry": acpPidEntry,
       "acpPidTblEncryptType": acpPidTblEncryptType,
       "acpPidTblUnitIndex": acpPidTblUnitIndex,
       "acpPidTblServiceIndex": acpPidTblServiceIndex,
       "acpPidTblPidIndex": acpPidTblPidIndex,
       "acpPidTblAssignedPid": acpPidTblAssignedPid,
       "acpPidTblEcmPid": acpPidTblEcmPid,
       "acpPidTblPidMask": acpPidTblPidMask,
       "acpMibRevision": acpMibRevision}
)
