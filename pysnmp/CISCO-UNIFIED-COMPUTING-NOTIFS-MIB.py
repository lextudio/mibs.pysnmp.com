# SNMP MIB module (CISCO-UNIFIED-COMPUTING-NOTIFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-NOTIFS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(cucsFaultAffectedObjectDn,
 cucsFaultAffectedObjectId,
 cucsFaultCode,
 cucsFaultCreationTime,
 cucsFaultDescription,
 cucsFaultId,
 cucsFaultIndex,
 cucsFaultLastModificationTime,
 cucsFaultOccur,
 cucsFaultProbableCause,
 cucsFaultSeverity,
 cucsFaultType) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-FAULT-MIB",
    "cucsFaultAffectedObjectDn",
    "cucsFaultAffectedObjectId",
    "cucsFaultCode",
    "cucsFaultCreationTime",
    "cucsFaultDescription",
    "cucsFaultId",
    "cucsFaultIndex",
    "cucsFaultLastModificationTime",
    "cucsFaultOccur",
    "cucsFaultProbableCause",
    "cucsFaultSeverity",
    "cucsFaultType")

(ciscoUnifiedComputingMIB,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "ciscoUnifiedComputingMIB",
    "ciscoUnifiedComputingMIBObjects")

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

ciscoUnifiedComputingMIBNotifs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 0)
)
ciscoUnifiedComputingMIBNotifs.setRevisions(
        ("2010-01-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

cucsFaultActiveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)
)
cucsFaultActiveNotif.setObjects(
      *(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
)
if mibBuilder.loadTexts:
    cucsFaultActiveNotif.setStatus(
        "current"
    )

cucsFaultClearNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)
)
cucsFaultClearNotif.setObjects(
      *(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
)
if mibBuilder.loadTexts:
    cucsFaultClearNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-NOTIFS-MIB",
    **{"ciscoUnifiedComputingMIBNotifs": ciscoUnifiedComputingMIBNotifs,
       "cucsFaultActiveNotif": cucsFaultActiveNotif,
       "cucsFaultClearNotif": cucsFaultClearNotif}
)
