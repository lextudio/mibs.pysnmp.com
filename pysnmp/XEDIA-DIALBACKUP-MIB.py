# SNMP MIB module (XEDIA-DIALBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-DIALBACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:46 2024
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

xediaDialBackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DialBackupObjects_ObjectIdentity = ObjectIdentity
dialBackupObjects = _DialBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1)
)
_DialBackupConfigurationTable_Object = MibTable
dialBackupConfigurationTable = _DialBackupConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1)
)
if mibBuilder.loadTexts:
    dialBackupConfigurationTable.setStatus("current")
_DialBackupConfigurationEntry_Object = MibTableRow
dialBackupConfigurationEntry = _DialBackupConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1)
)
dialBackupConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dialBackupConfigurationEntry.setStatus("current")


class _DialBackupPrimaryInterface_Type(DisplayString):
    """Custom type dialBackupPrimaryInterface based on DisplayString"""
    defaultValue = OctetString("none")


_DialBackupPrimaryInterface_Object = MibTableColumn
dialBackupPrimaryInterface = _DialBackupPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 1),
    _DialBackupPrimaryInterface_Type()
)
dialBackupPrimaryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialBackupPrimaryInterface.setStatus("current")


class _DialBackupFailoverTime_Type(Integer32):
    """Custom type dialBackupFailoverTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialBackupFailoverTime_Type.__name__ = "Integer32"
_DialBackupFailoverTime_Object = MibTableColumn
dialBackupFailoverTime = _DialBackupFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 2),
    _DialBackupFailoverTime_Type()
)
dialBackupFailoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialBackupFailoverTime.setStatus("current")
if mibBuilder.loadTexts:
    dialBackupFailoverTime.setUnits("seconds")


class _DialBackupFailbackTime_Type(Integer32):
    """Custom type dialBackupFailbackTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialBackupFailbackTime_Type.__name__ = "Integer32"
_DialBackupFailbackTime_Object = MibTableColumn
dialBackupFailbackTime = _DialBackupFailbackTime_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 3),
    _DialBackupFailbackTime_Type()
)
dialBackupFailbackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialBackupFailbackTime.setStatus("current")
if mibBuilder.loadTexts:
    dialBackupFailbackTime.setUnits("seconds")


class _DialBackupStatus_Type(Integer32):
    """Custom type dialBackupStatus based on Integer32"""
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


_DialBackupStatus_Type.__name__ = "Integer32"
_DialBackupStatus_Object = MibTableColumn
dialBackupStatus = _DialBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 4),
    _DialBackupStatus_Type()
)
dialBackupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialBackupStatus.setStatus("current")
_DialBackupConformance_ObjectIdentity = ObjectIdentity
dialBackupConformance = _DialBackupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 2)
)
_DialBackupCompliances_ObjectIdentity = ObjectIdentity
dialBackupCompliances = _DialBackupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 1)
)
_DialBackupGroups_ObjectIdentity = ObjectIdentity
dialBackupGroups = _DialBackupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 2)
)

# Managed Objects groups

dialBackupAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 2, 1)
)
dialBackupAllGroup.setObjects(
      *(("XEDIA-DIALBACKUP-MIB", "dialBackupPrimaryInterface"),
        ("XEDIA-DIALBACKUP-MIB", "dialBackupFailoverTime"),
        ("XEDIA-DIALBACKUP-MIB", "dialBackupFailbackTime"),
        ("XEDIA-DIALBACKUP-MIB", "dialBackupStatus"))
)
if mibBuilder.loadTexts:
    dialBackupAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dialBackupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dialBackupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-DIALBACKUP-MIB",
    **{"xediaDialBackupMIB": xediaDialBackupMIB,
       "dialBackupObjects": dialBackupObjects,
       "dialBackupConfigurationTable": dialBackupConfigurationTable,
       "dialBackupConfigurationEntry": dialBackupConfigurationEntry,
       "dialBackupPrimaryInterface": dialBackupPrimaryInterface,
       "dialBackupFailoverTime": dialBackupFailoverTime,
       "dialBackupFailbackTime": dialBackupFailbackTime,
       "dialBackupStatus": dialBackupStatus,
       "dialBackupConformance": dialBackupConformance,
       "dialBackupCompliances": dialBackupCompliances,
       "dialBackupCompliance": dialBackupCompliance,
       "dialBackupGroups": dialBackupGroups,
       "dialBackupAllGroup": dialBackupAllGroup}
)
