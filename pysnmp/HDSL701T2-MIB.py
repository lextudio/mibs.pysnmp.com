# SNMP MIB module (HDSL701T2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL701T2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:09 2024
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

(hdsl701T2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl701T2")

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

_Hdsl701T2System_ObjectIdentity = ObjectIdentity
hdsl701T2System = _Hdsl701T2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 1)
)
_Hdsl701T2Version_ObjectIdentity = ObjectIdentity
hdsl701T2Version = _Hdsl701T2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 1, 1)
)


class _Gdc701T2SystemMIBversion_Type(DisplayString):
    """Custom type gdc701T2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc701T2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc701T2SystemMIBversion_Object = MibScalar
gdc701T2SystemMIBversion = _Gdc701T2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 1, 1, 1),
    _Gdc701T2SystemMIBversion_Type()
)
gdc701T2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc701T2SystemMIBversion.setStatus("mandatory")
_Hdsl701T2Alarms_ObjectIdentity = ObjectIdentity
hdsl701T2Alarms = _Hdsl701T2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2)
)
_Hdsl701T2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl701T2NoResponseAlm = _Hdsl701T2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 1)
)
_Hdsl701T2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl701T2DiagRxErrAlm = _Hdsl701T2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 2)
)
_Hdsl701T2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl701T2PowerUpAlm = _Hdsl701T2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 3)
)
_Hdsl701T2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl701T2UnitFailure = _Hdsl701T2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 4)
)
_Hdsl701T2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl701T2ChecksumCorrupt = _Hdsl701T2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 5)
)
_Hdsl701T2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl701T2LossofSignal = _Hdsl701T2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 6)
)
_Hdsl701T2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl701T2UnavailableSec = _Hdsl701T2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 7)
)
_Hdsl701T2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl701T2ErrorSec = _Hdsl701T2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 8)
)
_Hdsl701T2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl701T2LossofSyncWord = _Hdsl701T2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 9)
)
_Hdsl701T2OutofFrame_ObjectIdentity = ObjectIdentity
hdsl701T2OutofFrame = _Hdsl701T2OutofFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 10)
)
_Hdsl701T2AllOnes_ObjectIdentity = ObjectIdentity
hdsl701T2AllOnes = _Hdsl701T2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 11)
)
_Hdsl701T2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl701T2RemoteLossofSig = _Hdsl701T2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 12)
)
_Hdsl701T2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl701T2RemoteAlarmInd = _Hdsl701T2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 13)
)
_Hdsl701T2MajorBER_ObjectIdentity = ObjectIdentity
hdsl701T2MajorBER = _Hdsl701T2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 14)
)
_Hdsl701T2MinorBER_ObjectIdentity = ObjectIdentity
hdsl701T2MinorBER = _Hdsl701T2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL701T2-MIB",
    **{"hdsl701T2System": hdsl701T2System,
       "hdsl701T2Version": hdsl701T2Version,
       "gdc701T2SystemMIBversion": gdc701T2SystemMIBversion,
       "hdsl701T2Alarms": hdsl701T2Alarms,
       "hdsl701T2NoResponseAlm": hdsl701T2NoResponseAlm,
       "hdsl701T2DiagRxErrAlm": hdsl701T2DiagRxErrAlm,
       "hdsl701T2PowerUpAlm": hdsl701T2PowerUpAlm,
       "hdsl701T2UnitFailure": hdsl701T2UnitFailure,
       "hdsl701T2ChecksumCorrupt": hdsl701T2ChecksumCorrupt,
       "hdsl701T2LossofSignal": hdsl701T2LossofSignal,
       "hdsl701T2UnavailableSec": hdsl701T2UnavailableSec,
       "hdsl701T2ErrorSec": hdsl701T2ErrorSec,
       "hdsl701T2LossofSyncWord": hdsl701T2LossofSyncWord,
       "hdsl701T2OutofFrame": hdsl701T2OutofFrame,
       "hdsl701T2AllOnes": hdsl701T2AllOnes,
       "hdsl701T2RemoteLossofSig": hdsl701T2RemoteLossofSig,
       "hdsl701T2RemoteAlarmInd": hdsl701T2RemoteAlarmInd,
       "hdsl701T2MajorBER": hdsl701T2MajorBER,
       "hdsl701T2MinorBER": hdsl701T2MinorBER}
)
