# SNMP MIB module (HDSL702G2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL702G2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:10 2024
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

(hdsl702G2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl702G2")

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

_Hdsl702G2System_ObjectIdentity = ObjectIdentity
hdsl702G2System = _Hdsl702G2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 1)
)
_Hdsl702G2Version_ObjectIdentity = ObjectIdentity
hdsl702G2Version = _Hdsl702G2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 1, 1)
)


class _Gdc702G2SystemMIBversion_Type(DisplayString):
    """Custom type gdc702G2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc702G2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc702G2SystemMIBversion_Object = MibScalar
gdc702G2SystemMIBversion = _Gdc702G2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 1, 1, 1),
    _Gdc702G2SystemMIBversion_Type()
)
gdc702G2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc702G2SystemMIBversion.setStatus("mandatory")
_Hdsl702G2Alarms_ObjectIdentity = ObjectIdentity
hdsl702G2Alarms = _Hdsl702G2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2)
)
_Hdsl702G2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl702G2NoResponseAlm = _Hdsl702G2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 1)
)
_Hdsl702G2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl702G2DiagRxErrAlm = _Hdsl702G2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 2)
)
_Hdsl702G2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl702G2PowerUpAlm = _Hdsl702G2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 3)
)
_Hdsl702G2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl702G2UnitFailure = _Hdsl702G2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 4)
)
_Hdsl702G2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl702G2ChecksumCorrupt = _Hdsl702G2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 5)
)
_Hdsl702G2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl702G2LossofSignal = _Hdsl702G2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 6)
)
_Hdsl702G2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl702G2UnavailableSec = _Hdsl702G2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 7)
)
_Hdsl702G2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl702G2ErrorSec = _Hdsl702G2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 8)
)
_Hdsl702G2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl702G2LossofSyncWord = _Hdsl702G2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 9)
)
_Hdsl702G2LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl702G2LossofFrameAlign = _Hdsl702G2LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 10)
)
_Hdsl702G2AllOnes_ObjectIdentity = ObjectIdentity
hdsl702G2AllOnes = _Hdsl702G2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 11)
)
_Hdsl702G2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl702G2RemoteLossofSig = _Hdsl702G2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 12)
)
_Hdsl702G2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl702G2RemoteAlarmInd = _Hdsl702G2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 13)
)
_Hdsl702G2MajorBER_ObjectIdentity = ObjectIdentity
hdsl702G2MajorBER = _Hdsl702G2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 14)
)
_Hdsl702G2MinorBER_ObjectIdentity = ObjectIdentity
hdsl702G2MinorBER = _Hdsl702G2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL702G2-MIB",
    **{"hdsl702G2System": hdsl702G2System,
       "hdsl702G2Version": hdsl702G2Version,
       "gdc702G2SystemMIBversion": gdc702G2SystemMIBversion,
       "hdsl702G2Alarms": hdsl702G2Alarms,
       "hdsl702G2NoResponseAlm": hdsl702G2NoResponseAlm,
       "hdsl702G2DiagRxErrAlm": hdsl702G2DiagRxErrAlm,
       "hdsl702G2PowerUpAlm": hdsl702G2PowerUpAlm,
       "hdsl702G2UnitFailure": hdsl702G2UnitFailure,
       "hdsl702G2ChecksumCorrupt": hdsl702G2ChecksumCorrupt,
       "hdsl702G2LossofSignal": hdsl702G2LossofSignal,
       "hdsl702G2UnavailableSec": hdsl702G2UnavailableSec,
       "hdsl702G2ErrorSec": hdsl702G2ErrorSec,
       "hdsl702G2LossofSyncWord": hdsl702G2LossofSyncWord,
       "hdsl702G2LossofFrameAlign": hdsl702G2LossofFrameAlign,
       "hdsl702G2AllOnes": hdsl702G2AllOnes,
       "hdsl702G2RemoteLossofSig": hdsl702G2RemoteLossofSig,
       "hdsl702G2RemoteAlarmInd": hdsl702G2RemoteAlarmInd,
       "hdsl702G2MajorBER": hdsl702G2MajorBER,
       "hdsl702G2MinorBER": hdsl702G2MinorBER}
)
