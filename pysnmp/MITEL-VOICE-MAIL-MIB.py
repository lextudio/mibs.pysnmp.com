# SNMP MIB module (MITEL-VOICE-MAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-VOICE-MAIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:30 2024
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

mitelVoiceMail = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10)
)
mitelVoiceMail.setRevisions(
        ("2002-03-24 11:49",
         "2002-04-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsIpera1000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera1000 = _MitelIdCsIpera1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelVoiceMailFaultTable_Object = MibTable
mitelVoiceMailFaultTable = _MitelVoiceMailFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1)
)
if mibBuilder.loadTexts:
    mitelVoiceMailFaultTable.setStatus("current")
_MitelVoiceMailFaultEntry_Object = MibTableRow
mitelVoiceMailFaultEntry = _MitelVoiceMailFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1)
)
mitelVoiceMailFaultEntry.setIndexNames(
    (0, "MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultTblIndex"),
)
if mibBuilder.loadTexts:
    mitelVoiceMailFaultEntry.setStatus("current")
_MitelVoiceMailFaultTblIndex_Type = Integer32
_MitelVoiceMailFaultTblIndex_Object = MibTableColumn
mitelVoiceMailFaultTblIndex = _MitelVoiceMailFaultTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 1),
    _MitelVoiceMailFaultTblIndex_Type()
)
mitelVoiceMailFaultTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelVoiceMailFaultTblIndex.setStatus("current")


class _MitelVoiceMailFaultId_Type(Integer32):
    """Custom type mitelVoiceMailFaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceMailDiskFull", 2),
          ("voiceMailDiskNearlyFull", 1))
    )


_MitelVoiceMailFaultId_Type.__name__ = "Integer32"
_MitelVoiceMailFaultId_Object = MibTableColumn
mitelVoiceMailFaultId = _MitelVoiceMailFaultId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 2),
    _MitelVoiceMailFaultId_Type()
)
mitelVoiceMailFaultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelVoiceMailFaultId.setStatus("current")


class _MitelVoiceMailFaultStatus_Type(Integer32):
    """Custom type mitelVoiceMailFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("message", 3),
          ("set", 1))
    )


_MitelVoiceMailFaultStatus_Type.__name__ = "Integer32"
_MitelVoiceMailFaultStatus_Object = MibTableColumn
mitelVoiceMailFaultStatus = _MitelVoiceMailFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 3),
    _MitelVoiceMailFaultStatus_Type()
)
mitelVoiceMailFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelVoiceMailFaultStatus.setStatus("current")
_MitelVoiceMailFaultOccur_Type = Counter32
_MitelVoiceMailFaultOccur_Object = MibTableColumn
mitelVoiceMailFaultOccur = _MitelVoiceMailFaultOccur_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 4),
    _MitelVoiceMailFaultOccur_Type()
)
mitelVoiceMailFaultOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelVoiceMailFaultOccur.setStatus("current")

# Managed Objects groups


# Notification objects

mitelVoiceMailDiskNearlyFullNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 408)
)
mitelVoiceMailDiskNearlyFullNotif.setObjects(
      *(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultStatus"),
        ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultOccur"))
)
if mibBuilder.loadTexts:
    mitelVoiceMailDiskNearlyFullNotif.setStatus(
        "current"
    )

mitelVoiceMailDiskFullNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 409)
)
mitelVoiceMailDiskFullNotif.setObjects(
      *(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultStatus"),
        ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultOccur"))
)
if mibBuilder.loadTexts:
    mitelVoiceMailDiskFullNotif.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
      *(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailDiskNearlyFullNotif"),
        ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailDiskFullNotif"))
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-VOICE-MAIL-MIB",
    **{"mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelVoiceMailDiskNearlyFullNotif": mitelVoiceMailDiskNearlyFullNotif,
       "mitelVoiceMailDiskFullNotif": mitelVoiceMailDiskFullNotif,
       "mitelProprietary": mitelProprietary,
       "mitelVoiceMail": mitelVoiceMail,
       "mitelVoiceMailFaultTable": mitelVoiceMailFaultTable,
       "mitelVoiceMailFaultEntry": mitelVoiceMailFaultEntry,
       "mitelVoiceMailFaultTblIndex": mitelVoiceMailFaultTblIndex,
       "mitelVoiceMailFaultId": mitelVoiceMailFaultId,
       "mitelVoiceMailFaultStatus": mitelVoiceMailFaultStatus,
       "mitelVoiceMailFaultOccur": mitelVoiceMailFaultOccur}
)
