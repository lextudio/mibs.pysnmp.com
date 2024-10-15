# SNMP MIB module (ARTEM-COMPOINT-BLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARTEM-COMPOINT-BLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:42 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

artem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4280)
)
artem.setRevisions(
        ("2005-06-10 12:17",
         "2005-05-24 13:24",
         "2005-04-29 12:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArtemBLD_ObjectIdentity = ObjectIdentity
artemBLD = _ArtemBLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 6)
)
if mibBuilder.loadTexts:
    artemBLD.setStatus("current")


class _ArtemBLDAdminStatus_Type(TruthValue):
    """Custom type artemBLDAdminStatus based on TruthValue"""


_ArtemBLDAdminStatus_Object = MibScalar
artemBLDAdminStatus = _ArtemBLDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 1),
    _ArtemBLDAdminStatus_Type()
)
artemBLDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBLDAdminStatus.setStatus("current")
_ArtemBLDLinkState_Type = TruthValue
_ArtemBLDLinkState_Object = MibScalar
artemBLDLinkState = _ArtemBLDLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 2),
    _ArtemBLDLinkState_Type()
)
artemBLDLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBLDLinkState.setStatus("current")


class _ArtemBLDTargetAddress_Type(IpAddress):
    """Custom type artemBLDTargetAddress based on IpAddress"""
    defaultHexValue = "00000000"


_ArtemBLDTargetAddress_Object = MibScalar
artemBLDTargetAddress = _ArtemBLDTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 3),
    _ArtemBLDTargetAddress_Type()
)
artemBLDTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBLDTargetAddress.setStatus("current")


class _ArtemBLDTargetIf_Type(Integer32):
    """Custom type artemBLDTargetIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtemBLDTargetIf_Type.__name__ = "Integer32"
_ArtemBLDTargetIf_Object = MibScalar
artemBLDTargetIf = _ArtemBLDTargetIf_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 4),
    _ArtemBLDTargetIf_Type()
)
artemBLDTargetIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBLDTargetIf.setStatus("current")


class _ArtemBLDCheckInterval_Type(Integer32):
    """Custom type artemBLDCheckInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ArtemBLDCheckInterval_Type.__name__ = "Integer32"
_ArtemBLDCheckInterval_Object = MibScalar
artemBLDCheckInterval = _ArtemBLDCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 5),
    _ArtemBLDCheckInterval_Type()
)
artemBLDCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBLDCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    artemBLDCheckInterval.setUnits("seconds")


class _ArtemBLDTimeout_Type(Integer32):
    """Custom type artemBLDTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ArtemBLDTimeout_Type.__name__ = "Integer32"
_ArtemBLDTimeout_Object = MibScalar
artemBLDTimeout = _ArtemBLDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 6),
    _ArtemBLDTimeout_Type()
)
artemBLDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBLDTimeout.setStatus("current")
if mibBuilder.loadTexts:
    artemBLDTimeout.setUnits("seconds")


class _ArtemBLDRetries_Type(Integer32):
    """Custom type artemBLDRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ArtemBLDRetries_Type.__name__ = "Integer32"
_ArtemBLDRetries_Object = MibScalar
artemBLDRetries = _ArtemBLDRetries_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 7),
    _ArtemBLDRetries_Type()
)
artemBLDRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBLDRetries.setStatus("current")
_ArtemBLDIfTable_Object = MibTable
artemBLDIfTable = _ArtemBLDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 8)
)
if mibBuilder.loadTexts:
    artemBLDIfTable.setStatus("current")
_ArtemBLDIfEntry_Object = MibTableRow
artemBLDIfEntry = _ArtemBLDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 8, 1)
)
artemBLDIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    artemBLDIfEntry.setStatus("current")
_ArtemBLDIfRowStatus_Type = RowStatus
_ArtemBLDIfRowStatus_Object = MibTableColumn
artemBLDIfRowStatus = _ArtemBLDIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 6, 8, 1, 1),
    _ArtemBLDIfRowStatus_Type()
)
artemBLDIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemBLDIfRowStatus.setStatus("current")
_ArtemBLDNotification_ObjectIdentity = ObjectIdentity
artemBLDNotification = _ArtemBLDNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 6, 9)
)

# Managed Objects groups

artemBLDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 6, 10)
)
artemBLDGroup.setObjects(
      *(("ARTEM-COMPOINT-BLD-MIB", "artemBLDAdminStatus"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDLinkState"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTargetAddress"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTargetIf"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDCheckInterval"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTimeout"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDRetries"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDIfRowStatus"))
)
if mibBuilder.loadTexts:
    artemBLDGroup.setStatus("current")


# Notification objects

artemBLDConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 4280, 6, 9, 1)
)
artemBLDConnection.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARTEM-COMPOINT-BLD-MIB", "artemBLDLinkState"))
)
if mibBuilder.loadTexts:
    artemBLDConnection.setStatus(
        "current"
    )


# Notifications groups

artemBLDNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4280, 6, 11)
)
artemBLDNotificationGroup.setObjects(
    ("ARTEM-COMPOINT-BLD-MIB", "artemBLDConnection")
)
if mibBuilder.loadTexts:
    artemBLDNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARTEM-COMPOINT-BLD-MIB",
    **{"artem": artem,
       "artemBLD": artemBLD,
       "artemBLDAdminStatus": artemBLDAdminStatus,
       "artemBLDLinkState": artemBLDLinkState,
       "artemBLDTargetAddress": artemBLDTargetAddress,
       "artemBLDTargetIf": artemBLDTargetIf,
       "artemBLDCheckInterval": artemBLDCheckInterval,
       "artemBLDTimeout": artemBLDTimeout,
       "artemBLDRetries": artemBLDRetries,
       "artemBLDIfTable": artemBLDIfTable,
       "artemBLDIfEntry": artemBLDIfEntry,
       "artemBLDIfRowStatus": artemBLDIfRowStatus,
       "artemBLDNotification": artemBLDNotification,
       "artemBLDConnection": artemBLDConnection,
       "artemBLDGroup": artemBLDGroup,
       "artemBLDNotificationGroup": artemBLDNotificationGroup}
)
