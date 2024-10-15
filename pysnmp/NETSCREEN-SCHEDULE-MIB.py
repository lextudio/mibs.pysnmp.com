# SNMP MIB module (NETSCREEN-SCHEDULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SCHEDULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:52 2024
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

(netscreenSchedule,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSchedule")

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

netscreenScheduleMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 14, 0)
)
netscreenScheduleMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSchOnceTable_Object = MibTable
nsSchOnceTable = _NsSchOnceTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1)
)
if mibBuilder.loadTexts:
    nsSchOnceTable.setStatus("current")
_NsSchOnceEntry_Object = MibTableRow
nsSchOnceEntry = _NsSchOnceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1)
)
nsSchOnceEntry.setIndexNames(
    (0, "NETSCREEN-SCHEDULE-MIB", "nsSchOnceIndex"),
)
if mibBuilder.loadTexts:
    nsSchOnceEntry.setStatus("current")


class _NsSchOnceIndex_Type(Integer32):
    """Custom type nsSchOnceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSchOnceIndex_Type.__name__ = "Integer32"
_NsSchOnceIndex_Object = MibTableColumn
nsSchOnceIndex = _NsSchOnceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 1),
    _NsSchOnceIndex_Type()
)
nsSchOnceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceIndex.setStatus("current")


class _NsSchOnceName_Type(DisplayString):
    """Custom type nsSchOnceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchOnceName_Type.__name__ = "DisplayString"
_NsSchOnceName_Object = MibTableColumn
nsSchOnceName = _NsSchOnceName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 2),
    _NsSchOnceName_Type()
)
nsSchOnceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceName.setStatus("current")


class _NsSchOnceStartTime_Type(DisplayString):
    """Custom type nsSchOnceStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchOnceStartTime_Type.__name__ = "DisplayString"
_NsSchOnceStartTime_Object = MibTableColumn
nsSchOnceStartTime = _NsSchOnceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 3),
    _NsSchOnceStartTime_Type()
)
nsSchOnceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceStartTime.setStatus("current")


class _NsSchOnceStopTime_Type(DisplayString):
    """Custom type nsSchOnceStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchOnceStopTime_Type.__name__ = "DisplayString"
_NsSchOnceStopTime_Object = MibTableColumn
nsSchOnceStopTime = _NsSchOnceStopTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 4),
    _NsSchOnceStopTime_Type()
)
nsSchOnceStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceStopTime.setStatus("current")


class _NsSchOnceComments_Type(DisplayString):
    """Custom type nsSchOnceComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchOnceComments_Type.__name__ = "DisplayString"
_NsSchOnceComments_Object = MibTableColumn
nsSchOnceComments = _NsSchOnceComments_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 5),
    _NsSchOnceComments_Type()
)
nsSchOnceComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceComments.setStatus("current")


class _NsSchOnceVsys_Type(Integer32):
    """Custom type nsSchOnceVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSchOnceVsys_Type.__name__ = "Integer32"
_NsSchOnceVsys_Object = MibTableColumn
nsSchOnceVsys = _NsSchOnceVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 6),
    _NsSchOnceVsys_Type()
)
nsSchOnceVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchOnceVsys.setStatus("current")
_NsSchRecurTable_Object = MibTable
nsSchRecurTable = _NsSchRecurTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2)
)
if mibBuilder.loadTexts:
    nsSchRecurTable.setStatus("current")
_NsSchRecurEntry_Object = MibTableRow
nsSchRecurEntry = _NsSchRecurEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1)
)
nsSchRecurEntry.setIndexNames(
    (0, "NETSCREEN-SCHEDULE-MIB", "nsSchRecurIndex"),
)
if mibBuilder.loadTexts:
    nsSchRecurEntry.setStatus("current")


class _NsSchRecurIndex_Type(Integer32):
    """Custom type nsSchRecurIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSchRecurIndex_Type.__name__ = "Integer32"
_NsSchRecurIndex_Object = MibTableColumn
nsSchRecurIndex = _NsSchRecurIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 1),
    _NsSchRecurIndex_Type()
)
nsSchRecurIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurIndex.setStatus("current")


class _NsSchRecurName_Type(DisplayString):
    """Custom type nsSchRecurName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchRecurName_Type.__name__ = "DisplayString"
_NsSchRecurName_Object = MibTableColumn
nsSchRecurName = _NsSchRecurName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 2),
    _NsSchRecurName_Type()
)
nsSchRecurName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurName.setStatus("current")


class _NsSchRecurWeekday_Type(Integer32):
    """Custom type nsSchRecurWeekday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_NsSchRecurWeekday_Type.__name__ = "Integer32"
_NsSchRecurWeekday_Object = MibTableColumn
nsSchRecurWeekday = _NsSchRecurWeekday_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 3),
    _NsSchRecurWeekday_Type()
)
nsSchRecurWeekday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurWeekday.setStatus("current")


class _NsSchRecurStartTime1_Type(DisplayString):
    """Custom type nsSchRecurStartTime1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchRecurStartTime1_Type.__name__ = "DisplayString"
_NsSchRecurStartTime1_Object = MibTableColumn
nsSchRecurStartTime1 = _NsSchRecurStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 4),
    _NsSchRecurStartTime1_Type()
)
nsSchRecurStartTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurStartTime1.setStatus("current")


class _NsSchRecurStopTime1_Type(DisplayString):
    """Custom type nsSchRecurStopTime1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchRecurStopTime1_Type.__name__ = "DisplayString"
_NsSchRecurStopTime1_Object = MibTableColumn
nsSchRecurStopTime1 = _NsSchRecurStopTime1_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 5),
    _NsSchRecurStopTime1_Type()
)
nsSchRecurStopTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurStopTime1.setStatus("current")


class _NsSchRecurStartTime2_Type(DisplayString):
    """Custom type nsSchRecurStartTime2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchRecurStartTime2_Type.__name__ = "DisplayString"
_NsSchRecurStartTime2_Object = MibTableColumn
nsSchRecurStartTime2 = _NsSchRecurStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 6),
    _NsSchRecurStartTime2_Type()
)
nsSchRecurStartTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurStartTime2.setStatus("current")


class _NsSchRecurStopTime2_Type(DisplayString):
    """Custom type nsSchRecurStopTime2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSchRecurStopTime2_Type.__name__ = "DisplayString"
_NsSchRecurStopTime2_Object = MibTableColumn
nsSchRecurStopTime2 = _NsSchRecurStopTime2_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 7),
    _NsSchRecurStopTime2_Type()
)
nsSchRecurStopTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurStopTime2.setStatus("current")


class _NsSchRecurComments_Type(DisplayString):
    """Custom type nsSchRecurComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsSchRecurComments_Type.__name__ = "DisplayString"
_NsSchRecurComments_Object = MibTableColumn
nsSchRecurComments = _NsSchRecurComments_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 8),
    _NsSchRecurComments_Type()
)
nsSchRecurComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurComments.setStatus("current")


class _NsSchRecurVsys_Type(Integer32):
    """Custom type nsSchRecurVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSchRecurVsys_Type.__name__ = "Integer32"
_NsSchRecurVsys_Object = MibTableColumn
nsSchRecurVsys = _NsSchRecurVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 9),
    _NsSchRecurVsys_Type()
)
nsSchRecurVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSchRecurVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SCHEDULE-MIB",
    **{"netscreenScheduleMibModule": netscreenScheduleMibModule,
       "nsSchOnceTable": nsSchOnceTable,
       "nsSchOnceEntry": nsSchOnceEntry,
       "nsSchOnceIndex": nsSchOnceIndex,
       "nsSchOnceName": nsSchOnceName,
       "nsSchOnceStartTime": nsSchOnceStartTime,
       "nsSchOnceStopTime": nsSchOnceStopTime,
       "nsSchOnceComments": nsSchOnceComments,
       "nsSchOnceVsys": nsSchOnceVsys,
       "nsSchRecurTable": nsSchRecurTable,
       "nsSchRecurEntry": nsSchRecurEntry,
       "nsSchRecurIndex": nsSchRecurIndex,
       "nsSchRecurName": nsSchRecurName,
       "nsSchRecurWeekday": nsSchRecurWeekday,
       "nsSchRecurStartTime1": nsSchRecurStartTime1,
       "nsSchRecurStopTime1": nsSchRecurStopTime1,
       "nsSchRecurStartTime2": nsSchRecurStartTime2,
       "nsSchRecurStopTime2": nsSchRecurStopTime2,
       "nsSchRecurComments": nsSchRecurComments,
       "nsSchRecurVsys": nsSchRecurVsys}
)
