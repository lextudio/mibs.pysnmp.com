# SNMP MIB module (HDSL700AG2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL700AG2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:07 2024
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

(hdsl700AG2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl700AG2")

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

_Hdsl700AG2System_ObjectIdentity = ObjectIdentity
hdsl700AG2System = _Hdsl700AG2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 1)
)
_Hdsl700AG2Version_ObjectIdentity = ObjectIdentity
hdsl700AG2Version = _Hdsl700AG2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 1, 1)
)


class _Gdc700AG2SystemMIBversion_Type(DisplayString):
    """Custom type gdc700AG2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc700AG2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc700AG2SystemMIBversion_Object = MibScalar
gdc700AG2SystemMIBversion = _Gdc700AG2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 1, 1, 1),
    _Gdc700AG2SystemMIBversion_Type()
)
gdc700AG2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc700AG2SystemMIBversion.setStatus("mandatory")
_Hdsl700AG2Alarms_ObjectIdentity = ObjectIdentity
hdsl700AG2Alarms = _Hdsl700AG2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2)
)
_Hdsl700AG2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl700AG2NoResponseAlm = _Hdsl700AG2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 1)
)
_Hdsl700AG2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl700AG2DiagRxErrAlm = _Hdsl700AG2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 2)
)
_Hdsl700AG2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl700AG2PowerUpAlm = _Hdsl700AG2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 3)
)
_Hdsl700AG2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl700AG2UnitFailure = _Hdsl700AG2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 4)
)
_Hdsl700AG2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl700AG2ChecksumCorrupt = _Hdsl700AG2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 5)
)
_Hdsl700AG2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl700AG2LossofSignal = _Hdsl700AG2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 6)
)
_Hdsl700AG2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl700AG2UnavailableSec = _Hdsl700AG2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 7)
)
_Hdsl700AG2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl700AG2ErrorSec = _Hdsl700AG2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 8)
)
_Hdsl700AG2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl700AG2LossofSyncWord = _Hdsl700AG2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 9)
)
_Hdsl700AG2LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl700AG2LossofFrameAlign = _Hdsl700AG2LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 10)
)
_Hdsl700AG2AllOnes_ObjectIdentity = ObjectIdentity
hdsl700AG2AllOnes = _Hdsl700AG2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 11)
)
_Hdsl700AG2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl700AG2RemoteLossofSig = _Hdsl700AG2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 12)
)
_Hdsl700AG2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl700AG2RemoteAlarmInd = _Hdsl700AG2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 13)
)
_Hdsl700AG2MajorBER_ObjectIdentity = ObjectIdentity
hdsl700AG2MajorBER = _Hdsl700AG2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 14)
)
_Hdsl700AG2MinorBER_ObjectIdentity = ObjectIdentity
hdsl700AG2MinorBER = _Hdsl700AG2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL700AG2-MIB",
    **{"hdsl700AG2System": hdsl700AG2System,
       "hdsl700AG2Version": hdsl700AG2Version,
       "gdc700AG2SystemMIBversion": gdc700AG2SystemMIBversion,
       "hdsl700AG2Alarms": hdsl700AG2Alarms,
       "hdsl700AG2NoResponseAlm": hdsl700AG2NoResponseAlm,
       "hdsl700AG2DiagRxErrAlm": hdsl700AG2DiagRxErrAlm,
       "hdsl700AG2PowerUpAlm": hdsl700AG2PowerUpAlm,
       "hdsl700AG2UnitFailure": hdsl700AG2UnitFailure,
       "hdsl700AG2ChecksumCorrupt": hdsl700AG2ChecksumCorrupt,
       "hdsl700AG2LossofSignal": hdsl700AG2LossofSignal,
       "hdsl700AG2UnavailableSec": hdsl700AG2UnavailableSec,
       "hdsl700AG2ErrorSec": hdsl700AG2ErrorSec,
       "hdsl700AG2LossofSyncWord": hdsl700AG2LossofSyncWord,
       "hdsl700AG2LossofFrameAlign": hdsl700AG2LossofFrameAlign,
       "hdsl700AG2AllOnes": hdsl700AG2AllOnes,
       "hdsl700AG2RemoteLossofSig": hdsl700AG2RemoteLossofSig,
       "hdsl700AG2RemoteAlarmInd": hdsl700AG2RemoteAlarmInd,
       "hdsl700AG2MajorBER": hdsl700AG2MajorBER,
       "hdsl700AG2MinorBER": hdsl700AG2MinorBER}
)
