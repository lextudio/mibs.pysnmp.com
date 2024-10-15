# SNMP MIB module (HDSL710D2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL710D2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:11 2024
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

(hdsl710D2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl710D2")

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

_Hdsl710D2System_ObjectIdentity = ObjectIdentity
hdsl710D2System = _Hdsl710D2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 1)
)
_Hdsl710D2Version_ObjectIdentity = ObjectIdentity
hdsl710D2Version = _Hdsl710D2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 1, 1)
)


class _Gdc710D2SystemMIBversion_Type(DisplayString):
    """Custom type gdc710D2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc710D2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc710D2SystemMIBversion_Object = MibScalar
gdc710D2SystemMIBversion = _Gdc710D2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 1, 1, 1),
    _Gdc710D2SystemMIBversion_Type()
)
gdc710D2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc710D2SystemMIBversion.setStatus("mandatory")
_Hdsl710D2Alarms_ObjectIdentity = ObjectIdentity
hdsl710D2Alarms = _Hdsl710D2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2)
)
_Hdsl710D2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl710D2NoResponseAlm = _Hdsl710D2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 1)
)
_Hdsl710D2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl710D2DiagRxErrAlm = _Hdsl710D2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 2)
)
_Hdsl710D2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl710D2PowerUpAlm = _Hdsl710D2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 3)
)
_Hdsl710D2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl710D2UnitFailure = _Hdsl710D2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 4)
)
_Hdsl710D2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl710D2ChecksumCorrupt = _Hdsl710D2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 5)
)
_Hdsl710D2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl710D2LossofSignal = _Hdsl710D2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 6)
)
_Hdsl710D2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl710D2UnavailableSec = _Hdsl710D2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 7)
)
_Hdsl710D2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl710D2ErrorSec = _Hdsl710D2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 8)
)
_Hdsl710D2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl710D2LossofSyncWord = _Hdsl710D2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 9)
)
_Hdsl710D2MajorBER_ObjectIdentity = ObjectIdentity
hdsl710D2MajorBER = _Hdsl710D2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 10)
)
_Hdsl710D2MinorBER_ObjectIdentity = ObjectIdentity
hdsl710D2MinorBER = _Hdsl710D2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL710D2-MIB",
    **{"hdsl710D2System": hdsl710D2System,
       "hdsl710D2Version": hdsl710D2Version,
       "gdc710D2SystemMIBversion": gdc710D2SystemMIBversion,
       "hdsl710D2Alarms": hdsl710D2Alarms,
       "hdsl710D2NoResponseAlm": hdsl710D2NoResponseAlm,
       "hdsl710D2DiagRxErrAlm": hdsl710D2DiagRxErrAlm,
       "hdsl710D2PowerUpAlm": hdsl710D2PowerUpAlm,
       "hdsl710D2UnitFailure": hdsl710D2UnitFailure,
       "hdsl710D2ChecksumCorrupt": hdsl710D2ChecksumCorrupt,
       "hdsl710D2LossofSignal": hdsl710D2LossofSignal,
       "hdsl710D2UnavailableSec": hdsl710D2UnavailableSec,
       "hdsl710D2ErrorSec": hdsl710D2ErrorSec,
       "hdsl710D2LossofSyncWord": hdsl710D2LossofSyncWord,
       "hdsl710D2MajorBER": hdsl710D2MajorBER,
       "hdsl710D2MinorBER": hdsl710D2MinorBER}
)
