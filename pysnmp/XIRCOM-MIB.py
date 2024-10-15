# SNMP MIB module (XIRCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XIRCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:41 2024
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

_Xircom_ObjectIdentity = ObjectIdentity
xircom = _Xircom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 588)
)
_Printers_ObjectIdentity = ObjectIdentity
printers = _Printers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 588, 1)
)
_PrinterStatus_Type = Integer32
_PrinterStatus_Object = MibScalar
printerStatus = _PrinterStatus_Object(
    (1, 3, 6, 1, 4, 1, 588, 1, 1),
    _PrinterStatus_Type()
)
printerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerStatus.setStatus("mandatory")
_AcceptPrintJobs_Type = Integer32
_AcceptPrintJobs_Object = MibScalar
acceptPrintJobs = _AcceptPrintJobs_Object(
    (1, 3, 6, 1, 4, 1, 588, 1, 2),
    _AcceptPrintJobs_Type()
)
acceptPrintJobs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptPrintJobs.setStatus("mandatory")
_QueuedJobs_Type = Integer32
_QueuedJobs_Object = MibScalar
queuedJobs = _QueuedJobs_Object(
    (1, 3, 6, 1, 4, 1, 588, 1, 3),
    _QueuedJobs_Type()
)
queuedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuedJobs.setStatus("mandatory")
_SendTrap_Type = Integer32
_SendTrap_Object = MibScalar
sendTrap = _SendTrap_Object(
    (1, 3, 6, 1, 4, 1, 588, 1, 4),
    _SendTrap_Type()
)
sendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

printerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 588, 1, 0, 0)
)
printerTrap.setObjects(
    ("XIRCOM-MIB", "printerStatus")
)
if mibBuilder.loadTexts:
    printerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XIRCOM-MIB",
    **{"xircom": xircom,
       "printers": printers,
       "printerTrap": printerTrap,
       "printerStatus": printerStatus,
       "acceptPrintJobs": acceptPrintJobs,
       "queuedJobs": queuedJobs,
       "sendTrap": sendTrap}
)
