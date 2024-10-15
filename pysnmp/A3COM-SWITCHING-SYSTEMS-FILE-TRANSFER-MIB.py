# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-FILE-TRANSFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-FILE-TRANSFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:48 2024
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class A3ComSysStorageType(Integer32):
    """Custom type A3ComSysStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class A3ComSysAddressType(Integer32):
    """Custom type A3ComSysAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )





class A3ComSysResourceType(Integer32):
    """Custom type A3ComSysResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class A3ComSysResourceBitMask(OctetString):
    """Custom type A3ComSysResourceBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComSysFtGroup_ObjectIdentity = ObjectIdentity
a3ComSysFtGroup = _A3ComSysFtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14)
)
_A3ComSysFtTable_Object = MibTable
a3ComSysFtTable = _A3ComSysFtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1)
)
if mibBuilder.loadTexts:
    a3ComSysFtTable.setStatus("mandatory")
_A3ComSysFtTableEntry_Object = MibTableRow
a3ComSysFtTableEntry = _A3ComSysFtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1)
)
a3ComSysFtTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILE-TRANSFER-MIB", "a3ComSysFtIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysFtTableEntry.setStatus("mandatory")


class _A3ComSysFtIndex_Type(Integer32):
    """Custom type a3ComSysFtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysFtIndex_Type.__name__ = "Integer32"
_A3ComSysFtIndex_Object = MibTableColumn
a3ComSysFtIndex = _A3ComSysFtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 1),
    _A3ComSysFtIndex_Type()
)
a3ComSysFtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtIndex.setStatus("mandatory")


class _A3ComSysFtDirection_Type(Integer32):
    """Custom type a3ComSysFtDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localToRemote", 1),
          ("remoteToLocal", 2))
    )


_A3ComSysFtDirection_Type.__name__ = "Integer32"
_A3ComSysFtDirection_Object = MibTableColumn
a3ComSysFtDirection = _A3ComSysFtDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 2),
    _A3ComSysFtDirection_Type()
)
a3ComSysFtDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtDirection.setStatus("mandatory")


class _A3ComSysFtLocalStorageType_Type(A3ComSysStorageType):
    """Custom type a3ComSysFtLocalStorageType based on A3ComSysStorageType"""
    defaultValue = 3


_A3ComSysFtLocalStorageType_Object = MibTableColumn
a3ComSysFtLocalStorageType = _A3ComSysFtLocalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 3),
    _A3ComSysFtLocalStorageType_Type()
)
a3ComSysFtLocalStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalStorageType.setStatus("mandatory")


class _A3ComSysFtLocalResourceType_Type(A3ComSysResourceType):
    """Custom type a3ComSysFtLocalResourceType based on A3ComSysResourceType"""
    defaultValue = 2


_A3ComSysFtLocalResourceType_Object = MibTableColumn
a3ComSysFtLocalResourceType = _A3ComSysFtLocalResourceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 4),
    _A3ComSysFtLocalResourceType_Type()
)
a3ComSysFtLocalResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceType.setStatus("mandatory")


class _A3ComSysFtLocalResourceMask_Type(A3ComSysResourceBitMask):
    """Custom type a3ComSysFtLocalResourceMask based on A3ComSysResourceBitMask"""
    defaultHexValue = "00000080"


_A3ComSysFtLocalResourceMask_Object = MibTableColumn
a3ComSysFtLocalResourceMask = _A3ComSysFtLocalResourceMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 5),
    _A3ComSysFtLocalResourceMask_Type()
)
a3ComSysFtLocalResourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceMask.setStatus("mandatory")


class _A3ComSysFtLocalResourceAttribute_Type(ObjectIdentifier):
    """Custom type a3ComSysFtLocalResourceAttribute based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 1)


_A3ComSysFtLocalResourceAttribute_Object = MibTableColumn
a3ComSysFtLocalResourceAttribute = _A3ComSysFtLocalResourceAttribute_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 6),
    _A3ComSysFtLocalResourceAttribute_Type()
)
a3ComSysFtLocalResourceAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceAttribute.setStatus("mandatory")


class _A3ComSysFtRemoteAddressType_Type(A3ComSysAddressType):
    """Custom type a3ComSysFtRemoteAddressType based on A3ComSysAddressType"""
    defaultValue = 2


_A3ComSysFtRemoteAddressType_Object = MibTableColumn
a3ComSysFtRemoteAddressType = _A3ComSysFtRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 7),
    _A3ComSysFtRemoteAddressType_Type()
)
a3ComSysFtRemoteAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteAddressType.setStatus("mandatory")


class _A3ComSysFtRemoteAddress_Type(OctetString):
    """Custom type a3ComSysFtRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A3ComSysFtRemoteAddress_Type.__name__ = "OctetString"
_A3ComSysFtRemoteAddress_Object = MibTableColumn
a3ComSysFtRemoteAddress = _A3ComSysFtRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 8),
    _A3ComSysFtRemoteAddress_Type()
)
a3ComSysFtRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteAddress.setStatus("mandatory")


class _A3ComSysFtRemoteFileName_Type(DisplayString):
    """Custom type a3ComSysFtRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteFileName_Type.__name__ = "DisplayString"
_A3ComSysFtRemoteFileName_Object = MibTableColumn
a3ComSysFtRemoteFileName = _A3ComSysFtRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 9),
    _A3ComSysFtRemoteFileName_Type()
)
a3ComSysFtRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteFileName.setStatus("mandatory")


class _A3ComSysFtRemoteUserName_Type(DisplayString):
    """Custom type a3ComSysFtRemoteUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteUserName_Type.__name__ = "DisplayString"
_A3ComSysFtRemoteUserName_Object = MibTableColumn
a3ComSysFtRemoteUserName = _A3ComSysFtRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 10),
    _A3ComSysFtRemoteUserName_Type()
)
a3ComSysFtRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteUserName.setStatus("mandatory")


class _A3ComSysFtRemoteUserPassword_Type(OctetString):
    """Custom type a3ComSysFtRemoteUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteUserPassword_Type.__name__ = "OctetString"
_A3ComSysFtRemoteUserPassword_Object = MibTableColumn
a3ComSysFtRemoteUserPassword = _A3ComSysFtRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 11),
    _A3ComSysFtRemoteUserPassword_Type()
)
a3ComSysFtRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteUserPassword.setStatus("mandatory")


class _A3ComSysFtForceTransfer_Type(Integer32):
    """Custom type a3ComSysFtForceTransfer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_A3ComSysFtForceTransfer_Type.__name__ = "Integer32"
_A3ComSysFtForceTransfer_Object = MibTableColumn
a3ComSysFtForceTransfer = _A3ComSysFtForceTransfer_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 12),
    _A3ComSysFtForceTransfer_Type()
)
a3ComSysFtForceTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtForceTransfer.setStatus("mandatory")
_A3ComSysFtBytesTransferred_Type = Counter32
_A3ComSysFtBytesTransferred_Object = MibTableColumn
a3ComSysFtBytesTransferred = _A3ComSysFtBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 13),
    _A3ComSysFtBytesTransferred_Type()
)
a3ComSysFtBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtBytesTransferred.setStatus("mandatory")


class _A3ComSysFtStatus_Type(Integer32):
    """Custom type a3ComSysFtStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("statusError", 10),
          ("statusFileIncompatible", 9),
          ("statusFileNotFound", 7),
          ("statusFileTooBig", 8),
          ("statusInProgress", 2),
          ("statusLocalInvalid", 3),
          ("statusRemoteInvalid", 4),
          ("statusRemoteUnreachable", 5),
          ("statusSuccessfulCompletion", 1),
          ("statusUserAuthFailed", 6))
    )


_A3ComSysFtStatus_Type.__name__ = "Integer32"
_A3ComSysFtStatus_Object = MibTableColumn
a3ComSysFtStatus = _A3ComSysFtStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 14),
    _A3ComSysFtStatus_Type()
)
a3ComSysFtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtStatus.setStatus("mandatory")
_A3ComSysFtDetailedStatus_Type = ObjectIdentifier
_A3ComSysFtDetailedStatus_Object = MibTableColumn
a3ComSysFtDetailedStatus = _A3ComSysFtDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 15),
    _A3ComSysFtDetailedStatus_Type()
)
a3ComSysFtDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtDetailedStatus.setStatus("mandatory")
_A3ComSysFtDetailedStatusString_Type = DisplayString
_A3ComSysFtDetailedStatusString_Object = MibTableColumn
a3ComSysFtDetailedStatusString = _A3ComSysFtDetailedStatusString_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 16),
    _A3ComSysFtDetailedStatusString_Type()
)
a3ComSysFtDetailedStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtDetailedStatusString.setStatus("mandatory")


class _A3ComSysFtOwnerString_Type(DisplayString):
    """Custom type a3ComSysFtOwnerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtOwnerString_Type.__name__ = "DisplayString"
_A3ComSysFtOwnerString_Object = MibTableColumn
a3ComSysFtOwnerString = _A3ComSysFtOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 17),
    _A3ComSysFtOwnerString_Type()
)
a3ComSysFtOwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtOwnerString.setStatus("mandatory")
_A3ComSysFtRowStatus_Type = RowStatus
_A3ComSysFtRowStatus_Object = MibTableColumn
a3ComSysFtRowStatus = _A3ComSysFtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 18),
    _A3ComSysFtRowStatus_Type()
)
a3ComSysFtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRowStatus.setStatus("mandatory")


class _A3ComSysFtProtocol_Type(Integer32):
    """Custom type a3ComSysFtProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftProtocolFtp", 2),
          ("ftProtocolTftp", 1))
    )


_A3ComSysFtProtocol_Type.__name__ = "Integer32"
_A3ComSysFtProtocol_Object = MibTableColumn
a3ComSysFtProtocol = _A3ComSysFtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 19),
    _A3ComSysFtProtocol_Type()
)
a3ComSysFtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtProtocol.setStatus("mandatory")
_A3ComSysFtResourceAttributes_ObjectIdentity = ObjectIdentity
a3ComSysFtResourceAttributes = _A3ComSysFtResourceAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2)
)
_A3ComSysFtSystemAttributes_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemAttributes = _A3ComSysFtSystemAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1)
)
_A3ComSysFtSystemOperationalCode_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemOperationalCode = _A3ComSysFtSystemOperationalCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 1)
)
_A3ComSysFtSystemConfiguration_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemConfiguration = _A3ComSysFtSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 2)
)
_A3ComSysFtSystemBridgeFilterCode_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemBridgeFilterCode = _A3ComSysFtSystemBridgeFilterCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 3)
)
_A3ComSysFtDetailedResourceStatus_ObjectIdentity = ObjectIdentity
a3ComSysFtDetailedResourceStatus = _A3ComSysFtDetailedResourceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3)
)
_A3ComSysFtSystemDetailedStatus_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemDetailedStatus = _A3ComSysFtSystemDetailedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1)
)
_A3ComSysFtSysStatusNotApplicable_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNotApplicable = _A3ComSysFtSysStatusNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 1)
)
_A3ComSysFtSysStatusNoImageLabel_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNoImageLabel = _A3ComSysFtSysStatusNoImageLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 2)
)
_A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusConfigIdMismatch = _A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 3)
)
_A3ComSysFtSysStatusChecksumError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusChecksumError = _A3ComSysFtSysStatusChecksumError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 4)
)
_A3ComSysFtSysStatusNvRamError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNvRamError = _A3ComSysFtSysStatusNvRamError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 5)
)
_A3ComSysFtSysStatusFlashError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusFlashError = _A3ComSysFtSysStatusFlashError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 6)
)
_A3ComSysFtSysStatusNoRoom_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNoRoom = _A3ComSysFtSysStatusNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 7)
)
_A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterNotApplicable = _A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 8)
)
_A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterSyntaxError = _A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 9)
)
_A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterdownloadError = _A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 10)
)
_A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterNoRoom = _A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-FILE-TRANSFER-MIB",
    **{"RowStatus": RowStatus,
       "A3ComSysStorageType": A3ComSysStorageType,
       "A3ComSysAddressType": A3ComSysAddressType,
       "A3ComSysResourceType": A3ComSysResourceType,
       "A3ComSysResourceBitMask": A3ComSysResourceBitMask,
       "a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComSysFtGroup": a3ComSysFtGroup,
       "a3ComSysFtTable": a3ComSysFtTable,
       "a3ComSysFtTableEntry": a3ComSysFtTableEntry,
       "a3ComSysFtIndex": a3ComSysFtIndex,
       "a3ComSysFtDirection": a3ComSysFtDirection,
       "a3ComSysFtLocalStorageType": a3ComSysFtLocalStorageType,
       "a3ComSysFtLocalResourceType": a3ComSysFtLocalResourceType,
       "a3ComSysFtLocalResourceMask": a3ComSysFtLocalResourceMask,
       "a3ComSysFtLocalResourceAttribute": a3ComSysFtLocalResourceAttribute,
       "a3ComSysFtRemoteAddressType": a3ComSysFtRemoteAddressType,
       "a3ComSysFtRemoteAddress": a3ComSysFtRemoteAddress,
       "a3ComSysFtRemoteFileName": a3ComSysFtRemoteFileName,
       "a3ComSysFtRemoteUserName": a3ComSysFtRemoteUserName,
       "a3ComSysFtRemoteUserPassword": a3ComSysFtRemoteUserPassword,
       "a3ComSysFtForceTransfer": a3ComSysFtForceTransfer,
       "a3ComSysFtBytesTransferred": a3ComSysFtBytesTransferred,
       "a3ComSysFtStatus": a3ComSysFtStatus,
       "a3ComSysFtDetailedStatus": a3ComSysFtDetailedStatus,
       "a3ComSysFtDetailedStatusString": a3ComSysFtDetailedStatusString,
       "a3ComSysFtOwnerString": a3ComSysFtOwnerString,
       "a3ComSysFtRowStatus": a3ComSysFtRowStatus,
       "a3ComSysFtProtocol": a3ComSysFtProtocol,
       "a3ComSysFtResourceAttributes": a3ComSysFtResourceAttributes,
       "a3ComSysFtSystemAttributes": a3ComSysFtSystemAttributes,
       "a3ComSysFtSystemOperationalCode": a3ComSysFtSystemOperationalCode,
       "a3ComSysFtSystemConfiguration": a3ComSysFtSystemConfiguration,
       "a3ComSysFtSystemBridgeFilterCode": a3ComSysFtSystemBridgeFilterCode,
       "a3ComSysFtDetailedResourceStatus": a3ComSysFtDetailedResourceStatus,
       "a3ComSysFtSystemDetailedStatus": a3ComSysFtSystemDetailedStatus,
       "a3ComSysFtSysStatusNotApplicable": a3ComSysFtSysStatusNotApplicable,
       "a3ComSysFtSysStatusNoImageLabel": a3ComSysFtSysStatusNoImageLabel,
       "a3ComSysFtSysStatusConfigIdMismatch": a3ComSysFtSysStatusConfigIdMismatch,
       "a3ComSysFtSysStatusChecksumError": a3ComSysFtSysStatusChecksumError,
       "a3ComSysFtSysStatusNvRamError": a3ComSysFtSysStatusNvRamError,
       "a3ComSysFtSysStatusFlashError": a3ComSysFtSysStatusFlashError,
       "a3ComSysFtSysStatusNoRoom": a3ComSysFtSysStatusNoRoom,
       "a3ComSysFtSysBridgeFilterNotApplicable": a3ComSysFtSysBridgeFilterNotApplicable,
       "a3ComSysFtSysBridgeFilterSyntaxError": a3ComSysFtSysBridgeFilterSyntaxError,
       "a3ComSysFtSysBridgeFilterdownloadError": a3ComSysFtSysBridgeFilterdownloadError,
       "a3ComSysFtSysBridgeFilterNoRoom": a3ComSysFtSysBridgeFilterNoRoom}
)
