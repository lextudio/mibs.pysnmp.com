# SNMP MIB module (INTEL-IPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-IPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:47 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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



class UserGroupSet(OctetString):
    """Custom type UserGroupSet based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipf_ObjectIdentity = ObjectIdentity
ipf = _Ipf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 34)
)
_IpfUGs_ObjectIdentity = ObjectIdentity
ipfUGs = _IpfUGs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 1)
)
_IpfUGsTable_Object = MibTable
ipfUGsTable = _IpfUGsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1)
)
if mibBuilder.loadTexts:
    ipfUGsTable.setStatus("mandatory")
_IpfUGsEntry_Object = MibTableRow
ipfUGsEntry = _IpfUGsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1)
)
ipfUGsEntry.setIndexNames(
    (0, "INTEL-IPF-MIB", "ipfUGsNumber"),
)
if mibBuilder.loadTexts:
    ipfUGsEntry.setStatus("mandatory")
_IpfUGsNumber_Type = Integer32
_IpfUGsNumber_Object = MibTableColumn
ipfUGsNumber = _IpfUGsNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 1),
    _IpfUGsNumber_Type()
)
ipfUGsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfUGsNumber.setStatus("mandatory")


class _IpfUGsName_Type(DisplayString):
    """Custom type ipfUGsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpfUGsName_Type.__name__ = "DisplayString"
_IpfUGsName_Object = MibTableColumn
ipfUGsName = _IpfUGsName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 2),
    _IpfUGsName_Type()
)
ipfUGsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfUGsName.setStatus("mandatory")
_IpfL3UGM_ObjectIdentity = ObjectIdentity
ipfL3UGM = _IpfL3UGM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2)
)
_IpfL3UGMTable_Object = MibTable
ipfL3UGMTable = _IpfL3UGMTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1)
)
if mibBuilder.loadTexts:
    ipfL3UGMTable.setStatus("mandatory")
_IpfL3UGMEntry_Object = MibTableRow
ipfL3UGMEntry = _IpfL3UGMEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1)
)
ipfL3UGMEntry.setIndexNames(
    (0, "INTEL-IPF-MIB", "ipfL3UGMIpAddress"),
)
if mibBuilder.loadTexts:
    ipfL3UGMEntry.setStatus("mandatory")
_IpfL3UGMIpAddress_Type = IpAddress
_IpfL3UGMIpAddress_Object = MibTableColumn
ipfL3UGMIpAddress = _IpfL3UGMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 1),
    _IpfL3UGMIpAddress_Type()
)
ipfL3UGMIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfL3UGMIpAddress.setStatus("mandatory")
_IpfL3UGMSubnetMask_Type = IpAddress
_IpfL3UGMSubnetMask_Object = MibTableColumn
ipfL3UGMSubnetMask = _IpfL3UGMSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 2),
    _IpfL3UGMSubnetMask_Type()
)
ipfL3UGMSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfL3UGMSubnetMask.setStatus("mandatory")
_IpfL3UGMUserGroups_Type = UserGroupSet
_IpfL3UGMUserGroups_Object = MibTableColumn
ipfL3UGMUserGroups = _IpfL3UGMUserGroups_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 3),
    _IpfL3UGMUserGroups_Type()
)
ipfL3UGMUserGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfL3UGMUserGroups.setStatus("mandatory")
_IpfL4UGM_ObjectIdentity = ObjectIdentity
ipfL4UGM = _IpfL4UGM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 3)
)
_IpfL4UGMTable_Object = MibTable
ipfL4UGMTable = _IpfL4UGMTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1)
)
if mibBuilder.loadTexts:
    ipfL4UGMTable.setStatus("mandatory")
_IpfL4UGMEntry_Object = MibTableRow
ipfL4UGMEntry = _IpfL4UGMEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1)
)
ipfL4UGMEntry.setIndexNames(
    (0, "INTEL-IPF-MIB", "ipfL4UGMPortNumber"),
)
if mibBuilder.loadTexts:
    ipfL4UGMEntry.setStatus("mandatory")
_IpfL4UGMPortNumber_Type = Integer32
_IpfL4UGMPortNumber_Object = MibTableColumn
ipfL4UGMPortNumber = _IpfL4UGMPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 1),
    _IpfL4UGMPortNumber_Type()
)
ipfL4UGMPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfL4UGMPortNumber.setStatus("mandatory")
_IpfL4UGMUserGroups_Type = UserGroupSet
_IpfL4UGMUserGroups_Object = MibTableColumn
ipfL4UGMUserGroups = _IpfL4UGMUserGroups_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 2),
    _IpfL4UGMUserGroups_Type()
)
ipfL4UGMUserGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfL4UGMUserGroups.setStatus("mandatory")
_IpfInfo_ObjectIdentity = ObjectIdentity
ipfInfo = _IpfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4)
)
_IpfInfoL3Rejects_Type = Counter32
_IpfInfoL3Rejects_Object = MibScalar
ipfInfoL3Rejects = _IpfInfoL3Rejects_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 1),
    _IpfInfoL3Rejects_Type()
)
ipfInfoL3Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInfoL3Rejects.setStatus("mandatory")
_IpfInfoL4Rejects_Type = Counter32
_IpfInfoL4Rejects_Object = MibScalar
ipfInfoL4Rejects = _IpfInfoL4Rejects_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 2),
    _IpfInfoL4Rejects_Type()
)
ipfInfoL4Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInfoL4Rejects.setStatus("mandatory")
_IpfInfoMostRecentChange_Type = TimeTicks
_IpfInfoMostRecentChange_Object = MibScalar
ipfInfoMostRecentChange = _IpfInfoMostRecentChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 3),
    _IpfInfoMostRecentChange_Type()
)
ipfInfoMostRecentChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInfoMostRecentChange.setStatus("mandatory")


class _IpfInfoOnOffSwitch_Type(Integer32):
    """Custom type ipfInfoOnOffSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpfInfoOnOffSwitch_Type.__name__ = "Integer32"
_IpfInfoOnOffSwitch_Object = MibScalar
ipfInfoOnOffSwitch = _IpfInfoOnOffSwitch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 4),
    _IpfInfoOnOffSwitch_Type()
)
ipfInfoOnOffSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfInfoOnOffSwitch.setStatus("mandatory")
_IpfInfoDeleteUserGroup_Type = Integer32
_IpfInfoDeleteUserGroup_Object = MibScalar
ipfInfoDeleteUserGroup = _IpfInfoDeleteUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 5),
    _IpfInfoDeleteUserGroup_Type()
)
ipfInfoDeleteUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfInfoDeleteUserGroup.setStatus("mandatory")
_IpfInfoDeleteL3UGM_Type = IpAddress
_IpfInfoDeleteL3UGM_Object = MibScalar
ipfInfoDeleteL3UGM = _IpfInfoDeleteL3UGM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 6),
    _IpfInfoDeleteL3UGM_Type()
)
ipfInfoDeleteL3UGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfInfoDeleteL3UGM.setStatus("mandatory")
_IpfInfoDeleteL4UGM_Type = Integer32
_IpfInfoDeleteL4UGM_Object = MibScalar
ipfInfoDeleteL4UGM = _IpfInfoDeleteL4UGM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 7),
    _IpfInfoDeleteL4UGM_Type()
)
ipfInfoDeleteL4UGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfInfoDeleteL4UGM.setStatus("mandatory")


class _IpfInfoCreateDeleteStatus_Type(Integer32):
    """Custom type ipfInfoCreateDeleteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createTableFull", 2),
          ("deleteNotFound", 3),
          ("ok", 1))
    )


_IpfInfoCreateDeleteStatus_Type.__name__ = "Integer32"
_IpfInfoCreateDeleteStatus_Object = MibScalar
ipfInfoCreateDeleteStatus = _IpfInfoCreateDeleteStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 8),
    _IpfInfoCreateDeleteStatus_Type()
)
ipfInfoCreateDeleteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInfoCreateDeleteStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-IPF-MIB",
    **{"UserGroupSet": UserGroupSet,
       "ipf": ipf,
       "ipfUGs": ipfUGs,
       "ipfUGsTable": ipfUGsTable,
       "ipfUGsEntry": ipfUGsEntry,
       "ipfUGsNumber": ipfUGsNumber,
       "ipfUGsName": ipfUGsName,
       "ipfL3UGM": ipfL3UGM,
       "ipfL3UGMTable": ipfL3UGMTable,
       "ipfL3UGMEntry": ipfL3UGMEntry,
       "ipfL3UGMIpAddress": ipfL3UGMIpAddress,
       "ipfL3UGMSubnetMask": ipfL3UGMSubnetMask,
       "ipfL3UGMUserGroups": ipfL3UGMUserGroups,
       "ipfL4UGM": ipfL4UGM,
       "ipfL4UGMTable": ipfL4UGMTable,
       "ipfL4UGMEntry": ipfL4UGMEntry,
       "ipfL4UGMPortNumber": ipfL4UGMPortNumber,
       "ipfL4UGMUserGroups": ipfL4UGMUserGroups,
       "ipfInfo": ipfInfo,
       "ipfInfoL3Rejects": ipfInfoL3Rejects,
       "ipfInfoL4Rejects": ipfInfoL4Rejects,
       "ipfInfoMostRecentChange": ipfInfoMostRecentChange,
       "ipfInfoOnOffSwitch": ipfInfoOnOffSwitch,
       "ipfInfoDeleteUserGroup": ipfInfoDeleteUserGroup,
       "ipfInfoDeleteL3UGM": ipfInfoDeleteL3UGM,
       "ipfInfoDeleteL4UGM": ipfInfoDeleteL4UGM,
       "ipfInfoCreateDeleteStatus": ipfInfoCreateDeleteStatus}
)
