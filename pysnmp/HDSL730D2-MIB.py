# SNMP MIB module (HDSL730D2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL730D2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:16 2024
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

(hdsl730D2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl730D2")

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

_Hdsl730D2System_ObjectIdentity = ObjectIdentity
hdsl730D2System = _Hdsl730D2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 1)
)
_Hdsl730D2Version_ObjectIdentity = ObjectIdentity
hdsl730D2Version = _Hdsl730D2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 1, 1)
)


class _Gdc730D2SystemMIBversion_Type(DisplayString):
    """Custom type gdc730D2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc730D2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc730D2SystemMIBversion_Object = MibScalar
gdc730D2SystemMIBversion = _Gdc730D2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 1, 1, 1),
    _Gdc730D2SystemMIBversion_Type()
)
gdc730D2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc730D2SystemMIBversion.setStatus("mandatory")
_Hdsl730D2Alarms_ObjectIdentity = ObjectIdentity
hdsl730D2Alarms = _Hdsl730D2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2)
)
_Hdsl730D2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl730D2NoResponseAlm = _Hdsl730D2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 1)
)
_Hdsl730D2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl730D2DiagRxErrAlm = _Hdsl730D2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 2)
)
_Hdsl730D2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl730D2PowerUpAlm = _Hdsl730D2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 3)
)
_Hdsl730D2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl730D2UnitFailure = _Hdsl730D2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 4)
)
_Hdsl730D2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl730D2ChecksumCorrupt = _Hdsl730D2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 5)
)
_Hdsl730D2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl730D2LossofSignal = _Hdsl730D2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 6)
)
_Hdsl730D2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl730D2UnavailableSec = _Hdsl730D2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 7)
)
_Hdsl730D2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl730D2ErrorSec = _Hdsl730D2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 8)
)
_Hdsl730D2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl730D2LossofSyncWord = _Hdsl730D2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 9)
)
_Hdsl730D2MajorBER_ObjectIdentity = ObjectIdentity
hdsl730D2MajorBER = _Hdsl730D2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 10)
)
_Hdsl730D2MinorBER_ObjectIdentity = ObjectIdentity
hdsl730D2MinorBER = _Hdsl730D2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL730D2-MIB",
    **{"hdsl730D2System": hdsl730D2System,
       "hdsl730D2Version": hdsl730D2Version,
       "gdc730D2SystemMIBversion": gdc730D2SystemMIBversion,
       "hdsl730D2Alarms": hdsl730D2Alarms,
       "hdsl730D2NoResponseAlm": hdsl730D2NoResponseAlm,
       "hdsl730D2DiagRxErrAlm": hdsl730D2DiagRxErrAlm,
       "hdsl730D2PowerUpAlm": hdsl730D2PowerUpAlm,
       "hdsl730D2UnitFailure": hdsl730D2UnitFailure,
       "hdsl730D2ChecksumCorrupt": hdsl730D2ChecksumCorrupt,
       "hdsl730D2LossofSignal": hdsl730D2LossofSignal,
       "hdsl730D2UnavailableSec": hdsl730D2UnavailableSec,
       "hdsl730D2ErrorSec": hdsl730D2ErrorSec,
       "hdsl730D2LossofSyncWord": hdsl730D2LossofSyncWord,
       "hdsl730D2MajorBER": hdsl730D2MajorBER,
       "hdsl730D2MinorBER": hdsl730D2MinorBER}
)
