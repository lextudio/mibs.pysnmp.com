# SNMP MIB module (MITEL-APPLICATION-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-APPLICATION-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:09 2024
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

mitelApplicationMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11)
)
mitelApplicationMon.setRevisions(
        ("2003-03-24 01:36",
         "2002-04-02 00:00")
)


# Types definitions



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )




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
_MitelApplicationMonFaultTable_Object = MibTable
mitelApplicationMonFaultTable = _MitelApplicationMonFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1)
)
if mibBuilder.loadTexts:
    mitelApplicationMonFaultTable.setStatus("current")
_MitelApplicationMonFaultEntry_Object = MibTableRow
mitelApplicationMonFaultEntry = _MitelApplicationMonFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1)
)
mitelApplicationMonFaultEntry.setIndexNames(
    (0, "MITEL-APPLICATION-MON-MIB", "mitelApplicationMonFaultTblIndex"),
)
if mibBuilder.loadTexts:
    mitelApplicationMonFaultEntry.setStatus("current")
_MitelApplicationMonFaultTblIndex_Type = Integer32
_MitelApplicationMonFaultTblIndex_Object = MibTableColumn
mitelApplicationMonFaultTblIndex = _MitelApplicationMonFaultTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 1),
    _MitelApplicationMonFaultTblIndex_Type()
)
mitelApplicationMonFaultTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultTblIndex.setStatus("current")


class _MitelApplicationMonFaultId_Type(Integer32):
    """Custom type mitelApplicationMonFaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("appMonTaskCrashed", 1)
    )


_MitelApplicationMonFaultId_Type.__name__ = "Integer32"
_MitelApplicationMonFaultId_Object = MibTableColumn
mitelApplicationMonFaultId = _MitelApplicationMonFaultId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 2),
    _MitelApplicationMonFaultId_Type()
)
mitelApplicationMonFaultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultId.setStatus("current")


class _MitelApplicationMonFaultStatus_Type(Integer32):
    """Custom type mitelApplicationMonFaultStatus based on Integer32"""
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


_MitelApplicationMonFaultStatus_Type.__name__ = "Integer32"
_MitelApplicationMonFaultStatus_Object = MibTableColumn
mitelApplicationMonFaultStatus = _MitelApplicationMonFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 3),
    _MitelApplicationMonFaultStatus_Type()
)
mitelApplicationMonFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultStatus.setStatus("current")
_MitelApplicationMonFaultOccur_Type = Counter32
_MitelApplicationMonFaultOccur_Object = MibTableColumn
mitelApplicationMonFaultOccur = _MitelApplicationMonFaultOccur_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 4),
    _MitelApplicationMonFaultOccur_Type()
)
mitelApplicationMonFaultOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultOccur.setStatus("current")
_MitelApplicationMonFaultDateTime_Type = DateAndTime
_MitelApplicationMonFaultDateTime_Object = MibTableColumn
mitelApplicationMonFaultDateTime = _MitelApplicationMonFaultDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 5),
    _MitelApplicationMonFaultDateTime_Type()
)
mitelApplicationMonFaultDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultDateTime.setStatus("current")
_MitelApplicationMonFaultDescr_Type = DisplayString
_MitelApplicationMonFaultDescr_Object = MibTableColumn
mitelApplicationMonFaultDescr = _MitelApplicationMonFaultDescr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 11, 1, 1, 6),
    _MitelApplicationMonFaultDescr_Type()
)
mitelApplicationMonFaultDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelApplicationMonFaultDescr.setStatus("current")

# Managed Objects groups


# Notification objects

mitelAppMonTaskCrashedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 411)
)
mitelAppMonTaskCrashedNotif.setObjects(
      *(("MITEL-APPLICATION-MON-MIB", "mitelApplicationMonFaultStatus"),
        ("MITEL-APPLICATION-MON-MIB", "mitelApplicationMonFaultDateTime"),
        ("MITEL-APPLICATION-MON-MIB", "mitelApplicationMonFaultDescr"))
)
if mibBuilder.loadTexts:
    mitelAppMonTaskCrashedNotif.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
    ("MITEL-APPLICATION-MON-MIB", "mitelAppMonTaskCrashedNotif")
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-APPLICATION-MON-MIB",
    **{"DateAndTime": DateAndTime,
       "mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelAppMonTaskCrashedNotif": mitelAppMonTaskCrashedNotif,
       "mitelProprietary": mitelProprietary,
       "mitelApplicationMon": mitelApplicationMon,
       "mitelApplicationMonFaultTable": mitelApplicationMonFaultTable,
       "mitelApplicationMonFaultEntry": mitelApplicationMonFaultEntry,
       "mitelApplicationMonFaultTblIndex": mitelApplicationMonFaultTblIndex,
       "mitelApplicationMonFaultId": mitelApplicationMonFaultId,
       "mitelApplicationMonFaultStatus": mitelApplicationMonFaultStatus,
       "mitelApplicationMonFaultOccur": mitelApplicationMonFaultOccur,
       "mitelApplicationMonFaultDateTime": mitelApplicationMonFaultDateTime,
       "mitelApplicationMonFaultDescr": mitelApplicationMonFaultDescr}
)
