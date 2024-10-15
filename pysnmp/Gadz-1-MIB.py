# SNMP MIB module (Gadz-1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Gadz-1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:31 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gadzoox_ObjectIdentity = ObjectIdentity
gadzoox = _Gadzoox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754)
)
_NetMgmt_ObjectIdentity = ObjectIdentity
netMgmt = _NetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1)
)


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold", 2),
          ("warm", 1))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 1),
    _SysReset_Type()
)
sysReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")


class _SysDiagnostic_Type(Integer32):
    """Custom type sysDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDiagnostic_Type.__name__ = "Integer32"
_SysDiagnostic_Object = MibScalar
sysDiagnostic = _SysDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 2),
    _SysDiagnostic_Type()
)
sysDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDiagnostic.setStatus("mandatory")
_Zoning_ObjectIdentity = ObjectIdentity
zoning = _Zoning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3)
)
_NlZoningPolicyControlOwner_Type = IpAddress
_NlZoningPolicyControlOwner_Object = MibScalar
nlZoningPolicyControlOwner = _NlZoningPolicyControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 1),
    _NlZoningPolicyControlOwner_Type()
)
nlZoningPolicyControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlZoningPolicyControlOwner.setStatus("mandatory")
_NlZoningPolicyTimeout_Type = Integer32
_NlZoningPolicyTimeout_Object = MibScalar
nlZoningPolicyTimeout = _NlZoningPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 2),
    _NlZoningPolicyTimeout_Type()
)
nlZoningPolicyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlZoningPolicyTimeout.setStatus("mandatory")


class _NlZoningPolicyStatus_Type(Integer32):
    """Custom type nlZoningPolicyStatus based on Integer32"""
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
        *(("no-current-owner", 0),
          ("request-in-progress", 3),
          ("request-invalid", 2),
          ("request-valid", 1))
    )


_NlZoningPolicyStatus_Type.__name__ = "Integer32"
_NlZoningPolicyStatus_Object = MibScalar
nlZoningPolicyStatus = _NlZoningPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 3),
    _NlZoningPolicyStatus_Type()
)
nlZoningPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlZoningPolicyStatus.setStatus("mandatory")


class _NlZoningPolicyControl_Type(Integer32):
    """Custom type nlZoningPolicyControl based on Integer32"""
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
        *(("clear-owner", 0),
          ("clear-zoning-configuration", 2),
          ("create-table", 1),
          ("default-zoning-configuration", 3))
    )


_NlZoningPolicyControl_Type.__name__ = "Integer32"
_NlZoningPolicyControl_Object = MibScalar
nlZoningPolicyControl = _NlZoningPolicyControl_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 4),
    _NlZoningPolicyControl_Type()
)
nlZoningPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlZoningPolicyControl.setStatus("mandatory")
_NlZoningPolicyLastError_Type = OctetString
_NlZoningPolicyLastError_Object = MibScalar
nlZoningPolicyLastError = _NlZoningPolicyLastError_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 5),
    _NlZoningPolicyLastError_Type()
)
nlZoningPolicyLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlZoningPolicyLastError.setStatus("mandatory")
_NlPendingZoneCount_Type = Integer32
_NlPendingZoneCount_Object = MibScalar
nlPendingZoneCount = _NlPendingZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 6),
    _NlPendingZoneCount_Type()
)
nlPendingZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneCount.setStatus("mandatory")
_NlPendingZoneTable_Object = MibTable
nlPendingZoneTable = _NlPendingZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    nlPendingZoneTable.setStatus("mandatory")
_NlPendingZoneEntry_Object = MibTableRow
nlPendingZoneEntry = _NlPendingZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1)
)
nlPendingZoneEntry.setIndexNames(
    (0, "Gadz-1-MIB", "nlPendingZoneIndex"),
)
if mibBuilder.loadTexts:
    nlPendingZoneEntry.setStatus("mandatory")
_NlPendingZoneIndex_Type = Integer32
_NlPendingZoneIndex_Object = MibTableColumn
nlPendingZoneIndex = _NlPendingZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 1),
    _NlPendingZoneIndex_Type()
)
nlPendingZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneIndex.setStatus("mandatory")
_NlPendingZoneName_Type = OctetString
_NlPendingZoneName_Object = MibTableColumn
nlPendingZoneName = _NlPendingZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 2),
    _NlPendingZoneName_Type()
)
nlPendingZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlPendingZoneName.setStatus("mandatory")


class _NlPendingZoneType_Type(Integer32):
    """Custom type nlPendingZoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("edgeDevice", 1)
    )


_NlPendingZoneType_Type.__name__ = "Integer32"
_NlPendingZoneType_Object = MibTableColumn
nlPendingZoneType = _NlPendingZoneType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 3),
    _NlPendingZoneType_Type()
)
nlPendingZoneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlPendingZoneType.setStatus("mandatory")
_NlPendingZoneMembers_Type = OctetString
_NlPendingZoneMembers_Object = MibTableColumn
nlPendingZoneMembers = _NlPendingZoneMembers_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 4),
    _NlPendingZoneMembers_Type()
)
nlPendingZoneMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlPendingZoneMembers.setStatus("mandatory")
_NlPendingZoneLipToZonePolicy_Type = Integer32
_NlPendingZoneLipToZonePolicy_Object = MibTableColumn
nlPendingZoneLipToZonePolicy = _NlPendingZoneLipToZonePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 5),
    _NlPendingZoneLipToZonePolicy_Type()
)
nlPendingZoneLipToZonePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlPendingZoneLipToZonePolicy.setStatus("mandatory")
_NlPendingZoneMemberCount_Type = Integer32
_NlPendingZoneMemberCount_Object = MibScalar
nlPendingZoneMemberCount = _NlPendingZoneMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 8),
    _NlPendingZoneMemberCount_Type()
)
nlPendingZoneMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberCount.setStatus("mandatory")
_NlPendingZoneMemberTable_Object = MibTable
nlPendingZoneMemberTable = _NlPendingZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    nlPendingZoneMemberTable.setStatus("mandatory")
_NlPendingZoneMemberEntry_Object = MibTableRow
nlPendingZoneMemberEntry = _NlPendingZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1)
)
nlPendingZoneMemberEntry.setIndexNames(
    (0, "Gadz-1-MIB", "nlPendingZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    nlPendingZoneMemberEntry.setStatus("mandatory")
_NlPendingZoneMemberIndex_Type = Integer32
_NlPendingZoneMemberIndex_Object = MibTableColumn
nlPendingZoneMemberIndex = _NlPendingZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 1),
    _NlPendingZoneMemberIndex_Type()
)
nlPendingZoneMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberIndex.setStatus("mandatory")
_NlPendingZoneMemberName_Type = OctetString
_NlPendingZoneMemberName_Object = MibTableColumn
nlPendingZoneMemberName = _NlPendingZoneMemberName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 2),
    _NlPendingZoneMemberName_Type()
)
nlPendingZoneMemberName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberName.setStatus("mandatory")


class _NlPendingZoneMemberType_Type(Integer32):
    """Custom type nlPendingZoneMemberType based on Integer32"""
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
        *(("hardAssignedALPAZoneMember", 2),
          ("portZoneMember", 1),
          ("typeNotYetAssigned", 0),
          ("wwnZoneMember", 3))
    )


_NlPendingZoneMemberType_Type.__name__ = "Integer32"
_NlPendingZoneMemberType_Object = MibTableColumn
nlPendingZoneMemberType = _NlPendingZoneMemberType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 3),
    _NlPendingZoneMemberType_Type()
)
nlPendingZoneMemberType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberType.setStatus("mandatory")
_NlPendingZoneMemberID_Type = OctetString
_NlPendingZoneMemberID_Object = MibTableColumn
nlPendingZoneMemberID = _NlPendingZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 4),
    _NlPendingZoneMemberID_Type()
)
nlPendingZoneMemberID.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberID.setStatus("mandatory")
_NlActiveZoneCount_Type = Integer32
_NlActiveZoneCount_Object = MibScalar
nlActiveZoneCount = _NlActiveZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 10),
    _NlActiveZoneCount_Type()
)
nlActiveZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneCount.setStatus("mandatory")
_NlActiveZoneTable_Object = MibTable
nlActiveZoneTable = _NlActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    nlActiveZoneTable.setStatus("mandatory")
_NlActiveZoneEntry_Object = MibTableRow
nlActiveZoneEntry = _NlActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1)
)
nlActiveZoneEntry.setIndexNames(
    (0, "Gadz-1-MIB", "nlActiveZoneIndex"),
)
if mibBuilder.loadTexts:
    nlActiveZoneEntry.setStatus("mandatory")
_NlActiveZoneIndex_Type = Integer32
_NlActiveZoneIndex_Object = MibTableColumn
nlActiveZoneIndex = _NlActiveZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 1),
    _NlActiveZoneIndex_Type()
)
nlActiveZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneIndex.setStatus("mandatory")
_NlActiveZoneName_Type = OctetString
_NlActiveZoneName_Object = MibTableColumn
nlActiveZoneName = _NlActiveZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 2),
    _NlActiveZoneName_Type()
)
nlActiveZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneName.setStatus("mandatory")


class _NlActiveZoneType_Type(Integer32):
    """Custom type nlActiveZoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("edgeDevice", 1)
    )


_NlActiveZoneType_Type.__name__ = "Integer32"
_NlActiveZoneType_Object = MibTableColumn
nlActiveZoneType = _NlActiveZoneType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 3),
    _NlActiveZoneType_Type()
)
nlActiveZoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneType.setStatus("mandatory")
_NlActiveZoneAddressSpace_Type = Integer32
_NlActiveZoneAddressSpace_Object = MibTableColumn
nlActiveZoneAddressSpace = _NlActiveZoneAddressSpace_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 4),
    _NlActiveZoneAddressSpace_Type()
)
nlActiveZoneAddressSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneAddressSpace.setStatus("mandatory")
_NlActiveZoneMembers_Type = OctetString
_NlActiveZoneMembers_Object = MibTableColumn
nlActiveZoneMembers = _NlActiveZoneMembers_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 5),
    _NlActiveZoneMembers_Type()
)
nlActiveZoneMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMembers.setStatus("mandatory")
_NlActiveZoneLipToZonePolicy_Type = Integer32
_NlActiveZoneLipToZonePolicy_Object = MibTableColumn
nlActiveZoneLipToZonePolicy = _NlActiveZoneLipToZonePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 6),
    _NlActiveZoneLipToZonePolicy_Type()
)
nlActiveZoneLipToZonePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneLipToZonePolicy.setStatus("mandatory")
_NlActiveZoneMemberCount_Type = Integer32
_NlActiveZoneMemberCount_Object = MibScalar
nlActiveZoneMemberCount = _NlActiveZoneMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 12),
    _NlActiveZoneMemberCount_Type()
)
nlActiveZoneMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberCount.setStatus("mandatory")
_NlActiveZoneMemberTable_Object = MibTable
nlActiveZoneMemberTable = _NlActiveZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    nlActiveZoneMemberTable.setStatus("mandatory")
_NlActiveZoneMemberEntry_Object = MibTableRow
nlActiveZoneMemberEntry = _NlActiveZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1)
)
nlActiveZoneMemberEntry.setIndexNames(
    (0, "Gadz-1-MIB", "nlActiveZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    nlActiveZoneMemberEntry.setStatus("mandatory")
_NlActiveZoneMemberIndex_Type = Integer32
_NlActiveZoneMemberIndex_Object = MibTableColumn
nlActiveZoneMemberIndex = _NlActiveZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 1),
    _NlActiveZoneMemberIndex_Type()
)
nlActiveZoneMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberIndex.setStatus("mandatory")
_NlActiveZoneMemberName_Type = OctetString
_NlActiveZoneMemberName_Object = MibTableColumn
nlActiveZoneMemberName = _NlActiveZoneMemberName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 2),
    _NlActiveZoneMemberName_Type()
)
nlActiveZoneMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberName.setStatus("mandatory")


class _NlActiveZoneMemberType_Type(Integer32):
    """Custom type nlActiveZoneMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardAssignedALPAZoneMember", 2),
          ("portZoneMember", 1),
          ("wwnZoneMember", 3))
    )


_NlActiveZoneMemberType_Type.__name__ = "Integer32"
_NlActiveZoneMemberType_Object = MibTableColumn
nlActiveZoneMemberType = _NlActiveZoneMemberType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 3),
    _NlActiveZoneMemberType_Type()
)
nlActiveZoneMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberType.setStatus("mandatory")
_NlActiveZoneMemberID_Type = OctetString
_NlActiveZoneMemberID_Object = MibTableColumn
nlActiveZoneMemberID = _NlActiveZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 4),
    _NlActiveZoneMemberID_Type()
)
nlActiveZoneMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberID.setStatus("mandatory")
_Download_ObjectIdentity = ObjectIdentity
download = _Download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3)
)


class _DownloadFile_Type(DisplayString):
    """Custom type downloadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DownloadFile_Type.__name__ = "DisplayString"
_DownloadFile_Object = MibScalar
downloadFile = _DownloadFile_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 1),
    _DownloadFile_Type()
)
downloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFile.setStatus("mandatory")


class _DownloadBootFile_Type(DisplayString):
    """Custom type downloadBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DownloadBootFile_Type.__name__ = "DisplayString"
_DownloadBootFile_Object = MibScalar
downloadBootFile = _DownloadBootFile_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 2),
    _DownloadBootFile_Type()
)
downloadBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadBootFile.setStatus("mandatory")
_DownloadTFTPServer_Type = IpAddress
_DownloadTFTPServer_Object = MibScalar
downloadTFTPServer = _DownloadTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 3),
    _DownloadTFTPServer_Type()
)
downloadTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTFTPServer.setStatus("mandatory")
_DownloadTargetID_Type = Integer32
_DownloadTargetID_Object = MibScalar
downloadTargetID = _DownloadTargetID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 4),
    _DownloadTargetID_Type()
)
downloadTargetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTargetID.setStatus("mandatory")


class _DownloadAction_Type(Integer32):
    """Custom type downloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downloadToPROM", 2),
          ("notDownloading", 1))
    )


_DownloadAction_Type.__name__ = "Integer32"
_DownloadAction_Object = MibScalar
downloadAction = _DownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 5),
    _DownloadAction_Type()
)
downloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadAction.setStatus("mandatory")


class _DownloadStatus_Type(Integer32):
    """Custom type downloadStatus based on Integer32"""
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
        *(("downloadAlreadyInProgress", 9),
          ("downloadCancelled", 10),
          ("downloadChecksumError", 5),
          ("downloadGeneralError", 3),
          ("downloadIncompatibleImage", 6),
          ("downloadNoResponseFromServer", 4),
          ("downloadStatusUnknown", 2),
          ("downloadSuccess", 1),
          ("downloadTftpAccessViolation", 8),
          ("downloadTftpFileNotFound", 7))
    )


_DownloadStatus_Type.__name__ = "Integer32"
_DownloadStatus_Object = MibScalar
downloadStatus = _DownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 6),
    _DownloadStatus_Type()
)
downloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadStatus.setStatus("mandatory")
_DownloadRetry_Type = Integer32
_DownloadRetry_Object = MibScalar
downloadRetry = _DownloadRetry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 7),
    _DownloadRetry_Type()
)
downloadRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadRetry.setStatus("mandatory")
_DownloadTimeOut_Type = Integer32
_DownloadTimeOut_Object = MibScalar
downloadTimeOut = _DownloadTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 8),
    _DownloadTimeOut_Type()
)
downloadTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTimeOut.setStatus("mandatory")


class _DownloadCfgFileFileName_Type(DisplayString):
    """Custom type downloadCfgFileFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DownloadCfgFileFileName_Type.__name__ = "DisplayString"
_DownloadCfgFileFileName_Object = MibScalar
downloadCfgFileFileName = _DownloadCfgFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 9),
    _DownloadCfgFileFileName_Type()
)
downloadCfgFileFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadCfgFileFileName.setStatus("mandatory")
_DownloadCfgFileServerIp_Type = IpAddress
_DownloadCfgFileServerIp_Object = MibScalar
downloadCfgFileServerIp = _DownloadCfgFileServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 10),
    _DownloadCfgFileServerIp_Type()
)
downloadCfgFileServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadCfgFileServerIp.setStatus("mandatory")


class _DownloadCfgFileAction_Type(Integer32):
    """Custom type downloadCfgFileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupConfig", 2),
          ("noAction", 1),
          ("restoreConfig", 3))
    )


_DownloadCfgFileAction_Type.__name__ = "Integer32"
_DownloadCfgFileAction_Object = MibScalar
downloadCfgFileAction = _DownloadCfgFileAction_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 11),
    _DownloadCfgFileAction_Type()
)
downloadCfgFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadCfgFileAction.setStatus("mandatory")


class _DownloadCfgFileBkupStatus_Type(Integer32):
    """Custom type downloadCfgFileBkupStatus based on Integer32"""
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
        *(("backUpRestoreCouldNotWriteFile", 10),
          ("backUpRestoreFileNotFound", 9),
          ("backUpRestoreGeneralError", 4),
          ("backUpRestoreIncomplete", 3),
          ("backUpRestoreNoFileNameSpecified", 5),
          ("backUpRestoreNoIpAddressSpecified", 6),
          ("backUpRestoreNoResponseFromServer", 8),
          ("backUpRestoreStatusUnknown", 2),
          ("backUpRestoreSuccess", 1),
          ("backUpRestoreTftpDriverError", 7))
    )


_DownloadCfgFileBkupStatus_Type.__name__ = "Integer32"
_DownloadCfgFileBkupStatus_Object = MibScalar
downloadCfgFileBkupStatus = _DownloadCfgFileBkupStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 12),
    _DownloadCfgFileBkupStatus_Type()
)
downloadCfgFileBkupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadCfgFileBkupStatus.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 4)
)
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 5)
)
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 6)
)
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7)
)
_ProxyMaxMembers_Type = Integer32
_ProxyMaxMembers_Object = MibScalar
proxyMaxMembers = _ProxyMaxMembers_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 1),
    _ProxyMaxMembers_Type()
)
proxyMaxMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyMaxMembers.setStatus("mandatory")
_ProxyCurMembers_Type = Integer32
_ProxyCurMembers_Object = MibScalar
proxyCurMembers = _ProxyCurMembers_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 2),
    _ProxyCurMembers_Type()
)
proxyCurMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyCurMembers.setStatus("mandatory")
_ProxyChanges_Type = Counter32
_ProxyChanges_Object = MibScalar
proxyChanges = _ProxyChanges_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 3),
    _ProxyChanges_Type()
)
proxyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyChanges.setStatus("mandatory")


class _ProxyBoardID_Type(OctetString):
    """Custom type proxyBoardID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProxyBoardID_Type.__name__ = "OctetString"
_ProxyBoardID_Object = MibScalar
proxyBoardID = _ProxyBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 4),
    _ProxyBoardID_Type()
)
proxyBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyBoardID.setStatus("mandatory")


class _ProxyFirmwareVersion_Type(OctetString):
    """Custom type proxyFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ProxyFirmwareVersion_Type.__name__ = "OctetString"
_ProxyFirmwareVersion_Object = MibScalar
proxyFirmwareVersion = _ProxyFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 5),
    _ProxyFirmwareVersion_Type()
)
proxyFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyFirmwareVersion.setStatus("mandatory")


class _ProxyTopologyCRC_Type(Integer32):
    """Custom type proxyTopologyCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProxyTopologyCRC_Type.__name__ = "Integer32"
_ProxyTopologyCRC_Object = MibScalar
proxyTopologyCRC = _ProxyTopologyCRC_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 6),
    _ProxyTopologyCRC_Type()
)
proxyTopologyCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyTopologyCRC.setStatus("mandatory")


class _ProxyEventStatus_Type(Integer32):
    """Custom type proxyEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ProxyEventStatus_Type.__name__ = "Integer32"
_ProxyEventStatus_Object = MibScalar
proxyEventStatus = _ProxyEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 7),
    _ProxyEventStatus_Type()
)
proxyEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyEventStatus.setStatus("mandatory")


class _ProxyDeviceEventInd_Type(Integer32):
    """Custom type proxyDeviceEventInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ProxyDeviceEventInd_Type.__name__ = "Integer32"
_ProxyDeviceEventInd_Object = MibScalar
proxyDeviceEventInd = _ProxyDeviceEventInd_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 8),
    _ProxyDeviceEventInd_Type()
)
proxyDeviceEventInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyDeviceEventInd.setStatus("mandatory")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1)
)
deviceEntry.setIndexNames(
    (0, "Gadz-1-MIB", "devDeviceID"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")
_DevDeviceID_Type = Integer32
_DevDeviceID_Object = MibTableColumn
devDeviceID = _DevDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 1),
    _DevDeviceID_Type()
)
devDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDeviceID.setStatus("mandatory")
_DevOID_Type = ObjectIdentifier
_DevOID_Object = MibTableColumn
devOID = _DevOID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 2),
    _DevOID_Type()
)
devOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devOID.setStatus("mandatory")


class _DevProductID_Type(OctetString):
    """Custom type devProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DevProductID_Type.__name__ = "OctetString"
_DevProductID_Object = MibTableColumn
devProductID = _DevProductID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 3),
    _DevProductID_Type()
)
devProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devProductID.setStatus("mandatory")


class _DevBoardID_Type(OctetString):
    """Custom type devBoardID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DevBoardID_Type.__name__ = "OctetString"
_DevBoardID_Object = MibTableColumn
devBoardID = _DevBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 4),
    _DevBoardID_Type()
)
devBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devBoardID.setStatus("mandatory")


class _DevFirmwareVersion_Type(OctetString):
    """Custom type devFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DevFirmwareVersion_Type.__name__ = "OctetString"
_DevFirmwareVersion_Object = MibTableColumn
devFirmwareVersion = _DevFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 5),
    _DevFirmwareVersion_Type()
)
devFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFirmwareVersion.setStatus("mandatory")


class _DevEventStatus_Type(Integer32):
    """Custom type devEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevEventStatus_Type.__name__ = "Integer32"
_DevEventStatus_Object = MibTableColumn
devEventStatus = _DevEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 6),
    _DevEventStatus_Type()
)
devEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devEventStatus.setStatus("mandatory")


class _DevReset_Type(Integer32):
    """Custom type devReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold", 2),
          ("warm", 1))
    )


_DevReset_Type.__name__ = "Integer32"
_DevReset_Object = MibTableColumn
devReset = _DevReset_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 7),
    _DevReset_Type()
)
devReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    devReset.setStatus("mandatory")


class _DevDiagnostic_Type(Integer32):
    """Custom type devDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DevDiagnostic_Type.__name__ = "Integer32"
_DevDiagnostic_Object = MibTableColumn
devDiagnostic = _DevDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 8),
    _DevDiagnostic_Type()
)
devDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDiagnostic.setStatus("mandatory")
_DevSysUpTimestamp_Type = TimeTicks
_DevSysUpTimestamp_Object = MibTableColumn
devSysUpTimestamp = _DevSysUpTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 9),
    _DevSysUpTimestamp_Type()
)
devSysUpTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSysUpTimestamp.setStatus("mandatory")
_DevCumulativeUpTime_Type = Counter32
_DevCumulativeUpTime_Object = MibTableColumn
devCumulativeUpTime = _DevCumulativeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 10),
    _DevCumulativeUpTime_Type()
)
devCumulativeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCumulativeUpTime.setStatus("mandatory")


class _DevContact_Type(OctetString):
    """Custom type devContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DevContact_Type.__name__ = "OctetString"
_DevContact_Object = MibTableColumn
devContact = _DevContact_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 11),
    _DevContact_Type()
)
devContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devContact.setStatus("mandatory")


class _DevLocation_Type(OctetString):
    """Custom type devLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DevLocation_Type.__name__ = "OctetString"
_DevLocation_Object = MibTableColumn
devLocation = _DevLocation_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 12),
    _DevLocation_Type()
)
devLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devLocation.setStatus("mandatory")


class _DevTopologyLink_Type(OctetString):
    """Custom type devTopologyLink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DevTopologyLink_Type.__name__ = "OctetString"
_DevTopologyLink_Object = MibTableColumn
devTopologyLink = _DevTopologyLink_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 13),
    _DevTopologyLink_Type()
)
devTopologyLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTopologyLink.setStatus("mandatory")


class _DevBeaconOnTime_Type(Integer32):
    """Custom type devBeaconOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_DevBeaconOnTime_Type.__name__ = "Integer32"
_DevBeaconOnTime_Object = MibTableColumn
devBeaconOnTime = _DevBeaconOnTime_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 14),
    _DevBeaconOnTime_Type()
)
devBeaconOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBeaconOnTime.setStatus("mandatory")


class _DevBeaconOffTime_Type(Integer32):
    """Custom type devBeaconOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_DevBeaconOffTime_Type.__name__ = "Integer32"
_DevBeaconOffTime_Object = MibTableColumn
devBeaconOffTime = _DevBeaconOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 15),
    _DevBeaconOffTime_Type()
)
devBeaconOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBeaconOffTime.setStatus("mandatory")


class _DevFaultLedState_Type(Integer32):
    """Custom type devFaultLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevFaultLedState_Type.__name__ = "Integer32"
_DevFaultLedState_Object = MibTableColumn
devFaultLedState = _DevFaultLedState_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 16),
    _DevFaultLedState_Type()
)
devFaultLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFaultLedState.setStatus("mandatory")


class _DevNumPorts_Type(Integer32):
    """Custom type devNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DevNumPorts_Type.__name__ = "Integer32"
_DevNumPorts_Object = MibTableColumn
devNumPorts = _DevNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 17),
    _DevNumPorts_Type()
)
devNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devNumPorts.setStatus("mandatory")


class _DevType_Type(OctetString):
    """Custom type devType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DevType_Type.__name__ = "OctetString"
_DevType_Object = MibTableColumn
devType = _DevType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 18),
    _DevType_Type()
)
devType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devType.setStatus("mandatory")


class _DevDescriptor_Type(OctetString):
    """Custom type devDescriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DevDescriptor_Type.__name__ = "OctetString"
_DevDescriptor_Object = MibTableColumn
devDescriptor = _DevDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 19),
    _DevDescriptor_Type()
)
devDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDescriptor.setStatus("mandatory")


class _ProxyControl_Type(Integer32):
    """Custom type proxyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ProxyControl_Type.__name__ = "Integer32"
_ProxyControl_Object = MibScalar
proxyControl = _ProxyControl_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 10),
    _ProxyControl_Type()
)
proxyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyControl.setStatus("mandatory")
_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 11)
)
_Gbic_ObjectIdentity = ObjectIdentity
gbic = _Gbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8)
)
_GbicTable_Object = MibTable
gbicTable = _GbicTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    gbicTable.setStatus("mandatory")
_GbicEntry_Object = MibTableRow
gbicEntry = _GbicEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1)
)
gbicEntry.setIndexNames(
    (0, "Gadz-1-MIB", "gbicDeviceIndex"),
    (0, "Gadz-1-MIB", "gbicPortIndex"),
)
if mibBuilder.loadTexts:
    gbicEntry.setStatus("mandatory")
_GbicDeviceIndex_Type = Integer32
_GbicDeviceIndex_Object = MibTableColumn
gbicDeviceIndex = _GbicDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 1),
    _GbicDeviceIndex_Type()
)
gbicDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbicDeviceIndex.setStatus("mandatory")
_GbicPortIndex_Type = Integer32
_GbicPortIndex_Object = MibTableColumn
gbicPortIndex = _GbicPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 2),
    _GbicPortIndex_Type()
)
gbicPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbicPortIndex.setStatus("mandatory")


class _GbicEntryValid_Type(Integer32):
    """Custom type gbicEntryValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_GbicEntryValid_Type.__name__ = "Integer32"
_GbicEntryValid_Object = MibTableColumn
gbicEntryValid = _GbicEntryValid_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 3),
    _GbicEntryValid_Type()
)
gbicEntryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbicEntryValid.setStatus("mandatory")


class _GbicInfo_Type(OctetString):
    """Custom type gbicInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_GbicInfo_Type.__name__ = "OctetString"
_GbicInfo_Object = MibTableColumn
gbicInfo = _GbicInfo_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 4),
    _GbicInfo_Type()
)
gbicInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbicInfo.setStatus("mandatory")
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 2)
)
_AreaSwitch_ObjectIdentity = ObjectIdentity
areaSwitch = _AreaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 3)
)
_ChannelAgent_ObjectIdentity = ObjectIdentity
channelAgent = _ChannelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 4)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5)
)
_TrapIPaddrTable_Object = MibTable
trapIPaddrTable = _TrapIPaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 1)
)
if mibBuilder.loadTexts:
    trapIPaddrTable.setStatus("mandatory")
_TrapIPentry_Object = MibTableRow
trapIPentry = _TrapIPentry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1)
)
trapIPentry.setIndexNames(
    (0, "Gadz-1-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    trapIPentry.setStatus("mandatory")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")
_TrapIPaddr_Type = IpAddress
_TrapIPaddr_Object = MibTableColumn
trapIPaddr = _TrapIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1, 2),
    _TrapIPaddr_Type()
)
trapIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPaddr.setStatus("mandatory")
_TrapDevID_Type = Integer32
_TrapDevID_Object = MibScalar
trapDevID = _TrapDevID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 2),
    _TrapDevID_Type()
)
trapDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevID.setStatus("mandatory")


class _TrapDevType_Type(OctetString):
    """Custom type trapDevType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TrapDevType_Type.__name__ = "OctetString"
_TrapDevType_Object = MibScalar
trapDevType = _TrapDevType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 3),
    _TrapDevType_Type()
)
trapDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevType.setStatus("mandatory")


class _TrapDevEventStatus_Type(Integer32):
    """Custom type trapDevEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TrapDevEventStatus_Type.__name__ = "Integer32"
_TrapDevEventStatus_Object = MibScalar
trapDevEventStatus = _TrapDevEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 4),
    _TrapDevEventStatus_Type()
)
trapDevEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevEventStatus.setStatus("mandatory")


class _TrapDevEnvironmentStatus_Type(OctetString):
    """Custom type trapDevEnvironmentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TrapDevEnvironmentStatus_Type.__name__ = "OctetString"
_TrapDevEnvironmentStatus_Object = MibScalar
trapDevEnvironmentStatus = _TrapDevEnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 5),
    _TrapDevEnvironmentStatus_Type()
)
trapDevEnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevEnvironmentStatus.setStatus("mandatory")


class _TrapDevPortStatus_Type(OctetString):
    """Custom type trapDevPortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_TrapDevPortStatus_Type.__name__ = "OctetString"
_TrapDevPortStatus_Object = MibScalar
trapDevPortStatus = _TrapDevPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 6),
    _TrapDevPortStatus_Type()
)
trapDevPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevPortStatus.setStatus("mandatory")


class _TrapDevPortAttributes_Type(OctetString):
    """Custom type trapDevPortAttributes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_TrapDevPortAttributes_Type.__name__ = "OctetString"
_TrapDevPortAttributes_Object = MibScalar
trapDevPortAttributes = _TrapDevPortAttributes_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 7),
    _TrapDevPortAttributes_Type()
)
trapDevPortAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevPortAttributes.setStatus("mandatory")


class _TrapDevConfigStatus_Type(OctetString):
    """Custom type trapDevConfigStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TrapDevConfigStatus_Type.__name__ = "OctetString"
_TrapDevConfigStatus_Object = MibScalar
trapDevConfigStatus = _TrapDevConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 8),
    _TrapDevConfigStatus_Type()
)
trapDevConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevConfigStatus.setStatus("mandatory")


class _TrapDevLIPStatus_Type(OctetString):
    """Custom type trapDevLIPStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_TrapDevLIPStatus_Type.__name__ = "OctetString"
_TrapDevLIPStatus_Object = MibScalar
trapDevLIPStatus = _TrapDevLIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 9),
    _TrapDevLIPStatus_Type()
)
trapDevLIPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDevLIPStatus.setStatus("mandatory")
_TrapMaxNumberTrapTargets_Type = Integer32
_TrapMaxNumberTrapTargets_Object = MibScalar
trapMaxNumberTrapTargets = _TrapMaxNumberTrapTargets_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 10),
    _TrapMaxNumberTrapTargets_Type()
)
trapMaxNumberTrapTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMaxNumberTrapTargets.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6)
)
_CapChas_ObjectIdentity = ObjectIdentity
capChas = _CapChas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1)
)
_CapChasTable_Object = MibTable
capChasTable = _CapChasTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    capChasTable.setStatus("mandatory")
_CapChasEntry_Object = MibTableRow
capChasEntry = _CapChasEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1)
)
capChasEntry.setIndexNames(
    (0, "Gadz-1-MIB", "capChasDeviceID"),
)
if mibBuilder.loadTexts:
    capChasEntry.setStatus("mandatory")
_CapChasDeviceID_Type = Integer32
_CapChasDeviceID_Object = MibTableColumn
capChasDeviceID = _CapChasDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 1),
    _CapChasDeviceID_Type()
)
capChasDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasDeviceID.setStatus("mandatory")


class _CapChasFeatureMask_Type(OctetString):
    """Custom type capChasFeatureMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CapChasFeatureMask_Type.__name__ = "OctetString"
_CapChasFeatureMask_Object = MibTableColumn
capChasFeatureMask = _CapChasFeatureMask_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 2),
    _CapChasFeatureMask_Type()
)
capChasFeatureMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasFeatureMask.setStatus("mandatory")


class _CapChasEventStatus_Type(OctetString):
    """Custom type capChasEventStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CapChasEventStatus_Type.__name__ = "OctetString"
_CapChasEventStatus_Object = MibTableColumn
capChasEventStatus = _CapChasEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 3),
    _CapChasEventStatus_Type()
)
capChasEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasEventStatus.setStatus("mandatory")


class _CapChasLedStatus_Type(OctetString):
    """Custom type capChasLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CapChasLedStatus_Type.__name__ = "OctetString"
_CapChasLedStatus_Object = MibTableColumn
capChasLedStatus = _CapChasLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 4),
    _CapChasLedStatus_Type()
)
capChasLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasLedStatus.setStatus("mandatory")


class _CapChasModuleStatus_Type(OctetString):
    """Custom type capChasModuleStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CapChasModuleStatus_Type.__name__ = "OctetString"
_CapChasModuleStatus_Object = MibTableColumn
capChasModuleStatus = _CapChasModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 5),
    _CapChasModuleStatus_Type()
)
capChasModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasModuleStatus.setStatus("mandatory")


class _CapChasWorldWideName_Type(OctetString):
    """Custom type capChasWorldWideName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CapChasWorldWideName_Type.__name__ = "OctetString"
_CapChasWorldWideName_Object = MibTableColumn
capChasWorldWideName = _CapChasWorldWideName_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 6),
    _CapChasWorldWideName_Type()
)
capChasWorldWideName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasWorldWideName.setStatus("mandatory")
_CapChasTemperature_Type = Integer32
_CapChasTemperature_Object = MibTableColumn
capChasTemperature = _CapChasTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 7),
    _CapChasTemperature_Type()
)
capChasTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasTemperature.setStatus("mandatory")
_CapChasTempMaxAllowed_Type = Integer32
_CapChasTempMaxAllowed_Object = MibTableColumn
capChasTempMaxAllowed = _CapChasTempMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 8),
    _CapChasTempMaxAllowed_Type()
)
capChasTempMaxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasTempMaxAllowed.setStatus("mandatory")
_CapChasTempMaxThreshold_Type = Integer32
_CapChasTempMaxThreshold_Object = MibTableColumn
capChasTempMaxThreshold = _CapChasTempMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 9),
    _CapChasTempMaxThreshold_Type()
)
capChasTempMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capChasTempMaxThreshold.setStatus("mandatory")
_CapChasSANDoctor_Type = Integer32
_CapChasSANDoctor_Object = MibTableColumn
capChasSANDoctor = _CapChasSANDoctor_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 10),
    _CapChasSANDoctor_Type()
)
capChasSANDoctor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capChasSANDoctor.setStatus("mandatory")
_CapChasSlotTable_Object = MibTable
capChasSlotTable = _CapChasSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    capChasSlotTable.setStatus("mandatory")
_CapChasSlotEntry_Object = MibTableRow
capChasSlotEntry = _CapChasSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1)
)
capChasSlotEntry.setIndexNames(
    (0, "Gadz-1-MIB", "capChasDevID"),
    (0, "Gadz-1-MIB", "capChasSlotNum"),
)
if mibBuilder.loadTexts:
    capChasSlotEntry.setStatus("mandatory")
_CapChasDevID_Type = Integer32
_CapChasDevID_Object = MibTableColumn
capChasDevID = _CapChasDevID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 1),
    _CapChasDevID_Type()
)
capChasDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasDevID.setStatus("mandatory")


class _CapChasSlotNum_Type(Integer32):
    """Custom type capChasSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CapChasSlotNum_Type.__name__ = "Integer32"
_CapChasSlotNum_Object = MibTableColumn
capChasSlotNum = _CapChasSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 2),
    _CapChasSlotNum_Type()
)
capChasSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasSlotNum.setStatus("mandatory")
_CapChasPimDevID_Type = Integer32
_CapChasPimDevID_Object = MibTableColumn
capChasPimDevID = _CapChasPimDevID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 3),
    _CapChasPimDevID_Type()
)
capChasPimDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasPimDevID.setStatus("mandatory")


class _CapSlotPimType_Type(OctetString):
    """Custom type capSlotPimType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CapSlotPimType_Type.__name__ = "OctetString"
_CapSlotPimType_Object = MibTableColumn
capSlotPimType = _CapSlotPimType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 4),
    _CapSlotPimType_Type()
)
capSlotPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSlotPimType.setStatus("mandatory")


class _CapSlotPimStatus_Type(Integer32):
    """Custom type capSlotPimStatus based on Integer32"""
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
        *(("empty", 1),
          ("present-and-active", 2),
          ("present-but-inactive", 3),
          ("unknown", 0))
    )


_CapSlotPimStatus_Type.__name__ = "Integer32"
_CapSlotPimStatus_Object = MibTableColumn
capSlotPimStatus = _CapSlotPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 5),
    _CapSlotPimStatus_Type()
)
capSlotPimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSlotPimStatus.setStatus("mandatory")
_CapSlotPimIPaddr_Type = IpAddress
_CapSlotPimIPaddr_Object = MibTableColumn
capSlotPimIPaddr = _CapSlotPimIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 6),
    _CapSlotPimIPaddr_Type()
)
capSlotPimIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSlotPimIPaddr.setStatus("mandatory")
_CapPim_ObjectIdentity = ObjectIdentity
capPim = _CapPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2)
)
_CapPimTable_Object = MibTable
capPimTable = _CapPimTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    capPimTable.setStatus("mandatory")
_CapPimEntry_Object = MibTableRow
capPimEntry = _CapPimEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1)
)
capPimEntry.setIndexNames(
    (0, "Gadz-1-MIB", "capPimDeviceID"),
)
if mibBuilder.loadTexts:
    capPimEntry.setStatus("mandatory")
_CapPimDeviceID_Type = Integer32
_CapPimDeviceID_Object = MibTableColumn
capPimDeviceID = _CapPimDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 1),
    _CapPimDeviceID_Type()
)
capPimDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimDeviceID.setStatus("mandatory")


class _CapPimFeatureMask_Type(OctetString):
    """Custom type capPimFeatureMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CapPimFeatureMask_Type.__name__ = "OctetString"
_CapPimFeatureMask_Object = MibTableColumn
capPimFeatureMask = _CapPimFeatureMask_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 2),
    _CapPimFeatureMask_Type()
)
capPimFeatureMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimFeatureMask.setStatus("mandatory")


class _CapPimEventStatus_Type(OctetString):
    """Custom type capPimEventStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CapPimEventStatus_Type.__name__ = "OctetString"
_CapPimEventStatus_Object = MibTableColumn
capPimEventStatus = _CapPimEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 3),
    _CapPimEventStatus_Type()
)
capPimEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimEventStatus.setStatus("mandatory")


class _CapPimLedStatus_Type(OctetString):
    """Custom type capPimLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CapPimLedStatus_Type.__name__ = "OctetString"
_CapPimLedStatus_Object = MibTableColumn
capPimLedStatus = _CapPimLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 4),
    _CapPimLedStatus_Type()
)
capPimLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimLedStatus.setStatus("mandatory")


class _CapPimPortAttributes_Type(OctetString):
    """Custom type capPimPortAttributes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CapPimPortAttributes_Type.__name__ = "OctetString"
_CapPimPortAttributes_Object = MibTableColumn
capPimPortAttributes = _CapPimPortAttributes_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 5),
    _CapPimPortAttributes_Type()
)
capPimPortAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimPortAttributes.setStatus("mandatory")


class _CapPimPortStatus_Type(OctetString):
    """Custom type capPimPortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CapPimPortStatus_Type.__name__ = "OctetString"
_CapPimPortStatus_Object = MibTableColumn
capPimPortStatus = _CapPimPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 6),
    _CapPimPortStatus_Type()
)
capPimPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimPortStatus.setStatus("mandatory")
_CapPortTable_Object = MibTable
capPortTable = _CapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    capPortTable.setStatus("mandatory")
_CapPortEntry_Object = MibTableRow
capPortEntry = _CapPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1)
)
capPortEntry.setIndexNames(
    (0, "Gadz-1-MIB", "capPortDeviceID"),
    (0, "Gadz-1-MIB", "capPortIndex"),
)
if mibBuilder.loadTexts:
    capPortEntry.setStatus("mandatory")
_CapPortDeviceID_Type = Integer32
_CapPortDeviceID_Object = MibTableColumn
capPortDeviceID = _CapPortDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 1),
    _CapPortDeviceID_Type()
)
capPortDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortDeviceID.setStatus("mandatory")
_CapPortIndex_Type = Integer32
_CapPortIndex_Object = MibTableColumn
capPortIndex = _CapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 2),
    _CapPortIndex_Type()
)
capPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortIndex.setStatus("mandatory")
_CapPortType_Type = Integer32
_CapPortType_Object = MibTableColumn
capPortType = _CapPortType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 3),
    _CapPortType_Type()
)
capPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capPortType.setStatus("mandatory")
_CapPortForcedBypass_Type = Integer32
_CapPortForcedBypass_Object = MibTableColumn
capPortForcedBypass = _CapPortForcedBypass_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 4),
    _CapPortForcedBypass_Type()
)
capPortForcedBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capPortForcedBypass.setStatus("mandatory")
_CapPortLipType_Type = Integer32
_CapPortLipType_Object = MibTableColumn
capPortLipType = _CapPortLipType_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 5),
    _CapPortLipType_Type()
)
capPortLipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capPortLipType.setStatus("mandatory")
_CapPortAlpaCount_Type = Integer32
_CapPortAlpaCount_Object = MibTableColumn
capPortAlpaCount = _CapPortAlpaCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 6),
    _CapPortAlpaCount_Type()
)
capPortAlpaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortAlpaCount.setStatus("mandatory")


class _CapPortAlpaBitmap_Type(OctetString):
    """Custom type capPortAlpaBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CapPortAlpaBitmap_Type.__name__ = "OctetString"
_CapPortAlpaBitmap_Object = MibTableColumn
capPortAlpaBitmap = _CapPortAlpaBitmap_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 7),
    _CapPortAlpaBitmap_Type()
)
capPortAlpaBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortAlpaBitmap.setStatus("mandatory")
_CapPortLipInitiatorCount_Type = Integer32
_CapPortLipInitiatorCount_Object = MibTableColumn
capPortLipInitiatorCount = _CapPortLipInitiatorCount_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 8),
    _CapPortLipInitiatorCount_Type()
)
capPortLipInitiatorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortLipInitiatorCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapLIPStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 0, 1)
)
trapLIPStatus.setObjects(
      *(("Gadz-1-MIB", "trapDevID"),
        ("Gadz-1-MIB", "trapDevType"),
        ("Gadz-1-MIB", "trapDevLIPStatus"))
)
if mibBuilder.loadTexts:
    trapLIPStatus.setStatus(
        ""
    )

trapMgmtTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 0, 2)
)
trapMgmtTopologyChange.setObjects(
      *(("Gadz-1-MIB", "trapDevID"),
        ("Gadz-1-MIB", "trapDevType"))
)
if mibBuilder.loadTexts:
    trapMgmtTopologyChange.setStatus(
        ""
    )

trapEnvironment = NotificationType(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 0, 3)
)
trapEnvironment.setObjects(
      *(("Gadz-1-MIB", "trapDevID"),
        ("Gadz-1-MIB", "trapDevType"),
        ("Gadz-1-MIB", "trapDevEnvironmentStatus"))
)
if mibBuilder.loadTexts:
    trapEnvironment.setStatus(
        ""
    )

trapPortStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 0, 4)
)
trapPortStatus.setObjects(
      *(("Gadz-1-MIB", "trapDevID"),
        ("Gadz-1-MIB", "trapDevType"),
        ("Gadz-1-MIB", "trapDevPortStatus"),
        ("Gadz-1-MIB", "trapDevPortAttributes"))
)
if mibBuilder.loadTexts:
    trapPortStatus.setStatus(
        ""
    )

trapConfigurationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 0, 5)
)
trapConfigurationStatus.setObjects(
      *(("Gadz-1-MIB", "trapDevID"),
        ("Gadz-1-MIB", "trapDevType"),
        ("Gadz-1-MIB", "trapDevConfigStatus"))
)
if mibBuilder.loadTexts:
    trapConfigurationStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Gadz-1-MIB",
    **{"gadzoox": gadzoox,
       "netMgmt": netMgmt,
       "common": common,
       "system": system,
       "sysReset": sysReset,
       "sysDiagnostic": sysDiagnostic,
       "zoning": zoning,
       "nlZoningPolicyControlOwner": nlZoningPolicyControlOwner,
       "nlZoningPolicyTimeout": nlZoningPolicyTimeout,
       "nlZoningPolicyStatus": nlZoningPolicyStatus,
       "nlZoningPolicyControl": nlZoningPolicyControl,
       "nlZoningPolicyLastError": nlZoningPolicyLastError,
       "nlPendingZoneCount": nlPendingZoneCount,
       "nlPendingZoneTable": nlPendingZoneTable,
       "nlPendingZoneEntry": nlPendingZoneEntry,
       "nlPendingZoneIndex": nlPendingZoneIndex,
       "nlPendingZoneName": nlPendingZoneName,
       "nlPendingZoneType": nlPendingZoneType,
       "nlPendingZoneMembers": nlPendingZoneMembers,
       "nlPendingZoneLipToZonePolicy": nlPendingZoneLipToZonePolicy,
       "nlPendingZoneMemberCount": nlPendingZoneMemberCount,
       "nlPendingZoneMemberTable": nlPendingZoneMemberTable,
       "nlPendingZoneMemberEntry": nlPendingZoneMemberEntry,
       "nlPendingZoneMemberIndex": nlPendingZoneMemberIndex,
       "nlPendingZoneMemberName": nlPendingZoneMemberName,
       "nlPendingZoneMemberType": nlPendingZoneMemberType,
       "nlPendingZoneMemberID": nlPendingZoneMemberID,
       "nlActiveZoneCount": nlActiveZoneCount,
       "nlActiveZoneTable": nlActiveZoneTable,
       "nlActiveZoneEntry": nlActiveZoneEntry,
       "nlActiveZoneIndex": nlActiveZoneIndex,
       "nlActiveZoneName": nlActiveZoneName,
       "nlActiveZoneType": nlActiveZoneType,
       "nlActiveZoneAddressSpace": nlActiveZoneAddressSpace,
       "nlActiveZoneMembers": nlActiveZoneMembers,
       "nlActiveZoneLipToZonePolicy": nlActiveZoneLipToZonePolicy,
       "nlActiveZoneMemberCount": nlActiveZoneMemberCount,
       "nlActiveZoneMemberTable": nlActiveZoneMemberTable,
       "nlActiveZoneMemberEntry": nlActiveZoneMemberEntry,
       "nlActiveZoneMemberIndex": nlActiveZoneMemberIndex,
       "nlActiveZoneMemberName": nlActiveZoneMemberName,
       "nlActiveZoneMemberType": nlActiveZoneMemberType,
       "nlActiveZoneMemberID": nlActiveZoneMemberID,
       "download": download,
       "downloadFile": downloadFile,
       "downloadBootFile": downloadBootFile,
       "downloadTFTPServer": downloadTFTPServer,
       "downloadTargetID": downloadTargetID,
       "downloadAction": downloadAction,
       "downloadStatus": downloadStatus,
       "downloadRetry": downloadRetry,
       "downloadTimeOut": downloadTimeOut,
       "downloadCfgFileFileName": downloadCfgFileFileName,
       "downloadCfgFileServerIp": downloadCfgFileServerIp,
       "downloadCfgFileAction": downloadCfgFileAction,
       "downloadCfgFileBkupStatus": downloadCfgFileBkupStatus,
       "security": security,
       "discovery": discovery,
       "monitor": monitor,
       "proxy": proxy,
       "proxyMaxMembers": proxyMaxMembers,
       "proxyCurMembers": proxyCurMembers,
       "proxyChanges": proxyChanges,
       "proxyBoardID": proxyBoardID,
       "proxyFirmwareVersion": proxyFirmwareVersion,
       "proxyTopologyCRC": proxyTopologyCRC,
       "proxyEventStatus": proxyEventStatus,
       "proxyDeviceEventInd": proxyDeviceEventInd,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "devDeviceID": devDeviceID,
       "devOID": devOID,
       "devProductID": devProductID,
       "devBoardID": devBoardID,
       "devFirmwareVersion": devFirmwareVersion,
       "devEventStatus": devEventStatus,
       "devReset": devReset,
       "devDiagnostic": devDiagnostic,
       "devSysUpTimestamp": devSysUpTimestamp,
       "devCumulativeUpTime": devCumulativeUpTime,
       "devContact": devContact,
       "devLocation": devLocation,
       "devTopologyLink": devTopologyLink,
       "devBeaconOnTime": devBeaconOnTime,
       "devBeaconOffTime": devBeaconOffTime,
       "devFaultLedState": devFaultLedState,
       "devNumPorts": devNumPorts,
       "devType": devType,
       "devDescriptor": devDescriptor,
       "proxyControl": proxyControl,
       "policy": policy,
       "gbic": gbic,
       "gbicTable": gbicTable,
       "gbicEntry": gbicEntry,
       "gbicDeviceIndex": gbicDeviceIndex,
       "gbicPortIndex": gbicPortIndex,
       "gbicEntryValid": gbicEntryValid,
       "gbicInfo": gbicInfo,
       "hub": hub,
       "areaSwitch": areaSwitch,
       "channelAgent": channelAgent,
       "traps": traps,
       "trapIPaddrTable": trapIPaddrTable,
       "trapIPentry": trapIPentry,
       "trapIndex": trapIndex,
       "trapIPaddr": trapIPaddr,
       "trapDevID": trapDevID,
       "trapDevType": trapDevType,
       "trapDevEventStatus": trapDevEventStatus,
       "trapDevEnvironmentStatus": trapDevEnvironmentStatus,
       "trapDevPortStatus": trapDevPortStatus,
       "trapDevPortAttributes": trapDevPortAttributes,
       "trapDevConfigStatus": trapDevConfigStatus,
       "trapDevLIPStatus": trapDevLIPStatus,
       "trapMaxNumberTrapTargets": trapMaxNumberTrapTargets,
       "switch": switch,
       "capChas": capChas,
       "trapLIPStatus": trapLIPStatus,
       "trapMgmtTopologyChange": trapMgmtTopologyChange,
       "trapEnvironment": trapEnvironment,
       "trapPortStatus": trapPortStatus,
       "trapConfigurationStatus": trapConfigurationStatus,
       "capChasTable": capChasTable,
       "capChasEntry": capChasEntry,
       "capChasDeviceID": capChasDeviceID,
       "capChasFeatureMask": capChasFeatureMask,
       "capChasEventStatus": capChasEventStatus,
       "capChasLedStatus": capChasLedStatus,
       "capChasModuleStatus": capChasModuleStatus,
       "capChasWorldWideName": capChasWorldWideName,
       "capChasTemperature": capChasTemperature,
       "capChasTempMaxAllowed": capChasTempMaxAllowed,
       "capChasTempMaxThreshold": capChasTempMaxThreshold,
       "capChasSANDoctor": capChasSANDoctor,
       "capChasSlotTable": capChasSlotTable,
       "capChasSlotEntry": capChasSlotEntry,
       "capChasDevID": capChasDevID,
       "capChasSlotNum": capChasSlotNum,
       "capChasPimDevID": capChasPimDevID,
       "capSlotPimType": capSlotPimType,
       "capSlotPimStatus": capSlotPimStatus,
       "capSlotPimIPaddr": capSlotPimIPaddr,
       "capPim": capPim,
       "capPimTable": capPimTable,
       "capPimEntry": capPimEntry,
       "capPimDeviceID": capPimDeviceID,
       "capPimFeatureMask": capPimFeatureMask,
       "capPimEventStatus": capPimEventStatus,
       "capPimLedStatus": capPimLedStatus,
       "capPimPortAttributes": capPimPortAttributes,
       "capPimPortStatus": capPimPortStatus,
       "capPortTable": capPortTable,
       "capPortEntry": capPortEntry,
       "capPortDeviceID": capPortDeviceID,
       "capPortIndex": capPortIndex,
       "capPortType": capPortType,
       "capPortForcedBypass": capPortForcedBypass,
       "capPortLipType": capPortLipType,
       "capPortAlpaCount": capPortAlpaCount,
       "capPortAlpaBitmap": capPortAlpaBitmap,
       "capPortLipInitiatorCount": capPortLipInitiatorCount}
)
