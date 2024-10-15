# SNMP MIB module (RADLAN-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-GVRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:22 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rlGvrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 64)
)
rlGvrp.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlPortGvrpTimersTable_Object = MibTable
rlPortGvrpTimersTable = _RlPortGvrpTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1)
)
if mibBuilder.loadTexts:
    rlPortGvrpTimersTable.setStatus("current")
_RlPortGvrpTimersEntry_Object = MibTableRow
rlPortGvrpTimersEntry = _RlPortGvrpTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1)
)
rlPortGvrpTimersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpTimersEntry.setStatus("current")


class _RlPortGvrpJoinTime_Type(TimeInterval):
    """Custom type rlPortGvrpJoinTime based on TimeInterval"""
    defaultValue = 20


_RlPortGvrpJoinTime_Object = MibTableColumn
rlPortGvrpJoinTime = _RlPortGvrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 1),
    _RlPortGvrpJoinTime_Type()
)
rlPortGvrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpJoinTime.setStatus("current")


class _RlPortGvrpLeaveTime_Type(TimeInterval):
    """Custom type rlPortGvrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_RlPortGvrpLeaveTime_Object = MibTableColumn
rlPortGvrpLeaveTime = _RlPortGvrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 2),
    _RlPortGvrpLeaveTime_Type()
)
rlPortGvrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpLeaveTime.setStatus("current")


class _RlPortGvrpLeaveAllTime_Type(TimeInterval):
    """Custom type rlPortGvrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_RlPortGvrpLeaveAllTime_Object = MibTableColumn
rlPortGvrpLeaveAllTime = _RlPortGvrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 3),
    _RlPortGvrpLeaveAllTime_Type()
)
rlPortGvrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpLeaveAllTime.setStatus("current")


class _RlPortGvrpOverrideGarp_Type(EnabledStatus):
    """Custom type rlPortGvrpOverrideGarp based on EnabledStatus"""


_RlPortGvrpOverrideGarp_Object = MibTableColumn
rlPortGvrpOverrideGarp = _RlPortGvrpOverrideGarp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 4),
    _RlPortGvrpOverrideGarp_Type()
)
rlPortGvrpOverrideGarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpOverrideGarp.setStatus("current")
_RlGvrpSupported_Type = TruthValue
_RlGvrpSupported_Object = MibScalar
rlGvrpSupported = _RlGvrpSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 2),
    _RlGvrpSupported_Type()
)
rlGvrpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGvrpSupported.setStatus("current")
_RlGvrpMibVersion_Type = Integer32
_RlGvrpMibVersion_Object = MibScalar
rlGvrpMibVersion = _RlGvrpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 3),
    _RlGvrpMibVersion_Type()
)
rlGvrpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGvrpMibVersion.setStatus("current")
_RlPortGvrpStatisticsTable_Object = MibTable
rlPortGvrpStatisticsTable = _RlPortGvrpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4)
)
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsTable.setStatus("current")
_RlPortGvrpStatisticsEntry_Object = MibTableRow
rlPortGvrpStatisticsEntry = _RlPortGvrpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1)
)
rlPortGvrpStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsEntry.setStatus("current")
_RlPortGvrpStatisticsRJE_Type = Counter32
_RlPortGvrpStatisticsRJE_Object = MibTableColumn
rlPortGvrpStatisticsRJE = _RlPortGvrpStatisticsRJE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 1),
    _RlPortGvrpStatisticsRJE_Type()
)
rlPortGvrpStatisticsRJE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRJE.setStatus("current")
_RlPortGvrpStatisticsRJIn_Type = Counter32
_RlPortGvrpStatisticsRJIn_Object = MibTableColumn
rlPortGvrpStatisticsRJIn = _RlPortGvrpStatisticsRJIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 2),
    _RlPortGvrpStatisticsRJIn_Type()
)
rlPortGvrpStatisticsRJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRJIn.setStatus("current")
_RlPortGvrpStatisticsREmp_Type = Counter32
_RlPortGvrpStatisticsREmp_Object = MibTableColumn
rlPortGvrpStatisticsREmp = _RlPortGvrpStatisticsREmp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 3),
    _RlPortGvrpStatisticsREmp_Type()
)
rlPortGvrpStatisticsREmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsREmp.setStatus("current")
_RlPortGvrpStatisticsRLIn_Type = Counter32
_RlPortGvrpStatisticsRLIn_Object = MibTableColumn
rlPortGvrpStatisticsRLIn = _RlPortGvrpStatisticsRLIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 4),
    _RlPortGvrpStatisticsRLIn_Type()
)
rlPortGvrpStatisticsRLIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLIn.setStatus("current")
_RlPortGvrpStatisticsRLE_Type = Counter32
_RlPortGvrpStatisticsRLE_Object = MibTableColumn
rlPortGvrpStatisticsRLE = _RlPortGvrpStatisticsRLE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 5),
    _RlPortGvrpStatisticsRLE_Type()
)
rlPortGvrpStatisticsRLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLE.setStatus("current")
_RlPortGvrpStatisticsRLA_Type = Counter32
_RlPortGvrpStatisticsRLA_Object = MibTableColumn
rlPortGvrpStatisticsRLA = _RlPortGvrpStatisticsRLA_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 6),
    _RlPortGvrpStatisticsRLA_Type()
)
rlPortGvrpStatisticsRLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLA.setStatus("current")
_RlPortGvrpStatisticsSJE_Type = Counter32
_RlPortGvrpStatisticsSJE_Object = MibTableColumn
rlPortGvrpStatisticsSJE = _RlPortGvrpStatisticsSJE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 7),
    _RlPortGvrpStatisticsSJE_Type()
)
rlPortGvrpStatisticsSJE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSJE.setStatus("current")
_RlPortGvrpStatisticsSJIn_Type = Counter32
_RlPortGvrpStatisticsSJIn_Object = MibTableColumn
rlPortGvrpStatisticsSJIn = _RlPortGvrpStatisticsSJIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 8),
    _RlPortGvrpStatisticsSJIn_Type()
)
rlPortGvrpStatisticsSJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSJIn.setStatus("current")
_RlPortGvrpStatisticsSEmp_Type = Counter32
_RlPortGvrpStatisticsSEmp_Object = MibTableColumn
rlPortGvrpStatisticsSEmp = _RlPortGvrpStatisticsSEmp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 9),
    _RlPortGvrpStatisticsSEmp_Type()
)
rlPortGvrpStatisticsSEmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSEmp.setStatus("current")
_RlPortGvrpStatisticsSLIn_Type = Counter32
_RlPortGvrpStatisticsSLIn_Object = MibTableColumn
rlPortGvrpStatisticsSLIn = _RlPortGvrpStatisticsSLIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 10),
    _RlPortGvrpStatisticsSLIn_Type()
)
rlPortGvrpStatisticsSLIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLIn.setStatus("current")
_RlPortGvrpStatisticsSLE_Type = Counter32
_RlPortGvrpStatisticsSLE_Object = MibTableColumn
rlPortGvrpStatisticsSLE = _RlPortGvrpStatisticsSLE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 11),
    _RlPortGvrpStatisticsSLE_Type()
)
rlPortGvrpStatisticsSLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLE.setStatus("current")
_RlPortGvrpStatisticsSLA_Type = Counter32
_RlPortGvrpStatisticsSLA_Object = MibTableColumn
rlPortGvrpStatisticsSLA = _RlPortGvrpStatisticsSLA_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 12),
    _RlPortGvrpStatisticsSLA_Type()
)
rlPortGvrpStatisticsSLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLA.setStatus("current")


class _RlPortGvrpStatisticsClear_Type(Integer32):
    """Custom type rlPortGvrpStatisticsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("passive", 2))
    )


_RlPortGvrpStatisticsClear_Type.__name__ = "Integer32"
_RlPortGvrpStatisticsClear_Object = MibTableColumn
rlPortGvrpStatisticsClear = _RlPortGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 13),
    _RlPortGvrpStatisticsClear_Type()
)
rlPortGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsClear.setStatus("current")
_RlPortGvrpErrorStatisticsTable_Object = MibTable
rlPortGvrpErrorStatisticsTable = _RlPortGvrpErrorStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5)
)
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsTable.setStatus("current")
_RlPortGvrpErrorStatisticsEntry_Object = MibTableRow
rlPortGvrpErrorStatisticsEntry = _RlPortGvrpErrorStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1)
)
rlPortGvrpErrorStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsEntry.setStatus("current")
_RlPortGvrpErrorStatisticsInvProt_Type = Counter32
_RlPortGvrpErrorStatisticsInvProt_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvProt = _RlPortGvrpErrorStatisticsInvProt_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 1),
    _RlPortGvrpErrorStatisticsInvProt_Type()
)
rlPortGvrpErrorStatisticsInvProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvProt.setStatus("current")
_RlPortGvrpErrorStatisticsInvAtyp_Type = Counter32
_RlPortGvrpErrorStatisticsInvAtyp_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAtyp = _RlPortGvrpErrorStatisticsInvAtyp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 2),
    _RlPortGvrpErrorStatisticsInvAtyp_Type()
)
rlPortGvrpErrorStatisticsInvAtyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAtyp.setStatus("current")
_RlPortGvrpErrorStatisticsInvAval_Type = Counter32
_RlPortGvrpErrorStatisticsInvAval_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAval = _RlPortGvrpErrorStatisticsInvAval_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 3),
    _RlPortGvrpErrorStatisticsInvAval_Type()
)
rlPortGvrpErrorStatisticsInvAval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAval.setStatus("current")
_RlPortGvrpErrorStatisticsInvPlen_Type = Counter32
_RlPortGvrpErrorStatisticsInvPlen_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvPlen = _RlPortGvrpErrorStatisticsInvPlen_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 4),
    _RlPortGvrpErrorStatisticsInvPlen_Type()
)
rlPortGvrpErrorStatisticsInvPlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvPlen.setStatus("current")
_RlPortGvrpErrorStatisticsInvAlen_Type = Counter32
_RlPortGvrpErrorStatisticsInvAlen_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAlen = _RlPortGvrpErrorStatisticsInvAlen_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 5),
    _RlPortGvrpErrorStatisticsInvAlen_Type()
)
rlPortGvrpErrorStatisticsInvAlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAlen.setStatus("current")
_RlPortGvrpErrorStatisticsInvEvent_Type = Counter32
_RlPortGvrpErrorStatisticsInvEvent_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvEvent = _RlPortGvrpErrorStatisticsInvEvent_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 6),
    _RlPortGvrpErrorStatisticsInvEvent_Type()
)
rlPortGvrpErrorStatisticsInvEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvEvent.setStatus("current")


class _RlPortGvrpErrorStatisticsClear_Type(Integer32):
    """Custom type rlPortGvrpErrorStatisticsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("passive", 2))
    )


_RlPortGvrpErrorStatisticsClear_Type.__name__ = "Integer32"
_RlPortGvrpErrorStatisticsClear_Object = MibTableColumn
rlPortGvrpErrorStatisticsClear = _RlPortGvrpErrorStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 7),
    _RlPortGvrpErrorStatisticsClear_Type()
)
rlPortGvrpErrorStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsClear.setStatus("current")
_RlPortGvrpApplicantStatusTable_Object = MibTable
rlPortGvrpApplicantStatusTable = _RlPortGvrpApplicantStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6)
)
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusTable.setStatus("current")
_RlPortGvrpApplicantStatusEntry_Object = MibTableRow
rlPortGvrpApplicantStatusEntry = _RlPortGvrpApplicantStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6, 1)
)
rlPortGvrpApplicantStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusEntry.setStatus("current")


class _RlPortGvrpApplicantStatusValue_Type(Integer32):
    """Custom type rlPortGvrpApplicantStatusValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonParticipant", 2),
          ("participant", 1))
    )


_RlPortGvrpApplicantStatusValue_Type.__name__ = "Integer32"
_RlPortGvrpApplicantStatusValue_Object = MibTableColumn
rlPortGvrpApplicantStatusValue = _RlPortGvrpApplicantStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6, 1, 1),
    _RlPortGvrpApplicantStatusValue_Type()
)
rlPortGvrpApplicantStatusValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusValue.setStatus("current")
_RlPortGvrpRegistrationModeTable_Object = MibTable
rlPortGvrpRegistrationModeTable = _RlPortGvrpRegistrationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8)
)
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeTable.setStatus("current")
_RlPortGvrpRegistrationModeEntry_Object = MibTableRow
rlPortGvrpRegistrationModeEntry = _RlPortGvrpRegistrationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8, 1)
)
rlPortGvrpRegistrationModeEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeEntry.setStatus("current")


class _RlPortGvrpRegistrationModeForbidden_Type(TruthValue):
    """Custom type rlPortGvrpRegistrationModeForbidden based on TruthValue"""


_RlPortGvrpRegistrationModeForbidden_Object = MibTableColumn
rlPortGvrpRegistrationModeForbidden = _RlPortGvrpRegistrationModeForbidden_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8, 1, 1),
    _RlPortGvrpRegistrationModeForbidden_Type()
)
rlPortGvrpRegistrationModeForbidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeForbidden.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-GVRP-MIB",
    **{"rlGvrp": rlGvrp,
       "rlPortGvrpTimersTable": rlPortGvrpTimersTable,
       "rlPortGvrpTimersEntry": rlPortGvrpTimersEntry,
       "rlPortGvrpJoinTime": rlPortGvrpJoinTime,
       "rlPortGvrpLeaveTime": rlPortGvrpLeaveTime,
       "rlPortGvrpLeaveAllTime": rlPortGvrpLeaveAllTime,
       "rlPortGvrpOverrideGarp": rlPortGvrpOverrideGarp,
       "rlGvrpSupported": rlGvrpSupported,
       "rlGvrpMibVersion": rlGvrpMibVersion,
       "rlPortGvrpStatisticsTable": rlPortGvrpStatisticsTable,
       "rlPortGvrpStatisticsEntry": rlPortGvrpStatisticsEntry,
       "rlPortGvrpStatisticsRJE": rlPortGvrpStatisticsRJE,
       "rlPortGvrpStatisticsRJIn": rlPortGvrpStatisticsRJIn,
       "rlPortGvrpStatisticsREmp": rlPortGvrpStatisticsREmp,
       "rlPortGvrpStatisticsRLIn": rlPortGvrpStatisticsRLIn,
       "rlPortGvrpStatisticsRLE": rlPortGvrpStatisticsRLE,
       "rlPortGvrpStatisticsRLA": rlPortGvrpStatisticsRLA,
       "rlPortGvrpStatisticsSJE": rlPortGvrpStatisticsSJE,
       "rlPortGvrpStatisticsSJIn": rlPortGvrpStatisticsSJIn,
       "rlPortGvrpStatisticsSEmp": rlPortGvrpStatisticsSEmp,
       "rlPortGvrpStatisticsSLIn": rlPortGvrpStatisticsSLIn,
       "rlPortGvrpStatisticsSLE": rlPortGvrpStatisticsSLE,
       "rlPortGvrpStatisticsSLA": rlPortGvrpStatisticsSLA,
       "rlPortGvrpStatisticsClear": rlPortGvrpStatisticsClear,
       "rlPortGvrpErrorStatisticsTable": rlPortGvrpErrorStatisticsTable,
       "rlPortGvrpErrorStatisticsEntry": rlPortGvrpErrorStatisticsEntry,
       "rlPortGvrpErrorStatisticsInvProt": rlPortGvrpErrorStatisticsInvProt,
       "rlPortGvrpErrorStatisticsInvAtyp": rlPortGvrpErrorStatisticsInvAtyp,
       "rlPortGvrpErrorStatisticsInvAval": rlPortGvrpErrorStatisticsInvAval,
       "rlPortGvrpErrorStatisticsInvPlen": rlPortGvrpErrorStatisticsInvPlen,
       "rlPortGvrpErrorStatisticsInvAlen": rlPortGvrpErrorStatisticsInvAlen,
       "rlPortGvrpErrorStatisticsInvEvent": rlPortGvrpErrorStatisticsInvEvent,
       "rlPortGvrpErrorStatisticsClear": rlPortGvrpErrorStatisticsClear,
       "rlPortGvrpApplicantStatusTable": rlPortGvrpApplicantStatusTable,
       "rlPortGvrpApplicantStatusEntry": rlPortGvrpApplicantStatusEntry,
       "rlPortGvrpApplicantStatusValue": rlPortGvrpApplicantStatusValue,
       "rlPortGvrpRegistrationModeTable": rlPortGvrpRegistrationModeTable,
       "rlPortGvrpRegistrationModeEntry": rlPortGvrpRegistrationModeEntry,
       "rlPortGvrpRegistrationModeForbidden": rlPortGvrpRegistrationModeForbidden}
)
