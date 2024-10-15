# SNMP MIB module (CISCO-LOCAL-DIRECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LOCAL-DIRECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:07 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoLocalDirectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99)
)
ciscoLocalDirectorMIB.setRevisions(
        ("2001-05-14 00:00",
         "1999-10-21 00:00",
         "1999-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CldMachineState(Integer32, TextualConvention):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("externalFailed", 8),
          ("failed", 4),
          ("inService", 1),
          ("maintenance", 6),
          ("maxCapacity", 5),
          ("outOfService", 2),
          ("stickyOnly", 7),
          ("testing", 3))
    )



class CldFailoverEnabledState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failoverOff", 2),
          ("failoverOn", 1))
    )



class CldFailoverCableState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badCable", 5),
          ("mySideNotConnected", 3),
          ("normalConnected", 1),
          ("otherSideNotConnected", 4),
          ("otherSidePoweredOff", 2))
    )



class CldFailoverUnitTypeDescriptor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class CldFailoverUnitStatusDescriptor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class MachineProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17,
              47)
        )
    )
    namedValues = NamedValues(
        *(("protocolTypeAll", 0),
          ("protocolTypeGRE", 47),
          ("protocolTypeTCP", 6),
          ("protocolTypeUDP", 17))
    )



class MachineBindID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLocalDirectorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBObjects = _CiscoLocalDirectorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1)
)
_CldVirtualMachine_ObjectIdentity = ObjectIdentity
cldVirtualMachine = _CldVirtualMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1)
)
_CldVirtualTable_Object = MibTable
cldVirtualTable = _CldVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldVirtualTable.setStatus("obsolete")
_CldVirtualTableEntry_Object = MibTableRow
cldVirtualTableEntry = _CldVirtualTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1)
)
cldVirtualTableEntry.setIndexNames(
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualIpAddress"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualPort"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualBindID"),
)
if mibBuilder.loadTexts:
    cldVirtualTableEntry.setStatus("obsolete")
_CldVirtualIpAddress_Type = IpAddress
_CldVirtualIpAddress_Object = MibTableColumn
cldVirtualIpAddress = _CldVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 1),
    _CldVirtualIpAddress_Type()
)
cldVirtualIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldVirtualIpAddress.setStatus("obsolete")


class _CldVirtualPort_Type(Integer32):
    """Custom type cldVirtualPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldVirtualPort_Type.__name__ = "Integer32"
_CldVirtualPort_Object = MibTableColumn
cldVirtualPort = _CldVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 2),
    _CldVirtualPort_Type()
)
cldVirtualPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldVirtualPort.setStatus("obsolete")


class _CldVirtualBindID_Type(Integer32):
    """Custom type cldVirtualBindID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldVirtualBindID_Type.__name__ = "Integer32"
_CldVirtualBindID_Object = MibTableColumn
cldVirtualBindID = _CldVirtualBindID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 3),
    _CldVirtualBindID_Type()
)
cldVirtualBindID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldVirtualBindID.setStatus("obsolete")
_CldVirtualState_Type = CldMachineState
_CldVirtualState_Object = MibTableColumn
cldVirtualState = _CldVirtualState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 4),
    _CldVirtualState_Type()
)
cldVirtualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVirtualState.setStatus("obsolete")
_CldVirtualTotalConnections_Type = Counter32
_CldVirtualTotalConnections_Object = MibTableColumn
cldVirtualTotalConnections = _CldVirtualTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 5),
    _CldVirtualTotalConnections_Type()
)
cldVirtualTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVirtualTotalConnections.setStatus("obsolete")
_CldVirtualTotalPackets_Type = Counter32
_CldVirtualTotalPackets_Object = MibTableColumn
cldVirtualTotalPackets = _CldVirtualTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 6),
    _CldVirtualTotalPackets_Type()
)
cldVirtualTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVirtualTotalPackets.setStatus("obsolete")
_CldVirtualTotalBytes_Type = Counter32
_CldVirtualTotalBytes_Object = MibTableColumn
cldVirtualTotalBytes = _CldVirtualTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 7),
    _CldVirtualTotalBytes_Type()
)
cldVirtualTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVirtualTotalBytes.setStatus("obsolete")


class _CldVirtualWeight_Type(Integer32):
    """Custom type cldVirtualWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CldVirtualWeight_Type.__name__ = "Integer32"
_CldVirtualWeight_Object = MibTableColumn
cldVirtualWeight = _CldVirtualWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 8),
    _CldVirtualWeight_Type()
)
cldVirtualWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVirtualWeight.setStatus("obsolete")
_CldeVirtualTable_Object = MibTable
cldeVirtualTable = _CldeVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cldeVirtualTable.setStatus("deprecated")
_CldeVirtualTableEntry_Object = MibTableRow
cldeVirtualTableEntry = _CldeVirtualTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1)
)
cldeVirtualTableEntry.setIndexNames(
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualIpAddress"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualPort"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualBindID"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualProtocol"),
)
if mibBuilder.loadTexts:
    cldeVirtualTableEntry.setStatus("deprecated")
_CldeVirtualIpAddress_Type = IpAddress
_CldeVirtualIpAddress_Object = MibTableColumn
cldeVirtualIpAddress = _CldeVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 1),
    _CldeVirtualIpAddress_Type()
)
cldeVirtualIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeVirtualIpAddress.setStatus("deprecated")


class _CldeVirtualPort_Type(Integer32):
    """Custom type cldeVirtualPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldeVirtualPort_Type.__name__ = "Integer32"
_CldeVirtualPort_Object = MibTableColumn
cldeVirtualPort = _CldeVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 2),
    _CldeVirtualPort_Type()
)
cldeVirtualPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeVirtualPort.setStatus("deprecated")


class _CldeVirtualBindID_Type(Integer32):
    """Custom type cldeVirtualBindID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldeVirtualBindID_Type.__name__ = "Integer32"
_CldeVirtualBindID_Object = MibTableColumn
cldeVirtualBindID = _CldeVirtualBindID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 3),
    _CldeVirtualBindID_Type()
)
cldeVirtualBindID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeVirtualBindID.setStatus("deprecated")
_CldeVirtualProtocol_Type = MachineProtocol
_CldeVirtualProtocol_Object = MibTableColumn
cldeVirtualProtocol = _CldeVirtualProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 4),
    _CldeVirtualProtocol_Type()
)
cldeVirtualProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeVirtualProtocol.setStatus("deprecated")
_CldeVirtualState_Type = CldMachineState
_CldeVirtualState_Object = MibTableColumn
cldeVirtualState = _CldeVirtualState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 5),
    _CldeVirtualState_Type()
)
cldeVirtualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeVirtualState.setStatus("deprecated")
_CldeVirtualTotalConnections_Type = Counter32
_CldeVirtualTotalConnections_Object = MibTableColumn
cldeVirtualTotalConnections = _CldeVirtualTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 6),
    _CldeVirtualTotalConnections_Type()
)
cldeVirtualTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeVirtualTotalConnections.setStatus("deprecated")
_CldeVirtualTotalPackets_Type = Counter32
_CldeVirtualTotalPackets_Object = MibTableColumn
cldeVirtualTotalPackets = _CldeVirtualTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 7),
    _CldeVirtualTotalPackets_Type()
)
cldeVirtualTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeVirtualTotalPackets.setStatus("deprecated")
_CldeVirtualTotalBytes_Type = Counter32
_CldeVirtualTotalBytes_Object = MibTableColumn
cldeVirtualTotalBytes = _CldeVirtualTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 8),
    _CldeVirtualTotalBytes_Type()
)
cldeVirtualTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeVirtualTotalBytes.setStatus("deprecated")


class _CldeVirtualWeight_Type(Integer32):
    """Custom type cldeVirtualWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CldeVirtualWeight_Type.__name__ = "Integer32"
_CldeVirtualWeight_Object = MibTableColumn
cldeVirtualWeight = _CldeVirtualWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 2, 1, 9),
    _CldeVirtualWeight_Type()
)
cldeVirtualWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeVirtualWeight.setStatus("deprecated")
_CldexVirtualTable_Object = MibTable
cldexVirtualTable = _CldexVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cldexVirtualTable.setStatus("current")
_CldexVirtualTableEntry_Object = MibTableRow
cldexVirtualTableEntry = _CldexVirtualTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1)
)
cldexVirtualTableEntry.setIndexNames(
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualIpAddress"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualPort"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualBindID"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualProtocol"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualRule"),
)
if mibBuilder.loadTexts:
    cldexVirtualTableEntry.setStatus("current")
_CldexVirtualIpAddress_Type = IpAddress
_CldexVirtualIpAddress_Object = MibTableColumn
cldexVirtualIpAddress = _CldexVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 1),
    _CldexVirtualIpAddress_Type()
)
cldexVirtualIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldexVirtualIpAddress.setStatus("current")


class _CldexVirtualPort_Type(Integer32):
    """Custom type cldexVirtualPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldexVirtualPort_Type.__name__ = "Integer32"
_CldexVirtualPort_Object = MibTableColumn
cldexVirtualPort = _CldexVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 2),
    _CldexVirtualPort_Type()
)
cldexVirtualPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldexVirtualPort.setStatus("current")


class _CldexVirtualBindID_Type(Integer32):
    """Custom type cldexVirtualBindID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldexVirtualBindID_Type.__name__ = "Integer32"
_CldexVirtualBindID_Object = MibTableColumn
cldexVirtualBindID = _CldexVirtualBindID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 3),
    _CldexVirtualBindID_Type()
)
cldexVirtualBindID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldexVirtualBindID.setStatus("current")
_CldexVirtualProtocol_Type = MachineProtocol
_CldexVirtualProtocol_Object = MibTableColumn
cldexVirtualProtocol = _CldexVirtualProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 4),
    _CldexVirtualProtocol_Type()
)
cldexVirtualProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldexVirtualProtocol.setStatus("current")


class _CldexVirtualRule_Type(SnmpAdminString):
    """Custom type cldexVirtualRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CldexVirtualRule_Type.__name__ = "SnmpAdminString"
_CldexVirtualRule_Object = MibTableColumn
cldexVirtualRule = _CldexVirtualRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 5),
    _CldexVirtualRule_Type()
)
cldexVirtualRule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldexVirtualRule.setStatus("current")
_CldexVirtualState_Type = CldMachineState
_CldexVirtualState_Object = MibTableColumn
cldexVirtualState = _CldexVirtualState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 6),
    _CldexVirtualState_Type()
)
cldexVirtualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldexVirtualState.setStatus("current")
_CldexVirtualTotalConnections_Type = Counter32
_CldexVirtualTotalConnections_Object = MibTableColumn
cldexVirtualTotalConnections = _CldexVirtualTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 7),
    _CldexVirtualTotalConnections_Type()
)
cldexVirtualTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldexVirtualTotalConnections.setStatus("current")
_CldexVirtualTotalPackets_Type = Counter32
_CldexVirtualTotalPackets_Object = MibTableColumn
cldexVirtualTotalPackets = _CldexVirtualTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 8),
    _CldexVirtualTotalPackets_Type()
)
cldexVirtualTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldexVirtualTotalPackets.setStatus("current")
_CldexVirtualTotalBytes_Type = Counter32
_CldexVirtualTotalBytes_Object = MibTableColumn
cldexVirtualTotalBytes = _CldexVirtualTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 9),
    _CldexVirtualTotalBytes_Type()
)
cldexVirtualTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldexVirtualTotalBytes.setStatus("current")


class _CldexVirtualWeight_Type(Integer32):
    """Custom type cldexVirtualWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CldexVirtualWeight_Type.__name__ = "Integer32"
_CldexVirtualWeight_Object = MibTableColumn
cldexVirtualWeight = _CldexVirtualWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 3, 1, 10),
    _CldexVirtualWeight_Type()
)
cldexVirtualWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldexVirtualWeight.setStatus("current")
_CldRealMachine_ObjectIdentity = ObjectIdentity
cldRealMachine = _CldRealMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2)
)
_CldRealTable_Object = MibTable
cldRealTable = _CldRealTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldRealTable.setStatus("obsolete")
_CldRealTableEntry_Object = MibTableRow
cldRealTableEntry = _CldRealTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1)
)
cldRealTableEntry.setIndexNames(
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldRealIpAddress"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldRealPort"),
)
if mibBuilder.loadTexts:
    cldRealTableEntry.setStatus("obsolete")
_CldRealIpAddress_Type = IpAddress
_CldRealIpAddress_Object = MibTableColumn
cldRealIpAddress = _CldRealIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 1),
    _CldRealIpAddress_Type()
)
cldRealIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldRealIpAddress.setStatus("obsolete")


class _CldRealPort_Type(Integer32):
    """Custom type cldRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldRealPort_Type.__name__ = "Integer32"
_CldRealPort_Object = MibTableColumn
cldRealPort = _CldRealPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 2),
    _CldRealPort_Type()
)
cldRealPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldRealPort.setStatus("obsolete")
_CldRealState_Type = CldMachineState
_CldRealState_Object = MibTableColumn
cldRealState = _CldRealState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 3),
    _CldRealState_Type()
)
cldRealState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRealState.setStatus("obsolete")
_CldRealTotalConnections_Type = Counter32
_CldRealTotalConnections_Object = MibTableColumn
cldRealTotalConnections = _CldRealTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 4),
    _CldRealTotalConnections_Type()
)
cldRealTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRealTotalConnections.setStatus("obsolete")
_CldRealTotalPackets_Type = Counter32
_CldRealTotalPackets_Object = MibTableColumn
cldRealTotalPackets = _CldRealTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 5),
    _CldRealTotalPackets_Type()
)
cldRealTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRealTotalPackets.setStatus("obsolete")
_CldRealTotalBytes_Type = Counter32
_CldRealTotalBytes_Object = MibTableColumn
cldRealTotalBytes = _CldRealTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 6),
    _CldRealTotalBytes_Type()
)
cldRealTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRealTotalBytes.setStatus("obsolete")


class _CldRealWeight_Type(Integer32):
    """Custom type cldRealWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CldRealWeight_Type.__name__ = "Integer32"
_CldRealWeight_Object = MibTableColumn
cldRealWeight = _CldRealWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 7),
    _CldRealWeight_Type()
)
cldRealWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldRealWeight.setStatus("obsolete")
_CldeRealTable_Object = MibTable
cldeRealTable = _CldeRealTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cldeRealTable.setStatus("current")
_CldeRealTableEntry_Object = MibTableRow
cldeRealTableEntry = _CldeRealTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1)
)
cldeRealTableEntry.setIndexNames(
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeRealIpAddress"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeRealPort"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeRealBindID"),
    (0, "CISCO-LOCAL-DIRECTOR-MIB", "cldeRealProtocol"),
)
if mibBuilder.loadTexts:
    cldeRealTableEntry.setStatus("current")
_CldeRealIpAddress_Type = IpAddress
_CldeRealIpAddress_Object = MibTableColumn
cldeRealIpAddress = _CldeRealIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 1),
    _CldeRealIpAddress_Type()
)
cldeRealIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeRealIpAddress.setStatus("current")


class _CldeRealPort_Type(Integer32):
    """Custom type cldeRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldeRealPort_Type.__name__ = "Integer32"
_CldeRealPort_Object = MibTableColumn
cldeRealPort = _CldeRealPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 2),
    _CldeRealPort_Type()
)
cldeRealPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeRealPort.setStatus("current")
_CldeRealBindID_Type = MachineBindID
_CldeRealBindID_Object = MibTableColumn
cldeRealBindID = _CldeRealBindID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 3),
    _CldeRealBindID_Type()
)
cldeRealBindID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeRealBindID.setStatus("current")
_CldeRealProtocol_Type = MachineProtocol
_CldeRealProtocol_Object = MibTableColumn
cldeRealProtocol = _CldeRealProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 4),
    _CldeRealProtocol_Type()
)
cldeRealProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldeRealProtocol.setStatus("current")
_CldeRealState_Type = CldMachineState
_CldeRealState_Object = MibTableColumn
cldeRealState = _CldeRealState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 5),
    _CldeRealState_Type()
)
cldeRealState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeRealState.setStatus("current")
_CldeRealTotalConnections_Type = Counter32
_CldeRealTotalConnections_Object = MibTableColumn
cldeRealTotalConnections = _CldeRealTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 6),
    _CldeRealTotalConnections_Type()
)
cldeRealTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeRealTotalConnections.setStatus("current")
_CldeRealTotalPackets_Type = Counter32
_CldeRealTotalPackets_Object = MibTableColumn
cldeRealTotalPackets = _CldeRealTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 7),
    _CldeRealTotalPackets_Type()
)
cldeRealTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeRealTotalPackets.setStatus("current")
_CldeRealTotalBytes_Type = Counter32
_CldeRealTotalBytes_Object = MibTableColumn
cldeRealTotalBytes = _CldeRealTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 8),
    _CldeRealTotalBytes_Type()
)
cldeRealTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldeRealTotalBytes.setStatus("current")


class _CldeRealWeight_Type(Integer32):
    """Custom type cldeRealWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CldeRealWeight_Type.__name__ = "Integer32"
_CldeRealWeight_Object = MibTableColumn
cldeRealWeight = _CldeRealWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 2, 1, 9),
    _CldeRealWeight_Type()
)
cldeRealWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldeRealWeight.setStatus("current")
_CldFailover_ObjectIdentity = ObjectIdentity
cldFailover = _CldFailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3)
)
_CldFailoverEnabled_Type = CldFailoverEnabledState
_CldFailoverEnabled_Object = MibScalar
cldFailoverEnabled = _CldFailoverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 1),
    _CldFailoverEnabled_Type()
)
cldFailoverEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldFailoverEnabled.setStatus("current")
_CldFailoverCableStatus_Type = CldFailoverCableState
_CldFailoverCableStatus_Object = MibScalar
cldFailoverCableStatus = _CldFailoverCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 2),
    _CldFailoverCableStatus_Type()
)
cldFailoverCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldFailoverCableStatus.setStatus("current")
_CldFailoverUnitType_Type = CldFailoverUnitTypeDescriptor
_CldFailoverUnitType_Object = MibScalar
cldFailoverUnitType = _CldFailoverUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 3),
    _CldFailoverUnitType_Type()
)
cldFailoverUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldFailoverUnitType.setStatus("current")
_CldFailoverUnitStatus_Type = CldFailoverUnitStatusDescriptor
_CldFailoverUnitStatus_Object = MibScalar
cldFailoverUnitStatus = _CldFailoverUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 4),
    _CldFailoverUnitStatus_Type()
)
cldFailoverUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldFailoverUnitStatus.setStatus("current")
_CldFailoverActiveTimeStamp_Type = TimeStamp
_CldFailoverActiveTimeStamp_Object = MibScalar
cldFailoverActiveTimeStamp = _CldFailoverActiveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 5),
    _CldFailoverActiveTimeStamp_Type()
)
cldFailoverActiveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldFailoverActiveTimeStamp.setStatus("current")
_CiscoLocalDirectorMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBNotificationPrefix = _CiscoLocalDirectorMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2)
)
_CiscoLocalDirectorMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBNotifications = _CiscoLocalDirectorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0)
)
_CiscoLocalDirectorMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBConformance = _CiscoLocalDirectorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3)
)
_CiscoLocalDirectorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBCompliances = _CiscoLocalDirectorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 1)
)
_CiscoLocalDirectorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLocalDirectorMIBGroups = _CiscoLocalDirectorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2)
)

# Managed Objects groups

ciscoLocalDirectorMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 1)
)
ciscoLocalDirectorMIBGroup.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualWeight"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealWeight"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorMIBGroup.setStatus("obsolete")

ciscoLocalDirectorFailoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 2)
)
ciscoLocalDirectorFailoverGroup.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverEnabled"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverCableStatus"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverUnitType"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverUnitStatus"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverActiveTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorFailoverGroup.setStatus("current")

ciscoLocalDirectorEMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 3)
)
ciscoLocalDirectorEMIBGroup.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualWeight"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealWeight"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorEMIBGroup.setStatus("deprecated")

ciscoLocalDirectorEMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 6)
)
ciscoLocalDirectorEMIBGroupRev1.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualWeight"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealState"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalConnections"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalPackets"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealTotalBytes"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealWeight"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorEMIBGroupRev1.setStatus("current")


# Notification objects

ciscoLocalDirectorVirtualStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 1)
)
ciscoLocalDirectorVirtualStateChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldVirtualState")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorVirtualStateChange.setStatus(
        "obsolete"
    )

ciscoLocalDirectorRealStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 2)
)
ciscoLocalDirectorRealStateChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldRealState")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorRealStateChange.setStatus(
        "obsolete"
    )

ciscoLocalDirectorFailoverEnableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 3)
)
ciscoLocalDirectorFailoverEnableChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverEnabled")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorFailoverEnableChange.setStatus(
        "current"
    )

ciscoLocalDirectorFailoverCableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 4)
)
ciscoLocalDirectorFailoverCableChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverCableStatus")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorFailoverCableChange.setStatus(
        "current"
    )

ciscoLocalDirectorFailoverUnitStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 5)
)
ciscoLocalDirectorFailoverUnitStatus.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldFailoverUnitStatus")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorFailoverUnitStatus.setStatus(
        "current"
    )

ciscoLocalDirectorEVirtualStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 6)
)
ciscoLocalDirectorEVirtualStateChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldeVirtualState")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorEVirtualStateChange.setStatus(
        "deprecated"
    )

ciscoLocalDirectorERealStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 7)
)
ciscoLocalDirectorERealStateChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldeRealState")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorERealStateChange.setStatus(
        "current"
    )

ciscoLocalDirectorExVirtualStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 8)
)
ciscoLocalDirectorExVirtualStateChange.setObjects(
    ("CISCO-LOCAL-DIRECTOR-MIB", "cldexVirtualState")
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorExVirtualStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoLocalDirectorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 4)
)
ciscoLocalDirectorNotificationGroup.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorVirtualStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorRealStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverEnableChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverCableChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverUnitStatus"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorNotificationGroup.setStatus(
        "obsolete"
    )

ciscoLocalDirectorNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 5)
)
ciscoLocalDirectorNotificationGroupRev1.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorEVirtualStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorERealStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverEnableChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverCableChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverUnitStatus"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorNotificationGroupRev1.setStatus(
        "deprecated"
    )

ciscoLocalDirectorNotificationGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 7)
)
ciscoLocalDirectorNotificationGroupRev2.setObjects(
      *(("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorExVirtualStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorERealStateChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverEnableChange"),
        ("CISCO-LOCAL-DIRECTOR-MIB", "ciscoLocalDirectorFailoverCableChange"))
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorNotificationGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLocalDirectorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLocalDirectorMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LOCAL-DIRECTOR-MIB",
    **{"CldMachineState": CldMachineState,
       "CldFailoverEnabledState": CldFailoverEnabledState,
       "CldFailoverCableState": CldFailoverCableState,
       "CldFailoverUnitTypeDescriptor": CldFailoverUnitTypeDescriptor,
       "CldFailoverUnitStatusDescriptor": CldFailoverUnitStatusDescriptor,
       "MachineProtocol": MachineProtocol,
       "MachineBindID": MachineBindID,
       "ciscoLocalDirectorMIB": ciscoLocalDirectorMIB,
       "ciscoLocalDirectorMIBObjects": ciscoLocalDirectorMIBObjects,
       "cldVirtualMachine": cldVirtualMachine,
       "cldVirtualTable": cldVirtualTable,
       "cldVirtualTableEntry": cldVirtualTableEntry,
       "cldVirtualIpAddress": cldVirtualIpAddress,
       "cldVirtualPort": cldVirtualPort,
       "cldVirtualBindID": cldVirtualBindID,
       "cldVirtualState": cldVirtualState,
       "cldVirtualTotalConnections": cldVirtualTotalConnections,
       "cldVirtualTotalPackets": cldVirtualTotalPackets,
       "cldVirtualTotalBytes": cldVirtualTotalBytes,
       "cldVirtualWeight": cldVirtualWeight,
       "cldeVirtualTable": cldeVirtualTable,
       "cldeVirtualTableEntry": cldeVirtualTableEntry,
       "cldeVirtualIpAddress": cldeVirtualIpAddress,
       "cldeVirtualPort": cldeVirtualPort,
       "cldeVirtualBindID": cldeVirtualBindID,
       "cldeVirtualProtocol": cldeVirtualProtocol,
       "cldeVirtualState": cldeVirtualState,
       "cldeVirtualTotalConnections": cldeVirtualTotalConnections,
       "cldeVirtualTotalPackets": cldeVirtualTotalPackets,
       "cldeVirtualTotalBytes": cldeVirtualTotalBytes,
       "cldeVirtualWeight": cldeVirtualWeight,
       "cldexVirtualTable": cldexVirtualTable,
       "cldexVirtualTableEntry": cldexVirtualTableEntry,
       "cldexVirtualIpAddress": cldexVirtualIpAddress,
       "cldexVirtualPort": cldexVirtualPort,
       "cldexVirtualBindID": cldexVirtualBindID,
       "cldexVirtualProtocol": cldexVirtualProtocol,
       "cldexVirtualRule": cldexVirtualRule,
       "cldexVirtualState": cldexVirtualState,
       "cldexVirtualTotalConnections": cldexVirtualTotalConnections,
       "cldexVirtualTotalPackets": cldexVirtualTotalPackets,
       "cldexVirtualTotalBytes": cldexVirtualTotalBytes,
       "cldexVirtualWeight": cldexVirtualWeight,
       "cldRealMachine": cldRealMachine,
       "cldRealTable": cldRealTable,
       "cldRealTableEntry": cldRealTableEntry,
       "cldRealIpAddress": cldRealIpAddress,
       "cldRealPort": cldRealPort,
       "cldRealState": cldRealState,
       "cldRealTotalConnections": cldRealTotalConnections,
       "cldRealTotalPackets": cldRealTotalPackets,
       "cldRealTotalBytes": cldRealTotalBytes,
       "cldRealWeight": cldRealWeight,
       "cldeRealTable": cldeRealTable,
       "cldeRealTableEntry": cldeRealTableEntry,
       "cldeRealIpAddress": cldeRealIpAddress,
       "cldeRealPort": cldeRealPort,
       "cldeRealBindID": cldeRealBindID,
       "cldeRealProtocol": cldeRealProtocol,
       "cldeRealState": cldeRealState,
       "cldeRealTotalConnections": cldeRealTotalConnections,
       "cldeRealTotalPackets": cldeRealTotalPackets,
       "cldeRealTotalBytes": cldeRealTotalBytes,
       "cldeRealWeight": cldeRealWeight,
       "cldFailover": cldFailover,
       "cldFailoverEnabled": cldFailoverEnabled,
       "cldFailoverCableStatus": cldFailoverCableStatus,
       "cldFailoverUnitType": cldFailoverUnitType,
       "cldFailoverUnitStatus": cldFailoverUnitStatus,
       "cldFailoverActiveTimeStamp": cldFailoverActiveTimeStamp,
       "ciscoLocalDirectorMIBNotificationPrefix": ciscoLocalDirectorMIBNotificationPrefix,
       "ciscoLocalDirectorMIBNotifications": ciscoLocalDirectorMIBNotifications,
       "ciscoLocalDirectorVirtualStateChange": ciscoLocalDirectorVirtualStateChange,
       "ciscoLocalDirectorRealStateChange": ciscoLocalDirectorRealStateChange,
       "ciscoLocalDirectorFailoverEnableChange": ciscoLocalDirectorFailoverEnableChange,
       "ciscoLocalDirectorFailoverCableChange": ciscoLocalDirectorFailoverCableChange,
       "ciscoLocalDirectorFailoverUnitStatus": ciscoLocalDirectorFailoverUnitStatus,
       "ciscoLocalDirectorEVirtualStateChange": ciscoLocalDirectorEVirtualStateChange,
       "ciscoLocalDirectorERealStateChange": ciscoLocalDirectorERealStateChange,
       "ciscoLocalDirectorExVirtualStateChange": ciscoLocalDirectorExVirtualStateChange,
       "ciscoLocalDirectorMIBConformance": ciscoLocalDirectorMIBConformance,
       "ciscoLocalDirectorMIBCompliances": ciscoLocalDirectorMIBCompliances,
       "ciscoLocalDirectorMIBCompliance": ciscoLocalDirectorMIBCompliance,
       "ciscoLocalDirectorMIBGroups": ciscoLocalDirectorMIBGroups,
       "ciscoLocalDirectorMIBGroup": ciscoLocalDirectorMIBGroup,
       "ciscoLocalDirectorFailoverGroup": ciscoLocalDirectorFailoverGroup,
       "ciscoLocalDirectorEMIBGroup": ciscoLocalDirectorEMIBGroup,
       "ciscoLocalDirectorNotificationGroup": ciscoLocalDirectorNotificationGroup,
       "ciscoLocalDirectorNotificationGroupRev1": ciscoLocalDirectorNotificationGroupRev1,
       "ciscoLocalDirectorEMIBGroupRev1": ciscoLocalDirectorEMIBGroupRev1,
       "ciscoLocalDirectorNotificationGroupRev2": ciscoLocalDirectorNotificationGroupRev2}
)
