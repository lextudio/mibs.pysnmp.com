# SNMP MIB module (NETSCREEN-IP-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-IP-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:45 2024
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

(netscreenIp,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenIp")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nsIpArp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1)
)
nsIpArp.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NsIpArpAOD_Type(Integer32):
    """Custom type nsIpArpAOD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIpArpAOD_Type.__name__ = "Integer32"
_NsIpArpAOD_Object = MibScalar
nsIpArpAOD = _NsIpArpAOD_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 1),
    _NsIpArpAOD_Type()
)
nsIpArpAOD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsIpArpAOD.setStatus("current")


class _NsIpArpCachUpdate_Type(Integer32):
    """Custom type nsIpArpCachUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsIpArpCachUpdate_Type.__name__ = "Integer32"
_NsIpArpCachUpdate_Object = MibScalar
nsIpArpCachUpdate = _NsIpArpCachUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 2),
    _NsIpArpCachUpdate_Type()
)
nsIpArpCachUpdate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsIpArpCachUpdate.setStatus("current")
_NsIpArpTable_Object = MibTable
nsIpArpTable = _NsIpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3)
)
if mibBuilder.loadTexts:
    nsIpArpTable.setStatus("current")
_NsIpArpEntry_Object = MibTableRow
nsIpArpEntry = _NsIpArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1)
)
nsIpArpEntry.setIndexNames(
    (0, "NETSCREEN-IP-ARP-MIB", "nsIpArpIndex"),
)
if mibBuilder.loadTexts:
    nsIpArpEntry.setStatus("current")


class _NsIpArpIndex_Type(Integer32):
    """Custom type nsIpArpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIpArpIndex_Type.__name__ = "Integer32"
_NsIpArpIndex_Object = MibTableColumn
nsIpArpIndex = _NsIpArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 1),
    _NsIpArpIndex_Type()
)
nsIpArpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpIndex.setStatus("current")
_NsIpArpIp_Type = IpAddress
_NsIpArpIp_Object = MibTableColumn
nsIpArpIp = _NsIpArpIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 2),
    _NsIpArpIp_Type()
)
nsIpArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpIp.setStatus("current")
_NsIpArpMac_Type = PhysAddress
_NsIpArpMac_Object = MibTableColumn
nsIpArpMac = _NsIpArpMac_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 3),
    _NsIpArpMac_Type()
)
nsIpArpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpMac.setStatus("current")
_NsIpArpVsys_Type = Integer32
_NsIpArpVsys_Object = MibTableColumn
nsIpArpVsys = _NsIpArpVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 4),
    _NsIpArpVsys_Type()
)
nsIpArpVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpVsys.setStatus("current")
_NsIpArpIfIdx_Type = Integer32
_NsIpArpIfIdx_Object = MibTableColumn
nsIpArpIfIdx = _NsIpArpIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 5),
    _NsIpArpIfIdx_Type()
)
nsIpArpIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpIfIdx.setStatus("current")


class _NsIpArpState_Type(Integer32):
    """Custom type nsIpArpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("pending", 1),
          ("static", 4),
          ("valid", 2))
    )


_NsIpArpState_Type.__name__ = "Integer32"
_NsIpArpState_Object = MibTableColumn
nsIpArpState = _NsIpArpState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 6),
    _NsIpArpState_Type()
)
nsIpArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpState.setStatus("current")
_NsIpArpAge_Type = Integer32
_NsIpArpAge_Object = MibTableColumn
nsIpArpAge = _NsIpArpAge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 7),
    _NsIpArpAge_Type()
)
nsIpArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpAge.setStatus("current")
_NsIpArpRetry_Type = Integer32
_NsIpArpRetry_Object = MibTableColumn
nsIpArpRetry = _NsIpArpRetry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 8),
    _NsIpArpRetry_Type()
)
nsIpArpRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpRetry.setStatus("current")
_NsIpArpPakQue_Type = Integer32
_NsIpArpPakQue_Object = MibTableColumn
nsIpArpPakQue = _NsIpArpPakQue_Object(
    (1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 9),
    _NsIpArpPakQue_Type()
)
nsIpArpPakQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpArpPakQue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-IP-ARP-MIB",
    **{"nsIpArp": nsIpArp,
       "nsIpArpAOD": nsIpArpAOD,
       "nsIpArpCachUpdate": nsIpArpCachUpdate,
       "nsIpArpTable": nsIpArpTable,
       "nsIpArpEntry": nsIpArpEntry,
       "nsIpArpIndex": nsIpArpIndex,
       "nsIpArpIp": nsIpArpIp,
       "nsIpArpMac": nsIpArpMac,
       "nsIpArpVsys": nsIpArpVsys,
       "nsIpArpIfIdx": nsIpArpIfIdx,
       "nsIpArpState": nsIpArpState,
       "nsIpArpAge": nsIpArpAge,
       "nsIpArpRetry": nsIpArpRetry,
       "nsIpArpPakQue": nsIpArpPakQue}
)
