# SNMP MIB module (XEDIA-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XhdlcObjects_ObjectIdentity = ObjectIdentity
xhdlcObjects = _XhdlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1)
)
_XhdlcStatsTable_Object = MibTable
xhdlcStatsTable = _XhdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xhdlcStatsTable.setStatus("current")
_XhdlcStatsEntry_Object = MibTableRow
xhdlcStatsEntry = _XhdlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1)
)
xhdlcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xhdlcStatsEntry.setStatus("current")
_XhdlcStatsOutErrorUnderFlows_Type = Counter32
_XhdlcStatsOutErrorUnderFlows_Object = MibTableColumn
xhdlcStatsOutErrorUnderFlows = _XhdlcStatsOutErrorUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 1),
    _XhdlcStatsOutErrorUnderFlows_Type()
)
xhdlcStatsOutErrorUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xhdlcStatsOutErrorUnderFlows.setStatus("current")
_XhdlcStatsInAborts_Type = Counter32
_XhdlcStatsInAborts_Object = MibTableColumn
xhdlcStatsInAborts = _XhdlcStatsInAborts_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 2),
    _XhdlcStatsInAborts_Type()
)
xhdlcStatsInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xhdlcStatsInAborts.setStatus("current")
_XhdlcStatsInResidualBits_Type = Counter32
_XhdlcStatsInResidualBits_Object = MibTableColumn
xhdlcStatsInResidualBits = _XhdlcStatsInResidualBits_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 3),
    _XhdlcStatsInResidualBits_Type()
)
xhdlcStatsInResidualBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xhdlcStatsInResidualBits.setStatus("current")
_XhdlcStatsInInvalidLen_Type = Counter32
_XhdlcStatsInInvalidLen_Object = MibTableColumn
xhdlcStatsInInvalidLen = _XhdlcStatsInInvalidLen_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 4),
    _XhdlcStatsInInvalidLen_Type()
)
xhdlcStatsInInvalidLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xhdlcStatsInInvalidLen.setStatus("current")
_XhdlcStatsInOverrun_Type = Counter32
_XhdlcStatsInOverrun_Object = MibTableColumn
xhdlcStatsInOverrun = _XhdlcStatsInOverrun_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 5),
    _XhdlcStatsInOverrun_Type()
)
xhdlcStatsInOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xhdlcStatsInOverrun.setStatus("current")
_XhdlcConfigTable_Object = MibTable
xhdlcConfigTable = _XhdlcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    xhdlcConfigTable.setStatus("current")
_XhdlcConfigEntry_Object = MibTableRow
xhdlcConfigEntry = _XhdlcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1)
)
xhdlcConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xhdlcConfigEntry.setStatus("current")


class _XhdlcConfigClocking_Type(Integer32):
    """Custom type xhdlcConfigClocking based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loopback", 3))
    )


_XhdlcConfigClocking_Type.__name__ = "Integer32"
_XhdlcConfigClocking_Object = MibTableColumn
xhdlcConfigClocking = _XhdlcConfigClocking_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1, 1),
    _XhdlcConfigClocking_Type()
)
xhdlcConfigClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xhdlcConfigClocking.setStatus("current")


class _XhdlcConfigCrcMode_Type(Integer32):
    """Custom type xhdlcConfigCrcMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2),
          ("crcnone", 3))
    )


_XhdlcConfigCrcMode_Type.__name__ = "Integer32"
_XhdlcConfigCrcMode_Object = MibTableColumn
xhdlcConfigCrcMode = _XhdlcConfigCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1, 2),
    _XhdlcConfigCrcMode_Type()
)
xhdlcConfigCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xhdlcConfigCrcMode.setStatus("current")
_XhdlcConformance_ObjectIdentity = ObjectIdentity
xhdlcConformance = _XhdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 2)
)
_XhdlcCompliances_ObjectIdentity = ObjectIdentity
xhdlcCompliances = _XhdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 1)
)
_XhdlcGroups_ObjectIdentity = ObjectIdentity
xhdlcGroups = _XhdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 2)
)

# Managed Objects groups

xhdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 2, 1)
)
xhdlcGroup.setObjects(
      *(("XEDIA-HDLC-MIB", "xhdlcStatsOutErrorUnderFlows"),
        ("XEDIA-HDLC-MIB", "xhdlcStatsInAborts"),
        ("XEDIA-HDLC-MIB", "xhdlcStatsInResidualBits"),
        ("XEDIA-HDLC-MIB", "xhdlcStatsInInvalidLen"),
        ("XEDIA-HDLC-MIB", "xhdlcStatsInOverrun"),
        ("XEDIA-HDLC-MIB", "xhdlcConfigClocking"),
        ("XEDIA-HDLC-MIB", "xhdlcConfigCrcMode"))
)
if mibBuilder.loadTexts:
    xhdlcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xhdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xhdlcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-HDLC-MIB",
    **{"xediaHdlcMIB": xediaHdlcMIB,
       "xhdlcObjects": xhdlcObjects,
       "xhdlcStatsTable": xhdlcStatsTable,
       "xhdlcStatsEntry": xhdlcStatsEntry,
       "xhdlcStatsOutErrorUnderFlows": xhdlcStatsOutErrorUnderFlows,
       "xhdlcStatsInAborts": xhdlcStatsInAborts,
       "xhdlcStatsInResidualBits": xhdlcStatsInResidualBits,
       "xhdlcStatsInInvalidLen": xhdlcStatsInInvalidLen,
       "xhdlcStatsInOverrun": xhdlcStatsInOverrun,
       "xhdlcConfigTable": xhdlcConfigTable,
       "xhdlcConfigEntry": xhdlcConfigEntry,
       "xhdlcConfigClocking": xhdlcConfigClocking,
       "xhdlcConfigCrcMode": xhdlcConfigCrcMode,
       "xhdlcConformance": xhdlcConformance,
       "xhdlcCompliances": xhdlcCompliances,
       "xhdlcCompliance": xhdlcCompliance,
       "xhdlcGroups": xhdlcGroups,
       "xhdlcGroup": xhdlcGroup}
)
