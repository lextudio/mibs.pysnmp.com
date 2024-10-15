# SNMP MIB module (HDSL731D2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL731D2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:18 2024
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

(hdsl731D2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl731D2")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hdsl731D2System_ObjectIdentity = ObjectIdentity
hdsl731D2System = _Hdsl731D2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 1)
)
_Hdsl731D2Version_ObjectIdentity = ObjectIdentity
hdsl731D2Version = _Hdsl731D2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 1, 1)
)


class _Gdc731D2SystemMIBversion_Type(DisplayString):
    """Custom type gdc731D2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc731D2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc731D2SystemMIBversion_Object = MibScalar
gdc731D2SystemMIBversion = _Gdc731D2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 1, 1, 1),
    _Gdc731D2SystemMIBversion_Type()
)
gdc731D2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc731D2SystemMIBversion.setStatus("mandatory")
_Hdsl731D2Alarms_ObjectIdentity = ObjectIdentity
hdsl731D2Alarms = _Hdsl731D2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2)
)
_Hdsl731D2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl731D2NoResponseAlm = _Hdsl731D2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 1)
)
_Hdsl731D2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl731D2DiagRxErrAlm = _Hdsl731D2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 2)
)
_Hdsl731D2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl731D2PowerUpAlm = _Hdsl731D2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 3)
)
_Hdsl731D2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl731D2UnitFailure = _Hdsl731D2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 4)
)
_Hdsl731D2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl731D2ChecksumCorrupt = _Hdsl731D2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 5)
)
_Hdsl731D2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl731D2LossofSignal = _Hdsl731D2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 6)
)
_Hdsl731D2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl731D2UnavailableSec = _Hdsl731D2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 7)
)
_Hdsl731D2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl731D2ErrorSec = _Hdsl731D2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 8)
)
_Hdsl731D2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl731D2LossofSyncWord = _Hdsl731D2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 9)
)
_Hdsl731D2MajorBER_ObjectIdentity = ObjectIdentity
hdsl731D2MajorBER = _Hdsl731D2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 10)
)
_Hdsl731D2MinorBER_ObjectIdentity = ObjectIdentity
hdsl731D2MinorBER = _Hdsl731D2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL731D2-MIB",
    **{"hdsl731D2System": hdsl731D2System,
       "hdsl731D2Version": hdsl731D2Version,
       "gdc731D2SystemMIBversion": gdc731D2SystemMIBversion,
       "hdsl731D2Alarms": hdsl731D2Alarms,
       "hdsl731D2NoResponseAlm": hdsl731D2NoResponseAlm,
       "hdsl731D2DiagRxErrAlm": hdsl731D2DiagRxErrAlm,
       "hdsl731D2PowerUpAlm": hdsl731D2PowerUpAlm,
       "hdsl731D2UnitFailure": hdsl731D2UnitFailure,
       "hdsl731D2ChecksumCorrupt": hdsl731D2ChecksumCorrupt,
       "hdsl731D2LossofSignal": hdsl731D2LossofSignal,
       "hdsl731D2UnavailableSec": hdsl731D2UnavailableSec,
       "hdsl731D2ErrorSec": hdsl731D2ErrorSec,
       "hdsl731D2LossofSyncWord": hdsl731D2LossofSyncWord,
       "hdsl731D2MajorBER": hdsl731D2MajorBER,
       "hdsl731D2MinorBER": hdsl731D2MinorBER}
)
