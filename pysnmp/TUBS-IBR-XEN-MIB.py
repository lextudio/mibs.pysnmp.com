# SNMP MIB module (TUBS-IBR-XEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-IBR-XEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:58 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(ibr,) = mibBuilder.importSymbols(
    "TUBS-SMI",
    "ibr")


# MODULE-IDENTITY

xenMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14)
)
xenMIB.setRevisions(
        ("2006-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XenDomainState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("crashed", 5),
          ("dying", 6),
          ("paused", 4),
          ("running", 2),
          ("shutdown", 7),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_XenObjects_ObjectIdentity = ObjectIdentity
xenObjects = _XenObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1)
)
_XenHost_ObjectIdentity = ObjectIdentity
xenHost = _XenHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1)
)
_XenHostXenVersion_Type = SnmpAdminString
_XenHostXenVersion_Object = MibScalar
xenHostXenVersion = _XenHostXenVersion_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 1),
    _XenHostXenVersion_Type()
)
xenHostXenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenHostXenVersion.setStatus("current")
_XenHostTotalMemKBytes_Type = Unsigned32
_XenHostTotalMemKBytes_Object = MibScalar
xenHostTotalMemKBytes = _XenHostTotalMemKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 2),
    _XenHostTotalMemKBytes_Type()
)
xenHostTotalMemKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenHostTotalMemKBytes.setStatus("current")
_XenHostCPUs_Type = Unsigned32
_XenHostCPUs_Object = MibScalar
xenHostCPUs = _XenHostCPUs_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 3),
    _XenHostCPUs_Type()
)
xenHostCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenHostCPUs.setStatus("current")
_XenHostCPUMHz_Type = Unsigned32
_XenHostCPUMHz_Object = MibScalar
xenHostCPUMHz = _XenHostCPUMHz_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 4),
    _XenHostCPUMHz_Type()
)
xenHostCPUMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenHostCPUMHz.setStatus("current")
_XenDomainTable_Object = MibTable
xenDomainTable = _XenDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    xenDomainTable.setStatus("current")
_XenDomainEntry_Object = MibTableRow
xenDomainEntry = _XenDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1)
)
xenDomainEntry.setIndexNames(
    (0, "TUBS-IBR-XEN-MIB", "xenDomainName"),
)
if mibBuilder.loadTexts:
    xenDomainEntry.setStatus("current")


class _XenDomainName_Type(SnmpAdminString):
    """Custom type xenDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_XenDomainName_Type.__name__ = "SnmpAdminString"
_XenDomainName_Object = MibTableColumn
xenDomainName = _XenDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 1),
    _XenDomainName_Type()
)
xenDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xenDomainName.setStatus("current")
_XenDomainState_Type = XenDomainState
_XenDomainState_Object = MibTableColumn
xenDomainState = _XenDomainState_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 2),
    _XenDomainState_Type()
)
xenDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenDomainState.setStatus("current")
_XenDomainMemKBytes_Type = Unsigned32
_XenDomainMemKBytes_Object = MibTableColumn
xenDomainMemKBytes = _XenDomainMemKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 3),
    _XenDomainMemKBytes_Type()
)
xenDomainMemKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenDomainMemKBytes.setStatus("current")
_XenDomainMaxMemKBytes_Type = Unsigned32
_XenDomainMaxMemKBytes_Object = MibTableColumn
xenDomainMaxMemKBytes = _XenDomainMaxMemKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 4),
    _XenDomainMaxMemKBytes_Type()
)
xenDomainMaxMemKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenDomainMaxMemKBytes.setStatus("current")
_XenVCPUTable_Object = MibTable
xenVCPUTable = _XenVCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    xenVCPUTable.setStatus("current")
_XenVCPUEntry_Object = MibTableRow
xenVCPUEntry = _XenVCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1)
)
xenVCPUEntry.setIndexNames(
    (0, "TUBS-IBR-XEN-MIB", "xenDomainName"),
    (0, "TUBS-IBR-XEN-MIB", "xenVCPUIndex"),
)
if mibBuilder.loadTexts:
    xenVCPUEntry.setStatus("current")
_XenVCPUIndex_Type = Unsigned32
_XenVCPUIndex_Object = MibTableColumn
xenVCPUIndex = _XenVCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 1),
    _XenVCPUIndex_Type()
)
xenVCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xenVCPUIndex.setStatus("current")
_XenVCPUMilliseconds_Type = Counter32
_XenVCPUMilliseconds_Object = MibTableColumn
xenVCPUMilliseconds = _XenVCPUMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 2),
    _XenVCPUMilliseconds_Type()
)
xenVCPUMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenVCPUMilliseconds.setStatus("current")
_XenNetworkTable_Object = MibTable
xenNetworkTable = _XenNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    xenNetworkTable.setStatus("current")
_XenNetworkEntry_Object = MibTableRow
xenNetworkEntry = _XenNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1)
)
xenNetworkEntry.setIndexNames(
    (0, "TUBS-IBR-XEN-MIB", "xenDomainName"),
    (0, "TUBS-IBR-XEN-MIB", "xenNetworkIndex"),
)
if mibBuilder.loadTexts:
    xenNetworkEntry.setStatus("current")
_XenNetworkIndex_Type = Unsigned32
_XenNetworkIndex_Object = MibTableColumn
xenNetworkIndex = _XenNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 1),
    _XenNetworkIndex_Type()
)
xenNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xenNetworkIndex.setStatus("current")
_XenNetworkInKBytes_Type = Counter32
_XenNetworkInKBytes_Object = MibTableColumn
xenNetworkInKBytes = _XenNetworkInKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 2),
    _XenNetworkInKBytes_Type()
)
xenNetworkInKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkInKBytes.setStatus("current")
_XenNetworkInPkts_Type = Counter32
_XenNetworkInPkts_Object = MibTableColumn
xenNetworkInPkts = _XenNetworkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 3),
    _XenNetworkInPkts_Type()
)
xenNetworkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkInPkts.setStatus("current")
_XenNetworkInErrors_Type = Counter32
_XenNetworkInErrors_Object = MibTableColumn
xenNetworkInErrors = _XenNetworkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 4),
    _XenNetworkInErrors_Type()
)
xenNetworkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkInErrors.setStatus("current")
_XenNetworkInDiscards_Type = Counter32
_XenNetworkInDiscards_Object = MibTableColumn
xenNetworkInDiscards = _XenNetworkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 5),
    _XenNetworkInDiscards_Type()
)
xenNetworkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkInDiscards.setStatus("current")
_XenNetworkOutKBytes_Type = Counter32
_XenNetworkOutKBytes_Object = MibTableColumn
xenNetworkOutKBytes = _XenNetworkOutKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 6),
    _XenNetworkOutKBytes_Type()
)
xenNetworkOutKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkOutKBytes.setStatus("current")
_XenNetworkOutPkts_Type = Counter32
_XenNetworkOutPkts_Object = MibTableColumn
xenNetworkOutPkts = _XenNetworkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 7),
    _XenNetworkOutPkts_Type()
)
xenNetworkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkOutPkts.setStatus("current")
_XenNetworkOutErrors_Type = Counter32
_XenNetworkOutErrors_Object = MibTableColumn
xenNetworkOutErrors = _XenNetworkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 8),
    _XenNetworkOutErrors_Type()
)
xenNetworkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkOutErrors.setStatus("current")
_XenNetworkOutDiscards_Type = Counter32
_XenNetworkOutDiscards_Object = MibTableColumn
xenNetworkOutDiscards = _XenNetworkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 9),
    _XenNetworkOutDiscards_Type()
)
xenNetworkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNetworkOutDiscards.setStatus("current")
_XenTraps_ObjectIdentity = ObjectIdentity
xenTraps = _XenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 2)
)
_XenConformance_ObjectIdentity = ObjectIdentity
xenConformance = _XenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 3)
)
_XenCompliances_ObjectIdentity = ObjectIdentity
xenCompliances = _XenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1)
)
_XenGroups_ObjectIdentity = ObjectIdentity
xenGroups = _XenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2)
)

# Managed Objects groups

xenGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2, 1)
)
xenGeneralGroup.setObjects(
      *(("TUBS-IBR-XEN-MIB", "xenHostXenVersion"),
        ("TUBS-IBR-XEN-MIB", "xenHostTotalMemKBytes"),
        ("TUBS-IBR-XEN-MIB", "xenHostCPUs"),
        ("TUBS-IBR-XEN-MIB", "xenHostCPUMHz"),
        ("TUBS-IBR-XEN-MIB", "xenDomainState"),
        ("TUBS-IBR-XEN-MIB", "xenDomainMemKBytes"),
        ("TUBS-IBR-XEN-MIB", "xenDomainMaxMemKBytes"),
        ("TUBS-IBR-XEN-MIB", "xenVCPUMilliseconds"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkInKBytes"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkInPkts"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkInErrors"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkInDiscards"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkOutKBytes"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkOutPkts"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkOutErrors"),
        ("TUBS-IBR-XEN-MIB", "xenNetworkOutDiscards"))
)
if mibBuilder.loadTexts:
    xenGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xenCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-IBR-XEN-MIB",
    **{"XenDomainState": XenDomainState,
       "xenMIB": xenMIB,
       "xenObjects": xenObjects,
       "xenHost": xenHost,
       "xenHostXenVersion": xenHostXenVersion,
       "xenHostTotalMemKBytes": xenHostTotalMemKBytes,
       "xenHostCPUs": xenHostCPUs,
       "xenHostCPUMHz": xenHostCPUMHz,
       "xenDomainTable": xenDomainTable,
       "xenDomainEntry": xenDomainEntry,
       "xenDomainName": xenDomainName,
       "xenDomainState": xenDomainState,
       "xenDomainMemKBytes": xenDomainMemKBytes,
       "xenDomainMaxMemKBytes": xenDomainMaxMemKBytes,
       "xenVCPUTable": xenVCPUTable,
       "xenVCPUEntry": xenVCPUEntry,
       "xenVCPUIndex": xenVCPUIndex,
       "xenVCPUMilliseconds": xenVCPUMilliseconds,
       "xenNetworkTable": xenNetworkTable,
       "xenNetworkEntry": xenNetworkEntry,
       "xenNetworkIndex": xenNetworkIndex,
       "xenNetworkInKBytes": xenNetworkInKBytes,
       "xenNetworkInPkts": xenNetworkInPkts,
       "xenNetworkInErrors": xenNetworkInErrors,
       "xenNetworkInDiscards": xenNetworkInDiscards,
       "xenNetworkOutKBytes": xenNetworkOutKBytes,
       "xenNetworkOutPkts": xenNetworkOutPkts,
       "xenNetworkOutErrors": xenNetworkOutErrors,
       "xenNetworkOutDiscards": xenNetworkOutDiscards,
       "xenTraps": xenTraps,
       "xenConformance": xenConformance,
       "xenCompliances": xenCompliances,
       "xenCompliance": xenCompliance,
       "xenGroups": xenGroups,
       "xenGeneralGroup": xenGeneralGroup}
)
