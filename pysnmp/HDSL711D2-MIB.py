# SNMP MIB module (HDSL711D2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL711D2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:12 2024
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

(hdsl711D2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl711D2")

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

_Hdsl711D2System_ObjectIdentity = ObjectIdentity
hdsl711D2System = _Hdsl711D2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 1)
)
_Hdsl711D2Version_ObjectIdentity = ObjectIdentity
hdsl711D2Version = _Hdsl711D2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 1, 1)
)


class _Gdc711D2SystemMIBversion_Type(DisplayString):
    """Custom type gdc711D2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc711D2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc711D2SystemMIBversion_Object = MibScalar
gdc711D2SystemMIBversion = _Gdc711D2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 1, 1, 1),
    _Gdc711D2SystemMIBversion_Type()
)
gdc711D2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc711D2SystemMIBversion.setStatus("mandatory")
_Hdsl711D2Alarms_ObjectIdentity = ObjectIdentity
hdsl711D2Alarms = _Hdsl711D2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2)
)
_Hdsl711D2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl711D2NoResponseAlm = _Hdsl711D2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 1)
)
_Hdsl711D2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl711D2DiagRxErrAlm = _Hdsl711D2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 2)
)
_Hdsl711D2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl711D2PowerUpAlm = _Hdsl711D2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 3)
)
_Hdsl711D2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl711D2UnitFailure = _Hdsl711D2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 4)
)
_Hdsl711D2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl711D2ChecksumCorrupt = _Hdsl711D2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 5)
)
_Hdsl711D2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl711D2LossofSignal = _Hdsl711D2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 6)
)
_Hdsl711D2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl711D2UnavailableSec = _Hdsl711D2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 7)
)
_Hdsl711D2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl711D2ErrorSec = _Hdsl711D2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 8)
)
_Hdsl711D2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl711D2LossofSyncWord = _Hdsl711D2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 9)
)
_Hdsl711D2MajorBER_ObjectIdentity = ObjectIdentity
hdsl711D2MajorBER = _Hdsl711D2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 10)
)
_Hdsl711D2MinorBER_ObjectIdentity = ObjectIdentity
hdsl711D2MinorBER = _Hdsl711D2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL711D2-MIB",
    **{"hdsl711D2System": hdsl711D2System,
       "hdsl711D2Version": hdsl711D2Version,
       "gdc711D2SystemMIBversion": gdc711D2SystemMIBversion,
       "hdsl711D2Alarms": hdsl711D2Alarms,
       "hdsl711D2NoResponseAlm": hdsl711D2NoResponseAlm,
       "hdsl711D2DiagRxErrAlm": hdsl711D2DiagRxErrAlm,
       "hdsl711D2PowerUpAlm": hdsl711D2PowerUpAlm,
       "hdsl711D2UnitFailure": hdsl711D2UnitFailure,
       "hdsl711D2ChecksumCorrupt": hdsl711D2ChecksumCorrupt,
       "hdsl711D2LossofSignal": hdsl711D2LossofSignal,
       "hdsl711D2UnavailableSec": hdsl711D2UnavailableSec,
       "hdsl711D2ErrorSec": hdsl711D2ErrorSec,
       "hdsl711D2LossofSyncWord": hdsl711D2LossofSyncWord,
       "hdsl711D2MajorBER": hdsl711D2MajorBER,
       "hdsl711D2MinorBER": hdsl711D2MinorBER}
)
