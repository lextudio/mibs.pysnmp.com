# SNMP MIB module (ANTIVIRUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANTIVIRUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:01 2024
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

(nai,
 naiTrapAgent,
 naiTrapAgentVersion,
 naiTrapAlarmSourceAddress,
 naiTrapAlarmSourceDNSName,
 naiTrapDescription,
 naiTrapGMTTime,
 naiTrapLocalTime,
 naiTrapPseudoID,
 naiTrapSeverity,
 naiTrapURL) = mibBuilder.importSymbols(
    "NAI-MIB",
    "nai",
    "naiTrapAgent",
    "naiTrapAgentVersion",
    "naiTrapAlarmSourceAddress",
    "naiTrapAlarmSourceDNSName",
    "naiTrapDescription",
    "naiTrapGMTTime",
    "naiTrapLocalTime",
    "naiTrapPseudoID",
    "naiTrapSeverity",
    "naiTrapURL")

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

_NaiAntiVirus_ObjectIdentity = ObjectIdentity
naiAntiVirus = _NaiAntiVirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401, 4)
)
_NaiAntiVirusTrapAgentUser_Type = OctetString
_NaiAntiVirusTrapAgentUser_Object = MibScalar
naiAntiVirusTrapAgentUser = _NaiAntiVirusTrapAgentUser_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 1),
    _NaiAntiVirusTrapAgentUser_Type()
)
naiAntiVirusTrapAgentUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapAgentUser.setStatus("mandatory")
_NaiAntiVirusTrapInfectedFile_Type = OctetString
_NaiAntiVirusTrapInfectedFile_Object = MibScalar
naiAntiVirusTrapInfectedFile = _NaiAntiVirusTrapInfectedFile_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 2),
    _NaiAntiVirusTrapInfectedFile_Type()
)
naiAntiVirusTrapInfectedFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapInfectedFile.setStatus("mandatory")
_NaiAntiVirusTrapVirusName_Type = OctetString
_NaiAntiVirusTrapVirusName_Object = MibScalar
naiAntiVirusTrapVirusName = _NaiAntiVirusTrapVirusName_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 3),
    _NaiAntiVirusTrapVirusName_Type()
)
naiAntiVirusTrapVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapVirusName.setStatus("mandatory")
_NaiAntiVirusTrapTaskName_Type = OctetString
_NaiAntiVirusTrapTaskName_Object = MibScalar
naiAntiVirusTrapTaskName = _NaiAntiVirusTrapTaskName_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 4),
    _NaiAntiVirusTrapTaskName_Type()
)
naiAntiVirusTrapTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapTaskName.setStatus("mandatory")
_NaiAntiVirusTrapStatus_Type = Integer32
_NaiAntiVirusTrapStatus_Object = MibScalar
naiAntiVirusTrapStatus = _NaiAntiVirusTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 5),
    _NaiAntiVirusTrapStatus_Type()
)
naiAntiVirusTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapStatus.setStatus("optional")
_NaiAntiVirusTrapOS_Type = OctetString
_NaiAntiVirusTrapOS_Object = MibScalar
naiAntiVirusTrapOS = _NaiAntiVirusTrapOS_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 6),
    _NaiAntiVirusTrapOS_Type()
)
naiAntiVirusTrapOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapOS.setStatus("mandatory")
_NaiAntiVirusTrapEngineVersion_Type = OctetString
_NaiAntiVirusTrapEngineVersion_Object = MibScalar
naiAntiVirusTrapEngineVersion = _NaiAntiVirusTrapEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 7),
    _NaiAntiVirusTrapEngineVersion_Type()
)
naiAntiVirusTrapEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapEngineVersion.setStatus("mandatory")
_NaiAntiVirusTrapDATVersion_Type = OctetString
_NaiAntiVirusTrapDATVersion_Object = MibScalar
naiAntiVirusTrapDATVersion = _NaiAntiVirusTrapDATVersion_Object(
    (1, 3, 6, 1, 4, 1, 3401, 4, 8),
    _NaiAntiVirusTrapDATVersion_Type()
)
naiAntiVirusTrapDATVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiAntiVirusTrapDATVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

naiAntiVirusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3401, 4, 0, 1)
)
naiAntiVirusTrap.setObjects(
      *(("NAI-MIB", "naiTrapAgent"),
        ("NAI-MIB", "naiTrapAgentVersion"),
        ("NAI-MIB", "naiTrapSeverity"),
        ("NAI-MIB", "naiTrapDescription"),
        ("NAI-MIB", "naiTrapAlarmSourceAddress"),
        ("NAI-MIB", "naiTrapAlarmSourceDNSName"),
        ("NAI-MIB", "naiTrapGMTTime"),
        ("NAI-MIB", "naiTrapLocalTime"),
        ("NAI-MIB", "naiTrapURL"),
        ("NAI-MIB", "naiTrapPseudoID"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapAgentUser"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapInfectedFile"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapVirusName"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapTaskName"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapStatus"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapOS"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapEngineVersion"),
        ("ANTIVIRUS-MIB", "naiAntiVirusTrapDATVersion"))
)
if mibBuilder.loadTexts:
    naiAntiVirusTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANTIVIRUS-MIB",
    **{"naiAntiVirus": naiAntiVirus,
       "naiAntiVirusTrap": naiAntiVirusTrap,
       "naiAntiVirusTrapAgentUser": naiAntiVirusTrapAgentUser,
       "naiAntiVirusTrapInfectedFile": naiAntiVirusTrapInfectedFile,
       "naiAntiVirusTrapVirusName": naiAntiVirusTrapVirusName,
       "naiAntiVirusTrapTaskName": naiAntiVirusTrapTaskName,
       "naiAntiVirusTrapStatus": naiAntiVirusTrapStatus,
       "naiAntiVirusTrapOS": naiAntiVirusTrapOS,
       "naiAntiVirusTrapEngineVersion": naiAntiVirusTrapEngineVersion,
       "naiAntiVirusTrapDATVersion": naiAntiVirusTrapDATVersion}
)
