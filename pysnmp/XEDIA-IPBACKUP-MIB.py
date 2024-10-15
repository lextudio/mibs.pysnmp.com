# SNMP MIB module (XEDIA-IPBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-IPBACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaIpBackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BackupId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_XipbackupObjects_ObjectIdentity = ObjectIdentity
xipbackupObjects = _XipbackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1)
)
_XipbackupGeneral_ObjectIdentity = ObjectIdentity
xipbackupGeneral = _XipbackupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1)
)


class _XipbackupAdminStatus_Type(Integer32):
    """Custom type xipbackupAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XipbackupAdminStatus_Type.__name__ = "Integer32"
_XipbackupAdminStatus_Object = MibScalar
xipbackupAdminStatus = _XipbackupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 1),
    _XipbackupAdminStatus_Type()
)
xipbackupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xipbackupAdminStatus.setStatus("current")


class _XipbackupBridgeAdminStatus_Type(Integer32):
    """Custom type xipbackupBridgeAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XipbackupBridgeAdminStatus_Type.__name__ = "Integer32"
_XipbackupBridgeAdminStatus_Object = MibScalar
xipbackupBridgeAdminStatus = _XipbackupBridgeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 2),
    _XipbackupBridgeAdminStatus_Type()
)
xipbackupBridgeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xipbackupBridgeAdminStatus.setStatus("current")
_XipbackupInstTable_Object = MibTable
xipbackupInstTable = _XipbackupInstTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2)
)
if mibBuilder.loadTexts:
    xipbackupInstTable.setStatus("current")
_XipbackupInstEntry_Object = MibTableRow
xipbackupInstEntry = _XipbackupInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1)
)
xipbackupInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XEDIA-IPBACKUP-MIB", "xipbackupInstId"),
)
if mibBuilder.loadTexts:
    xipbackupInstEntry.setStatus("current")
_XipbackupInstId_Type = BackupId
_XipbackupInstId_Object = MibTableColumn
xipbackupInstId = _XipbackupInstId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 1),
    _XipbackupInstId_Type()
)
xipbackupInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xipbackupInstId.setStatus("current")


class _XipbackupInstTrackIp_Type(IpAddress):
    """Custom type xipbackupInstTrackIp based on IpAddress"""
    defaultValue = 0


_XipbackupInstTrackIp_Object = MibTableColumn
xipbackupInstTrackIp = _XipbackupInstTrackIp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 2),
    _XipbackupInstTrackIp_Type()
)
xipbackupInstTrackIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xipbackupInstTrackIp.setStatus("current")


class _XipbackupInstInitializeCode_Type(Integer32):
    """Custom type xipbackupInstInitializeCode based on Integer32"""
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
        *(("bridgeDown", 9),
          ("globalDisabled", 2),
          ("instanceDisabled", 3),
          ("interfaceDown", 8),
          ("noAddressOnSubnet", 6),
          ("noAssociatedIpAddr", 5),
          ("ready", 1),
          ("rowStatusNotActive", 4),
          ("trackedIpDown", 7))
    )


_XipbackupInstInitializeCode_Type.__name__ = "Integer32"
_XipbackupInstInitializeCode_Object = MibTableColumn
xipbackupInstInitializeCode = _XipbackupInstInitializeCode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 3),
    _XipbackupInstInitializeCode_Type()
)
xipbackupInstInitializeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xipbackupInstInitializeCode.setStatus("current")
_XipbackupConformance_ObjectIdentity = ObjectIdentity
xipbackupConformance = _XipbackupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 2)
)
_XipbackupCompliances_ObjectIdentity = ObjectIdentity
xipbackupCompliances = _XipbackupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1)
)
_XipbackupGroups_ObjectIdentity = ObjectIdentity
xipbackupGroups = _XipbackupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2)
)

# Managed Objects groups

xipbackupAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2, 1)
)
xipbackupAllGroup.setObjects(
      *(("XEDIA-IPBACKUP-MIB", "xipbackupAdminStatus"),
        ("XEDIA-IPBACKUP-MIB", "xipbackupBridgeAdminStatus"),
        ("XEDIA-IPBACKUP-MIB", "xipbackupInstTrackIp"),
        ("XEDIA-IPBACKUP-MIB", "xipbackupInstInitializeCode"))
)
if mibBuilder.loadTexts:
    xipbackupAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xipbackupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xipbackupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-IPBACKUP-MIB",
    **{"BackupId": BackupId,
       "xediaIpBackupMIB": xediaIpBackupMIB,
       "xipbackupObjects": xipbackupObjects,
       "xipbackupGeneral": xipbackupGeneral,
       "xipbackupAdminStatus": xipbackupAdminStatus,
       "xipbackupBridgeAdminStatus": xipbackupBridgeAdminStatus,
       "xipbackupInstTable": xipbackupInstTable,
       "xipbackupInstEntry": xipbackupInstEntry,
       "xipbackupInstId": xipbackupInstId,
       "xipbackupInstTrackIp": xipbackupInstTrackIp,
       "xipbackupInstInitializeCode": xipbackupInstInitializeCode,
       "xipbackupConformance": xipbackupConformance,
       "xipbackupCompliances": xipbackupCompliances,
       "xipbackupCompliance": xipbackupCompliance,
       "xipbackupGroups": xipbackupGroups,
       "xipbackupAllGroup": xipbackupAllGroup}
)
